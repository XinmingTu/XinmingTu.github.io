---
layout: page
title: Preview
description: Writing in progress.
permalink: /preview/
nav: false
sitemap: false
---

<div class="post">
  <ul class="post-list">
    {% assign preview_pages = site.pages | where: "preview", true | sort: "date" | reverse %}
    {% for post in preview_pages %}
      {% assign read_time = post.content | number_of_words | divided_by: 180 | plus: 1 %}
      <li>
        <h3>
          {% if post.redirect == blank %}
            <a class="post-title" href="{{ post.url | relative_url }}">{{ post.title }}</a>
          {% elsif post.redirect contains '://' %}
            <a class="post-title" href="{{ post.redirect }}" target="_blank" rel="noopener noreferrer">{{ post.title }}</a>
          {% else %}
            <a class="post-title" href="{{ post.redirect | relative_url }}">{{ post.title }}</a>
          {% endif %}
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
