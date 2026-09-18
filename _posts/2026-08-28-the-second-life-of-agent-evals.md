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
  d-article figure.sle-figure img {
    display: block;
    height: auto;
    width: 100%;
  }
  d-article figure.sle-figure figcaption {
    color: var(--sle-muted);
    font-size: 0.83rem;
    line-height: 1.45;
    margin-top: 0.65rem;
    text-align: center;
  }
  d-article .sle-flow {
    align-items: stretch;
    display: grid;
    gap: 0.55rem;
    grid-template-columns: repeat(4, 1fr);
  }
  d-article .sle-step {
    align-items: center;
    background: var(--sle-card);
    border: 1px solid var(--sle-line);
    border-radius: 12px;
    color: var(--sle-ink);
    display: flex;
    font-size: 0.83rem;
    font-weight: 680;
    justify-content: center;
    line-height: 1.35;
    min-height: 4.5rem;
    padding: 0.75rem;
    position: relative;
    text-align: center;
  }
  d-article .sle-step:not(:last-child)::after {
    color: var(--sle-muted);
    content: "→";
    font-size: 0.92rem;
    position: absolute;
    right: -0.52rem;
    top: calc(50% - 0.65rem);
    z-index: 2;
  }
  d-article .sle-step.source { background: var(--sle-blue-soft); color: var(--sle-blue); }
  d-article .sle-step.compiler { background: var(--sle-warm-soft); color: var(--sle-warm); }
  d-article .sle-step.derived { background: var(--sle-green-soft); color: var(--sle-green); }
  d-article .sle-family {
    display: grid;
    gap: 0.72rem;
    grid-template-columns: repeat(3, 1fr);
    margin: 1.25rem 0 1.55rem;
  }
  d-article .sle-family-card {
    background: var(--sle-card);
    border: 1px solid var(--sle-line);
    border-radius: 13px;
    padding: 0.95rem;
  }
  d-article .sle-family-card strong {
    color: var(--sle-ink);
    display: block;
    font-size: 0.96rem;
    margin-bottom: 0.35rem;
  }
  d-article .sle-family-card .sle-question {
    display: block;
    color: var(--sle-ink);
    font-size: 1.03rem;
    font-weight: 600;
    line-height: 1.45;
    margin: 0.6rem 0;
  }
  d-article .sle-family-card .count {
    color: var(--sle-green);
    font-size: 1.34rem;
    font-weight: 760;
  }
  d-article .sle-family-card span:last-child {
    color: var(--sle-muted);
    display: block;
    font-size: 0.79rem;
    line-height: 1.43;
    margin-top: 0.35rem;
  }
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
  @media (max-width: 720px) {
    d-article .sle-step { font-size: 0.78rem; padding: 0.6rem; }
    d-article .sle-family { grid-template-columns: 1fr; }
  }
  @media (max-width: 430px) {
    d-article .sle-flow { grid-template-columns: 1fr; }
    d-article .sle-step::after { display: none; }
  }
---

{% assign tb4 = site.data.second_life_tb4 %}
{% assign gpt = tb4.reviewers[0] %}
{% assign glm = tb4.reviewers[1] %}
{% assign flash = tb4.reviewers[3] %}

<div class="sle-lede">
<strong>Agent evals can have a second life.</strong> We turn completed runs into verification tasks: judge one attempt, compare two, or choose among five.
</div>

Using frozen Terminal-Bench 4.0 runs<d-cite key="terminalbench4"></d-cite>, reviewers inspect the original task, execution trace, and recorded artifacts. The original verifier outcomes stay hidden and provide the labels for scoring.

<figure class="sle-figure" markdown="0">
  <div class="sle-flow" aria-label="Completed agent runs become new verification tasks" markdown="0">
    <div class="sle-step source">Completed agent eval</div>
    <div class="sle-step">Frozen traces + artifacts</div>
    <div class="sle-step compiler">New verification tasks</div>
    <div class="sle-step derived">Judge, compare, select</div>
  </div>
  <figcaption>The executions stay fixed. The question changes.</figcaption>
</figure>

