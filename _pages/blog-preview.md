---
layout: default
title: Preview
description: Writing in progress.
permalink: /blog/preview/
nav: false
sitemap: false
---

<div class="post">
  <div class="header-bar">
    <h1>Preview</h1>
    <h2>Writing in progress.</h2>
  </div>

  <ul class="post-list">
    {% assign preview_posts = site.posts | where: "preview", true | sort: "date" | reverse %}
    {% for post in preview_posts %}
      {% assign read_time = post.content | number_of_words | divided_by: 180 | plus: 1 %}
      <li>
        <h3>
          <a class="post-title" href="{{ post.url | relative_url }}">{{ post.title }}</a>
        </h3>
        {% if post.description %}
          <p>{{ post.description }}</p>
        {% endif %}
        <p class="post-meta">
          {{ read_time }} min read &nbsp; &middot; &nbsp;
          {{ post.date | date: "%B %-d, %Y" }}
        </p>
      </li>
    {% else %}
      <li><p>No drafts at the moment.</p></li>
    {% endfor %}
  </ul>
</div>
