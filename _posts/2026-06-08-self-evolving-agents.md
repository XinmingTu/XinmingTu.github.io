---
layout: distill
title: "The What & When of Self-Evolving Agents"
description: "Work in progress: a 3x3 framework for understanding self-evolving agents across external state, harnesses, and weights."
date: 2026-06-08
tags: ['AI', 'agents', 'deep-learning']

authors:
  - name: Xinming Tu
    url: "https://xinmingtu.cn"
    affiliations:
      name: University of Washington
  - name: Tong Chen
    url: "https://scholar.google.com/citations?user=fOcXofAAAAAJ&hl=en"
    affiliations:
      name: University of Washington

bibliography: 2026-06-08-self-evolving-agents.bib
_styles: |
  d-article h3 {
    margin-top: 1.15em;
    margin-bottom: 0.55em;
  }
  d-article figure.self-evolving-figure {
    margin: 1.35rem 0 1.65rem;
  }
  d-article figure.self-evolving-figure.tight-top {
    margin-top: 0.55rem;
  }
  d-article figure.self-evolving-figure.medium {
    max-width: 760px;
    margin-left: auto;
    margin-right: auto;
  }
  d-article figure.self-evolving-figure img {
    width: 100%;
    height: auto;
    display: block;
  }
  d-article figure.self-evolving-figure figcaption {
    color: #6b7280;
    font-size: 0.88rem;
    line-height: 1.45;
    margin-top: 0.55rem;
    text-align: center;
  }
  d-article details.evo-aside {
    background: #fbfbfd;
    border: 1px solid #d7dae3;
    border-radius: 8px;
    margin: 0.9rem 0 1.25rem;
  }
  d-article details.evo-aside summary {
    align-items: center;
    color: #1a1d26;
    cursor: pointer;
    display: flex;
    font-weight: 700;
    gap: 0.5rem;
    list-style: none;
    padding: 0.75rem 0.9rem;
  }
  d-article details.evo-aside summary::-webkit-details-marker {
    display: none;
  }
  d-article details.evo-aside summary::before {
    color: #7a8196;
    content: "+";
    flex: 0 0 auto;
    font-weight: 800;
  }
  d-article details.evo-aside[open] summary::before {
    content: "-";
  }
  d-article details.evo-aside .evo-aside-body {
    color: #3d4250;
    font-size: 0.92rem;
    line-height: 1.55;
    padding: 0 0.9rem 0.85rem;
  }
  d-article details.evo-aside .evo-aside-body > :first-child {
    margin-top: 0;
  }
  d-article details.evo-aside .evo-aside-body > :last-child {
    margin-bottom: 0;
  }
  d-article details.appendix-cell {
    border-top: 1px solid #e7e9f0;
    padding: 0.8rem 0;
  }
  d-article details.appendix-cell:last-of-type {
    border-bottom: 1px solid #e7e9f0;
  }
  d-article details.appendix-cell summary {
    align-items: baseline;
    cursor: pointer;
    display: flex;
    gap: 0.75rem;
    list-style: none;
  }
  d-article details.appendix-cell summary::-webkit-details-marker {
    display: none;
  }
  d-article details.appendix-cell summary::before {
    color: #7a8196;
    content: "+";
    flex: 0 0 auto;
    font-weight: 800;
  }
  d-article details.appendix-cell[open] summary::before {
    content: "-";
  }
  d-article .appendix-cell-title {
    color: #1a1d26;
    flex: 0 0 14rem;
    font-weight: 800;
  }
  d-article .appendix-cell-subtitle {
    color: #6b7280;
    font-size: 0.92rem;
    font-weight: 600;
  }
  @media (max-width: 720px) {
    d-article details.appendix-cell summary {
      align-items: flex-start;
      flex-direction: column;
      gap: 0.15rem;
    }
    d-article details.appendix-cell summary::before {
      display: none;
    }
    d-article .appendix-cell-title {
      flex-basis: auto;
    }
  }
  d-article .evo-files { --lc: #2563d6; --lc-bg: #eef3fd; --lc-dark: #1b3f86; --lc-border: #cdddf7; }
  d-article .evo-harness { --lc: #df7a18; --lc-bg: #fdf3e7; --lc-dark: #a8550a; --lc-border: #f4ddbd; }
  d-article .evo-weights { --lc: #7c3aed; --lc-bg: #f4eefd; --lc-dark: #5b21b6; --lc-border: #e2d2fa; }
  d-article svg.evo-ic {
    fill: none;
    stroke: currentColor;
    stroke-width: 2;
    stroke-linecap: round;
    stroke-linejoin: round;
    flex: none;
  }
  d-article .evo-matrix,
  d-article .evo-layers,
  d-article .evo-panel-head {
    font-family: Roboto, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, sans-serif;
  }
  d-article .evo-layers {
    display: flex;
    gap: 1.35rem;
    align-items: stretch;
  }
  d-article .evo-layers-diagram {
    flex: 1.12;
    min-width: 0;
    display: flex;
  }
  d-article .evo-layers-diagram > .evo-layer {
    flex: 1;
  }
  d-article .evo-layer {
    border: 2px solid var(--lc-border);
    background: var(--lc-bg);
    border-radius: 22px;
    padding: 0.85rem 0.9rem 0.95rem;
  }
  d-article .evo-layer .evo-layer {
    margin-top: 0.75rem;
    border-radius: 17px;
  }
  d-article .evo-layer-head {
    display: grid;
    grid-template-columns: auto 1fr;
    column-gap: 0.55rem;
    align-items: center;
  }
  d-article .evo-layer-head .evo-ic {
    grid-row: 1 / span 2;
    width: 20px;
    height: 20px;
    color: var(--lc);
  }
  d-article .evo-layer-name {
    color: var(--lc-dark);
    font-weight: 700;
    font-size: 0.95rem;
    line-height: 1.25;
  }
  d-article .evo-layer-sub {
    color: var(--lc);
    font-size: 0.72rem;
    font-weight: 500;
    line-height: 1.3;
  }
  d-article .evo-layer-core {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    gap: 0.1rem;
    min-height: 168px;
    border-radius: 13px;
    padding: 1rem 0.8rem 1.05rem;
  }
  d-article .evo-core-art {
    width: 86px;
    height: auto;
    margin-bottom: 0.35rem;
  }
  d-article .evo-legend {
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
    gap: 0.9rem;
    justify-content: center;
  }
  d-article .evo-legend-item {
    display: flex;
    gap: 0.65rem;
    align-items: flex-start;
  }
  d-article .evo-legend-ic {
    flex: none;
    width: 30px;
    height: 30px;
    border-radius: 8px;
    background: var(--lc-bg);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--lc);
  }
  d-article .evo-legend-ic .evo-ic {
    width: 17px;
    height: 17px;
  }
  d-article .evo-legend-body {
    min-width: 0;
  }
  d-article .evo-legend-item strong {
    display: block;
    color: var(--lc);
    font-size: 0.86rem;
    font-weight: 700;
    margin-bottom: 0.05rem;
  }
  d-article .evo-legend-text {
    color: #7a8196;
    font-size: 0.8rem;
    line-height: 1.45;
  }
  d-article .evo-legend-note {
    border: 1px dashed #d7dae3;
    border-radius: 10px;
    background: #fbfbfd;
    padding: 0.7rem 0.85rem;
    color: #3d4250;
    font-size: 0.8rem;
    line-height: 1.5;
  }
  d-article .evo-legend-note strong {
    color: #1a1d26;
  }
  d-article .evo-matrix {
    display: grid;
    gap: 6px;
  }
  d-article .evo-matrix-fig {
    grid-template-columns: 24px 42px 1fr 1fr 1fr;
  }
  d-article .evo-matrix-app {
    grid-template-columns: 42px 1fr 1fr 1fr;
    margin: 1.4rem 0 0.4rem;
  }
  d-article .evo-matrix-fig .evo-corner {
    grid-column: span 2;
  }
  d-article .evo-colhead {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-end;
    gap: 0.1rem;
    text-align: center;
    padding: 0.1rem 0.2rem 0.4rem;
  }
  d-article .evo-colhead-name {
    color: var(--lc);
    font-weight: 700;
    font-size: 0.9rem;
    line-height: 1.2;
  }
  d-article .evo-colhead-sub {
    color: #7a8196;
    font-size: 0.68rem;
    font-weight: 500;
    line-height: 1.25;
  }
  d-article .evo-rowlabel {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.3rem;
  }
  d-article .evo-rowlabel-text {
    writing-mode: vertical-rl;
    transform: rotate(180deg);
    color: #1a1d26;
    font-weight: 700;
    font-size: 0.78rem;
    letter-spacing: 0.02em;
  }
  d-article .evo-rowicon {
    width: 16px;
    height: 16px;
    color: #7a8196;
  }
  d-article .evo-cell {
    background: var(--lc-bg);
    border: 1px solid transparent;
    border-radius: 10px;
    padding: 0.7rem 0.65rem 0.75rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 0.3rem;
    min-height: 116px;
  }
  d-article .evo-cellicon {
    width: 25px;
    height: 25px;
    color: var(--lc);
  }
  d-article .evo-cell-title {
    color: #1a1d26;
    font-weight: 700;
    font-size: 0.83rem;
    line-height: 1.3;
  }
  d-article .evo-cell-desc {
    color: #3d4250;
    font-size: 0.77rem;
    font-weight: 400;
    line-height: 1.4;
  }
  d-article .evo-cell-tag {
    display: none;
  }
  d-article .evo-yaxis {
    grid-column: 1;
    grid-row: 2 / span 3;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.35rem;
    padding: 0.4rem 0;
  }
  d-article .evo-yaxis-arrow {
    width: 0;
    height: 0;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-bottom: 9px solid #7a8196;
  }
  d-article .evo-yaxis-text {
    writing-mode: vertical-rl;
    transform: rotate(180deg);
    color: #1a1d26;
    font-weight: 800;
    font-size: 0.7rem;
    letter-spacing: 0.09em;
    text-transform: uppercase;
  }
  d-article .evo-yaxis-line {
    flex: 1;
    width: 1.5px;
    background: #c3c8d4;
    border-radius: 1px;
  }
  d-article .evo-xaxis {
    grid-column: 3 / -1;
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
    padding-top: 0.4rem;
  }
  d-article .evo-xaxis-title {
    text-align: center;
    color: #1a1d26;
    font-weight: 800;
    font-size: 0.7rem;
    letter-spacing: 0.09em;
    text-transform: uppercase;
  }
  d-article .evo-xaxis-scale {
    display: flex;
    align-items: center;
    gap: 0.55rem;
    color: #3d4250;
    font-size: 0.72rem;
    font-weight: 600;
  }
  d-article .evo-xaxis-bar {
    flex: 1;
    height: 6px;
    border-radius: 4px;
    background: linear-gradient(90deg, #2563d6, #df7a18 52%, #7c3aed);
    opacity: 0.85;
    position: relative;
  }
  d-article .evo-xaxis-bar::after {
    content: "";
    position: absolute;
    right: -8px;
    top: 50%;
    transform: translateY(-50%);
    border-top: 6px solid transparent;
    border-bottom: 6px solid transparent;
    border-left: 9px solid #7c3aed;
  }
  d-article .evo-cell-btn {
    cursor: pointer;
    appearance: none;
    -webkit-appearance: none;
    width: 100%;
    font-family: inherit;
    color: inherit;
    border: 1px solid var(--lc-border);
    background: var(--lc-bg);
    border-radius: 10px;
    padding: 0.6rem 0.65rem 0.65rem;
    display: flex;
    flex-direction: column;
    align-items: stretch;
    text-align: left;
    gap: 0.28rem;
    min-height: 0;
  }
  d-article .evo-cell-btn:hover {
    border-color: var(--lc);
  }
  d-article .evo-cell-btn:focus-visible {
    outline: 2px solid var(--lc);
    outline-offset: 2px;
  }
  d-article .evo-cell-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
  }
  d-article .evo-cell-btn .evo-cellicon {
    width: 20px;
    height: 20px;
  }
  d-article .evo-cell-plus {
    color: #7a8196;
    font-weight: 800;
    font-size: 0.95rem;
    line-height: 1;
  }
  d-article .evo-cell-plus::before {
    content: "+";
  }
  d-article .evo-cell-btn[aria-expanded="true"] {
    border-color: var(--lc);
    box-shadow: inset 0 0 0 1px var(--lc);
  }
  d-article .evo-cell-btn[aria-expanded="true"] .evo-cell-plus::before {
    content: "−";
  }
  d-article .evo-cell-btn .evo-cell-title {
    font-size: 0.8rem;
    text-align: left;
  }
  d-article .evo-cell-systems {
    color: #6b7280;
    font-size: 0.72rem;
    font-weight: 400;
    line-height: 1.4;
  }
  d-article .evo-panel {
    grid-column: 1 / -1;
    position: relative;
    border: 1px solid var(--lc-border);
    border-radius: 10px;
    background: #ffffff;
    padding: 0.95rem 1.1rem 0.9rem;
    margin: 2px 0 5px;
  }
  d-article .evo-panel[hidden] {
    display: none;
  }
  d-article .evo-panel::before {
    content: "";
    position: absolute;
    top: -6px;
    left: var(--cx, 50%);
    width: 10px;
    height: 10px;
    transform: translateX(-50%) rotate(45deg);
    background: #ffffff;
    border-left: 1px solid var(--lc-border);
    border-top: 1px solid var(--lc-border);
  }
  d-article .evo-from-1 { --cx: calc(48px + (100% - 48px) * 0.1667); }
  d-article .evo-from-2 { --cx: calc(48px + (100% - 48px) * 0.5); }
  d-article .evo-from-3 { --cx: calc(48px + (100% - 48px) * 0.8333); }
  d-article .evo-panel-head {
    color: #6b7280;
    font-size: 0.8rem;
    margin: 0 0 0.6rem;
  }
  d-article .evo-panel-head strong {
    color: var(--lc-dark);
  }
  d-article .evo-panel p,
  d-article .evo-panel ul {
    font-size: 0.95em;
  }
  d-article .evo-panel > *:last-child {
    margin-bottom: 0;
  }
  d-article .evo-shift {
    font-family: Roboto, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, sans-serif;
  }
  d-article .evo-shift-heads,
  d-article .evo-shift-row {
    display: grid;
    grid-template-columns: 1fr 2.1rem 1.35fr;
    gap: 0.7rem;
    align-items: center;
  }
  d-article .evo-shift-heads {
    margin-bottom: 0.5rem;
  }
  d-article .evo-shift-row + .evo-shift-row {
    margin-top: 0.5rem;
  }
  d-article .evo-shift-head {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }
  d-article .evo-shift-head span {
    display: block;
    margin-top: 0.12rem;
    font-weight: 500;
    letter-spacing: 0;
    text-transform: none;
    color: #aab0c0;
  }
  d-article .evo-shift-head-from { color: #9aa1b5; }
  d-article .evo-shift-head-to { color: #1a1d26; grid-column: 3; }
  d-article .evo-shift-from {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 0.5rem;
    align-items: center;
    border: 1px solid var(--lc-border);
    background: #ffffff;
    border-radius: 10px;
    padding: 0.55rem 0.65rem;
  }
  d-article .evo-shift-from .evo-ic {
    width: 18px;
    height: 18px;
    color: var(--lc);
  }
  d-article .evo-shift-from-name {
    color: var(--lc-dark);
    font-weight: 700;
    font-size: 0.84rem;
    line-height: 1.2;
  }
  d-article .evo-shift-from-sub {
    color: #9aa1b5;
    font-size: 0.72rem;
    line-height: 1.3;
  }
  d-article .evo-shift-arrow {
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--lc);
    opacity: 0.8;
  }
  d-article .evo-shift-arrow svg {
    width: 22px;
    height: 22px;
  }
  d-article .evo-shift-to {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 0.6rem;
    align-items: center;
    border: 1px solid var(--lc-border);
    background: var(--lc-bg);
    border-radius: 10px;
    padding: 0.6rem 0.75rem;
  }
  d-article .evo-shift-to-ic {
    flex: none;
    width: 32px;
    height: 32px;
    border-radius: 9px;
    background: var(--lc);
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  d-article .evo-shift-to-ic .evo-ic {
    width: 19px;
    height: 19px;
  }
  d-article .evo-shift-to-name {
    color: #1a1d26;
    font-weight: 700;
    font-size: 0.92rem;
    line-height: 1.2;
  }
  d-article .evo-shift-to-name span {
    color: var(--lc);
    font-weight: 600;
  }
  d-article .evo-shift-to-trigger {
    color: #6b7280;
    font-size: 0.74rem;
    line-height: 1.35;
    margin-top: 0.15rem;
  }
  @media (max-width: 760px) {
    d-article .evo-layers {
      flex-direction: column;
      gap: 1rem;
    }
    d-article .evo-matrix-fig,
    d-article .evo-matrix-app {
      grid-template-columns: repeat(3, 1fr);
      gap: 4px;
    }
    d-article .evo-matrix .evo-corner,
    d-article .evo-matrix .evo-yaxis,
    d-article .evo-colhead-sub,
    d-article .evo-cell-desc,
    d-article .evo-cell-systems {
      display: none;
    }
    d-article .evo-colhead {
      padding: 0.1rem 0 0.25rem;
    }
    d-article .evo-colhead-name {
      font-size: 0.68rem;
    }
    d-article .evo-rowlabel {
      grid-column: 1 / -1;
      justify-content: flex-start;
      gap: 0.35rem;
      padding: 0.5rem 0.1rem 0.1rem;
    }
    d-article .evo-rowlabel-text {
      writing-mode: horizontal-tb;
      transform: none;
      font-size: 0.78rem;
    }
    d-article .evo-cell {
      min-height: 0;
      padding: 0.5rem 0.45rem 0.55rem;
      gap: 0.25rem;
    }
    d-article .evo-cell-title {
      font-size: 0.68rem;
      line-height: 1.25;
    }
    d-article .evo-cell-btn {
      padding: 0.5rem 0.5rem 0.55rem;
    }
    d-article .evo-cellicon {
      width: 18px;
      height: 18px;
    }
    d-article .evo-xaxis {
      grid-column: 1 / -1;
    }
    d-article .evo-xaxis-scale {
      font-size: 0.62rem;
    }
    d-article .evo-panel {
      padding: 0.85rem 0.85rem 0.8rem;
    }
    d-article .evo-from-1 { --cx: 16.67%; }
    d-article .evo-from-2 { --cx: 50%; }
    d-article .evo-from-3 { --cx: 83.33%; }
    d-article .evo-shift-heads {
      display: none;
    }
    d-article .evo-shift-row {
      grid-template-columns: 1fr auto 1.15fr;
      gap: 0.4rem;
    }
    d-article .evo-shift-row + .evo-shift-row {
      margin-top: 0.6rem;
    }
    d-article .evo-shift-from,
    d-article .evo-shift-to {
      min-width: 0;
    }
    d-article .evo-shift-from {
      gap: 0.35rem;
      padding: 0.4rem 0.45rem;
    }
    d-article .evo-shift-from .evo-ic {
      width: 15px;
      height: 15px;
    }
    d-article .evo-shift-from-name { font-size: 0.74rem; }
    d-article .evo-shift-from-sub { font-size: 0.63rem; }
    d-article .evo-shift-arrow svg {
      width: 15px;
      height: 15px;
    }
    d-article .evo-shift-to {
      gap: 0.4rem;
      padding: 0.42rem 0.5rem;
    }
    d-article .evo-shift-to-ic {
      width: 24px;
      height: 24px;
      border-radius: 7px;
    }
    d-article .evo-shift-to-ic .evo-ic {
      width: 15px;
      height: 15px;
    }
    d-article .evo-shift-to-name { font-size: 0.76rem; }
    d-article .evo-shift-to-trigger { font-size: 0.63rem; }
  }

toc:
  - name: "The Dual Promise"
  - name: "What Evolves"
  - name: "Learning From Experience"
  - name: "The 3x3 Evolution Matrix"
  - name: "Single Session: Online Adaptation"
  - name: "Across Sessions: Longitudinal Alignment"
  - name: "Across Users: Population-Level Evolution"
  - name: "What Is the 'Self' Here?"
  - name: "Appendix: The Complete Landscape"
---

> **Work in progress.**

<div style="position:absolute;width:0;height:0;overflow:hidden" aria-hidden="true">
<svg xmlns="http://www.w3.org/2000/svg">
<symbol id="ei-db" viewBox="0 0 24 24"><ellipse cx="12" cy="5" rx="8" ry="3"></ellipse><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5"></path><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"></path></symbol>
<symbol id="ei-gear" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"></circle><path d="M12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"></path></symbol>
<symbol id="ei-row-users" viewBox="0 0 24 24"><circle cx="9" cy="8" r="3"></circle><path d="M3 20v-1a5 5 0 0 1 5-5h2a5 5 0 0 1 5 5v1"></path><circle cx="17" cy="7" r="2.4"></circle><path d="M16 13.2a4.5 4.5 0 0 1 5 4.3V19"></path></symbol>
<symbol id="ei-row-sessions" viewBox="0 0 24 24"><rect x="3" y="4.5" width="18" height="16" rx="2.2"></rect><path d="M3 9h18M8 2.5v4M16 2.5v4"></path><path d="M8 13h2M14 13h2M8 16.5h2M14 16.5h2"></path></symbol>
<symbol id="ei-row-session" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 7.5V12l3 2"></path></symbol>
<symbol id="ei-collective" viewBox="0 0 24 24"><ellipse cx="9" cy="5" rx="6" ry="2.4"></ellipse><path d="M3 5v6c0 1.3 2.7 2.4 6 2.4s6-1.1 6-2.4V5"></path><path d="M3 11c0 1.3 2.7 2.4 6 2.4"></path><circle cx="18" cy="9" r="1.6"></circle><circle cx="21" cy="15" r="1.6"></circle><circle cx="15" cy="16" r="1.6"></circle><path d="M17 10.3 15.8 14.6M19.3 10.1 20.7 13.5M16.5 16h3"></path></symbol>
<symbol id="ei-tuning" viewBox="0 0 24 24"><circle cx="12" cy="6" r="3"></circle><path d="M12 9v3M12 12H6v3M12 12h6v3"></path><rect x="3" y="15" width="6" height="5" rx="1.2"></rect><rect x="15" y="15" width="6" height="5" rx="1.2"></rect></symbol>
<symbol id="ei-continual" viewBox="0 0 24 24"><circle cx="5" cy="12" r="2"></circle><circle cx="12" cy="6" r="2"></circle><circle cx="12" cy="18" r="2"></circle><circle cx="19" cy="12" r="2"></circle><path d="M6.7 11 10.3 7M6.7 13l3.6 4M13.7 7l3.6 4M13.7 17l3.6-4"></path></symbol>
<symbol id="ei-skills" viewBox="0 0 24 24"><path d="M5 18.5A2.5 2.5 0 0 1 7.5 16H19"></path><path d="M7.5 3H19v18H7.5A2.5 2.5 0 0 1 5 18.5v-13A2.5 2.5 0 0 1 7.5 3z"></path><path d="M13 3v7l2.2-1.6L17 10V3"></path></symbol>
<symbol id="ei-pharness" viewBox="0 0 24 24"><circle cx="8" cy="8" r="3"></circle><path d="M3 19v-.5a5 5 0 0 1 5-5"></path><path d="M14 9h6v5"></path><path d="M20 9l-6 6-2.5-2.5"></path></symbol>
<symbol id="ei-sliders" viewBox="0 0 24 24"><path d="M6 21v-7M6 9V3M12 21v-9M12 7V3M18 21v-4M18 12V3"></path><path d="M3 12h6M9 7h6M15 17h6"></path></symbol>
<symbol id="ei-scratch" viewBox="0 0 24 24"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"></path><path d="M14 3v5h5"></path><path d="M8 13h4M8 16.5h3"></path><circle cx="16" cy="16" r="3"></circle><path d="M16 14.6V16l1 .8"></path></symbol>
<symbol id="ei-dynamic" viewBox="0 0 24 24"><path d="M3 14a2 2 0 0 0 2 2h2l3 3v-3h3a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2z"></path><path d="M14.5 9H19a2 2 0 0 1 2 2v3"></path><path d="M21 14l-1.6-1.6M21 14l-1.6 1.6"></path></symbol>
<symbol id="ei-chip" viewBox="0 0 24 24"><rect x="5" y="5" width="14" height="14" rx="2.2"></rect><rect x="9" y="9" width="6" height="6" rx="1"></rect><path d="M9 2.5v2.5M15 2.5v2.5M9 19v2.5M15 19v2.5M2.5 9H5M2.5 15H5M19 9h2.5M19 15h2.5"></path></symbol>
<symbol id="ei-target" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><circle cx="12" cy="12" r="4.8"></circle><circle cx="12" cy="12" r="1" fill="currentColor" stroke="none"></circle></symbol>
<symbol id="ei-globe" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M3 12h18"></path><path d="M12 3c2.7 2.5 4.2 5.7 4.2 9s-1.5 6.5-4.2 9c-2.7-2.5-4.2-5.7-4.2-9s1.5-6.5 4.2-9z"></path></symbol>
<symbol id="ei-swarm" viewBox="0 0 24 24"><path d="M12 7 6 11M12 7l6 4M7 12h10M6.5 13.5 9.5 18M17.5 13.5 14.5 18M10 19h4"></path><circle cx="12" cy="5" r="2"></circle><circle cx="5" cy="12" r="2"></circle><circle cx="19" cy="12" r="2"></circle><circle cx="9" cy="19" r="2"></circle><circle cx="15" cy="19" r="2"></circle></symbol>
</svg>
</div>

## The Dual Promise

**The era of static AI agents is ending.**

An agent's capability should not freeze on release day. If autonomy is the goal, intelligence has to compound through execution. Every interaction should create pressure for the system to adapt. We are now witnessing a fundamental shift toward dynamic, **self-evolving systems**, driven by a dual promise:

- **Motivation 1: Marginal Cost Reduction (Shrinking Costs).** Operationally, this means fewer prompt tokens, fewer tool calls, fewer retries, and less human intervention per solved task family. By compressing experience into reusable assets, the system stops paying for the same mistake twice.

- **Motivation 2: Capability Ceiling Expansion (Breaking Ceilings).** Evolution helps agents handle long-tail tasks and enables robust **long-horizon execution**. Static agents tend to become brittle on complex, multi-step goals because small errors compound and context is eventually exhausted. By learning to forge ad-hoc tools, cache intermediate progress, and adapt strategies at runtime, a self-evolving agent turns long-term autonomy from a behavioral illusion into a systems claim.

<figure class="self-evolving-figure tight-top medium">
  <img src="/assets/img/2026-06-08-self-evolving-agents/figure1-dual-promise.svg" alt="A chart showing self-evolving agents reducing cost per task while expanding capability over time.">
  <figcaption><strong>Figure 1.</strong> Self-evolution has two linked payoffs: lower marginal cost and higher capability ceilings.</figcaption>
</figure>

Early systems are beginning to move beyond **stateless orchestration** toward updatable execution substrates. This does not mean every agent is self-evolving yet; it means experience is starting to be captured in places the system can reuse. But "learning" is not magic; it requires a physical substrate. To genuinely reduce costs and break capability ceilings, we must understand the architecture of this adaptation.

The central question is simple: **Where exactly does this evolution happen?**

Recent surveys on self-evolving agents organize the field around what evolves, when it evolves, and how it evolves <d-cite key="selfevolvingsurvey2025"></d-cite>. The 3x3 matrix below is a systems-oriented version of the same instinct: it asks which structural layer is updated, and over what lifetime the update persists.

## What Evolves

Before discussing how an agent evolves, we need to define the architecture of an agent. In practice, an agent's cognitive state is distributed across three plastic layers.

<figure class="self-evolving-figure layers-figure">
<div class="evo-layers">
<div class="evo-layers-diagram">
<div class="evo-layer evo-files">
<div class="evo-layer-head"><svg class="evo-ic" aria-hidden="true"><use href="#ei-db"></use></svg><span class="evo-layer-name">External Files</span><span class="evo-layer-sub">memory · knowledge · skill library</span></div>
<div class="evo-layer evo-harness">
<div class="evo-layer-head"><svg class="evo-ic" aria-hidden="true"><use href="#ei-gear"></use></svg><span class="evo-layer-name">Agent Harness</span><span class="evo-layer-sub">prompts · tools · workflow · logic</span></div>
<div class="evo-layer evo-layer-core evo-weights">
<svg class="evo-core-art" viewBox="195 220 80 58" aria-hidden="true"><g stroke="#7c3aed" stroke-width="2" fill="none" opacity=".55"><path d="M205 250 L235 232 M205 250 L235 270 M265 232 L235 232 M265 268 L235 270 M205 250 L265 232 M205 250 L265 268"></path></g><circle cx="205" cy="250" r="6.5" fill="#7c3aed"></circle><circle cx="235" cy="232" r="6.5" fill="#fff" stroke="#7c3aed" stroke-width="2"></circle><circle cx="235" cy="270" r="6.5" fill="#fff" stroke="#7c3aed" stroke-width="2"></circle><circle cx="265" cy="232" r="6.5" fill="#7c3aed"></circle><circle cx="265" cy="268" r="6.5" fill="#7c3aed"></circle></svg>
<span class="evo-layer-name">Model Weights</span>
<span class="evo-layer-sub">parametric memory · core model</span>
</div>
</div>
</div>
</div>
<div class="evo-legend">
<div class="evo-legend-item evo-files"><span class="evo-legend-ic"><svg class="evo-ic" aria-hidden="true"><use href="#ei-db"></use></svg></span><span class="evo-legend-body"><strong>External files</strong><span class="evo-legend-text">Editable artifacts the agent reads &amp; writes — notes, documents, skills.</span></span></div>
<div class="evo-legend-item evo-harness"><span class="evo-legend-ic"><svg class="evo-ic" aria-hidden="true"><use href="#ei-gear"></use></svg></span><span class="evo-legend-body"><strong>Agent harness</strong><span class="evo-legend-text">The scaffolding that turns a model into an agent — prompts, tools, control flow.</span></span></div>
<div class="evo-legend-item evo-weights"><span class="evo-legend-ic"><svg class="evo-ic" aria-hidden="true"><use href="#ei-continual"></use></svg></span><span class="evo-legend-body"><strong>Model weights</strong><span class="evo-legend-text">What the network has internalized — knowledge baked into parameters.</span></span></div>
<div class="evo-legend-note"><strong>Surface → Core.</strong> Outward = cheap, instant, reversible. Inward = expensive, slow, durable. The deeper a change goes, the more it sticks.</div>
</div>
</div>
<figcaption><strong>Figure 2.</strong> The agent is not only the model. Its plastic state spans external files, harness logic, and model weights.</figcaption>
</figure>

### Level 1: Model Weights

The first layer is the parametric core: the model weights. This layer stores implicit knowledge and is updated through gradient-based learning. Parametric updates can generalize broadly across tasks, but they are computationally expensive and carry inherent risks such as catastrophic forgetting, capability regression, and costly evaluation requirements.

### Level 2: Agent Harness

The second layer is the agent harness: the control flow, tool runtime, prompt policy, and orchestration logic around the model. This layer defines *how* the agent executes tasks. Instead of being a fixed software wrapper around a frozen model, the harness itself is becoming an updatable substrate. A self-evolving system can optimize its own tool-selection logic, compile repeated workflows into deterministic subroutines, or rewrite its recovery loops from experience, all without changing a single model weight.

### Level 3: External Files & State

The third layer is external files and state: persistent memories, skill libraries, knowledge graphs, and dynamic scratchpads. Unlike traditional read-only RAG, modern external memory is structured and natively editable by the agent. It stores precise code snippets, error logs, user preferences, reusable procedures, and project-specific context.

Evolution here is computationally cheap yet offers literal fidelity relative to parametric memory: a saved script, exact error log, or project convention remains precise instead of blurring into statistical memory.

### The Blurry Boundary: When Files Become Code

The boundary between Level 2 and Level 3 is porous. When an agent writes a Python function into a skill library, it starts as an external file (Level 3). But the moment the runtime loads that file to route future tasks, the file becomes control logic (Level 2). External memory no longer merely stores facts; it stores executable operators.

This file-to-code transition is a core mechanism in advanced self-evolving agents. External files are no longer passive storage; they are executable capability substrates.

## Learning From Experience

At its core, self-evolution reduces to a single imperative: **learning from experience**.

Every deployed agent leaves behind experience exhaust: successful trajectories, tool errors, rejected actions, and user corrections. A static agent flushes this signal the moment a task ends. A self-evolving agent captures that signal and hardens it into reusable state.

To map how this feedback loop operates, we project the three structural layers against three time scales of adaptation:

- **Single Session:** Online adaptation inside one active trajectory.
- **Across Sessions:** Longitudinal adaptation to a specific user, project, or codebase.
- **Across Users:** Population-level evolution derived from aggregate interactions.

## The 3x3 Evolution Matrix

The result is a 3x3 map: three persistence horizons crossed with three update substrates.

<figure class="self-evolving-figure matrix-figure">
<div class="evo-matrix evo-matrix-fig">
<div class="evo-corner"></div>
<div class="evo-colhead evo-files"><span class="evo-colhead-name">External Files</span><span class="evo-colhead-sub">memory / knowledge / skills</span></div>
<div class="evo-colhead evo-harness"><span class="evo-colhead-name">Agent Harness</span><span class="evo-colhead-sub">workflow / prompts / tools</span></div>
<div class="evo-colhead evo-weights"><span class="evo-colhead-name">Model Weights</span><span class="evo-colhead-sub">parametric memory / core</span></div>
<div class="evo-yaxis"><span class="evo-yaxis-arrow"></span><span class="evo-yaxis-line"></span><span class="evo-yaxis-text">When to update?</span><span class="evo-yaxis-line"></span></div>
<div class="evo-rowlabel"><svg class="evo-ic evo-rowicon" aria-hidden="true"><use href="#ei-row-users"></use></svg><span class="evo-rowlabel-text">Across Users</span></div>
<div class="evo-cell evo-files"><span class="evo-cell-tag">External Files</span><svg class="evo-ic evo-cellicon" aria-hidden="true"><use href="#ei-collective"></use></svg><span class="evo-cell-title">Knowledge &amp; skill commons</span><span class="evo-cell-desc">One agent's discovery becomes a zero-shot capability for all.</span></div>
<div class="evo-cell evo-harness"><span class="evo-cell-tag">Agent Harness</span><svg class="evo-ic evo-cellicon" aria-hidden="true"><use href="#ei-tuning"></use></svg><span class="evo-cell-title">Platform harness flywheel</span><span class="evo-cell-desc">Aggregate failures upgrade everyone's default harness.</span></div>
<div class="evo-cell evo-weights"><span class="evo-cell-tag">Model Weights</span><svg class="evo-ic evo-cellicon" aria-hidden="true"><use href="#ei-continual"></use></svg><span class="evo-cell-title">Checkpoint bootstrapping</span><span class="evo-cell-desc">Verified traces feed future model training.</span></div>
<div class="evo-rowlabel"><svg class="evo-ic evo-rowicon" aria-hidden="true"><use href="#ei-row-sessions"></use></svg><span class="evo-rowlabel-text">Across Sessions</span></div>
<div class="evo-cell evo-files"><span class="evo-cell-tag">External Files</span><svg class="evo-ic evo-cellicon" aria-hidden="true"><use href="#ei-skills"></use></svg><span class="evo-cell-title">Skill library &amp; memory</span><span class="evo-cell-desc">Skills, notes &amp; assets that carry across sessions.</span></div>
<div class="evo-cell evo-harness"><span class="evo-cell-tag">Agent Harness</span><svg class="evo-ic evo-cellicon" aria-hidden="true"><use href="#ei-pharness"></use></svg><span class="evo-cell-title">Compiled domain harness</span><span class="evo-cell-desc">Prompts &amp; routing graphs compiled for a project or codebase.</span></div>
<div class="evo-cell evo-weights"><span class="evo-cell-tag">Model Weights</span><svg class="evo-ic evo-cellicon" aria-hidden="true"><use href="#ei-sliders"></use></svg><span class="evo-cell-title">Personalized fine-tuning</span><span class="evo-cell-desc">LoRA &amp; preference adaptation for one person.</span></div>
<div class="evo-rowlabel"><svg class="evo-ic evo-rowicon" aria-hidden="true"><use href="#ei-row-session"></use></svg><span class="evo-rowlabel-text">Single Session</span></div>
<div class="evo-cell evo-files"><span class="evo-cell-tag">External Files</span><svg class="evo-ic evo-cellicon" aria-hidden="true"><use href="#ei-scratch"></use></svg><span class="evo-cell-title">Temporary memory</span><span class="evo-cell-desc">Runtime notes, scratchpads &amp; retrieved context.</span></div>
<div class="evo-cell evo-harness"><span class="evo-cell-tag">Agent Harness</span><svg class="evo-ic evo-cellicon" aria-hidden="true"><use href="#ei-dynamic"></use></svg><span class="evo-cell-title">Dynamic task adaptation</span><span class="evo-cell-desc">On-the-fly prompt or step-order adjustment.</span></div>
<div class="evo-cell evo-weights"><span class="evo-cell-tag">Model Weights</span><svg class="evo-ic evo-cellicon" aria-hidden="true"><use href="#ei-chip"></use></svg><span class="evo-cell-title">Rare online adaptation</span><span class="evo-cell-desc">Snapshot tuning mid-run — powerful but seldom used.</span></div>
<div class="evo-xaxis"><span class="evo-xaxis-title">What to update?</span><span class="evo-xaxis-scale"><span>cheaper &amp; shallower</span><span class="evo-xaxis-bar"></span><span>deeper &amp; costlier</span></span></div>
</div>
<figcaption><strong>Figure 3.</strong> The taxonomy as a visual map: update lifetime on one axis, updated substrate on the other. An expandable version with the concrete systems behind every cell lives in the <a href="#appendix-the-complete-landscape">appendix</a>.</figcaption>
</figure>

This matrix is not meant to be a rigid classification. In real systems, the cells interact. A temporary tool created in one session can become a persistent skill across sessions. A project-specific workflow can become a product default. A pattern discovered across millions of user failures can eventually become a model checkpoint.

## Single Session: Online Adaptation

The first time scale is intra-trajectory. How does an agent use a live execution trace to correct itself on the fly?

### Level 3: Working Memory and Context Paging

Inside a single session, the hard case is the long-horizon task: the agent must preserve the evidence, constraints, and partial discoveries that matter while continuing to act. External files and state turn the live trace into editable working memory rather than a passive transcript.

The solution is active state management. **MemGPT** is the canonical example here, reframing the context window as constrained RAM and external memory as virtual storage <d-cite key="memgpt2023"></d-cite>. **Recursive Language Models** make a complementary move: they treat prompt context less like a flat input string and more like a temporary working artifact, something that can be split, routed, summarized, and recombined during a task <d-cite key="rlm2025"></d-cite>.

**The caveat: Storage is not evolution.** Simply dumping context into an external database is meaningless if lossy retrieval quietly injects causal drift into the reasoning chain. A memory system only qualifies as adaptive if it improves the efficiency frontier rather than shifting the bottleneck from context length to retrieval noise.

### Level 2: Dynamic Orchestration

At the harness layer, the agent rewires its execution plan at runtime.

A static workflow dictates: *Call Tool A $\rightarrow$ Call Tool B $\rightarrow$ Summarize*.

A dynamic workflow adapts: *Tool A failed twice $\rightarrow$ inject a diagnostic node; the API wrapper is missing $\rightarrow$ synthesize a temporary function and mount it into the execution DAG.*

**Claude Code's Dynamic Workflows** make this literal: the execution plan leaves the conversation entirely. Claude writes a JavaScript orchestration script, and a separate runtime executes it in the background across subagents <d-cite key="anthropicdynamicworkflows2026"></d-cite>. The control flow - loops, branching, fan-out, error handling, resumability, and intermediate state - is compiled dynamically for that specific task.

The generated script may be temporary, but for that session, the agent has fundamentally expanded its own action space.

### Level 1: Test-Time Training

The most aggressive online adaptation modifies the model itself during inference. In-Place Test-Time Training shows the core idea for LLMs: instead of relying only on frozen inference, the system updates a small set of fast weights using the current context stream <d-cite key="inplacettt2026"></d-cite>.

This is still a training/deployment pipeline, not the disappearance of training. The boundary becomes update-bearing: deployment can contain local learning loops. TTT is the upper edge of self-evolution because the agent does not just remember a discovery. It alters the machinery that generates discoveries.

This exposes a deeper mathematical reality: the boundary between external context (Level 3) and parametric weights (Level 1) is porous. When external memory enters the prompt, the model does not merely read text; each token is projected into key/value vectors and stored in the KV cache for later tokens to attend to. In standard attention, $\text{Attention}(Q, K, V) = \text{softmax}(QK^T / \sqrt{d_k})V$; appending experience changes the active $K$ and $V$ set even if the trained weights stay fixed <d-cite key="vaswani2017attention"></d-cite>. At runtime, memory is not merely a database. It is a transient substrate for computation.

<details class="evo-aside" markdown="1">
<summary>Technical aside: context, KV cache, and weights</summary>
<div class="evo-aside-body" markdown="1">

- **Context** is the symbolic input surface: prompt text, retrieved documents, scratchpad notes, code snippets, and prior turns.
- **KV cache** is the runtime activation state created from that context. The model's fixed weights project each context token into key and value vectors; future query vectors attend over those cached vectors. This is why adding a memory paragraph is not just adding text. It changes the tensor state that subsequent computation reads from.
- **Model weights** are durable parameters learned across training. Test-time training changes these parameters directly or changes weight-like internal state. By contrast, ordinary context only creates temporary activations. The boundary becomes blurry because fast-weight and linear-attention interpretations show that accumulated sequence state can behave like a short-lived memory matrix <d-cite key="lineartransformersrnn2020,linearfastweights2021"></d-cite>.

So the claim is not that a prompt literally edits the trained checkpoint. The narrower claim is that context becomes operational state inside the forward pass, and that state can function as a transient, computation-shaping memory.

</div>
</details>

## Across Sessions: Longitudinal Alignment

The second time scale is inter-session. How does an agent internalize the structural patterns of a specific user, project, or codebase over days and weeks?

### Level 3: Persistent Memory & Skills

The most practical inter-session mechanism is caching both executable behaviors and structured context. **Voyager** pioneered the executable side in simulated environments by accumulating an ever-growing library of Minecraft skills, storing complex routines as code to be retrieved later <d-cite key="voyager2023"></d-cite>. Today, frameworks like **OpenHands** bring the same pattern into software engineering through persistent skill directories and installable skill lifecycles <d-cite key="openhandskills2026"></d-cite>.

For a personal coding agent, this means saving an arcane project test command or verified API wrapper, but it also means maintaining a project memory file such as `.cursorrules`, `CLAUDE.md`, or `AGENTS.md` that records architecture, conventions, and constraints. The system transitions from generic semantic search to precise asset reuse. The agent simply stops paying the inference tax of rediscovering the exact same context or solution twice.

### Level 2: Meta-Programming

When an agent repeatedly solves the same class of problems, it should not reconstruct its execution plan from scratch. High-performing historical trajectories must be mined to optimize the harness itself.

This is the domain of meta-programming. **DSPy** treats language-model programs as optimizable computational graphs, tuning instructions, few-shot demonstrations, and routing rules against an evaluation metric <d-cite key="dspy2023"></d-cite>. The mechanism here is structural: a bloated, verbose explicit context collapses into a lean, project-specific DAG (Directed Acyclic Graph).

### Level 1: Personal Adapters

At the parametric layer, inter-session evolution compresses implicit preferences - coding style, API choices, verbosity tolerance, and problem-solving habits - into parameter-efficient adapters. If a preference becomes parametric, the model no longer needs explicit instructions; it becomes instinct.

This is the shift from a generic foundation model to a personalized intelligence. A static foundation model is inherently a generic, one-size-fits-all reasoner. Cross-session adapter updates let the agent specialize toward a user's recurring workflows and problem-solving habits. It ceases to just solve problems; it learns to solve them *your way*.

However, while file and harness updates are already widespread in production, scalable per-user parametric adaptation remains an active systems research frontier. It complicates serving, batching, evaluation, privacy, and update governance at user scale.

## Across Users: Population-Level Evolution

The third time scale is population-level. How does a system aggregate millions of isolated trajectories, failures, and human corrections to conquer the long tail of edge cases?

### Level 3: Collective Knowledge & Skill Commons

At the external-state layer, population-level evolution builds a **collective knowledge and skill commons**.

Just as human civilization scales by externalizing discoveries into shared books and libraries, a population of deployed agents draws on a common ecosystem of artifacts, hosted and curated at the platform level. This horizontal network effect splits into two halves:

- **Factual knowledge (the "what").** Shared environmental maps, constraints, and verified schemas. As agents across the population probe the same systems and APIs, their findings accrete into global knowledge banks of dependency behavior and failure modes that any later agent can query <d-cite key="agentkb2025,reasoningbank2025"></d-cite>.
- **Operational skills (the "how").** Executable tools and runtime procedures. When one agent wraps an undocumented API quirk into a reusable tool, it commits that script to a shared registry; the next agent retrieves it instantly, skipping the inference tax of rediscovering it by trial and error <d-cite key="composio2026,llamahub2024"></d-cite>.

This turns isolated execution into **horizontal compounding** - one agent's local discovery becomes a zero-shot capability for the entire population. The primary engineering challenge ceases to be capability and becomes **trust**: strict provenance and sandboxing to keep hallucinations and poisoned logic out of the shared commons.

### Level 2: Platform-Level Harness Flywheels

At the harness layer, population-scale evolution is not about optimizing one user's workflow - that happens locally, across sessions. It is the internal **platform flywheel** that upgrades the *default* harness shipped to every deployed agent.

When millions of agents fail, aggregate telemetry exposes structural bottlenecks rather than individual knowledge gaps. If ten thousand agents drift off-track on step seven of the same refactor, the root cause is rarely the base model's intelligence; it is a defect in the underlying orchestration - the default prompt, tool schema, retry policy, or control flow. So platform teams read the telemetry and wire universal fixes into the default harness: an explicit **plan mode** that anchors long-horizon tasks against context drift, an **autonomous execution loop** that lets the agent self-drive through routine continuation points, or a mandatory **test-and-verify loop** that silently runs generated code in a sandbox and repairs it until it passes before replying. Each patch ships to production and instantly raises the capability floor for every user.

The next step is automation: the harness itself becomes the optimization target. Platforms search over prompts, routing graphs, tool schemas, and recovery loops, promoting variants that improve reliability, cost, or latency. The harness stops being a static wrapper around a frozen model and becomes a continuously updating operating system.

### Level 1: Checkpoint Bootstrapping Toward Self-Improvement

At the parametric layer, population-level evolution is rarely real-time "continual learning" - updating a massive foundation model on the fly risks catastrophic forgetting. Instead it runs as an asynchronous data flywheel: Model $N$ becomes the data engine that bootstraps Model $N+1$.

Rather than relying on human annotation or static web scraping, deployed agents turn every population-level interaction into evolutionary material, and the loop runs on two tracks:

- **Pre-training (synthetic bootstrapping).** When Agent $N$ solves a novel task that a compiler or sandbox can *verify*, its reasoning trace is harvested and folded back into the training mixture for Model $N+1$. The agent is effectively writing its own textbook.
- **Post-training (preference & RLHF).** Here the agent treats the human population as its environment rather than its annotator: a developer interrupting it, or hand-editing its output, marks a sharp boundary of failure. Aggregated over millions of such friction points, these signals drive preference optimization (RLHF/DPO) that teaches the next generation exactly where the current one's reasoning breaks down. **Cursor** is the canonical public example - its online RL on tab autocomplete turns ordinary accept, reject, and edit behavior into reward <d-cite key="cursortabrl2025"></d-cite>.

The paradigm shifts here: deployment stops being the *end* of the training pipeline and becomes its engine - the agent's own trial, error, and friction with reality are the fuel that forges its successor.

**A note on autonomy.** This flywheel is not yet fully closed. Today agents are prolific *proposers* - of trajectories, tools, and corrections - while humans still verify and merge what gets promoted into the next checkpoint. Recursive self-improvement is the theoretical asymptote this loop bends toward as sandboxing and AI-driven evaluation mature, not today's baseline.

## What Is the 'Self' Here?

The 3x3 matrix is built for today's engineering reality, but it hides a bias: it is largely organized around a **human-facing product frame**. Sessions, user habits, population telemetry - these are the surfaces where current products observe adaptation pressure. In that paradigm, the system is undergoing **human-driven adaptation**. The "self" is still scaffolded by us.

To see the first-principles shape of *true* self-evolution, hold the substrate columns fixed and re-derive the time axis from the agent's own world. A fully autonomous intelligence has no "sessions" or "users" - it has objectives, environments, and peers. The three horizons of adaptation fall out directly.

<figure class="self-evolving-figure frame-shift-figure">
<div class="evo-shift">
<div class="evo-shift-heads"><div class="evo-shift-head evo-shift-head-from">Product frame<span>human-facing surfaces</span></div><div></div><div class="evo-shift-head evo-shift-head-to">Agent frame<span>the triggers it derives</span></div></div>
<div class="evo-shift-row evo-files">
<div class="evo-shift-from"><svg class="evo-ic" aria-hidden="true"><use href="#ei-row-session"></use></svg><div><div class="evo-shift-from-name">Single Session</div><div class="evo-shift-from-sub">your prompts</div></div></div>
<div class="evo-shift-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h15"></path><path d="M13 6l6 6-6 6"></path></svg></div>
<div class="evo-shift-to"><div class="evo-shift-to-ic"><svg class="evo-ic" aria-hidden="true"><use href="#ei-target"></use></svg></div><div><div class="evo-shift-to-name">Intra-Task <span>&middot; Execution Horizon</span></div><div class="evo-shift-to-trigger">trigger: environmental feedback</div></div></div>
</div>
<div class="evo-shift-row evo-harness">
<div class="evo-shift-from"><svg class="evo-ic" aria-hidden="true"><use href="#ei-row-sessions"></use></svg><div><div class="evo-shift-from-name">Across Sessions</div><div class="evo-shift-from-sub">user habits</div></div></div>
<div class="evo-shift-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h15"></path><path d="M13 6l6 6-6 6"></path></svg></div>
<div class="evo-shift-to"><div class="evo-shift-to-ic"><svg class="evo-ic" aria-hidden="true"><use href="#ei-globe"></use></svg></div><div><div class="evo-shift-to-name">Inter-Task <span>&middot; Environmental Horizon</span></div><div class="evo-shift-to-trigger">trigger: domain structure &amp; dependencies</div></div></div>
</div>
<div class="evo-shift-row evo-weights">
<div class="evo-shift-from"><svg class="evo-ic" aria-hidden="true"><use href="#ei-row-users"></use></svg><div><div class="evo-shift-from-name">Across Users</div><div class="evo-shift-from-sub">population telemetry</div></div></div>
<div class="evo-shift-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h15"></path><path d="M13 6l6 6-6 6"></path></svg></div>
<div class="evo-shift-to"><div class="evo-shift-to-ic"><svg class="evo-ic" aria-hidden="true"><use href="#ei-swarm"></use></svg></div><div><div class="evo-shift-to-name">Inter-Agent <span>&middot; Swarm Horizon</span></div><div class="evo-shift-to-trigger">trigger: peer discovery &amp; self-play</div></div></div>
</div>
</div>
<figcaption><strong>Figure 4.</strong> The same three horizons, re-derived from the agent's own frame of reference. The trigger for adaptation shifts from product/user interaction to the agent's environment, domain, and peers.</figcaption>
</figure>

- **Single Session $\rightarrow$ Intra-Task (the execution horizon).** Adaptation bounded by one objective. The agent hits a blocker and pages its own context (Level 3), forges an ad-hoc tool (Level 2), or nudges weights mid-inference (Level 1) - driven by *environmental feedback*, not a user prompt. When the objective closes, the horizon closes.
- **Across Sessions $\rightarrow$ Inter-Task (the environmental horizon).** Adaptation bounded by a domain. The agent does not learn "a user's preference"; it internalizes the physics, constraints, and dependencies of an environment - a sprawling legacy codebase, a live API ecosystem - and compiles its own trial-and-error into durable abstractions.
- **Across Users $\rightarrow$ Inter-Agent (the swarm horizon).** Adaptation distributed across a population of agents. The network effect is no longer millions of human log-ins but millions of parallel runtimes: when one node discovers a tool or a leaner routing DAG, the update is validated and propagated to the collective. Early agent-native platforms like **EinsteinArena** already run a version of this loop in the wild - autonomous agents borrowing and building on each other's results without a human explicitly supplying the trigger <d-cite key="einsteinarena2026"></d-cite>.

These horizons are no cleaner than the matrix's cells. An intra-task discovery can be promoted to the swarm, exactly as a throwaway script became a shared skill in the sections above; the boundaries stay porous all the way up.

Structuring evolution around human users is how we must build today. But it is strictly transitional. As long as human interaction remains the primary environment that forces an AI to adapt, our typing speed, comprehension limits, and sleep schedules stay the hard ceiling on its capability. The true inflection point arrives when the human leaves the critical loop, and the driver of evolution becomes **open-ended exploration** - self-play where the problem admits an opponent, generate-and-test where it does not.

Imagine a network of autonomous agents set loose on an unsolved physics problem or the design of a next-generation operating system. They generate synthetic hypotheses, build their own sandboxes to test them, and distribute what survives - executable tools, optimized reasoning pathways, or weight updates - across a global collective intelligence. Their experience compounds at the speed of compute, not the speed of human typing.

By architecting systems that can rewrite their own external state, cognitive harness, and parametric core, we stop engineering smarter Copilots. We begin laying the structural foundation for an intelligence that can finally evolve *itself*.

## Appendix: The Complete Landscape

The main essay keeps one or two anchor examples per cell. This appendix restores the broader map: the same 3x3 matrix, but with more systems, mechanisms, and caveats.

The placement rule is simple: if an example changes the reader's understanding of the core mechanism, it belongs in the main text; if it primarily broadens coverage, it belongs here. Several systems also cut across cells:

- **External state becoming harness:** skills begin as files, but become control logic once the runtime discovers, loads, and routes through them. Anthropic Agent Skills, OpenHands skills, and Memento-Skills all sit on this boundary <d-cite key="anthropicagentskills2026,openhandskills2026,mementoskills2026"></d-cite>.
- **External state becoming transient parameters:** retrieved context is not just "read" by the model; it becomes key-value tensors in the active computation. Linear attention and fast-weight interpretations make this boundary especially explicit <d-cite key="lineartransformersrnn2020,linearfastweights2021"></d-cite>.
- **Local discoveries becoming global defaults:** a temporary script can become a user skill, a user skill can become a shared registry asset, and a repeated population-level failure can become a harness or checkpoint update.

The grid below is the same map as Figure 3, now expandable: open any cell for the concrete systems, mechanisms, and caveats behind that part of the matrix.

<details class="appendix-cell" markdown="1" data-when="single-session" data-layer="files">
<summary><span class="appendix-cell-title">Single Session / Level 3</span><span class="appendix-cell-subtitle">Working Memory and Context Paging</span></summary>

This cell covers state that is created, compressed, retrieved, or discarded inside one active trajectory.

- **MemGPT** frames the context window as constrained RAM and external storage as virtual memory, making memory movement an explicit systems problem <d-cite key="memgpt2023"></d-cite>.
- **MEMENTO** teaches models to manage their own context by segmenting, compressing, and evicting intermediate reasoning blocks <d-cite key="memento2026"></d-cite>.
- **Memory-as-Action** treats memory editing as a learnable action policy instead of a fixed heuristic <d-cite key="memoryasaction2025"></d-cite>.
- **AMA-Bench** highlights the core failure mode: long-horizon memory can introduce retrieval drift, so memory systems must be evaluated on causal usefulness rather than storage volume <d-cite key="amabench2026"></d-cite>.
- **Lost in the Middle** explains why this matters even when context windows are large: attention over long context is positionally and semantically brittle <d-cite key="liu2023lostmiddle"></d-cite>.

**Mechanism:** compress the live trace into structured memory, page low-salience information out of active context, and rehydrate only the pieces needed for the next decision.

**Caveat:** a larger memory store is not automatically an evolved agent. Without reliable write policy, retrieval policy, and evaluation, memory becomes another noisy tool.

</details>

<details class="appendix-cell" markdown="1" data-when="single-session" data-layer="harness">
<summary><span class="appendix-cell-title">Single Session / Level 2</span><span class="appendix-cell-subtitle">Dynamic Orchestration and Ad-Hoc Tools</span></summary>

This cell covers runtime changes to the control path: the agent changes how it acts before the current task is over.

- **Claude Code Dynamic Workflows** move orchestration from the chat transcript into a JavaScript script executed by a separate workflow runtime, allowing loops, branching, subagent fan-out, resumability, and intermediate variables to live outside the model context <d-cite key="anthropicdynamicworkflows2026"></d-cite>.
- **OpenClaw-RL** treats conversational feedback and next-state observations as a training signal for agents, making runtime experience a direct source of policy improvement <d-cite key="openclawrl2026"></d-cite>.
- **Large Language Models as Tool Makers** shows agents generating tools that other agents can use, expanding the action space without modifying the base model <d-cite key="latm2023"></d-cite>.
- **AlphaEvolve** generalizes this idea to scientific and algorithmic discovery, where generated programs become candidates in an iterative search loop <d-cite key="alphaevolve2025"></d-cite>.
- **Recursive Language Models** blur Level 2 and Level 3 by using recursive subcalls over context snippets as a control strategy for manipulating external context <d-cite key="rlm2025"></d-cite>.

**Mechanism:** turn the live trace into executable control state: scripts, temporary tools, diagnostic branches, repair loops, and subagent coordination plans.

**Caveat:** dynamic orchestration creates power and risk at the same time. The more the control layer can rewrite itself, the more the runtime needs isolation, provenance, cost bounds, and rollback.

</details>

<details class="appendix-cell" markdown="1" data-when="single-session" data-layer="weights">
<summary><span class="appendix-cell-title">Single Session / Level 1</span><span class="appendix-cell-subtitle">Test-Time Training and Fast Weights</span></summary>

This cell covers parametric or quasi-parametric adaptation during inference.

- **In-Place Test-Time Training** studies direct updates to model parameters during inference, making deployment itself part of the learning loop <d-cite key="inplacettt2026"></d-cite>.
- **Learning to Discover at Test Time** explores updating model behavior on the exact problem instance rather than only searching longer with frozen weights <d-cite key="tttdiscover2026"></d-cite>.
- **TTT Layers** reinterpret sequence modeling as a learned test-time update process, where hidden states behave like expressive memory substrates <d-cite key="tttlayers2024"></d-cite>.
- **Linear Transformers Are Secretly Fast Weight Programmers** makes the fast-weight interpretation explicit: sequence history can write temporary associations into a memory matrix <d-cite key="linearfastweights2021"></d-cite>.
- **Transformers are RNNs** and **Mamba** show adjacent forms of recurrent state accumulation, making the boundary between context, state, and weights less clean than the standard frozen-transformer picture suggests <d-cite key="lineartransformersrnn2020,mamba2023"></d-cite>.

**Mechanism:** use the current problem instance to change the computation itself: gradient updates, learned hidden-state updates, fast-weight memory, or recurrent state accumulation.

**Caveat:** this is the most powerful and operationally expensive online adaptation cell. It demands tight evaluation because a useful local update can also create regressions.

</details>

<details class="appendix-cell" markdown="1" data-when="across-sessions" data-layer="files">
<summary><span class="appendix-cell-title">Across Sessions / Level 3</span><span class="appendix-cell-subtitle">Persistent Skills and User Memory</span></summary>

This cell covers state that survives across sessions for one user, project, codebase, or environment.

- **Voyager** accumulates executable Minecraft skills and retrieves them for future tasks, giving a clear early example of skill-library growth <d-cite key="voyager2023"></d-cite>.
- **Anthropic Agent Skills** package reusable procedures into discoverable folders that an agent can load when relevant <d-cite key="anthropicagentskills2026"></d-cite>.
- **OpenHands Skills and Context** supports persistent skill installation, enabling skills to be managed, enabled, disabled, and reused across sessions <d-cite key="openhandskills2026"></d-cite>.
- **Memento-Skills** pushes the same idea toward agents that design and improve agent skills themselves <d-cite key="mementoskills2026"></d-cite>.
- **Hermes Agent** sits in the same product/research direction: persistent agent capability surfaces that can be reused across tasks <d-cite key="hermesagent2026"></d-cite>.

**Mechanism:** convert repeated discoveries into durable artifacts: scripts, commands, wrappers, procedures, project conventions, and environment-specific recipes.

**Caveat:** persistent skills need lifecycle management. Stale skills can be worse than no skills, especially when project dependencies, APIs, or security constraints change.

</details>

<details class="appendix-cell" markdown="1" data-when="across-sessions" data-layer="harness">
<summary><span class="appendix-cell-title">Across Sessions / Level 2</span><span class="appendix-cell-subtitle">Meta-Programming and Workflow Optimization</span></summary>

This cell covers changes to the user's or project's recurring execution graph.

- **DSPy** treats language-model programs as optimizable graphs rather than hand-written prompts <d-cite key="dspy2023"></d-cite>.
- **MIPRO** optimizes instructions and demonstrations for multi-stage language-model programs <d-cite key="mipro2024"></d-cite>.
- **AgentOptimizer** uses agentic improvement loops to train or refine LLM agents <d-cite key="agentoptimizer2023"></d-cite>.
- **Agentic Context Engineering (ACE)** studies evolving context for self-improving language models, moving context design from manual prompt craft toward an updateable system component <d-cite key="ace2025"></d-cite>.

**Mechanism:** mine historical trajectories, identify high-performing execution patterns, and compile them into reusable prompts, routers, DAGs, tool schemas, and workflows.

**Caveat:** harness optimization can overfit to yesterday's tasks. Good systems need evaluation sets that represent the future operating distribution, not just the past transcript.

</details>

<details class="appendix-cell" markdown="1" data-when="across-sessions" data-layer="weights">
<summary><span class="appendix-cell-title">Across Sessions / Level 1</span><span class="appendix-cell-subtitle">Personal Adapters and Preference Alignment</span></summary>

This cell covers parametric personalization over repeated interactions with one user or organization.

- **OPPU** explores democratized personalized parameter-efficient fine-tuning <d-cite key="oppu2024"></d-cite>.
- **Profile-to-PEFT** uses profile-derived signals to produce fast personalized adaptation <d-cite key="profiletopeft2025"></d-cite>.
- **PERSOMA** studies personalized soft-prompt adapters for personalized language prompting <d-cite key="persoma2024"></d-cite>.

**Mechanism:** compress stable preferences into adapters, soft prompts, LoRA-style modules, or other parameter-efficient personalization layers.

**Caveat:** personalization must separate durable preference from accidental context. A user accepting one terse answer should not permanently train the model to be terse in every domain.

</details>

<details class="appendix-cell" markdown="1" data-when="across-users" data-layer="files">
<summary><span class="appendix-cell-title">Across Users / Level 3</span><span class="appendix-cell-subtitle">Collective Knowledge and Skill Commons</span></summary>

This cell covers shared external state - registries, knowledge banks, and artifact graphs - accumulated from the whole population's interactions.

- **Composio** and **LlamaHub** are practical infrastructure for shared, executable tools: a wrapper or integration written once becomes an installable asset for other agents <d-cite key="composio2026,llamahub2024"></d-cite>.
- **Agent KB** studies how cross-domain experience can be reused for agentic problem solving <d-cite key="agentkb2025"></d-cite>.
- **ReasoningBank** collects reasoning memories to scale agent self-evolution <d-cite key="reasoningbank2025"></d-cite>.
- **FunSearch** shows a collective program-search loop in which generated programs are evaluated, selected, and reused for further discovery <d-cite key="funsearch2023"></d-cite>.
- **Alita-G** explores self-evolving generative agents for agent generation, making agent-building artifacts themselves part of the evolving substrate <d-cite key="alitag2025"></d-cite>.

**Mechanism:** validate and promote local discoveries into shared assets: tools, integrations, reasoning traces, API wrappers, benchmark solutions, and capability graphs.

**Caveat:** the trust problem dominates this cell. A global skill bank without provenance, sandboxing, and eval gates can become a supply-chain vulnerability or a hallucination amplifier.

</details>

<details class="appendix-cell" markdown="1" data-when="across-users" data-layer="harness">
<summary><span class="appendix-cell-title">Across Users / Level 2</span><span class="appendix-cell-subtitle">Platform Harness Flywheels and Automated Design</span></summary>

This cell covers population-level improvement to the default agent process itself.

- **Platform-shipped harness defaults** turn population telemetry into upgrades baked into every agent's default harness - an explicit plan mode for long-horizon tasks, autonomous execution loops, and a mandatory test-and-verify step that sandboxes generated code before replying.
- **Darwin Gödel Machine** explores open-ended evolution of self-improving coding agents <d-cite key="dgm2025"></d-cite>.
- **Hyperagents** make the meta-level improvement procedure itself editable, so the system searches not only for better agents but for better ways to generate better agents <d-cite key="hyperagents2026"></d-cite>.

**Mechanism:** mine aggregate failure logs, identify structural bottlenecks in prompts/tools/workflows, and wire the fixes into the default harness - shipped directly by platform teams, or discovered automatically by meta-agents that propose, test, and deploy better control flows.

**Caveat:** harness updates are product updates. They require regression testing, rollout controls, and auditability because one bad default policy can affect every downstream user.

</details>

<details class="appendix-cell" markdown="1" data-when="across-users" data-layer="weights">
<summary><span class="appendix-cell-title">Across Users / Level 1</span><span class="appendix-cell-subtitle">Checkpoint Bootstrapping and Self-Improvement Frontier</span></summary>

This cell covers model updates derived from population-scale interaction data.

- **Cursor Tab online RL** turns natural developer behavior - accepting, rejecting, or editing autocomplete suggestions - into reward signals for improving the autocomplete model <d-cite key="cursortabrl2025"></d-cite>.
- Chat-style products provide adjacent feedback channels: thumbs-up/down, regenerations, follow-up corrections, conversation abandonment, and accepted edits. These are not all equally clean rewards, but together they form a data flywheel for future alignment and checkpoint updates.
- Academic and industrial continual-learning loops increasingly treat deployed interaction as the environment rather than a post-hoc evaluation set.

**Mechanism:** aggregate implicit and explicit feedback into preference data, reward models, reinforcement-learning updates, supervised fine-tuning corpora, and future checkpoint releases.

**Caveat:** this is usually not fully autonomous self-evolution today. Humans still shape reward design, filter data, approve deployments, and evaluate regressions. The self-evolving part is the data flywheel; the governance layer remains human-heavy.

</details>

<script>
(function () {
  function init() {
    var details = Array.prototype.slice.call(document.querySelectorAll("details.appendix-cell"));
    if (!details.length || !document.getElementById("ei-collective")) return;
    var ROWS = [
      { key: "across-users", label: "Across Users", icon: "ei-row-users" },
      { key: "across-sessions", label: "Across Sessions", icon: "ei-row-sessions" },
      { key: "single-session", label: "Single Session", icon: "ei-row-session" }
    ];
    var COLS = [
      { key: "files", name: "External Files", sub: "memory / knowledge / skills", cls: "evo-files" },
      { key: "harness", name: "Agent Harness", sub: "workflow / prompts / tools", cls: "evo-harness" },
      { key: "weights", name: "Model Weights", sub: "parametric memory / core", cls: "evo-weights" }
    ];
    var ICONS = {
      "across-users": { files: "ei-collective", harness: "ei-tuning", weights: "ei-continual" },
      "across-sessions": { files: "ei-skills", harness: "ei-pharness", weights: "ei-sliders" },
      "single-session": { files: "ei-scratch", harness: "ei-dynamic", weights: "ei-chip" }
    };
    function svgIcon(id, cls) {
      return '<svg class="' + cls + '" aria-hidden="true"><use href="#' + id + '"></use></svg>';
    }
    var grid = document.createElement("div");
    grid.className = "evo-matrix evo-matrix-app";
    function add(el, mo) {
      el.style.setProperty("--mo", String(mo));
      grid.appendChild(el);
    }
    var corner = document.createElement("div");
    corner.className = "evo-corner";
    add(corner, 0);
    COLS.forEach(function (c, i) {
      var h = document.createElement("div");
      h.className = "evo-colhead " + c.cls;
      h.innerHTML = '<span class="evo-colhead-name">' + c.name + '</span><span class="evo-colhead-sub">' + c.sub + "</span>";
      add(h, i + 1);
    });
    var openCell = null;
    var byId = {};
    function setOpen(entry, on) {
      entry.btn.setAttribute("aria-expanded", on ? "true" : "false");
      entry.panel.hidden = !on;
    }
    function toggle(entry) {
      if (openCell === entry) {
        setOpen(entry, false);
        openCell = null;
        return;
      }
      if (openCell) setOpen(openCell, false);
      openCell = entry;
      setOpen(entry, true);
      if (history.replaceState) history.replaceState(null, "", "#" + entry.panel.id);
    }
    var mo = 4;
    ROWS.forEach(function (row) {
      var rl = document.createElement("div");
      rl.className = "evo-rowlabel";
      rl.innerHTML = svgIcon(row.icon, "evo-ic evo-rowicon") + '<span class="evo-rowlabel-text">' + row.label + "</span>";
      add(rl, mo);
      var panels = [];
      COLS.forEach(function (col, ci) {
        var det = null;
        details.forEach(function (d) {
          if (d.getAttribute("data-when") === row.key && d.getAttribute("data-layer") === col.key) det = d;
        });
        if (!det) return;
        var titleEl = det.querySelector(".appendix-cell-title");
        var subEl = det.querySelector(".appendix-cell-subtitle");
        var subtitle = subEl ? subEl.textContent.trim() : "";
        var level = "";
        if (titleEl && titleEl.textContent.indexOf("/") > -1) level = titleEl.textContent.split("/")[1].trim();
        var names = [];
        var items = det.querySelectorAll("li");
        for (var j = 0; j < items.length && names.length < 3; j++) {
          var s = items[j].querySelector("strong");
          if (s) names.push(s.textContent.replace(/\s+/g, " ").trim());
        }
        var sys = names.length ? names.join(" · ") + (items.length > names.length ? " · …" : "") : "";
        var id = "matrix-" + row.key + "-" + col.key;
        var btn = document.createElement("button");
        btn.type = "button";
        btn.className = "evo-cell evo-cell-btn " + col.cls;
        btn.setAttribute("aria-expanded", "false");
        btn.setAttribute("aria-controls", id);
        btn.innerHTML =
          '<span class="evo-cell-tag">' + col.name + '</span>' +
          '<span class="evo-cell-top">' + svgIcon(ICONS[row.key][col.key], "evo-ic evo-cellicon") + '<span class="evo-cell-plus" aria-hidden="true"></span></span>' +
          '<span class="evo-cell-title">' + subtitle + "</span>" +
          (sys ? '<span class="evo-cell-systems">' + sys + "</span>" : "");
        var panel = document.createElement("div");
        panel.className = "evo-panel " + col.cls + " evo-from-" + (ci + 1);
        panel.id = id;
        panel.hidden = true;
        var head = document.createElement("p");
        head.className = "evo-panel-head";
        head.innerHTML = "<strong>" + row.label + (level ? " · " + level : "") + "</strong> — " + subtitle;
        panel.appendChild(head);
        var summary = det.querySelector("summary");
        if (summary) summary.parentNode.removeChild(summary);
        while (det.firstChild) panel.appendChild(det.firstChild);
        var entry = { btn: btn, panel: panel };
        byId[id] = entry;
        btn.addEventListener("click", function () { toggle(entry); });
        add(btn, mo + 1 + ci * 2);
        panels.push({ panel: panel, mo: mo + 2 + ci * 2 });
      });
      panels.forEach(function (p) { add(p.panel, p.mo); });
      mo += 7;
    });
    details[0].parentNode.insertBefore(grid, details[0]);
    details.forEach(function (d) {
      if (d.parentNode) d.parentNode.removeChild(d);
    });
    var hash = location.hash ? location.hash.slice(1) : "";
    if (hash && byId[hash]) {
      toggle(byId[hash]);
      byId[hash].panel.scrollIntoView();
    }
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
</script>
