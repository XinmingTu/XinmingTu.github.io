---
layout: default
title: Preview
description: Writing in progress.
permalink: /blog/preview/
nav: false
preview: true
sitemap: false
---

<div class="post blog-index">
  <header class="blog-index-header">
    <h1>Preview</h1>
    <p>Writing in progress.</p>
  </header>

  {% include blog_index_nav.html preview=true %}

  <ul class="blog-list">
    {% assign preview_posts = site.posts | where: "preview", true | sort: "date" | reverse %}
    {% for post in preview_posts %}
      {% include blog_list_item.html post=post %}
    {% else %}
      <li class="blog-list-empty">No drafts at the moment.</li>
    {% endfor %}
  </ul>
</div>
