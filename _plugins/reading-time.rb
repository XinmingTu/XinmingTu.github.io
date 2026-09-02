require "nokogiri"

module Jekyll
  module ReadingTimeFilter
    # Estimate one reading of a bilingual article, not both translations.
    # HTML attributes and executable/style content are not reading material.
    def reading_time_minutes(content)
      fragment = Nokogiri::HTML.fragment(content.to_s)
      fragment.css("script, style, template, noscript, button").remove
      fragment.css(".lang-zh").remove if fragment.at_css(".lang-en")
      text = fragment.xpath(".//text()").map(&:text).join(" ")

      characters = text.scan(/\p{Han}/).length
      words = text.gsub(/\p{Han}/, " ").scan(/[\p{L}\p{N}]+(?:['’-][\p{L}\p{N}]+)*/).length
      [(words / 200.0 + characters / 400.0).ceil, 1].max
    end
  end
end

Liquid::Template.register_filter(Jekyll::ReadingTimeFilter)
