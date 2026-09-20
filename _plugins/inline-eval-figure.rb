require "nokogiri"

module Jekyll
  # Inline the checked-in Matplotlib output, so the site's theme variables
  # reach the figure. Original SVGs remain suitable for standalone use.
  class InlineEvalFigure < Liquid::Tag
    COLORS = {
      "#20242d" => "--sle-ink", "#434a57" => "--sle-body",
      "#747d8b" => "--sle-muted", "#dfe4e9" => "--sle-line",
      "#b0b0b0" => "--sle-figure-grid", "#000000" => "--sle-body",
      "#4f68b3" => "--sle-blue", "#287a68" => "--sle-green",
      "#a75e3c" => "--sle-warm", "#8971aa" => "--sle-purple"
    }.freeze

    def initialize(tag_name, name, tokens)
      super
      @name = name.strip
      raise ArgumentError, "Invalid evaluation figure name" unless @name.match?(/\Atb4-[a-z-]+\z/)
    end

    def render(context)
      site = context.registers[:site]
      path = site.in_source_dir("assets/img/2026-08-28-second-life-agent-evals/#{@name}.svg")
      document = Nokogiri::XML(File.read(path)) { |config| config.nonet }
      svg = document.root
      prefix = "eval-#{@name}"
      # Matplotlib IDs repeat across images. Inline copies need unique IDs
      # for clip paths, marker references and accessibility descriptions.
      svg.xpath(".//*[@id]").each { |node| node["id"] = "#{prefix}-#{node['id']}" }
      svg.traverse do |node|
        next unless node.element?
        node.attribute_nodes.each do |attribute|
          value = attribute.value.gsub(/url\(#([^)]+)\)/, "url(##{prefix}-\\1)")
          value = "##{prefix}-#{value.delete_prefix('#')}" if attribute.name == "href" && value.start_with?("#")
          attribute.value = value
        end
      end
      # Remove only figure/axes canvas patches; heatmap cells and data marks stay.
      svg.xpath(".//*[local-name()='g']").each do |group|
        next unless group["id"].to_s.match?(/-(figure|axes)_\d+\z/)
        group.element_children.select { |node| node["id"].to_s.match?(/-patch_\d+\z/) }.first&.tap do |patch|
          patch.remove if patch.to_s.include?("fill: #ffffff")
        end
      end
      svg.xpath(".//*[@style]").each do |node|
        # The confusion matrices use 19px cell annotations on a fixed color
        # scale. Keep their original dark/white inks in both page themes.
        fixed_cell_ink = @name.start_with?("tb4-single-confusion") &&
          node.name == "text" && node["style"].include?("font-size: 19px")
        next if fixed_cell_ink

        node["style"] = node["style"].gsub(/#[0-9a-fA-F]{6}/) do |color|
          variable = COLORS[color.downcase]
          variable ? "var(#{variable}, #{color})" : color
        end
        # Small opaque annotation boxes should match the surrounding page.
        if node.name == "path" && node["style"].include?("fill: #ffffff")
          node["style"] = node["style"].sub("fill: #ffffff", "fill: var(--global-bg-color, #ffffff)")
        end
      end
      svg.xpath(".//*[local-name()='style']").each do |style|
        style.content = style.content.gsub("*{", "##{prefix} *{")
      end
      description = document.at_xpath("//*[local-name()='description']")&.text || @name
      title = Nokogiri::XML::Node.new("title", document)
      title["id"] = "#{prefix}-title"
      title.content = description
      svg.prepend_child(title)
      svg["id"] = prefix
      svg["role"] = "img"
      svg["aria-labelledby"] = title["id"]
      svg["class"] = "sle-inline-figure"
      svg["focusable"] = "false"
      svg.to_xml
    end
  end
end

Liquid::Template.register_tag("inline_eval_figure", Jekyll::InlineEvalFigure)
