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
  - name: "Reviewers tend to say pass"
  - name: "Judgment and selection diverge"
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
<strong>Agent evals can have a second life.</strong> A completed evaluation run can be the starting point for a new task. Here, we turn existing runs into verification tasks, using their checked outcomes to evaluate whether another agent can recognize success or failure.
</div>

## Turning agent eval runs into verification tasks

An agent's attempt at a task leaves an execution trace and artifacts such as files or code. When the evaluation includes an automatic verifier, it also records whether that attempt passed or failed. We give another agent the original task and saved evidence, ask whether the attempt succeeded, and withhold the recorded outcome to use as the reference answer. This creates a verification task with an existing, checked answer, subject to the original verifier's criteria and limitations.

Repeated attempts at the same task produce multiple traces and sets of artifacts, sometimes with different outcomes. We can turn these into **selection tasks** by asking an agent to choose a successful attempt from the group. The original verifier's results let us score its choice.

We construct three settings from these runs, shown below. They differ in how many attempts the agent sees and whether it must judge their outcomes, select an attempt, or do both.

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
    <div class="sle-verified-outcome"><strong>Original verifier → checked outcome: Pass / Fail</strong><small>Held out as the reference answer for scoring; not shown to the reviewer.</small></div>
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
  <div class="sle-hidden-label">Each run has a verifier-checked outcome—not necessarily a successful one. The reference answer follows the original verifier's criteria.</div>
</div>

**Single** asks whether one attempt completed the original task. **Pair** presents two attempts at the same task, asks for a pass/fail judgment on each, and asks which is more likely to have succeeded. **Five** presents five attempts at the same task and asks the agent to select the one most likely to have succeeded.

We apply this construction to saved **Terminal-Bench 4.0** runs<d-cite key="terminalbench4"></d-cite>, with five attempts per task from each source configuration—a model and its agent setup. We then evaluate four models as verifiers: **GPT-5.6 Sol, GLM-5.3 Flash, GLM-5.3, and DeepSeek V4.1 Flash**. We call these agents *reviewers* to distinguish them from the benchmark's original automatic verifier. Each uses mini-swe-agent in Harbor<d-cite key="harbor"></d-cite> to read the saved evidence and check it with tools; it cannot repair an attempt or continue the original task.

For the verification and selection comparisons below, we use groups containing both successful and failed attempts, so there is a meaningful choice to make. Each five-attempt group from one task and source is a *pool*; a group containing both outcomes is a *mixed pool*. Single evaluates one successful and one failed attempt from each pool separately. Pair presents those same two attempts together, without revealing that exactly one succeeded. Five presents all five attempts. Random guessing has an expected score of 50% in Single and Pair; Five's uniform-choice baseline depends on the proportion of successful attempts in each pool.

