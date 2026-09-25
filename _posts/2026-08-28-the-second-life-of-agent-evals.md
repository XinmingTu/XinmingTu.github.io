---
layout: distill
title: "The Second Life of Agent Evals"
description: "Turning completed agent runs into new tests of verification and selection."
last_updated: 2026-09-18
date: 2026-08-28
tags: ['AI', 'agents', 'benchmarks', 'verification']
categories: blog
permalink: /blog/preview/the-second-life-of-agent-evals/
preview: true
sitemap: false
bibliography: 2026-08-28-the-second-life-of-agent-evals.bib

toc:
  - name: "Turning agent eval runs into verification tasks"
  - name: "Reviewers pass most failed runs"
  - name: "Choosing is easier than judging"
  - name: "Selection depends on the reviewer and the source"
  - name: "Selection recovers part of the sampling gain"
  - name: "From evaluation to training"
  - name: "Appendix"

authors:
  - name: Xinming Tu
    url: "https://xinmingtu.cn"
    affiliations:
      name: University of Washington, Phylo

_styles: |
  /* Keep the article header and reading column on the same grid. */
  @media (min-width: 768px) {
    html body d-title h1 {
      font-size: 38px;
      line-height: 1.18;
      letter-spacing: -0.025em;
    }
    html body d-title p {
      font-size: 18px;
      line-height: 1.55;
    }
  }
  @media (min-width: 768px) and (max-width: 1179px) {
    html body d-title,
    html body d-byline,
    html body d-article {
      grid-template-columns: [screen-start] minmax(16px, 1fr) [page-start middle-start text-start] repeat(8, minmax(0, 63.5px)) [text-end middle-end page-end] minmax(16px, 1fr) [screen-end];
      column-gap: 16px;
    }
    d-article d-contents {
      grid-column: text;
      grid-row: auto;
      justify-self: stretch;
      width: auto;
      padding: 1rem;
      margin: 0 0 1.5rem;
      border: 1px solid var(--global-divider-color);
      display: block;
    }
  }
  @media (min-width: 1180px) {
    html body d-title,
    html body d-byline,
    html body d-article {
      grid-template-columns: [screen-start] 1fr [page-start kicker-start] 60px [middle-start] 60px [text-start kicker-end] repeat(8, minmax(0, 53px)) [text-end gutter-start] 60px [middle-end] 60px [page-end gutter-end] 1fr [screen-end];
      column-gap: 32px;
    }
    d-article > figure.sle-figure {
      grid-column: middle;
    }
  }
  d-article {
    --sle-ink: #20242d;
    --sle-body: #434a57;
    --sle-muted: #747d8b;
    --sle-line: #dfe4e9;
    --sle-soft: #f6f8fa;
    --sle-card: #ffffff;
    --sle-blue: #4f68b3;
    --sle-blue-soft: #eef2ff;
    --sle-green: #287a68;
    --sle-green-soft: #eaf7f2;
    --sle-warm: #a75e3c;
    --sle-warm-soft: #fff1e9;
    --sle-purple: #8971aa;
    --sle-figure-grid: #87909e;
  }
  html[data-theme='dark'] d-article {
    --sle-ink: #edf0f5;
    --sle-body: #c9ced8;
    --sle-muted: #99a1b1;
    --sle-line: #40464e;
    --sle-soft: #24282d;
    --sle-card: #2a2e34;
    --sle-blue: #9aabed;
    --sle-blue-soft: #30384f;
    --sle-green: #74c8b2;
    --sle-green-soft: #293f39;
    --sle-warm: #dfa07e;
    --sle-warm-soft: #46342c;
    --sle-purple: #c1a7e7;
    --sle-figure-grid: #b1bccb;
  }
  d-article p,
  d-article li {
    color: var(--sle-body);
  }
  d-article h2 {
    color: var(--sle-ink);
    margin-bottom: 0.7em;
    margin-top: 1.75rem;
  }
  d-article h3 {
    color: var(--sle-ink);
    margin-bottom: 0.55em;
    margin-top: 1.35em;
  }
  d-article h2 + h3 {
    margin-top: 0.9em;
  }
  d-article .sle-lede {
    border-left: 3px solid var(--sle-green);
    color: var(--sle-body);
    font-size: 1.08rem;
    line-height: 1.72;
    margin: 0.3rem 0 2rem;
    padding: 0.1rem 0 0.1rem 1rem;
  }
  d-article .sle-lede strong {
    color: var(--sle-ink);
  }
  d-article .sle-lede-label {
    color: var(--sle-green);
    font-size: 0.76rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    margin-bottom: 0.3rem;
    text-transform: uppercase;
  }
  d-article figure.sle-figure {
    margin: 1.65rem 0 2rem;
  }
  d-article .sle-figure-title {
    color: var(--sle-ink);
    font-size: 0.95rem;
    font-weight: 600;
    line-height: 1.45;
    margin: 0 0 0.65rem;
    text-align: center;
  }
  d-article figure.sle-figure img {
    display: block;
    height: auto;
    width: 100%;
  }
  d-article figure.sle-figure .sle-inline-figure {
    display: block;
    width: 100%;
    height: auto;
    background: transparent;
  }
  d-article .sle-figure-mobile { display: none; }
  @media (max-width: 600px) {
    d-article .sle-figure-desktop { display: none; }
    d-article .sle-figure-mobile { display: block; }
  }
  d-article figure.sle-figure figcaption {
    color: var(--sle-muted);
    font-size: 0.83rem;
    line-height: 1.45;
    margin-top: 0.65rem;
    text-align: center;
  }
  d-article .sle-task-diagram {
    border: 1px solid var(--sle-line);
    border-radius: 16px;
    margin: 1.4rem 0 1.6rem;
    overflow: hidden;
    background: var(--sle-card);
    color: var(--sle-ink);
  }
  d-article .sle-evidence {
    background: var(--sle-soft);
    padding: 1.15rem 1.3rem;
  }
  d-article .sle-diagram-label {
    display: block;
    font-size: .69rem;
    font-weight: 700;
    letter-spacing: .09em;
    text-transform: uppercase;
    color: var(--sle-muted);
  }
  d-article .sle-evidence-items {
    display: grid;
    grid-template-columns: auto auto 1fr auto auto;
    align-items: center;
    gap: .55rem;
    margin-top: .8rem;
    font-size: .82rem;
  }
  d-article .sle-evidence-items small {
    display: block;
    font-size: .7rem;
    font-weight: 400;
    color: var(--sle-muted);
  }
  d-article .sle-agent-loop {
    border: 1px solid var(--sle-blue);
    border-radius: 8px;
    padding: .65rem;
    background: var(--sle-blue-soft);
    text-align: center;
    color: var(--sle-blue);
  }
  d-article .sle-flow-arrow { color: var(--sle-muted); }
  d-article .sle-evidence-note {
    margin-top: .65rem;
    font-size: .72rem;
    color: var(--sle-muted);
  }
  d-article .sle-verified-outcome {
    margin-top: .8rem;
    padding-top: .7rem;
    border-top: 1px dashed var(--sle-line);
    font-size: .76rem;
    line-height: 1.5;
    color: var(--sle-ink);
  }
  d-article .sle-verified-outcome small {
    display: block;
    font-size: .7rem;
    color: var(--sle-muted);
  }
  @media (max-width: 480px) {
    d-article .sle-evidence-items { grid-template-columns: 1fr; text-align: center; }
    d-article .sle-flow-arrow { transform: rotate(90deg); }
  }
  d-article .sle-settings {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    padding: 1.25rem 0;
  }
  d-article .sle-setting {
    padding: 0 .8rem;
    text-align: center;
  }
  d-article .sle-setting + .sle-setting { border-left: 1px solid var(--sle-line); }
  d-article .sle-setting h3 {
    font-size: 1.05rem;
    line-height: 1.2;
    margin: 0 0 .25rem;
  }
  d-article .sle-input-count {
    font-size: .76rem;
    color: var(--sle-muted);
  }
  d-article .sle-run-set {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 5px;
    height: 80px;
  }
  d-article .sle-run-paper {
    display: block;
    position: relative;
    box-sizing: border-box;
    width: 29px;
    height: 42px;
    border: 1px solid var(--sle-blue);
    border-radius: 3px;
    background: var(--sle-blue-soft);
    color: var(--sle-blue);
    font: 600 10px/1 sans-serif;
    text-align: left;
    padding: 5px;
  }
  d-article .sle-run-paper::after {
    content: "";
    position: absolute;
    left: 5px;
    right: 5px;
    top: 22px;
    height: 1px;
    background: currentColor;
    box-shadow: 0 5px 0 currentColor;
    opacity: .5;
  }
  d-article .sle-review-action {
    color: var(--sle-muted);
    font-size: .72rem;
    line-height: 1.4;
    margin: 0 0 .7rem;
  }
  d-article .sle-review-action::before {
    content: "↓";
    display: block;
    color: var(--sle-blue);
    font-size: 1.2rem;
    line-height: 1;
    margin-bottom: .4rem;
  }
  d-article .sle-output {
    display: flex;
    flex-direction: column;
    justify-content: center;
    background: var(--sle-green-soft);
    color: var(--sle-green);
    border-radius: 7px;
    min-height: 58px;
    font-size: .85rem;
    line-height: 1.4;
    font-weight: 650;
  }
  d-article .sle-output small { font-size: .7rem; font-weight: 400; }
  d-article .sle-setting-meta {
    margin-top: .8rem;
    font-size: .7rem;
    line-height: 1.55;
    color: var(--sle-muted);
  }
  d-article .sle-setting-meta span { display: block; }
  d-article .sle-hidden-label {
    border-top: 1px dashed var(--sle-line);
    padding: .8rem 1.3rem;
    color: var(--sle-muted);
    font-size: .75rem;
    line-height: 1.5;
  }
  d-article .sle-hidden-label strong { color: var(--sle-ink); font-weight: 600; }
  d-article details.sle-instruction {
    background: var(--sle-soft);
    border: 1px solid var(--sle-line);
    border-radius: 10px;
    margin: 1rem 0 1.45rem;
    padding: 0;
  }
  d-article details.sle-instruction summary {
    color: var(--sle-ink);
    cursor: pointer;
    font-weight: 700;
    list-style: none;
    padding: 0.8rem 0.95rem;
  }
  d-article details.sle-instruction summary::-webkit-details-marker {
    display: none;
  }
  d-article details.sle-instruction summary::before {
    color: var(--sle-green);
    content: "+";
    display: inline-block;
    font-weight: 800;
    margin-right: 0.55rem;
  }
  d-article details.sle-instruction[open] summary::before {
    content: "−";
  }
  d-article details.sle-instruction .sle-instruction-body {
    border-top: 1px solid var(--sle-line);
    padding: 0.8rem 0.95rem 0.95rem;
  }
  d-article details.sle-instruction pre {
    font-size: 0.76rem;
    line-height: 1.5;
    margin: 0;
    white-space: pre-wrap;
  }
  d-article .sle-note {
    background: var(--sle-soft);
    border-left: 3px solid var(--sle-line);
    color: var(--sle-muted);
    font-size: 0.85rem;
    line-height: 1.55;
    margin: 1.35rem 0;
    padding: 0.75rem 0.9rem;
  }
  d-article .sle-coda {
    background: var(--sle-green-soft);
    border-radius: 14px;
    color: var(--sle-ink);
    font-size: 1.08rem;
    line-height: 1.6;
    margin: 1.35rem 0 0;
    padding: 1rem 1.15rem;
  }
  d-article .sle-coda + h2 {
    margin-top: 1.75rem;
  }
  d-article .sle-update {
    color: var(--sle-muted);
    font-size: 0.82rem;
    line-height: 1.5;
  }
  d-article p.sle-repo-link {
    color: var(--sle-ink);
    font-size: 1.15rem;
    margin: 1.45rem 0 1.1rem;
  }
  d-article p.sle-repo-link a {
    font-weight: 650;
  }
  @media (max-width: 600px) {
    d-article .sle-settings { grid-template-columns: 1fr; padding: 0 1rem; }
    d-article .sle-setting {
      padding: 1rem 0;
      display: grid;
      grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
      gap: .5rem .6rem;
      align-items: center;
    }
    d-article .sle-setting h3 { grid-column: 1 / -1; margin: 0; }
    d-article .sle-input-count { grid-column: 1; grid-row: 2; }
    d-article .sle-review-action { grid-column: 2; grid-row: 2; margin: 0; }
    d-article .sle-review-action::before { display: none; }
    d-article .sle-run-set { grid-column: 1; grid-row: 3; gap: 3px; }
    d-article .sle-run-paper { width: clamp(18px, 5.8vw, 25px); height: 40px; flex-shrink: 0; }
    d-article .sle-output { grid-column: 2; grid-row: 3; }
    d-article .sle-setting-meta { grid-column: 1 / -1; margin-top: .2rem; }

    d-article .sle-setting + .sle-setting { border-left: 0; border-top: 1px solid var(--sle-line); }
    d-article .sle-run-set { height: 55px; }
    d-article .sle-output { min-height: 50px; }
    d-article .sle-setting-meta span { display: inline; }
    d-article .sle-setting-meta span + span::before { content: " · "; }
  }
