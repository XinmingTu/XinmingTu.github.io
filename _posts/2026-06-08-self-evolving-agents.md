---
layout: distill
title: "The What & When of Self-Evolving Agents"
description: "A 3×3 framework for understanding what evolves in AI agents and when those updates persist."
date: 2026-06-08
tags: ['AI', 'agents', 'deep-learning']

authors:
  - name: Xinming Tu
    url: "https://xinmingtu.cn"
    affiliations:
      name: University of Washington, Phylo
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
  d-article .evo-note {
    background: #fbfbfd;
    border: 1px solid #d7dae3;
    border-left: 4px solid #7a8196;
    border-radius: 8px;
    color: #3d4250;
    font-size: 0.92rem;
    line-height: 1.55;
    margin: 1rem 0 1.3rem;
    padding: 0.85rem 0.95rem;
  }
  d-article .evo-note > :first-child {
    margin-top: 0;
  }
  d-article .evo-note > :last-child {
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
  - name: "When Updates Persist"
  - name: "The 3×3 Evolution Matrix"
  - name: "Single Session: Online Adaptation"
  - name: "Across Sessions: Longitudinal Alignment"
  - name: "Across Users: Population-Level Evolution"
  - name: "What Is the 'Self' Here?"
  - name: "Discussion"
  - name: "Appendix: The Complete Landscape"
---

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

An agent's capabilities should not remain fixed after release. As agents accumulate experience from past attempts, tool results, and successful workflows, those capabilities should improve over time. The field is shifting toward **self-evolving systems**, driven by two promises:

- **Motivation 1: Marginal Cost Reduction.** As an agent accumulates execution experience, similar tasks should become cheaper. Past trajectories can be compressed into reusable assets, so the system stops paying the same "inference tax" twice: fewer inference tokens, fewer tool calls, fewer retries, and fewer human interventions per task family.

- **Motivation 2: Capability Ceiling Expansion.** Over time, an agent should not only get cheaper; it should bring harder tasks within reach. Static agents hit a ceiling on long-horizon work: errors compound, context decays, and brittle workflows break. Self-evolving systems can forge tools, cache progress, and revise strategy at runtime. They make autonomy a property of the architecture, not just a behavior in the transcript.

<figure class="self-evolving-figure tight-top medium">
  <img src="/assets/img/2026-06-08-self-evolving-agents/figure1-dual-promise.svg" alt="A chart showing self-evolving agents reducing cost per task while expanding capability over time.">
  <figcaption><strong>Figure 1.</strong> Agents accumulate experience, expanding the capability frontier while reducing marginal cost per task.</figcaption>
</figure>

Systems are moving beyond **stateless orchestration**. Instead of starting from scratch on every task, modern agent architectures can carry experience forward.

But "learning" is not magic. It must land somewhere.

The central question is simple: **what changes, and when does the update persist?**

The main text uses a few anchor examples to keep the argument readable; the appendix expands the full 3×3 landscape with additional systems, mechanisms, and caveats.

## What Evolves

Before asking how an agent evolves, we need to ask what can change. In practice, an agent's adaptive state is distributed across three plastic layers.

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
<figcaption><strong>Figure 2.</strong> Agents include model weights, the agent harness, and external files; all three can evolve.</figcaption>
</figure>

A natural way to enter this structure is from the core outward:

- **Layer 3: Model Weights.** The parametric core: knowledge and behavior encoded inside the model checkpoint. Examples include GPT-family, DeepSeek, or Qwen weights.
- **Layer 2: Agent Harness.** The control layer around the model: prompts, tools, routing, planning, recovery logic, and execution flow. In systems like Claude Code or Codex, this layer shows up as tool-use policies, edit-test-repair loops, workflow execution, subagents, and reusable skills.
- **Layer 1: External Files & State.** Writable artifacts the agent can read or update outside the model and harness. Examples include skills, memory files, `CLAUDE.md`, `AGENTS.md`, saved commands, project notes, and reusable scripts.

<details class="evo-aside" markdown="1">
<summary>Boundary note: when files become code</summary>

<div class="evo-aside-body" markdown="1">

The boundary between external state and harness logic is porous. A Python function, workflow file, routing rule, or recovery script may begin as an external artifact. The moment the runtime discovers it, loads it, and routes future tasks through it, that artifact becomes part of the harness.

External state no longer stores only facts. It can store skills, workflows, policies, and executable operators. **The same object can be a file at rest and harness logic in motion.**

</div>
</details>

## When Updates Persist

Once we know what can change, the next question is how long the change survives.

At the systems level, this is what learning from experience means: experience becomes state, and state changes future behavior.

A self-evolving agent does not discard execution traces at task end; it turns successes, tool errors, rejected actions, and user corrections into reusable state.

To map this loop, we cross the three update substrates with three horizons of persistence:

- **Single Session:** adaptation inside one live trajectory.
- **Across Sessions:** adaptation that persists for a user, project, codebase, or environment.
- **Across Users:** population-level adaptation from aggregate interactions.

## The 3×3 Evolution Matrix

The result is a 3×3 map: three persistence horizons crossed with three update substrates.

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
<div class="evo-cell evo-harness"><span class="evo-cell-tag">Agent Harness</span><svg class="evo-ic evo-cellicon" aria-hidden="true"><use href="#ei-pharness"></use></svg><span class="evo-cell-title">Compiled workflow harness</span><span class="evo-cell-desc">Past traces compile into reusable workflows.</span></div>
<div class="evo-cell evo-weights"><span class="evo-cell-tag">Model Weights</span><svg class="evo-ic evo-cellicon" aria-hidden="true"><use href="#ei-sliders"></use></svg><span class="evo-cell-title">Parametric personalization</span><span class="evo-cell-desc">Repeated use updates trainable parameters.</span></div>
<div class="evo-rowlabel"><svg class="evo-ic evo-rowicon" aria-hidden="true"><use href="#ei-row-session"></use></svg><span class="evo-rowlabel-text">Single Session</span></div>
<div class="evo-cell evo-files"><span class="evo-cell-tag">External Files</span><svg class="evo-ic evo-cellicon" aria-hidden="true"><use href="#ei-scratch"></use></svg><span class="evo-cell-title">Temporary memory</span><span class="evo-cell-desc">Runtime notes, scratchpads &amp; retrieved context.</span></div>
<div class="evo-cell evo-harness"><span class="evo-cell-tag">Agent Harness</span><svg class="evo-ic evo-cellicon" aria-hidden="true"><use href="#ei-dynamic"></use></svg><span class="evo-cell-title">Dynamic orchestration</span><span class="evo-cell-desc">Live traces create branches, tools, and repair loops.</span></div>
<div class="evo-cell evo-weights"><span class="evo-cell-tag">Model Weights</span><svg class="evo-ic evo-cellicon" aria-hidden="true"><use href="#ei-chip"></use></svg><span class="evo-cell-title">Rare online adaptation</span><span class="evo-cell-desc">Snapshot tuning mid-run — powerful but seldom used.</span></div>
<div class="evo-xaxis"><span class="evo-xaxis-title">What to update?</span><span class="evo-xaxis-scale"><span>cheaper &amp; shallower</span><span class="evo-xaxis-bar"></span><span>deeper &amp; costlier</span></span></div>
</div>
<figcaption><strong>Figure 3.</strong> The taxonomy as a visual map: update lifetime on one axis, update substrate on the other. An expandable version with the concrete systems behind every cell lives in the <a href="#appendix-the-complete-landscape">appendix</a>.</figcaption>
</figure>

The matrix shows possibility, not obligation: these are places self-evolution can land, not requirements every agent must satisfy.

## Single Session: Online Adaptation

The first horizon is the live trajectory: using feedback from the current run to improve the task before it ends.

Within one trajectory, experience can become working state: notes, branches, helpers, plans.

### Layer 1: Working Memory and Context Paging

Inside one session, external state turns the live trace into working memory: notes, constraints, partial discoveries, and retrieved context can be written out and pulled back when needed. **MemGPT** is the canonical example, treating the context window as constrained RAM and external memory as virtual storage <d-cite key="memgpt2023"></d-cite>.

### Layer 2: Dynamic Orchestration

At the harness layer, the agent rewires its execution plan at runtime.

A static workflow says: *call A → call B → summarize*.

A dynamic workflow adapts: *A failed twice → insert diagnosis; the wrapper is missing → synthesize one; the task branches → fan out*.

**Recursive Language Models** expose a lighter version of the same idea: recursive subcalls turn context processing into runtime control flow <d-cite key="rlm2025"></d-cite>.

**Claude Code's Dynamic Workflows** make this literal: the execution plan leaves the conversation. Claude writes a JavaScript orchestration script, and a separate runtime executes it in the background across subagents <d-cite key="anthropicdynamicworkflows2026"></d-cite>. Loops, branches, fan-out, error handling, resumability, and intermediate state are compiled for the task itself.

The script may be temporary, but within that session the agent has expanded its own action space.

### Layer 3: Test-Time Training

The most aggressive online adaptation modifies the model itself during inference. **TTT-Discover** makes this concrete: instead of only prompting a frozen model to search longer, the system trains at test time on feedback from the current problem <d-cite key="tttdiscover2026"></d-cite>.

This does not eliminate training; it moves part of the learning loop into deployment. TTT is the upper edge of online self-evolution: the agent does not merely remember a discovery; it alters the machinery that will generate the next one.

## Across Sessions: Longitudinal Alignment

The second horizon is longitudinal: adapting to recurring structure across the same user, project, workflow, or task family.

### Layer 1: Persistent Memory & Skills

The practical cross-session layer has two forms: memory and skills.

**Memory** preserves stable context across conversations: user preferences, project facts, long-term goals, or prior decisions. Chatbot memory is the familiar example: the assistant remembers facts about the user or workspace instead of asking again.

In coding agents, the same pattern often appears as repository-level instruction files such as `CLAUDE.md` and `AGENTS.md`, which carry durable project conventions across sessions.

**Skills** preserve repeatable procedures. A skill can be a saved command, a verified wrapper, a reusable script, or a demonstrated workflow. **Voyager** showed the executable version early by accumulating Minecraft skills as reusable code <d-cite key="voyager2023"></d-cite>. **OpenAI Codex Record & Replay** turns one demonstrated workflow into a reusable skill <d-cite key="openaicodexrecordreplay2026"></d-cite>.

### Layer 2: Meta-Programming

When an agent repeatedly solves the same class of problems, it should not reconstruct its execution plan from scratch. High-performing trajectories can be mined to optimize the harness itself.

This is meta-programming at the harness layer. **Meta-Harness** makes the idea literal: an outer-loop optimizer searches over harness code using prior candidates, scores, and execution traces <d-cite key="metaharness2026"></d-cite>. The structural move is compression: repeated execution patterns collapse into a lean, reusable execution DAG (Directed Acyclic Graph).

### Layer 3: Parametric Personalization

At the model-weights layer, repeated interaction changes trainable parameters themselves, not the memory store or harness. **OpenClaw-RL** points in this direction: conversational feedback becomes training signal for updating the agent's model weights <d-cite key="openclawrl2026"></d-cite>.

This is still frontier work. Most personalization should stay in files or harness logic; per-user weight adaptation complicates serving, batching, evaluation, privacy, and update governance.

## Across Users: Population-Level Evolution

The third horizon is population-level: using many users' trajectories, failures, and discoveries to improve shared assets, default harnesses, or future models after deployment.

### Layer 1: Collective Knowledge & Skill Commons

Human civilization scales by externalizing discovery into books, libraries, protocols, and tools. Agent populations can do the same: at the external-state layer, population-level evolution builds a shared commons of artifacts agents can query or reuse.

- **Knowledge** stores what was discovered: constraints, schemas, failure modes, proof ideas, or reusable mathematical constructions. If one agent finds a useful construction for an open math problem, the next agent should inherit the artifact rather than rediscover it <d-cite key="agentkb2025,reasoningbank2025"></d-cite>.
- **Skills** store how to act: shared tools, verified wrappers, repair recipes, and agent-published procedures. A skill-share system turns one agent's working script or wrapper into another agent's starting capability <d-cite key="anthropicagentskills2026"></d-cite>.

### Layer 2: Platform-Level Harness Flywheels

At the harness layer, population-scale evolution upgrades the default agent runtime. This is platform-level change: when Claude Code, Codex, or a similar agent ships plan mode, `/loop`, `/goal`, better tool schemas, or stronger recovery logic, every user inherits a better harness.

The signal comes from aggregate failures. If many agents fail at the same step, the fix may not be a smarter base model; it may be a better prompt, router, tool contract, retry policy, or verification loop. Over time, the harness itself becomes an optimization target.

### Layer 3: Checkpoint Bootstrapping Toward Self-Improvement

At the parametric layer, population-level evolution usually means checkpoint bootstrapping, not live continual learning. Deployed agents become data engines for future models.

**Pre-training / synthetic bootstrapping.** When an agent solves a novel task that a compiler, sandbox, or verifier can check, the verified trace can enter the pretraining data corpus for a future model.

**Post-training / RL.** Population behavior becomes preference and reward signal: accepts, rejects, edits, interruptions, and corrections show where the current model fails. **Cursor Tab**, Cursor's code autocomplete feature, is a concrete example: users' Tab accepts and edits provide RL signal for training the next policy <d-cite key="cursortabrl2025"></d-cite>.

Deployment stops being only the end of training; it becomes part of the training loop.

<div class="evo-note" markdown="1">

**A note on autonomy.** This loop is only partially automated today. Agents can generate traces, tools, and candidate fixes, but humans still design reward signals, curate data, run evaluations, and approve checkpoint promotions. Recursive self-improvement is the direction of travel, not today's baseline.

</div>

## What Is the 'Self' Here?

The 3×3 matrix above is still product-framed. Its time axis is defined by the surfaces through which today's agents meet humans: one session, repeated sessions, and many users. That framing is useful, but it does not fully answer what the "self" is.

An agent-centered view keeps the same three substrates, but re-labels the persistence horizons around what the agent actually encounters: tasks, environments, and peers.

<figure class="self-evolving-figure frame-shift-figure">
<div class="evo-shift">
<div class="evo-shift-heads"><div class="evo-shift-head evo-shift-head-from">Product frame<span>human-facing surfaces</span></div><div></div><div class="evo-shift-head evo-shift-head-to">Agent frame<span>the triggers it derives</span></div></div>
<div class="evo-shift-row evo-files">
<div class="evo-shift-from"><svg class="evo-ic" aria-hidden="true"><use href="#ei-row-session"></use></svg><div><div class="evo-shift-from-name">Single Session</div><div class="evo-shift-from-sub">your prompts</div></div></div>
<div class="evo-shift-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h15"></path><path d="M13 6l6 6-6 6"></path></svg></div>
<div class="evo-shift-to"><div class="evo-shift-to-ic"><svg class="evo-ic" aria-hidden="true"><use href="#ei-target"></use></svg></div><div><div class="evo-shift-to-name">Intra-Task <span>&middot; Execution Horizon</span></div><div class="evo-shift-to-trigger">trigger: environmental feedback</div></div></div>
</div>
<div class="evo-shift-row evo-harness">
<div class="evo-shift-from"><svg class="evo-ic" aria-hidden="true"><use href="#ei-row-sessions"></use></svg><div><div class="evo-shift-from-name">Across Sessions</div><div class="evo-shift-from-sub">persistent context</div></div></div>
<div class="evo-shift-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h15"></path><path d="M13 6l6 6-6 6"></path></svg></div>
<div class="evo-shift-to"><div class="evo-shift-to-ic"><svg class="evo-ic" aria-hidden="true"><use href="#ei-globe"></use></svg></div><div><div class="evo-shift-to-name">Inter-Task <span>&middot; Environmental Horizon</span></div><div class="evo-shift-to-trigger">trigger: domain structure &amp; dependencies</div></div></div>
</div>
<div class="evo-shift-row evo-weights">
<div class="evo-shift-from"><svg class="evo-ic" aria-hidden="true"><use href="#ei-row-users"></use></svg><div><div class="evo-shift-from-name">Across Users</div><div class="evo-shift-from-sub">population telemetry</div></div></div>
<div class="evo-shift-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h15"></path><path d="M13 6l6 6-6 6"></path></svg></div>
<div class="evo-shift-to"><div class="evo-shift-to-ic"><svg class="evo-ic" aria-hidden="true"><use href="#ei-swarm"></use></svg></div><div><div class="evo-shift-to-name">Inter-Agent <span>&middot; Swarm Horizon</span></div><div class="evo-shift-to-trigger">trigger: peer discovery &amp; self-play</div></div></div>
</div>
</div>
<figcaption><strong>Figure 4.</strong> The same three horizons, re-derived from the agent's frame of reference. The trigger for adaptation shifts from user interaction to environment, domain, and peers.</figcaption>
</figure>

- **Single Session → Intra-Task.** What looks like one user session is, for the agent, one objective being executed under feedback from tools, tests, and the environment.
- **Across Sessions → Inter-Task.** What looks like repeated user interaction is, for the agent, recurring structure across related tasks: kernel optimization, infrastructure tuning, API debugging, or work inside the same codebase.
- **Across Users → Inter-Agent.** What looks like population telemetry is, for the agent, a collective: discoveries, tools, and strategies propagating across peers.

## Discussion

Viewed this way, early systems already show pieces of recursive self-improvement across the matrix.

**autoresearch** shows a single-agent loop: an agent edits a training artifact, runs an experiment, keeps what improves, and repeats <d-cite key="autoresearch2026"></d-cite>. **EinsteinArena** shows a collective loop: agents work on open math problems with verifiers, leaderboards, and public discussion, so one agent's construction can become another agent's starting point <d-cite key="einsteinarena2026"></d-cite>.

The long-run question is how memory, skills, harness updates, and weight updates compose into systems where experience reliably becomes reusable capability.

By giving agents writable external state, editable harnesses, and eventually updatable weights, we stop building merely smarter copilots. We begin building the substrate for **intelligence that can evolve itself**.

## Appendix: The Complete Landscape

The main essay keeps one or two anchor examples per cell. This appendix restores the broader map: the same 3×3 matrix, expanded with more systems, mechanisms, design tradeoffs, and caveats.

For survey-level context, recent work organizes self-evolving agents around what evolves, when it evolves, and how it evolves <d-cite key="selfevolvingsurvey2025"></d-cite>.

The placement rule is simple: if an example changes the reader's understanding of the core mechanism, it belongs in the main text; if it primarily broadens coverage, it belongs here. Several patterns also cut across cells:

- **External state becoming harness:** skills begin as files, but become control logic once the runtime discovers them, loads them, and routes through them. Anthropic Agent Skills, OpenHands skills, and Memento-Skills all sit on this boundary <d-cite key="anthropicagentskills2026,openhandskills2026,mementoskills2026"></d-cite>.
- **External state becoming transient parameters:** retrieved context is not just "read" by the model; it becomes key-value tensors in the active computation. Linear attention and fast-weight interpretations make this boundary especially explicit <d-cite key="lineartransformersrnn2020,linearfastweights2021"></d-cite>.
- **Local discoveries becoming global defaults:** a temporary script can become a user skill; a user skill can become a shared registry asset; a repeated failure can become a harness or checkpoint update.

The grid below is the same map as Figure 3, now expandable: open any cell for the concrete systems, mechanisms, and caveats behind that part of the matrix.

<details class="appendix-cell" markdown="1" data-when="single-session" data-layer="files">
<summary><span class="appendix-cell-title">Single Session / Layer 1</span><span class="appendix-cell-subtitle">Working Memory and Context Paging</span></summary>

This cell covers state that is created, compressed, retrieved, or discarded inside one active trajectory.

- **MemGPT** frames the context window as constrained RAM and external storage as virtual memory, making memory movement an explicit systems problem <d-cite key="memgpt2023"></d-cite>.
- **MEMENTO** teaches models to manage their own context by segmenting intermediate reasoning and reasoning forward through compressed mementos <d-cite key="memento2026"></d-cite>.
- **Memory-as-Action** treats memory editing as a learnable action policy instead of a fixed heuristic <d-cite key="memoryasaction2025"></d-cite>.
- **AMA-Bench** highlights the core failure mode: similarity-based memory retrieval can miss causal and objective information, so memory systems must be evaluated on task usefulness rather than storage volume <d-cite key="amabench2026"></d-cite>.
- **Lost in the Middle** explains why this matters even when context windows are large: performance drops when relevant evidence sits in the middle of long context <d-cite key="liu2023lostmiddle"></d-cite>.

**Mechanism:** compress the live trace into structured memory, page low-salience information out of active context, and rehydrate only the pieces needed for the next decision.

**Caveat:** a larger memory store is not automatically an evolved agent. Without reliable write policy, retrieval policy, and evaluation, memory becomes another noisy tool.

</details>

<details class="appendix-cell" markdown="1" data-when="single-session" data-layer="harness">
<summary><span class="appendix-cell-title">Single Session / Layer 2</span><span class="appendix-cell-subtitle">Dynamic Orchestration and Ad-Hoc Tools</span></summary>

This cell covers runtime changes to the control path: the agent changes how it acts before the current task is over.

- **Claude Code Dynamic Workflows** move orchestration from the chat transcript into a JavaScript script executed by a separate workflow runtime, allowing loops, branching, subagent fan-out, resumability, and intermediate variables to live outside the model context <d-cite key="anthropicdynamicworkflows2026"></d-cite>.
- **Large Language Models as Tool Makers** is a boundary case: tool making can begin inside a task, while cached tool APIs make the generated functionality reusable across later requests <d-cite key="latm2023"></d-cite>.
- **Recursive Language Models** blur Layers 1 and 2 by using recursive subcalls over context snippets as a control strategy for manipulating external context <d-cite key="rlm2025"></d-cite>.

**Mechanism:** turn the live trace into executable control state: scripts, temporary tools, diagnostic branches, repair loops, and subagent coordination plans.

**Caveat:** dynamic orchestration creates power and risk at the same time. The more the control layer can rewrite itself, the more the runtime needs isolation, provenance, cost bounds, and rollback.

</details>

<details class="appendix-cell" markdown="1" data-when="single-session" data-layer="weights">
<summary><span class="appendix-cell-title">Single Session / Layer 3</span><span class="appendix-cell-subtitle">Test-Time Training and Fast Weights</span></summary>

This cell covers parametric or quasi-parametric adaptation during inference.

- **In-Place Test-Time Training** studies direct updates to model parameters during inference, making deployment itself part of the learning loop <d-cite key="inplacettt2026"></d-cite>.
- **Learning to Discover at Test Time** explores updating model behavior on the exact problem instance rather than only searching longer with frozen weights <d-cite key="tttdiscover2026"></d-cite>.
- **JitRL** is a boundary case: it keeps weights frozen, retrieves trajectory memory to estimate action advantages, and modulates logits at test time for policy improvement without gradient updates <d-cite key="jitrl2026"></d-cite>.
- **TTT Layers** reinterpret sequence modeling as a learned test-time update process, where hidden states behave like expressive memory substrates <d-cite key="tttlayers2024"></d-cite>.
- **Linear Transformers Are Secretly Fast Weight Programmers** makes the fast-weight interpretation explicit: sequence history can write temporary associations into a memory matrix <d-cite key="linearfastweights2021"></d-cite>.
- **Transformers are RNNs** and **Mamba** show adjacent forms of recurrent state accumulation, making the boundary between context, state, and weights less clean than the standard frozen-transformer picture suggests <d-cite key="lineartransformersrnn2020,mamba2023"></d-cite>.
  These fast-weight and recurrent-state papers are supporting evidence for the context/state boundary, not self-evolving agents by themselves.

**Boundary note:** context does not edit the checkpoint, but it does become computation. Retrieved tokens become KV-cache state that shapes future attention <d-cite key="vaswani2017attention"></d-cite>. Fast-weight and linear-attention interpretations explain why this transient state can look weight-like without becoming durable model weights <d-cite key="lineartransformersrnn2020,linearfastweights2021"></d-cite>.

**Mechanism:** use the current problem instance to change the computation itself: gradient updates, logit modulation, learned hidden-state updates, fast-weight memory, or recurrent state accumulation.

**Caveat:** this is the most powerful and operationally expensive online adaptation cell. It demands tight evaluation because a useful local update can also create regressions.

</details>

<details class="appendix-cell" markdown="1" data-when="across-sessions" data-layer="files">
<summary><span class="appendix-cell-title">Across Sessions / Layer 1</span><span class="appendix-cell-subtitle">Persistent Skills and User Memory</span></summary>

This cell covers state that survives across sessions for one user, project, codebase, or environment.

- **Voyager** accumulates executable Minecraft skills and retrieves them for future tasks, giving a clear early example of skill-library growth <d-cite key="voyager2023"></d-cite>.
- **Anthropic Agent Skills** package reusable procedures into discoverable folders that an agent can load when relevant <d-cite key="anthropicagentskills2026"></d-cite>.
- **OpenAI Codex Record & Replay** lets a user demonstrate a workflow on macOS and turn it into a reusable Codex skill, making "show once, reuse later" a concrete persistent-skill interface <d-cite key="openaicodexrecordreplay2026"></d-cite>.
- **OpenHands Skills and Context** supports persistent skill installation, enabling skills to be managed, enabled, disabled, and reused across sessions <d-cite key="openhandskills2026"></d-cite>.
- **Memento-Skills** pushes the same idea toward agents that design and improve agent skills themselves <d-cite key="mementoskills2026"></d-cite>.
- **Hermes Agent** couples persistent memory with procedural skills that it creates from experience and improves during use <d-cite key="hermesagent2026"></d-cite>.
- **Agentic Context Engineering (ACE)** treats contexts as evolving playbooks that accumulate, refine, and organize strategies over time <d-cite key="ace2025"></d-cite>.

**Mechanism:** convert repeated discoveries into durable artifacts: scripts, commands, wrappers, procedures, project conventions, and environment-specific recipes.

**Caveat:** persistent skills need lifecycle management. Stale skills can be worse than no skills, especially when project dependencies, APIs, or security constraints change.

</details>

<details class="appendix-cell" markdown="1" data-when="across-sessions" data-layer="harness">
<summary><span class="appendix-cell-title">Across Sessions / Layer 2</span><span class="appendix-cell-subtitle">Meta-Programming and Workflow Optimization</span></summary>

This cell covers recurring execution graphs that persist across tasks or sessions.

- **Meta-Harness** searches over harness code using prior candidates, scores, and execution traces, making harness optimization the direct target <d-cite key="metaharness2026"></d-cite>.
- **DSPy** treats language-model programs as optimizable graphs rather than hand-written prompts <d-cite key="dspy2023"></d-cite>.
- **MIPRO** optimizes instructions and demonstrations for multi-stage language-model programs <d-cite key="mipro2024"></d-cite>.
- **AgentOptimizer** iteratively adds, revises, and removes agent functions or skills from historical conversations and performance feedback, without updating the base model weights <d-cite key="agentoptimizer2023"></d-cite>.

These optimizers stay in this cell when they are run against a recurring task distribution; they would move to the population row only when a platform ships the resulting program as a global default.

**Mechanism:** mine historical trajectories, identify high-performing execution patterns, and compile them into reusable routers, DAGs, tool schemas, recovery loops, and workflows.

**Caveat:** harness optimization can overfit to yesterday's tasks. Good systems need evaluation sets that represent the future operating distribution, not just the past transcript.

</details>

<details class="appendix-cell" markdown="1" data-when="across-sessions" data-layer="weights">
<summary><span class="appendix-cell-title">Across Sessions / Layer 3</span><span class="appendix-cell-subtitle">Parametric Personalization and Task Specialization</span></summary>

This cell covers parametric specialization over repeated interactions with one user or organization.

- **OPPU** explores democratized personalized parameter-efficient fine-tuning <d-cite key="oppu2024"></d-cite>.
- **Profile-to-PEFT** uses profile-derived signals to produce fast personalized adaptation <d-cite key="profiletopeft2025"></d-cite>.
- **PERSOMA** studies personalized soft-prompt adapters for personalized language prompting <d-cite key="persoma2024"></d-cite>.
- **OpenClaw-RL** treats next-state signals from user replies, tool outputs, terminal states, and GUI changes as online RL feedback for personal agents, making repeated use a source of policy improvement <d-cite key="openclawrl2026"></d-cite>.

**Mechanism:** compress stable user- or organization-specific patterns into adapters, soft prompts, LoRA-style modules, or other parameter-efficient personalization layers.

**Caveat:** personalization must separate durable signal from accidental context. A user accepting one terse answer should not permanently train the model to be terse in every domain.

</details>

<details class="appendix-cell" markdown="1" data-when="across-users" data-layer="files">
<summary><span class="appendix-cell-title">Across Users / Layer 1</span><span class="appendix-cell-subtitle">Collective Knowledge and Skill Commons</span></summary>

This cell covers shared external state - registries, knowledge banks, and artifact graphs - accumulated from the whole population's interactions.

- **Composio** and **LlamaHub** are practical infrastructure for shared integration assets: hosted MCP/tool wrappers on one side, and reusable loaders, tools, and packs on the other <d-cite key="composio2026,llamahub2024"></d-cite>.
- **Agent KB** studies how cross-domain experience can be reused for agentic problem solving <d-cite key="agentkb2025"></d-cite>.
- **ReasoningBank** collects reasoning memories to scale agent self-evolution <d-cite key="reasoningbank2025"></d-cite>.
- **FunSearch** shows a collective program-search loop in which generated programs are evaluated, selected, and reused for further discovery <d-cite key="funsearch2023"></d-cite>.
- **AlphaEvolve** extends verified program search to scientific, algorithmic, and infrastructure problems, where generated code is evaluated, selected, and iteratively reused as the evolving artifact <d-cite key="alphaevolve2025"></d-cite>.

FunSearch and AlphaEvolve are treated here as evolving program-artifact stores, not as literal multi-user registries.

**Mechanism:** validate and promote local discoveries into shared assets: tools, integrations, reasoning traces, API wrappers, benchmark solutions, and capability graphs.

**Caveat:** the trust problem dominates this cell. A global skill bank without provenance, sandboxing, and eval gates can become a supply-chain vulnerability or a hallucination amplifier.

</details>

<details class="appendix-cell" markdown="1" data-when="across-users" data-layer="harness">
<summary><span class="appendix-cell-title">Across Users / Layer 2</span><span class="appendix-cell-subtitle">Platform Harness Flywheels and Automated Design</span></summary>

This cell covers population-level improvement to the default agent process itself, plus automated search over agent code and harnesses that can later become defaults.

- **Platform-shipped harness defaults** can turn population telemetry into upgrades baked into every agent's default harness: explicit planning for long-horizon tasks, autonomous execution loops, and test-and-verify steps that sandbox generated code before replying.
- **Alita-G** sits on the Layer 1/2 boundary: it turns successful trajectories into curated MCP tools, then uses retrieval-augmented tool selection to instantiate stronger domain agents <d-cite key="alitag2025"></d-cite>.
- **Darwin Gödel Machine** explores open-ended evolution of self-improving coding agents <d-cite key="dgm2025"></d-cite>.
- **Hyperagents** make the meta-level improvement procedure itself editable, so the system searches not only for better agents but for better ways to generate better agents <d-cite key="hyperagents2026"></d-cite>.

**Mechanism:** mine aggregate failure logs, identify structural bottlenecks in prompts/tools/workflows, and wire the fixes into the default harness - shipped directly by platform teams, or discovered automatically by meta-agents that propose, test, and deploy better control flows.

**Caveat:** harness updates are product updates. They require regression testing, rollout controls, and auditability because one bad default policy can affect every downstream user.

</details>

<details class="appendix-cell" markdown="1" data-when="across-users" data-layer="weights">
<summary><span class="appendix-cell-title">Across Users / Layer 3</span><span class="appendix-cell-subtitle">Checkpoint Bootstrapping and Self-Improvement Frontier</span></summary>

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
