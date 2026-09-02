# Preview posts are unlisted, not private: keep their direct URLs while
# excluding them from the public blog, archives, normal RSS feeds and sitemap.
module Jekyll
  class PreviewVisibility < Generator
    safe true
    # After jekyll-archives (:normal), before pagination and feeds (:lowest).
    priority :low

    def generate(site)
      site.posts.docs.each do |post|
        next unless post.data["preview"] == true

        # jekyll-paginate-v2 filters these before splitting into pages.
        post.data["pagination"] = { "enabled" => false }
        post.data["sitemap"] = false
        # jekyll-feed excludes draft posts unless explicitly built --drafts.
        # This does not disable output for these documents in _posts.
        post.data["draft"] = true
      end

      return unless defined?(Jekyll::Archives::Archive)

      archives = site.pages.grep(Jekyll::Archives::Archive)
      archives.each do |archive|
        archive.posts = archive.posts.reject { |post| post.data["preview"] == true }
      end
      empty_archives = archives.select { |archive| archive.posts.empty? }
      site.pages.reject! { |page| empty_archives.include?(page) }
      site.config["archives"]&.reject! { |page| empty_archives.include?(page) }
    end
  end
end