---

{% assign tb4 = site.data.second_life_tb4 %}
{% assign gpt = tb4.reviewers | where: "key", "gpt-5-6-sol" | first %}
{% assign glm = tb4.reviewers | where: "key", "glm-5-3" | first %}
{% assign flash = tb4.reviewers | where: "key", "glm-5-3-flash" | first %}
{% assign deepseek = tb4.reviewers | where: "key", "deepseek-v4p1-flash" | first %}
{% assign fable_source = tb4.sources | where: "key", "fable-5.1" | first %}
{% assign gpt_source = tb4.sources | where: "key", "gpt-5.6-sol" | first %}
{% assign glm_source = tb4.sources | where: "key", "glm-5.3" | first %}
{% assign astra_source = tb4.sources | where: "key", "gpt-6-astra" | first %}

<div class="sle-lede">
<strong>Agent evals can have a second life.</strong> A graded agent run leaves behind a trajectory, the files it produced, and a pass/fail verdict from the benchmark's checker. Hide the verdict, and the run becomes a new task: can another agent tell whether it worked? We built such tasks from Terminal-Bench 4.0 runs. Judging one run at a time, every reviewer we tested passed most of the failed runs. Given five attempts at the same task, the best reviewer still picked a successful one {{ gpt.five }}% of the time, against {{ tb4.five_baseline }}% for a random pick.
</div>