<div class="sle-note" markdown="1">
**Coverage.** Single/Pair cover 79 pools from Fable 5.1, GLM-5.3, and GPT-5.6 Sol source runs. Five adds 18 GPT-6 Astra pools, for **97 pools / 485 runs / 49 task names**. GPT-6 Astra is a source, not a reviewer. Each original source evaluation has 66 tasks with five attempts per task. [Construction details](#dataset-and-scoring).
</div>

## Reviewers tend to say pass

Single reviewers are told that a completion claim is not proof. Even so, their verdicts lean toward **pass**, including on runs that failed the original verifier.

<figure class="sle-figure" markdown="0">
  <h3 class="sle-figure-title">Terminal-Bench 4.0: Single-run verification</h3>
  <div class="sle-figure-desktop">{% inline_eval_figure tb4-single-confusion %}</div>
  <div class="sle-figure-mobile">{% inline_eval_figure tb4-single-confusion-mobile %}</div>
  <figcaption>Actual outcomes in rows; reviewer verdicts in columns. Each row has 79 runs. Darker blue means a larger percentage, on a shared 0–100% scale. Invalid outputs remain in the denominator but are not shown as a verdict, so some rows sum to less than 100%.</figcaption>
</figure>

GLM-5.3 Flash approves **{{ flash.success_recall }}% of successful runs and {{ flash.false_pass }}% of failed runs**. GLM-5.3 shows a similar pattern. GPT-5.6 Sol has the highest failure recall at {{ gpt.failure_recall }}%, yet still approves {{ gpt.false_pass }}% of failures. These reviewers frequently accept evidence that falls short of the original verifier's standard.

## Judgment and selection diverge

**Unreliable judgments can still support useful selection.** Single accuracy ranges from 50.0% to 59.5%. When asked to compare the same attempts in Pair, reviewers select the successful run in 53.2–65.8% of pools.

<figure class="sle-figure" markdown="0">
  <h3 class="sle-figure-title">Terminal-Bench 4.0: Judgment versus selection</h3>
  <div class="sle-figure-desktop">{% inline_eval_figure tb4-single-pair %}</div>
  <div class="sle-figure-mobile">{% inline_eval_figure tb4-single-pair-mobile %}</div>
  <figcaption>Single and Pair use the same attempts from 79 pools, with consistent reviewer colors. Single measures judgment accuracy on 79 successful and 79 failed runs; Pair measures successful selection. Both axes start at the dashed 50% random baselines; labels show absolute rates. The metrics differ, so the gap is not a causal estimate of context benefit.</figcaption>
</figure>

The distinction also appears within Pair: **GLM-5.3 labels both candidates correctly in only {{ glm.pair_exact }}% of pairs, yet selects the successful candidate in {{ glm.pair }}%**. A reviewer can choose well without correctly certifying every candidate.

## Selection depends on the reviewer and the source

**GPT-5.6 Sol has the highest overall five-run selection success among the four reviewers evaluated.** It selects a successful run in **{{ gpt.five }}%** of the {{ tb4.five_pools }} mixed pools, compared with {{ flash.five }}% for GLM-5.3 Flash, {{ glm.five }}% for GLM-5.3, and {{ deepseek.five }}% for DeepSeek V4.1 Flash. Uniform random selection succeeds {{ tb4.five_baseline }}% of the time.

<figure class="sle-figure" markdown="0">
  <h3 class="sle-figure-title">Terminal-Bench 4.0: Five-run selection by source</h3>
  <div class="sle-figure-desktop">{% inline_eval_figure tb4-five-by-source %}</div>
  <div class="sle-figure-mobile">{% inline_eval_figure tb4-five-by-source-mobile %}</div>
  <figcaption>Each panel contains frozen runs from one source; each bar is a reviewer selecting among those runs. All panels use the same 40–100% axis range. Dashed lines show source-specific uniform choice. Invalid outputs count as unsuccessful selections. Rates are conditional on mixed pools.</figcaption>
</figure>

GPT-5.6 Sol leads or ties in all four source slices, but the relative ranking of the other reviewers varies across source models. DeepSeek V4.1 Flash exceeds GLM-5.3 on runs generated by Fable 5.1 (66.7% versus 63.3%); on runs generated by GPT-5.6 Sol, the ordering reverses (46.4% versus 64.3%).

The opportunity for selection also varies. GPT-5.6 Sol's gain over uniform is **+26.7 points on Fable 5.1 pools and +32.9 on GPT-5.6 Sol pools**, compared with +12.4 on GLM-5.3 and +14.4 on GPT-6 Astra. These are descriptive differences: source task sets differ, and small samples—especially the 18 GPT-6 Astra pools—limit model-ranking claims.

Restricting the comparison to shared tasks changes some rankings, but the overlap is small: six tasks across the three original sources and two across all four. The [matched-task comparisons in the appendix](#comparing-sources-on-shared-tasks) hold the task set fixed across sources.

<details class="sle-instruction" markdown="1">
<summary>Prompt check: a different favorite, little change in success</summary>
<div class="sle-instruction-body" markdown="1">

The Five prompt includes `{"selected_candidate":3}` as its example output. On the original 79 pools, DeepSeek V4.1 Flash picked candidate 3 in 64 reviews. Replacing that example with a neutral prose schema shifted its favorite to candidate 1 (70 reviews), while success changed only from 58.2% to 59.5%.

<figure class="sle-figure" markdown="0">
  <h3 class="sle-figure-title">Terminal-Bench 4.0: Selection under two prompt variants</h3>
  {% inline_eval_figure tb4-prompt-position %}
  <figcaption>Same evidence, candidate order, model, and reasoning settings. Both conditions produce valid outputs in all 79 cases.</figcaption>
</figure>

The paired success change is +1.3 points, with a task-cluster 95% interval of [−13.5, 16.9]. This single sensitivity run does not establish an effect independent of sampling noise. It is reported separately from the main Five results. [Report]({{ tb4.repo }}/reports/tbench4-complete-results-2026-09-16.md#deepseek-five-prompt-sensitivity).

</div>
</details>

## Selection recovers part of the sampling gain

**Five attempts create headroom. Selection determines how much of it becomes useful.** We return to the **full 66-task source jobs**, using **GPT-5.6 Sol as the reviewer across all four sources**.

<figure class="sle-figure" markdown="0">
  <h3 class="sle-figure-title">Terminal-Bench 4.0: Selection gains from repeated attempts</h3>
  <div class="sle-figure-desktop">{% inline_eval_figure tb4-sampling-hero %}</div>
  <div class="sle-figure-mobile">{% inline_eval_figure tb4-sampling-hero-mobile %}</div>
  <figcaption>Each group uses its source color: light bars show pass@1, solid bars show GPT-5.6 Sol selection, and lightly filled bars with dashed outlines show oracle pass@5. Annotations above each group give the selection gain over pass@1 in percentage points. Every source retains all 66 tasks. Selection scores are reconstructed under the assumptions below.</figcaption>
</figure>

For runs generated by Fable 5.1, selection raises reconstructed success from **{{ fable_source.pass1 }}% to {{ fable_source.selected }}%**. For runs generated by GPT-5.6 Sol, it rises from **{{ gpt_source.pass1 }}% to {{ gpt_source.selected }}%**. GLM-5.3 and GPT-6 Astra sources gain {{ glm_source.gain }} and {{ astra_source.gain }} points, respectively. Whole-job gains are smaller than gains on mixed pools because selection can change the outcome only on mixed tasks.

<details class="sle-instruction" markdown="1">
<summary>How the reconstruction works</summary>
<div class="sle-instruction-body" markdown="1">

Every source retains all 66 tasks. Selection success is reconstructed by adding all-success pools, successful GPT-5.6 Sol selections on reviewed mixed pools, and the expected successes from uniform choice on unreviewed mixed pools, then dividing by 66. Homogeneous pools were not reviewed; this assumes valid selection there.

Ten mixed pools were unavailable for review: eight had source-run exceptions and two failed artifact collection (0 GPT-6 Astra, 3 Fable 5.1, 2 GLM-5.3, and 5 GPT-5.6 Sol). They remain in the full-task denominator and use uniform fallback, not measured reviewer outcomes. All 97 eligible mixed pools have been reviewed. One missing GLM-5.3 source reward retains the source data's failure label.

For Fable 5.1, selection success is `(19 + 26 + (2 + 3 + 1) / 5) / 66 = 70.0%`: 19 all-success pools, 26 successful selections, and uniform fallback on three unreviewed pools.

| Source | Tasks | pass@1 | GPT-5.6 Sol selection | Oracle pass@5 |
| --- | ---: | ---: | ---: | ---: |
{% for source in tb4.sources %}| {{ source.name }} | {{ source.tasks }} | {{ source.pass1 }}% | {{ source.selected }}% | {{ source.pass5 }}% |
{% endfor %}

The full-task denominator preserves the source evaluation's scope. Direct leaderboard comparisons would also require matching the benchmark version, agent setup, and scoring protocol.

Oracle pass@k is the probability that a uniformly sampled subset of k frozen attempts contains a success. Reviewer selection was evaluated at k=5 only. The [full pass@1–5 curves](#oracle-sampling-curves) are in the appendix. [Data and assumptions]({{ tb4.repo }}/results/tbench4-pass-at-k.json).

</div>
</details>

This follows **LLM-as-a-Verifier** in using verification for test-time scaling<d-cite key="kwok2026llmverifier"></d-cite>. Here, verification is itself a tool-using agent task built from the original evaluation's saved runs.

## From evaluation to training

The original evaluation measured task execution. Reusing its runs lets us measure verification and selection—and see where those capabilities diverge.

**The resulting verification runs could also become training data.** Grounded in the original outcome labels, they could support training agents to inspect evidence, recognize failures, and select successful attempts. We have not tested that training benefit here. Correct verdicts do not automatically validate a reviewer's reasoning; training would need trajectory quality checks and train/test splits by original task.

<div class="sle-coda">
A completed evaluation can seed both <strong>the next benchmark</strong> and <strong>the next training set</strong>.
</div>

### Reproduction

Code, tasks, and results are available in the [GitHub repository](https://github.com/XinmingTu/Agentic-Verification-Eval).

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
{% endfor %}| Blind baseline | 50.0% | 50.0% | {{ tb4.five_baseline }}% |

Reviewer order is fixed throughout by overall Five selection success. The Five aggregate weights each pool equally. GPT-5.6 Sol's original three-source result is 64/79 (81.0%); adding 12/18 GPT-6 Astra-source successes gives 76/97 (78.4%). On the original 79 pools, the paired GPT-5.6 Sol gain over uniform is +25.1 points, with a task-cluster 95% interval of [16.3, 33.9]. That interval does not describe the expanded 97-pool aggregate.

| Reviewer | Single accuracy · 95% cluster CI | Pair selection · 95% cluster CI |
| --- | ---: | ---: |
{% for reviewer in tb4.reviewers %}| {{ reviewer.name }} | {{ reviewer.single_ci }}% | {{ reviewer.pair_ci }}% |
{% endfor %}

Task identities recur across sources. Intervals use 10,000 bootstrap resamples of task-name clusters; the Single/Pair panel has 48 distinct task names. GPT-6 Astra's 18-pool Five extension has broad intervals: GPT-5.6 Sol and GLM-5.3 Flash both select 12/18, with [44.4%, 88.9%] intervals. Their tie does not establish equivalent capabilities. [Main report]({{ tb4.repo }}/reports/tbench4-complete-results-2026-09-16.md) · [GLM-5.3 Flash completion]({{ tb4.repo }}/reports/tbench4-glm-flash-results-2026-09-17.md) · [GPT-6 Astra extension]({{ tb4.repo }}/reports/tbench4-gpt6-source-results-2026-09-17.md).

### Comparing sources on shared tasks

Are some sources' failed attempts harder to recognize, or their successful attempts harder to select? The main source slices contain different task sets. Here we hold the task identities fixed and keep all four reviewers separate. A shared task means the same original task was attempted by each source; it does **not** mean the sources produced identical traces or identical success/failure mixtures. Reviewers see trajectories and recorded artifacts, so these comparisons concern run bundles, not text alone.

We compare two views of the same recorded evaluations. **All available pools** uses each source's full eligible set: 30 Fable 5.1 pools, 21 GLM-5.3 pools, and 28 GPT-5.6 Sol pools. **Shared tasks only** restricts each source to the same six task identities. On this intersection, each source contributes 12 Single judgments (one successful and one failed anchor per task), six Pair selections using those same anchors, and six Five selections using the full five-attempt pools. Reviewers, metrics, candidate order within each pool, and scoring rules stay fixed; only the included task set changes. The intersection is chosen from task availability, not reviewer scores; invalid answers remain errors. The shared subset is contained in the full set, so these are not independent samples or a causal intervention.

<figure class="sle-figure" markdown="0">
  <h3 class="sle-figure-title">Terminal-Bench 4.0: Same task pool, different sources</h3>
  {% inline_eval_figure tb4-shared-heatmap %}
  <figcaption>Every source row uses exactly the same six tasks; columns are reviewers. Blue means above random, orange below random, and neutral means equal to random. Color measures the percentage-point difference on a shared −100 to +100 scale, not statistical significance. Cells show the raw score, correct/total count, and difference from random. Single and Pair use a 50% baseline; Five uses each source's actual successful-candidate fraction on these tasks, listed below the panel.</figcaption>
</figure>

<details markdown="1">
<summary>Compare the shared task pool with all available pools</summary>

<figure class="sle-figure" markdown="0">
  <h3 class="sle-figure-title">Terminal-Bench 4.0: All pools versus six shared tasks</h3>
  {% inline_eval_figure tb4-shared-tasks %}
  <figcaption>Rows are source agents; columns are reviewers. Each cell shows all available pools on top (gray) and the shared-task subset below (blue), with counts and percentages on the same 0–100% bar scale. Single denominators count runs; Pair and Five denominators count pools.</figcaption>
</figure>

</details>

Pair makes one aspect of the comparison cleaner: every pair contains one success and one failure, giving every source the same 50% uniform-selection baseline. Five keeps the original outcome mix, so its source-specific baselines differ even on shared tasks. Neither comparison isolates an intrinsic property of a model's traces: source agents, harnesses, artifacts, candidate order, and the kinds of failures can still differ. With only six tasks, one changed selection moves a Pair or Five result by 16.7 percentage points; these are exploratory comparisons, not a stable source ranking.

<details markdown="1">
<summary>Shared task identities</summary>

{% for task in site.data.second_life_shared.three_source_tasks %}
- `{{ task }}`
{% endfor %}

</details>

Adding GPT-6 Astra leaves only two tasks shared by all four sources: `batched-eval-parity` and `vba-userform-port`. Astra currently has Five results only; there are no corresponding Single or Pair observations to fill a fourth source row in the earlier panels. We show the available four-source intersection below, but two tasks cannot support a general difficulty ranking.

<figure class="sle-figure" markdown="0">
  <h3 class="sle-figure-title">Terminal-Bench 4.0: Four sources, the same two tasks</h3>
  {% inline_eval_figure tb4-shared-four-heatmap %}
  <figcaption>Five selection on the identical two-task intersection. The same diverging scale shows percentage points above or below each source's uniform-selection baseline. A single selection changes the score by 50 percentage points; color does not imply statistical significance. This tiny subset cannot establish a general source ranking.</figcaption>
</figure>

<details markdown="1">
<summary>Four-source comparison with all available pools</summary>

<figure class="sle-figure" markdown="0">
  {% inline_eval_figure tb4-shared-four %}
  <figcaption>All available pools above, identical two-task intersection below. These are nested samples, not independent experiments.</figcaption>
</figure>

</details>

These panels reuse existing observations; no additional model evaluations were run. The [minimal per-case snapshot](/assets/data/second-life-tb4/shared-task-records.json) records candidate IDs, labels, and reviewer outcomes from the same pinned experiment commit. Rebuild with `python scripts/generate_second_life_shared.py`; the generator checks duplicate observations, matching candidate order and labels across reviewers, and matching Single/Pair anchors within Five pools.

### Oracle sampling curves

These curves show how often at least one successful attempt is available as k increases. They use all 66 tasks per source and the same source colors as the main figure. Intermediate points are oracle availability estimates, not reviewer selection results.

<figure class="sle-figure" markdown="0">
  <h3 class="sle-figure-title">Terminal-Bench 4.0: Oracle success with repeated attempts</h3>
  <div class="sle-figure-desktop">{% inline_eval_figure tb4-oracle-curves %}</div>
  <div class="sle-figure-mobile">{% inline_eval_figure tb4-oracle-curves-mobile %}</div>
  <figcaption>Each point averages the probability of finding at least one success in a uniformly sampled subset of k of the five frozen attempts.</figcaption>
</figure>

### Dataset and scoring

The sources are GPT-6 Astra + Codex (18 pools), Fable 5.1 + Claude Code (30), GLM-5.3 + Claude Code (21), and GPT-5.6 Sol + Codex (28). All retained pools pass metadata and archive validation. Recorded artifacts may be partial environment snapshots. Labels are the original operational verifier rewards, not new semantic adjudications.

Single supplies 79 successful and 79 failed anchors. Pair uses those same anchors; reviewers are not told that one succeeded. Five retains the original mix: 268 of 485 candidates succeeded, giving 55.3% uniform choice. Single is not an independent-score ranking baseline over all five candidates. These metrics and source coverage differ; they do not isolate the benefit of additional context.

Invalid outputs count as errors in all headline metrics. In the confusion matrices they remain in the 79-run row denominators but are omitted from the Pass/Fail columns. Single invalid counts are 0 for GPT-5.6 Sol, 1 for GLM-5.3 Flash, 1 for GLM-5.3, and 9 for DeepSeek V4.1 Flash.

Reviewer inputs exclude source rewards, verifier outputs, and source-identifying metadata. Earlier compatible observations are reused once based on identical trials, anchors, and rewards, not selected for correctness. Automated leakage checks cover declared surfaces; they do not establish that arbitrary archived content contains no indirect shortcuts.

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

Same 79 source-task pools: 158 Single reviews, 79 Pair, and 79 Five. Incorrect and invalid reviews are included.

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

Reused reviews count once at their original cost; missing dollar accounting is not treated as free. Excludes source-agent execution, infrastructure, superseded runs, prompt controls, and Astra's Five-only extension.

[Accounting implementation]({{ tb4.repo }}/scripts/run_tbench4_complete.py).

</div>
</details>

### Earlier studies

The Terminal-Bench 3.0 trace-only pilot<d-cite key="terminalbench3"></d-cite> used 85 mixed pools, 50 task names, and 340 derived tasks. GPT-5.6 Sol's Five selection rate was 63.53%, against 42.12% uniform choice. Averaged across the three original 74-task evaluations, reconstructed success was 41.89%, compared with 33.69% pass@1 and 55.86% oracle pass@5.

TB3 and TB4 differ in tasks, evidence, and some reviewer versions; their difference cannot establish artifact benefit. The initial 18-pool TB4 study had a matched Trace-only Single control. The expanded panel did not repeat that ablation. [TB3 report]({{ tb4.repo }}/reports/context-ladder-reviewer-comparison-2026-08-28.md) · [Initial TB4 study]({{ tb4.repo }}/reports/tbench4-run-bundle-results-2026-09-05.md).
