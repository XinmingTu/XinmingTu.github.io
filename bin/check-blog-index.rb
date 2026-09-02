# Run after a local build: bundle exec ruby bin/check-blog-index.rb
require "jekyll"
require "jekyll-paginate-v2"
require "nokogiri"
require_relative "../_plugins/preview-visibility"
require_relative "../_plugins/reading-time"

def check(message)
  raise message unless yield
end

reader = Object.new.extend(Jekyll::ReadingTimeFilter)
check("English reading time should round up") { reader.reading_time_minutes("word " * 401) == 3 }
check("Empty content should have a one-minute minimum") { reader.reading_time_minutes(nil) == 1 }
check("Chinese reading time should count characters") { reader.reading_time_minutes("文" * 401) == 2 }
check("Mixed-language reading time should include both scripts") do
  reader.reading_time_minutes(("word " * 200) + ("文" * 400)) == 2
end
check("Translations should not double reading time") do
  reader.reading_time_minutes("<div class='lang-en'>#{'word ' * 201}</div><div class='lang-zh'>#{'文' * 2000}</div>") == 2
end
check("Style and script contents should not affect reading time") do
  reader.reading_time_minutes("<style>#{'word ' * 1000}</style><script>#{'word ' * 1000}</script><p>Hello</p>") == 1
end

source = File.expand_path("..", __dir__)
expected_posts = nil
preview_posts = nil

# Exercise the real pagination generator, including a forced multi-page case.
[8, 2].each do |per_page|
  site = Jekyll::Site.new(Jekyll.configuration("source" => source, "quiet" => true))
  site.read
  documents = site.posts.docs.dup
  expected_posts = documents.select { |post| post.data["categories"].include?("blog") && post.data["preview"] != true }.sort_by(&:date).reverse
  preview_posts = documents.select { |post| post.data["preview"] == true }.sort_by(&:date).reverse
  template = site.pages.find { |page| page.url == "/blog/" }
  check("Blog listing template is missing") { template }
  template.data["pagination"]["per_page"] = per_page

  Jekyll::Archives::Archives.new(site.config).generate(site)
  Jekyll::PreviewVisibility.new.generate(site)
  check("Preview filtering must not remove source documents") { site.posts.docs == documents }
  check("Preview documents must stay writable but be omitted from feeds and sitemap") do
    preview_posts.all? { |post| post.write? && post.data["draft"] == true && post.data["sitemap"] == false }
  end
  check("Public archives must contain published posts only") do
    site.pages.grep(Jekyll::Archives::Archive).all? do |archive|
      !archive.posts.empty? && archive.posts.none? { |post| post.data["preview"] }
    end
  end
  Jekyll::PaginateV2::Generator::PaginationGenerator.new.generate(site)
  pages = site.pages.select(&:pager).sort_by { |page| page.pager.page }

  check("Unexpected number of listing pages") { pages.size == (expected_posts.size.to_f / per_page).ceil }
  check("Published posts must appear exactly once, in date order") do
    pages.flat_map { |page| page.pager.posts.map(&:url) } == expected_posts.map(&:url)
  end
  pages.each_with_index do |page, index|
    check("A non-final listing page is underfilled") { index == pages.size - 1 || page.pager.posts.size == per_page }
    check("Pagination cannot include preview posts") { page.pager.posts.none? { |post| post.data["preview"] } }
  end
end

# Check generated content and links without a browser or changing the site.
index = Nokogiri::HTML(File.read(File.join(source, "_site/blog/index.html")))
preview = Nokogiri::HTML(File.read(File.join(source, "_site/blog/preview/index.html")))
check("The generated first page should contain up to eight published posts") do
  index.css(".blog-list-content h2 a").map { |link| link["href"] } == expected_posts.first(8).map { |post| post.data["redirect"] || post.url }
end
check("The preview listing must retain all drafts") do
  preview.css(".blog-list-content h2 a").map { |link| link["href"] } == preview_posts.map(&:url)
end
[index, preview].each do |page|
  check("Every entry must retain a reading-time estimate") do
    items = page.css(".blog-list-item")
    items.all? { |item| item.at_css(".blog-list-reading-time")&.text&.match?(/\A\d+ min read\z/) }
  end
end
preview_posts.each do |post|
  check("A preview article stopped being generated: #{post.url}") do
    File.file?(File.join(source, "_site", post.url, "index.html"))
  end
  article = Nokogiri::HTML(File.read(File.join(source, "_site", post.url, "index.html")))
  check("Preview articles must request no indexing") do
    article.at_css('meta[name="robots"]')&.[]("content") == "noindex, nofollow"
  end
end

check("The preview index must request no indexing") do
  preview.at_css('meta[name="robots"]')&.[]("content") == "noindex, nofollow"
end
check("The public blog must not expose a Preview navigation link") do
  index.css("a[href]").none? { |link| link["href"].include?("/preview/") }
end

# Catch discovery leaks from RSS, sitemap, archive pages, homepage and any
# future generated search indexes. Preview pages themselves remain accessible.
destination = File.join(source, "_site")
unlisted_paths = ["/blog/preview/"] + preview_posts.map(&:url)
Dir.glob(File.join(destination, "**", "*.{html,xml,json}")).each do |path|
  next if path.start_with?(File.join(destination, "blog/preview/"))

  content = File.read(path)
  check("Preview URL leaked into public output: #{path.delete_prefix(destination)}") do
    unlisted_paths.none? { |url| content.include?(url) }
  end
end
feed = Nokogiri::XML(File.read(File.join(destination, "feed.xml")))
check("RSS must retain published posts") do
  feed.xpath("//*[local-name()='entry']/*[local-name()='link']/@href").any? do |href|
    href.value.end_with?(expected_posts.first.url)
  end
end

puts "Blog checks passed: #{expected_posts.size} published posts, #{preview_posts.size} unlisted previews; pagination, reading time, direct links and discovery exclusions verified."