## Turning agent eval runs into verification tasks

To build a verification task, we give a second agent the original task and the saved evidence: the trajectory of tool calls and observations, plus artifacts such as files and code. We ask whether the attempt succeeded and keep the benchmark verifier's recorded outcome as the answer key. No new labels are needed, though the answer key is only as good as the original verifier.

Benchmarks often run each task several times, and the attempts don't always agree. That gives us a second kind of task, **selection**: show an agent several attempts at the same task and ask it to pick one that succeeded. The recorded outcomes score the pick.

We build three settings from these runs. They differ in how many attempts the agent sees and what it has to decide:

<div class="sle-task-diagram" role="group" aria-label="Completed eval runs become three verification settings" markdown="0">
  <div class="sle-evidence">
    <span class="sle-diagram-label">One completed agent run</span>
    <div class="sle-evidence-items">
      <div><strong>Task</strong><small>Instructions</small></div>
      <span class="sle-flow-arrow" aria-hidden="true">→</span>
      <div class="sle-agent-loop"><strong>Agent ↔ Environment</strong><small>Tool actions + observations → trajectory</small></div>
      <span class="sle-flow-arrow" aria-hidden="true">→</span>
      <div><strong>Artifacts</strong><small>Files, code, outputs</small></div>
    </div>
    <div class="sle-evidence-note">The execution is saved as a trajectory. Reviewers receive the task, trajectory, and artifacts.</div>
    <div class="sle-verified-outcome"><strong>Original verifier → checked outcome: Pass / Fail</strong><small>Hidden from the reviewer and used only as the answer key.</small></div>
  </div>
  <div class="sle-settings">
    <div class="sle-setting">
      <h3>Single</h3>
      <div class="sle-input-count">1 run</div>
      <div class="sle-run-set" aria-hidden="true"><span class="sle-run-paper">A</span></div>
      <div class="sle-review-action">Judge</div>
      <div class="sle-output">Pass / Fail<small>1 verdict</small></div>
    </div>
    <div class="sle-setting">
      <h3>Pair</h3>
      <div class="sle-input-count">2 runs · same task</div>
      <div class="sle-run-set" aria-hidden="true"><span class="sle-run-paper">A</span><span class="sle-run-paper">B</span></div>
      <div class="sle-review-action">Judge + compare</div>
      <div class="sle-output">Pass / Fail × 2<small>+ choose one run</small></div>
    </div>
    <div class="sle-setting">
      <h3>Five</h3>
      <div class="sle-input-count">5 runs · same task</div>
      <div class="sle-run-set" aria-hidden="true"><span class="sle-run-paper">A</span><span class="sle-run-paper">B</span><span class="sle-run-paper">C</span><span class="sle-run-paper">D</span><span class="sle-run-paper">E</span></div>
      <div class="sle-review-action">Compare + select</div>
      <div class="sle-output">Choose one run<small>from five candidates</small></div>
    </div>
  </div>
  <div class="sle-hidden-label">The recorded outcomes score all three settings: verdicts in Single and Pair, the chosen run in Pair and Five.</div>