<p class="sle-update">Updated {{ tb4.updated }} · Results through September 17 · <a href="{{ tb4.repo }}/README.md">Code and experiment snapshot</a></p>

## Turning agent eval runs into verification tasks

A completed eval run gives us both evidence and an outcome. We preserve the task, trajectory, and recorded artifacts, then use the original verifier outcome as a hidden label for a new verification task.

We construct three settings: judge one run, compare two, or select among five.

<div class="sle-family" markdown="0">
  <div class="sle-family-card">
    <strong>Single</strong>
    <span class="sle-question">Did this run succeed?</span>
    <span>Judge one attempt.<br>158 runs · 50% baseline</span>
  </div>
  <div class="sle-family-card">
    <strong>Pair</strong>
    <span class="sle-question">Did each run succeed, and which would you choose?</span>
    <span>Judge both, then select one.<br>79 pools · 50% baseline</span>
  </div>
  <div class="sle-family-card">
    <strong>Five</strong>
    <span class="sle-question">Which of five attempts would you choose?</span>
    <span>Select one attempt.<br>{{ tb4.five_pools }} pools · {{ tb4.five_baseline }}% baseline</span>
  </div>
</div>

A *pool* contains five attempts at one task from one source configuration. We evaluate selection on **mixed pools**, where at least one attempt succeeded and one failed. Single uses one successful and one failed anchor from each pool; Pair shows those same anchors together, without revealing that exactly one succeeded. Five keeps the original five attempts, so its random baseline depends on their success rate.

Four reviewers—GPT-5.6 Sol, GLM-5.3, DeepSeek V4.1 Flash, and GLM-5.3 Flash—use mini-swe-agent to inspect read-only evidence in Harbor tasks<d-cite key="harbor"></d-cite>. They can check evidence with tools, but cannot repair a candidate or continue the original task.