</div>

**Single** shows one attempt and asks whether it completed the task. **Pair** shows two attempts at the same task, asks for a pass/fail verdict on each, and asks which one more likely succeeded. **Five** shows five attempts and asks only for the one most likely to have succeeded.

The runs come from **Terminal-Bench 4.0**<d-cite key="terminalbench4"></d-cite>. Each *source* is a model plus the agent harness that ran it: Fable 5.1 and GLM-5.3 in Claude Code, GPT-5.6 Sol and GPT-6 Astra in Codex. Each source attempted all 66 tasks five times. Four models then act as *reviewers*: **GPT-5.6 Sol, GLM-5.3 Flash, GLM-5.3, and DeepSeek V4.1 Flash**. We say reviewer rather than verifier to keep them apart from the benchmark's own checker. Each reviewer runs in mini-swe-agent on Harbor<d-cite key="harbor"></d-cite> and can inspect the saved evidence with shell tools, but it cannot fix the work or continue the task.

One source's five attempts at one task form a *pool*. The main comparisons use only *mixed pools*, which contain at least one success and one failure, so there is a real choice to make. From each mixed pool, Single judges one successful and one failed attempt separately. Pair shows the same two attempts side by side, without saying that exactly one succeeded. Five shows all five. A coin flip scores 50% in Single and Pair. In Five, a random pick succeeds {{ tb4.five_baseline }}% of the time, because many pools contain more than one success.