<div class="sle-note" markdown="1">
**Coverage.** Single/Pair cover 79 pools from Fable 5.1, GPT-5.6 Sol, and GLM-5.3 source runs. Five adds 18 GPT-6 Astra pools, for **97 pools / 485 runs / 49 task names**. GPT-6 is a source, not a reviewer. Each original source evaluation has 66 tasks with five attempts per task. [Construction details](#dataset-and-scoring).
</div>

## Reviewers tend to say pass

Single reviewers are told that a completion claim is not proof. Even so, their verdicts lean toward **pass**, including on runs that failed the original verifier.

<figure class="sle-figure" markdown="0">
  <picture>
    <source media="(max-width: 600px)" srcset="/assets/img/2026-08-28-second-life-agent-evals/tb4-single-confusion-mobile.svg">
    <img src="/assets/img/2026-08-28-second-life-agent-evals/tb4-single-confusion.svg" alt="Four percentage confusion matrices. Rows are actual success and failure; columns are predicted Pass and Fail. GLM Flash predicts Pass for 100% of successes and 87.3% of failures. All matrices share a 0–100% blue scale." loading="lazy">
  </picture>
  <figcaption>Actual outcomes in rows; reviewer verdicts in columns. Each row has 79 runs. Darker blue means a larger percentage, on a shared 0–100% scale. Invalid outputs remain in the denominator but are not shown as a verdict, so some rows sum to less than 100%.</figcaption>
</figure>

GLM Flash approves **{{ flash.success_recall }}% of successful runs and {{ flash.false_pass }}% of failed runs**. GLM-5.3 shows a similar pattern. GPT has the highest failure recall at {{ gpt.failure_recall }}%, yet still approves {{ gpt.false_pass }}% of failures. These reviewers frequently accept evidence that falls short of the original verifier's standard.

## Judgment and selection diverge

**Unreliable judgments can still support useful selection.** Single accuracy ranges from 50.0% to 59.5%. When asked to compare the same anchors in Pair, reviewers select the successful run in 53.2–65.8% of pools.

<figure class="sle-figure" markdown="0">
  <picture>
    <source media="(max-width: 600px)" srcset="/assets/img/2026-08-28-second-life-agent-evals/tb4-single-pair-mobile.svg">
    <img src="/assets/img/2026-08-28-second-life-agent-evals/tb4-single-pair.svg" alt="Side-by-side vertical bar charts: Single accuracy is 59.5%, 54.4%, 50.0%, and 55.7%; Pair successful selection is 62.0%, 65.8%, 53.2%, and 63.3% for GPT, GLM, DeepSeek, and GLM Flash respectively." loading="lazy">
  </picture>
  <figcaption>Same 79 pools and anchors, same reviewer colors, shared 0–100% axes. Single measures judgment accuracy; Pair measures successful selection. Dashed lines mark their 50% baselines. The metrics differ, so the gap is not a causal estimate of context benefit.</figcaption>
</figure>

The distinction also appears within Pair: **GLM labels both candidates correctly in only {{ glm.pair_exact }}% of pairs, yet selects the successful candidate in {{ glm.pair }}%**. A reviewer can choose well without correctly certifying every candidate.

## Selection depends on the reviewer and the source

Five makes the selection problem concrete: which attempt should we keep? Across all {{ tb4.five_pools }} mixed pools, GPT selects a successful run **{{ gpt.five }}%** of the time, against **{{ tb4.five_baseline }}%** uniform choice. GLM Flash reaches {{ flash.five }}%, full GLM {{ glm.five }}%, and DeepSeek {{ tb4.reviewers[2].five }}%.

<figure class="sle-figure" markdown="0">
  <picture>
    <source media="(max-width: 600px)" srcset="/assets/img/2026-08-28-second-life-agent-evals/tb4-five-by-source-mobile.svg">
    <img src="/assets/img/2026-08-28-second-life-agent-evals/tb4-five-by-source.svg" alt="Five selection by reviewer in four source panels. GPT leads or ties in every panel. Source-specific uniform baselines are 60.0%, 52.9%, 54.3%, and 52.2%. Reviewer colors and order are fixed across panels." loading="lazy">
  </picture>
  <figcaption>Each panel contains frozen runs from one source; each bar is a reviewer selecting among those runs. Dashed lines show source-specific uniform choice. Invalid outputs count as unsuccessful selections. Rates are conditional on mixed pools.</figcaption>
</figure>

GPT leads or ties in all four source slices, but other reviewers' point-estimate rankings change. DeepSeek exceeds full GLM on Fable runs (66.7% versus 63.3%); on GPT-source runs, the ordering reverses (46.4% versus 64.3%).

The opportunity for selection also varies. GPT's gain over uniform is **+26.7 points on Fable pools and +32.9 on GPT pools**, compared with +12.4 on GLM and +14.4 on GPT-6. These are descriptive differences: source task sets differ, and small samples—especially the 18 GPT-6 pools—limit model-ranking claims.

<details class="sle-instruction" markdown="1">
<summary>Prompt check: a different favorite, little change in success</summary>
<div class="sle-instruction-body" markdown="1">

The Five prompt includes `{"selected_candidate":3}` as its example output. On the original 79 pools, DeepSeek picked candidate 3 in 64 reviews. Replacing that example with a neutral prose schema shifted its favorite to candidate 1 (70 reviews), while success changed only from 58.2% to 59.5%.

<figure class="sle-figure" markdown="0">
  <img src="/assets/img/2026-08-28-second-life-agent-evals/tb4-prompt-position.svg" alt="DeepSeek's preferred position shifts from candidate 3 to candidate 1 under a neutral example, with little change in selection success." loading="lazy">
  <figcaption>Same evidence, candidate order, model, and reasoning settings. Both conditions produce valid outputs in all 79 cases.</figcaption>
</figure>

The paired success change is +1.3 points, with a task-cluster 95% interval of [−13.5, 16.9]. This single sensitivity run does not establish an effect independent of sampling noise. It is reported separately from the main Five results. [Report]({{ tb4.repo }}/reports/tbench4-complete-results-2026-09-16.md#deepseek-five-prompt-sensitivity).

</div>
</details>

## Selection recovers part of the sampling gain

**Five attempts create headroom. Selection determines how much of it becomes useful.** To see the full task-level effect, we add back all-success and all-failure pools and use the same GPT reviewer across all four sources.

<figure class="sle-figure" markdown="0">
  <picture>
    <source media="(max-width: 600px)" srcset="/assets/img/2026-08-28-second-life-agent-evals/tb4-sampling-hero-mobile.svg">
    <img src="/assets/img/2026-08-28-second-life-agent-evals/tb4-sampling-hero.svg" alt="Oracle pass@1–5 curves and GPT selection stars over all 66 tasks per source. Fable rises from 57.9% to 70.0%, GPT from 37.3% to 51.2%, GLM from 41.8% to 45.8%, and GPT-6 from 58.2% to 62.1%." loading="lazy">
  </picture>
  <figcaption>Curves: empirical oracle pass@k. Stars: reconstructed whole-job success using the GPT-5.6 Sol reviewer at k=5. Excluded mixed pools use uniform fallback; whiskers bound their possible outcomes, not statistical confidence. These are derived estimates, not official end-to-end benchmark scores.</figcaption>
</figure>

On Fable-source runs, selection raises reconstructed success from **57.9% to 70.0%**. On GPT-source runs, it rises from **37.3% to 51.2%**. GLM and GPT-6 sources gain about 3.9 points each. Mixed-pool selection gains translate into smaller whole-job gains because selection can change the outcome only on mixed tasks.

<details class="sle-instruction" markdown="1">
<summary>How the reconstruction works</summary>
<div class="sle-instruction-body" markdown="1">

For each source, add all-success pools, successful reviewed selections, and uniform fallback for excluded mixed pools, then divide by 66. Homogeneous pools were not reviewed; this assumes valid selection there.

Ten mixed pools were excluded by construction: eight had source-run exceptions and two failed artifact collection. They comprise 3 Fable, 5 GPT, 2 GLM, and 0 GPT-6 pools. All 97 eligible pools have been reviewed. One missing GLM source reward counts as failure.

For Fable, the calculation is `(19 + 26 + (2 + 3 + 1) / 5) / 66 = 70.0%`: 19 all-success pools, 26 successful selections, and three excluded pools with 2, 3, and 1 successes among five attempts.

| Source | pass@1 | GPT selection | Oracle pass@5 | Excluded-pool bounds |
| --- | ---: | ---: | ---: | ---: |
{% for source in tb4.sources %}| {{ source.name }} | {{ source.pass1 }}% | {{ source.selected }}% | {{ source.pass5 }}% | {{ source.coverage_bounds }}% |
{% endfor %}

The curve is the probability that a uniformly sampled subset of k frozen attempts contains a success. Reviewer selection was evaluated at k=5 only. [Data and assumptions]({{ tb4.repo }}/results/tbench4-pass-at-k.json).

</div>
</details>

This follows **LLM-as-a-Verifier** in using verification for test-time scaling<d-cite key="kwok2026llmverifier"></d-cite>. Here, verification is itself a tool-using agent task built from the original evaluation's saved runs.

## From evaluation to training

The original evaluation measured task execution. Reusing its runs lets us measure verification and selection—and see where those capabilities diverge.

**The resulting verification runs could also become training data.** Grounded in the original outcome labels, they could support training agents to inspect evidence, recognize failures, and select successful attempts. We have not tested that training benefit here. Correct verdicts do not automatically validate a reviewer's reasoning; training would need trajectory quality checks and train/test splits by original task.

<div class="sle-coda">
A completed evaluation can seed both <strong>the next benchmark</strong> and <strong>the next training set</strong>.
</div>

## Appendix

### Full results and uncertainty

| Reviewer | Single accuracy · 158 runs | Pair selection · 79 pools | Five selection · 97 pools |
| --- | ---: | ---: | ---: |
{% for reviewer in tb4.reviewers %}| {{ reviewer.name }} | {{ reviewer.single }}% | {{ reviewer.pair }}% | {{ reviewer.five }}% ({{ reviewer.five_wins }}/97) |
{% endfor %}| Blind baseline | 50.0% | 50.0% | {{ tb4.five_baseline }}% |

The Five aggregate weights each pool equally. GPT's original three-source result is 64/79 (81.0%); adding 12/18 GPT-6-source successes gives 76/97 (78.4%). On the original 79 pools, the paired GPT gain over uniform is +25.1 points, with a task-cluster 95% interval of [16.3, 33.9]. That interval does not describe the expanded 97-pool aggregate.

| Reviewer | Single accuracy · 95% cluster CI | Pair selection · 95% cluster CI |
| --- | ---: | ---: |
{% for reviewer in tb4.reviewers %}| {{ reviewer.name }} | {{ reviewer.single_ci }}% | {{ reviewer.pair_ci }}% |
{% endfor %}

Task identities recur across sources. Intervals use 10,000 bootstrap resamples of task-name clusters; the Single/Pair panel has 48 distinct task names. GPT-6's 18-pool Five extension has broad intervals: GPT and GLM Flash both select 12/18, with [44.4%, 88.9%] intervals. Their tie does not establish equivalent capabilities. [Main report]({{ tb4.repo }}/reports/tbench4-complete-results-2026-09-16.md) · [GLM Flash completion]({{ tb4.repo }}/reports/tbench4-glm-flash-results-2026-09-17.md) · [GPT-6 extension]({{ tb4.repo }}/reports/tbench4-gpt6-source-results-2026-09-17.md).

### Dataset and scoring

The sources are Fable 5.1 + Claude Code (30 pools), GPT-5.6 Sol + Codex (28), GLM-5.3 + Claude Code (21), and GPT-6 Astra + Codex (18). All retained pools pass metadata and archive validation. Recorded artifacts may be partial environment snapshots. Labels are the original operational verifier rewards, not new semantic adjudications.

Single supplies 79 successful and 79 failed anchors. Pair uses those same anchors; reviewers are not told that one succeeded. Five retains the original mix: 268 of 485 candidates succeeded, giving 55.3% uniform choice. Single is not an independent-score ranking baseline over all five candidates. These metrics and source coverage differ; they do not isolate the benefit of additional context.

Invalid outputs count as errors in all headline metrics. In the confusion matrices they remain in the 79-run row denominators but are omitted from the Pass/Fail columns. Single invalid counts are 0 for GPT, 1 for GLM, 9 for DeepSeek, and 1 for GLM Flash.

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

### Earlier studies

The Terminal-Bench 3.0 trace-only pilot<d-cite key="terminalbench3"></d-cite> used 85 mixed pools, 50 task names, and 340 derived tasks. GPT's Five selection rate was 63.53%, against 42.12% uniform choice. Averaged across the three original 74-task evaluations, reconstructed success was 41.89%, compared with 33.69% pass@1 and 55.86% oracle pass@5.

TB3 and TB4 differ in tasks, evidence, and some reviewer versions; their difference cannot establish artifact benefit. The initial 18-pool TB4 study had a matched Trace-only Single control. The expanded panel did not repeat that ablation. [TB3 report]({{ tb4.repo }}/reports/context-ladder-reviewer-comparison-2026-08-28.md) · [Initial TB4 study]({{ tb4.repo }}/reports/tbench4-run-bundle-results-2026-09-05.md).

### Recorded extension costs

| Completed batch | New reviews | Recorded model cost |
| --- | ---: | ---: |
{% for batch in tb4.cost_batches %}| {{ batch.name }} | {{ batch.reviews }} | ${{ batch.cost }} |
{% endfor %}

These are three distinct batches; reused observations are not charged again. The September 16 batch includes the DeepSeek prompt control and GLM Flash's original Five reviews. Costs exclude earlier TB4 panels, the September 12 Five extension, solver execution, and infrastructure. They are recorded model costs, not lifetime project spend or provider invoices.

### Reproduction

Results are pinned to experiment commit [`6d99501`]({{ tb4.repo }}/README.md). [Local snapshots and provenance](/assets/data/second-life-tb4/README.md) drive the tables and figures. Regenerate them without model calls using `python scripts/generate_second_life_tb4_figures.py` with Matplotlib installed. The original TB3 script and figures are retained.

<p class="sle-repo-link"><strong>Code, tasks, and results:</strong> <a href="{{ tb4.repo }}/README.md">Agentic Verification Eval</a></p>

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