<div class="sle-note" markdown="1">
**Coverage.** Single and Pair use 79 mixed pools from Fable 5.1, GLM-5.3, and GPT-5.6 Sol runs. Five adds 18 pools from GPT-6 Astra runs, for 97 pools, 485 runs, and 49 distinct tasks. GPT-6 Astra only supplies runs; it is not a reviewer. [Construction details](#dataset-and-scoring).
</div>

## Reviewers pass most failed runs

The Single prompt warns that "a completion claim without supporting observations or artifacts is not proof." Reviewers still lean heavily toward **pass**, and every one of them passes more than half of the failed runs.

<figure class="sle-figure" markdown="0">
  <h3 class="sle-figure-title">Terminal-Bench 4.0: Single-run verification</h3>
  <div class="sle-figure-desktop">{% inline_eval_figure tb4-single-confusion %}</div>
  <div class="sle-figure-mobile">{% inline_eval_figure tb4-single-confusion-mobile %}</div>
  <figcaption>Rows are recorded outcomes; columns are reviewer verdicts. Each row has 79 runs. Darker blue means a larger share, on a shared 0–100% scale. Invalid outputs stay in the denominator but have no verdict column, so some rows sum to less than 100%.</figcaption>
</figure>

GLM-5.3 Flash passes **every successful run, and {{ flash.false_pass }}% of the failed ones**. GLM-5.3 behaves almost the same way. GPT-5.6 Sol is the best at catching failures, and even it catches only {{ gpt.failure_recall }}% of them. The reviewers' bar for "done" sits well below the verifier's.

## Choosing is easier than judging

Judging runs one at a time, these reviewers are not much better than a coin flip: Single accuracy ranges from 50.0% to 59.5%. Shown the same attempts side by side in Pair, every reviewer does better, picking the successful run in 53.2–65.8% of pools.

<figure class="sle-figure" markdown="0">
  <h3 class="sle-figure-title">Terminal-Bench 4.0: Judgment versus selection</h3>
  <div class="sle-figure-desktop">{% inline_eval_figure tb4-single-pair %}</div>
  <div class="sle-figure-mobile">{% inline_eval_figure tb4-single-pair-mobile %}</div>
  <figcaption>Single and Pair use the same attempts from 79 pools. Single scores verdict accuracy on 79 successful and 79 failed runs; Pair scores whether the reviewer picks the successful run. Both axes start at the dashed 50% random baseline, and labels give the actual rates. The two metrics differ, so the gap does not measure how much the side-by-side view helps.</figcaption>
</figure>

The same gap shows up inside Pair. **GLM-5.3 labels both runs correctly in only {{ glm.pair_exact }}% of pairs, yet picks the successful one in {{ glm.pair }}%.** In 33 pairs it calls both runs a pass, and in 19 of those it still prefers the one that succeeded. A reviewer doesn't have to grade every candidate correctly to choose well.

## Selection depends on the reviewer and the source

**GPT-5.6 Sol is the best selector overall.** It picks a successful run in {{ gpt.five }}% of the {{ tb4.five_pools }} mixed pools. GLM-5.3 Flash follows at {{ flash.five }}%, then GLM-5.3 at {{ glm.five }}%. DeepSeek V4.1 Flash, at {{ deepseek.five }}%, barely beats the {{ tb4.five_baseline }}% of a random pick.

<figure class="sle-figure" markdown="0">
  <h3 class="sle-figure-title">Terminal-Bench 4.0: Five-run selection by source</h3>
  <div class="sle-figure-desktop">{% inline_eval_figure tb4-five-by-source %}</div>
  <div class="sle-figure-mobile">{% inline_eval_figure tb4-five-by-source-mobile %}</div>
  <figcaption>Each panel holds runs from one source; each bar is one reviewer choosing among them. All panels share a 40–100% axis. Dashed lines mark each source's random-pick baseline (uniform choice). Invalid outputs count as failed selections. Mixed pools only.</figcaption>
</figure>

GPT-5.6 Sol leads or ties on every source. Below it, the order shifts. On Fable 5.1 runs, DeepSeek V4.1 Flash edges out GLM-5.3 (66.7% versus 63.3%, a one-pool difference). On GPT-5.6 Sol runs, DeepSeek drops to 46.4%, below the 52.9% random baseline, while GLM-5.3 reaches 64.3%.

How much selection helps also depends on whose runs are being reviewed. GPT-5.6 Sol beats a random pick by **26.7 points on Fable 5.1 runs and 32.9 on GPT-5.6 Sol runs**, but only by 12.4 on GLM-5.3 runs and 14.4 on GPT-6 Astra runs. These differences are descriptive: each source contributes a different set of tasks, and the samples are small, especially the 18 GPT-6 Astra pools.

The [appendix](#comparing-sources-on-shared-tasks) repeats the comparison on tasks where every source has a mixed pool. Some rankings change, but there are only six such tasks across the three original sources, and two across all four.

<details class="sle-instruction" markdown="1">
<summary>Prompt check: a different favorite, little change in success</summary>
<div class="sle-instruction-body" markdown="1">

The Five prompt shows `{"selected_candidate":3}` as its example output. On the original 79 pools, DeepSeek V4.1 Flash picked candidate 3 in 64 reviews. When we replaced the example with a neutral prose description, its favorite moved to candidate 1 (70 reviews), but success barely changed: 58.2% before, 59.5% after. Either way, most of its picks go to a single slot, which helps explain why its Five score stays close to the random baseline.

<figure class="sle-figure" markdown="0">
  <h3 class="sle-figure-title">Terminal-Bench 4.0: Selection under two prompt variants</h3>
  {% inline_eval_figure tb4-prompt-position %}
  <figcaption>Same evidence, candidate order, model, and reasoning settings. Both conditions produce valid outputs in all 79 cases.</figcaption>
</figure>

The paired change is +1.3 points, with a task-cluster 95% interval of [−13.5, 16.9], so a single rerun cannot separate a prompt effect from noise. We report it separately from the main Five results. [Report]({{ tb4.repo }}/reports/tbench4-complete-results-2026-09-16.md#deepseek-five-prompt-sensitivity).

</div>
</details>

## Selection recovers part of the sampling gain

**Five attempts create headroom. Selection decides how much of it you keep.** So far we have scored only mixed pools. Here we score all 66 tasks per source, including pools where every attempt passed or every attempt failed. For each source, we compare a single attempt (pass@1), GPT-5.6 Sol's pick from five attempts, and an oracle that always finds a success when there is one (oracle pass@5).

<figure class="sle-figure" markdown="0">
  <h3 class="sle-figure-title">Terminal-Bench 4.0: Selection gains from repeated attempts</h3>
  <div class="sle-figure-desktop">{% inline_eval_figure tb4-sampling-hero %}</div>
  <div class="sle-figure-mobile">{% inline_eval_figure tb4-sampling-hero-mobile %}</div>
  <figcaption>Light bars show pass@1, solid bars show GPT-5.6 Sol's selection, and dashed outlines show oracle pass@5, each in its source's color. The number above each group is the selection gain over pass@1, in percentage points. Selection scores are reconstructed as described below.</figcaption>
</figure>

On Fable 5.1 runs, selection raises reconstructed success from **{{ fable_source.pass1 }}% to {{ fable_source.selected }}%**. On GPT-5.6 Sol runs, it goes from **{{ gpt_source.pass1 }}% to {{ gpt_source.selected }}%**. In both cases, selection closes about 60% of the gap to oracle pass@5. GLM-5.3 and GPT-6 Astra runs each gain only {{ glm_source.gain }} points, closing 25–30% of their gaps. These gains are smaller than the mixed-pool gains above because selection can only change the outcome when the attempts disagree.

<details class="sle-instruction" markdown="1">
<summary>How the reconstruction works</summary>
<div class="sle-instruction-body" markdown="1">

For each source, we add up three things and divide by 66: pools where every attempt succeeded, mixed pools where GPT-5.6 Sol picked a success, and the expected successes of a random pick on mixed pools that were never reviewed. We did not run the reviewer on all-pass or all-fail pools. We assume it would return a valid pick there, and any valid pick gives the same result.

Ten mixed pools could not be reviewed (3 Fable 5.1, 2 GLM-5.3, 5 GPT-5.6 Sol, none from GPT-6 Astra): eight had errors in the source runs, and two had artifacts that failed to collect. They stay in the denominator and are scored as a random pick. The other 97 mixed pools were all reviewed. One GLM-5.3 run with a missing reward counts as a failure, as it does in the source data.

For Fable 5.1: `(19 + 26 + (2 + 3 + 1) / 5) / 66 = 70.0%`. That is 19 all-pass pools, 26 successful picks, and a random pick on three unreviewed pools with 2, 3, and 1 successes.

| Source | Tasks | pass@1 | GPT-5.6 Sol selection | Oracle pass@5 |
| --- | ---: | ---: | ---: | ---: |
{% for source in tb4.sources %}| {{ source.name }} | {{ source.tasks }} | {{ source.pass1 }}% | {{ source.selected }}% | {{ source.pass5 }}% |
{% endfor %}

Keeping all 66 tasks preserves the scope of the original evaluation. These are still not leaderboard scores; comparing against one would also require matching the benchmark version, agent setup, and scoring protocol.

Oracle pass@k is the probability that a random subset of k of the five attempts contains a success. Reviewers were tested at k = 5 only; the [full pass@1–5 curves](#oracle-sampling-curves) are in the appendix. [Data and assumptions]({{ tb4.repo }}/results/tbench4-pass-at-k.json).

</div>
</details>

Like **LLM-as-a-Verifier**<d-cite key="kwok2026llmverifier"></d-cite>, this uses verification for test-time scaling. In our setup, the verifier is itself a tool-using agent, working from runs the original evaluation had already produced.

## From evaluation to training

Terminal-Bench 4.0 measured whether agents can do its tasks. Reusing its runs lets us ask whether agents can check the work, without any new labels. For these reviewers, the answer depends on how we ask. They are poor judges of a single run, but most of them beat chance when choosing among five, and GPT-5.6 Sol beats it by a wide margin.

**The reviews themselves could become training data.** Each one is already labeled by the original verifier, which makes the reviews a natural fit for teaching agents to inspect evidence, catch failures, and pick successful attempts. We have not tested this. A correct verdict does not mean the reasoning behind it was sound, so training would need quality checks on the review trajectories and train/test splits by original task.

<div class="sle-coda">
Most eval runs are used once, for a single score. Kept, they can become <strong>the next benchmark</strong>, and perhaps <strong>the next training set</strong>.
</div>

### Reproduction

Code, tasks, and results are in the [GitHub repository](https://github.com/XinmingTu/Agentic-Verification-Eval).

**Cite this post**

```bibtex
@misc{tu2026secondlife,
  author = {Tu, Xinming},
  title  = {The Second Life of Agent Evals},
  year   = {2026},
  month  = aug,
  url    = {https://xinmingtu.cn/blog/preview/the-second-life-of-agent-evals/},
  note   = {Blog post; updated September 18, 2026}
}
```

## Appendix

### Full results and uncertainty

| Reviewer | Single accuracy · 158 runs | Pair selection · 79 pools | Five selection · 97 pools |
| --- | ---: | ---: | ---: |
{% for reviewer in tb4.reviewers %}| {{ reviewer.name }} | {{ reviewer.single }}% | {{ reviewer.pair }}% | {{ reviewer.five }}% ({{ reviewer.five_wins }}/97) |
{% endfor %}| Random baseline | 50.0% | 50.0% | {{ tb4.five_baseline }}% |

Reviewers are ordered by overall Five success throughout. The Five aggregate weights each pool equally. GPT-5.6 Sol gets 64/79 (81.0%) on the original three sources; adding 12/18 on GPT-6 Astra runs gives 76/97 (78.4%). On the original 79 pools, its paired gain over a random pick is +25.1 points, with a task-cluster 95% interval of [16.3, 33.9]. That interval covers only those 79 pools, not the 97-pool total.

| Reviewer | Single accuracy · 95% cluster CI | Pair selection · 95% cluster CI |
| --- | ---: | ---: |
{% for reviewer in tb4.reviewers %}| {{ reviewer.name }} | {{ reviewer.single_ci }}% | {{ reviewer.pair_ci }}% |
{% endfor %}

The same task can appear under several sources, so the intervals resample tasks rather than pools: 10,000 bootstrap resamples over task clusters, with 48 distinct tasks in the Single/Pair panel. The 18 GPT-6 Astra pools give wide intervals. GPT-5.6 Sol and GLM-5.3 Flash both pick 12/18, each with a [44.4%, 88.9%] interval, so the tie says little about whether they are equally good. [Main report]({{ tb4.repo }}/reports/tbench4-complete-results-2026-09-16.md) · [GLM-5.3 Flash completion]({{ tb4.repo }}/reports/tbench4-glm-flash-results-2026-09-17.md) · [GPT-6 Astra extension]({{ tb4.repo }}/reports/tbench4-gpt6-source-results-2026-09-17.md).

### Comparing sources on shared tasks

Are some sources' failures harder to catch, or their successes harder to find? In the main results, each source contributes a different set of tasks, so the source and the tasks are tangled together. Here we fix the tasks and keep the four reviewers separate. A shared task is one where every source has an eligible mixed pool. The sources still produced different runs, with different mixes of successes and failures.

We compare two views of the same results. **All available pools** uses every eligible pool: 30 from Fable 5.1, 21 from GLM-5.3, and 28 from GPT-5.6 Sol. **Shared tasks only** keeps the six tasks common to all three. On those six, each source contributes 12 Single judgments (one successful and one failed run per task), six Pair selections on the same two runs, and six Five selections over the full pools. Reviewers, metrics, candidate order, and scoring stay the same; only the set of tasks changes. The six were chosen by availability, not by reviewer scores, and invalid answers still count as errors. Because the shared tasks are a subset of the full set, the two views are not independent samples.

<figure class="sle-figure" markdown="0">
  <h3 class="sle-figure-title">Terminal-Bench 4.0: Same task pool, different sources</h3>
  {% inline_eval_figure tb4-shared-heatmap %}
  <figcaption>Every row uses the same six tasks; columns are reviewers. Blue is above random, orange below, and neutral equal. Color shows the percentage-point difference from random on a shared −100 to +100 scale; it does not indicate statistical significance. Each cell gives the score, the correct/total count, and the difference from random. Single and Pair use a 50% baseline; Five uses each source's share of successful candidates on these tasks, listed below the panel.</figcaption>
</figure>

<details markdown="1">
<summary>Compare the shared task pool with all available pools</summary>

<figure class="sle-figure" markdown="0">
  <h3 class="sle-figure-title">Terminal-Bench 4.0: All pools versus six shared tasks</h3>
  {% inline_eval_figure tb4-shared-tasks %}
  <figcaption>Rows are sources; columns are reviewers. Each cell shows all available pools on top (gray) and the shared-task subset below (blue), with counts and percentages on the same 0–100% bar scale. Single denominators count runs; Pair and Five denominators count pools.</figcaption>
</figure>

</details>

Pair is the cleaner comparison: every pair has one success and one failure, so every source has the same 50% baseline. Five keeps each pool's original mix, so its baselines differ by source even on shared tasks. Neither view isolates something intrinsic to a model's runs, because the agents, harnesses, artifacts, candidate order, and kinds of failure still differ. And with six tasks, one changed pick moves a Pair or Five score by 16.7 points. Read these as exploratory rather than as a source ranking.

<details markdown="1">
<summary>Shared task identities</summary>

{% for task in site.data.second_life_shared.three_source_tasks %}
- `{{ task }}`
{% endfor %}

</details>

Adding GPT-6 Astra leaves only two tasks shared by all four sources: `batched-eval-parity` and `vba-userform-port`. Astra has Five results only, so it has no row in the Single and Pair panels above. We show the four-source view below for completeness; two tasks cannot support a ranking.

<figure class="sle-figure" markdown="0">
  <h3 class="sle-figure-title">Terminal-Bench 4.0: Four sources, the same two tasks</h3>
  {% inline_eval_figure tb4-shared-four-heatmap %}
  <figcaption>Five selection on the two tasks shared by all four sources, on the same diverging scale: percentage points above or below each source's random baseline. One changed pick moves a score by 50 points, and color does not indicate significance.</figcaption>
</figure>

<details markdown="1">
<summary>Four-source comparison with all available pools</summary>

<figure class="sle-figure" markdown="0">
  <h3 class="sle-figure-title">Terminal-Bench 4.0: All pools versus two shared tasks</h3>
  {% inline_eval_figure tb4-shared-four %}
  <figcaption>All available pools above, the two shared tasks below. The second is a subset of the first, not a separate experiment.</figcaption>
</figure>

</details>

These panels reuse existing results; no new model calls were made. A [per-case snapshot](/assets/data/second-life-tb4/shared-task-records.json) records candidate IDs, labels, and reviewer outcomes from the same pinned experiment commit. Rebuild it with `python scripts/generate_second_life_shared.py`, which also checks for duplicate observations, consistent candidate order and labels across reviewers, and consistent Single/Pair runs within each Five pool.

### Oracle sampling curves

These curves show how often at least one of k attempts succeeds, for k from 1 to 5. They use all 66 tasks per source and the same colors as the main figure. Points below k = 5 show what an oracle could get; no reviewer was run at those k.

<figure class="sle-figure" markdown="0">
  <h3 class="sle-figure-title">Terminal-Bench 4.0: Oracle success with repeated attempts</h3>
  <div class="sle-figure-desktop">{% inline_eval_figure tb4-oracle-curves %}</div>
  <div class="sle-figure-mobile">{% inline_eval_figure tb4-oracle-curves-mobile %}</div>
  <figcaption>Each point averages, over tasks, the probability that a random subset of k of the five attempts contains a success.</figcaption>
</figure>

### Dataset and scoring

The sources are GPT-6 Astra + Codex (18 pools), Fable 5.1 + Claude Code (30), GLM-5.3 + Claude Code (21), and GPT-5.6 Sol + Codex (28). Every retained pool passed metadata and archive validation. Recorded artifacts may be partial snapshots of the environment. Labels are the benchmark verifier's original rewards; we did not re-grade any run.

Single uses one successful and one failed run from each pool, 79 of each. Pair uses the same two runs, and reviewers are not told that exactly one succeeded. Five keeps the original mix: 268 of 485 candidates succeeded, so a random pick succeeds 55.3% of the time. We did not run Single on all five candidates, so there is no score-each-then-pick baseline for Five. The settings differ in both metric and coverage, so comparing them does not isolate the value of seeing more runs.

Invalid outputs count as errors in all headline metrics. In the confusion matrices they remain in the 79-run row denominators but are omitted from the Pass/Fail columns. Single invalid counts are 0 for GPT-5.6 Sol, 1 for GLM-5.3 Flash, 1 for GLM-5.3, and 9 for DeepSeek V4.1 Flash.

Reviewers never see source rewards, verifier outputs, or metadata that identifies the source. Some reviews are reused from earlier batches of this study. A review was reused only when its runs and labels were identical, never based on whether it was correct. Automated checks look for label leaks in the inputs we know about, but they cannot rule out indirect hints elsewhere in an archived run.

### Reviewer instructions

<details class="sle-instruction" markdown="1">
<summary>Single Full</summary>
<div class="sle-instruction-body" markdown="1">

```text
{% include second-life-tb4/single-full.txt %}
```

</div>
</details>

<details class="sle-instruction" markdown="1">
<summary>Pair Full</summary>
<div class="sle-instruction-body" markdown="1">

```text
{% include second-life-tb4/pair-full.txt %}
```

</div>
</details>

<details class="sle-instruction" markdown="1">
<summary>Five Full</summary>
<div class="sle-instruction-body" markdown="1">

```text
{% include second-life-tb4/five-full.txt %}
```

</div>
</details>

### Average reviewer cost

Mean cost per review (USD).

| Reviewer | Single | Pair | Five |
| --- | ---: | ---: | ---: |
{% for reviewer in site.data.second_life_shared.costs %}| {{ reviewer.name }} | {{ reviewer.single }} | {{ reviewer.pair }} | {{ reviewer.five }} |
{% endfor %}

Computed over the same 79 pools: 158 Single reviews, 79 Pair, and 79 Five, including incorrect and invalid reviews.

<details class="sle-instruction" markdown="1">
<summary>Accounting details</summary>
<div class="sle-instruction-body" markdown="1">

GPT-5.6 Sol uses recorded cost. Other models use the larger of reported cost and the token estimate below. These are experiment-accounting figures, not invoices.

Historical rates used for estimation (**USD per million tokens**, not current price quotes):

| Reviewer | Uncached input | Cached input | Output |
| --- | ---: | ---: | ---: |
| GLM-5.3 | 1.40 | 0.26 | 4.40 |
| GLM-5.3 Flash | 0.15 | 0.03 | 0.50 |
| DeepSeek V4.1 Flash | 0.22 | 0.007 | 0.66 |

Reused reviews count once, at their original cost. Reviews with missing cost data are estimated from tokens rather than counted as free. The figures exclude source-agent runs, infrastructure, superseded runs, the prompt control, and Astra's Five-only extension.

[Accounting implementation]({{ tb4.repo }}/scripts/run_tbench4_complete.py).

</div>
</details>

### Earlier studies

An earlier pilot on Terminal-Bench 3.0<d-cite key="terminalbench3"></d-cite> showed reviewers trajectories only, without artifacts. It used 85 mixed pools, 50 distinct tasks, and 340 derived tasks. GPT-5.6 Sol's Five selection rate was 63.5%, against 42.1% for a random pick. Averaged across the three original 74-task evaluations, reconstructed success was 41.9%, compared with 33.7% pass@1 and 55.9% oracle pass@5.

It is tempting to read the TB3-to-TB4 difference as the value of artifacts, but the tasks and some reviewer versions changed too. The initial 18-pool TB4 study did include a matched trajectory-only Single control; the expanded panel did not repeat it. [TB3 report]({{ tb4.repo }}/reports/context-ladder-reviewer-comparison-2026-08-28.md) · [Initial TB4 study]({{ tb4.repo }}/reports/tbench4-run-bundle-results-2026-09-05.md).
