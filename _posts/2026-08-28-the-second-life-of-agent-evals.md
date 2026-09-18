---
layout: distill
title: "The Second Life of Agent Evals"
description: "Frozen Terminal-Bench 4.0 runs become new verification tasks: weak absolute judgment, useful comparative selection."
last_updated: 2026-09-18
date: 2026-08-28
tags: ['AI', 'agents', 'benchmarks', 'verification']
categories: blog
permalink: /blog/preview/the-second-life-of-agent-evals/
preview: true
sitemap: false
bibliography: 2026-08-28-the-second-life-of-agent-evals.bib

toc:
  - name: "From frozen runs to verification tasks"
  - name: "Completion is not correctness"
  - name: "Comparison helps ranking"
  - name: "Ranking turns sampling into performance"
  - name: "A prompt can move the choice without improving it"
  - name: "Beyond verification"
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
{% assign flash = tb4.reviewers[3] %}

<div class="sle-lede">
<div class="sle-lede-label">Summary</div>
<strong>An agent evaluation can have a second life.</strong> We turn frozen Terminal-Bench 4.0 runs into new verification tasks: judge one run, compare two, or select among five. Single-run accuracy remains 50.0–59.5%, while the strongest Five reviewer selects a successful run in <strong>{{ gpt.five }}%</strong> of mixed pools, against {{ tb4.five_baseline }}% uniform choice.
</div>

The executions stay fixed. The question changes—from solving the task to judging the run.

An evaluation leaves behind more than a score. It records actions, observations, and the files an agent produced. Preserve that evidence alongside its outcome, and a completed run can become the environment for a new agent task.

<figure class="sle-figure" markdown="0">
  <div class="sle-flow" aria-label="Frozen source runs are compiled into new verification tasks" markdown="0">
    <div class="sle-step source">Source agent eval</div>
    <div class="sle-step">Frozen run bundles + hidden outcomes</div>
    <div class="sle-step compiler">Derived-task builder</div>
    <div class="sle-step derived">Verify, compare, select</div>
  </div>
  <figcaption>The output of one agent evaluation becomes the environment of another.</figcaption>
</figure>

<p class="sle-update">Updated {{ tb4.updated }} · TB4 results through September 17 · <a href="{{ tb4.repo }}/README.md">Frozen experiment snapshot</a></p>

## From frozen runs to verification tasks

Our main experiment uses Terminal-Bench 4.0<d-cite key="terminalbench4"></d-cite>. Each source evaluation contains 66 tasks with five attempts per task. We reuse four source configurations: Fable 5.1 with Claude Code, GPT-5.6 Sol with Codex, GLM-5.3 with Claude Code, and GPT-6 Astra with Codex. **GPT-6 is a source of completed runs, not a reviewer.**

The reusable object is a **run bundle: trajectory plus recorded artifacts**. The original task instruction supplies the context. Another agent inspects that evidence using shell tools, without changing the source execution. Recorded artifacts may be only a partial snapshot of the original environment.

A *pool* is five attempts at the same task from one source configuration. We retain archive-valid, metadata-eligible *mixed pools*: at least one attempt succeeded and at least one failed. Selection can change the outcome in these pools. The four sources contribute 30, 28, 21, and 18 pools respectively: **{{ tb4.five_pools }} pools, {{ tb4.source_runs }} source runs, and 49 distinct task names**.

We compile those bundles into Harbor-format tasks<d-cite key="harbor"></d-cite> with different instructions and output contracts:

<div class="sle-family" markdown="0">
  <div class="sle-family-card">
    <strong>Verify one run</strong>
    <span class="count">158 tasks</span>
    <span><em>Single</em> · Judge one successful or failed anchor. Three sources, 79 pools.</span>
  </div>
  <div class="sle-family-card">
    <strong>Compare two runs</strong>
    <span class="count">79 tasks</span>
    <span><em>Pair</em> · Judge both anchors and choose one. The same three sources.</span>
  </div>
  <div class="sle-family-card">
    <strong>Choose among five</strong>
    <span class="count">{{ tb4.five_pools }} tasks</span>
    <span><em>Five</em> · Select among all five runs. Four sources, including GPT-6.</span>
  </div>
</div>

Single and Pair cover 79 pools and 48 task names from the first three sources; GPT-6-source Single/Pair were not run. Every Single pair of anchors contains one successful and one failed run, giving 158 balanced judgments. Every Pair contains one of each, though its reviewer is not told that exactly one succeeded. Both have a 50% blind baseline. Five preserves each pool's original mix: {{ tb4.candidate_successes }} of {{ tb4.source_runs }} candidates succeeded, so uniform selection has a **{{ tb4.five_baseline }}%** baseline.

All four reviewers—GPT-5.6 Sol, GLM-5.3, DeepSeek V4.1 Flash, and GLM-5.3 Flash—use mini-swe-agent to inspect the same frozen evidence. Original rewards and verifier outputs are withheld from their inputs and used only for scoring. Evidence is read-only; reviewers may inspect it and perform scratch checks, but may not repair a candidate or continue the original task.

The [experiment repository]({{ tb4.repo }}/README.md) records the builders, manifests, compact results, and reproduction steps. The earlier TB3 trace-only study is retained as a [pilot](#the-tb3-pilot).

## Completion is not correctness

Single asks a direct question: did this completed run satisfy the original task? Its instruction tells the reviewer to check concrete requirements and explicitly warns that a completion claim is not proof.

<details class="sle-instruction" markdown="1">
<summary>Show the Single Full instruction</summary>
<div class="sle-instruction-body" markdown="1">

```text
{% include second-life-tb4/single-full.txt %}
```

</div>
</details>

<figure class="sle-figure" markdown="0">
  <img src="/assets/img/2026-08-28-second-life-agent-evals/tb4-single-verdicts.svg" alt="Four Single Full verdict matrices. Each reviewer sees 79 successful and 79 failed runs. Pass, Fail, and Invalid are separate columns; GLM and GLM Flash approve most failed runs." loading="lazy">
  <figcaption>Rows: original environment outcome. Columns: reviewer output. Every row contains 79 runs. Orange cells are incorrect verdicts; gray cells are invalid outputs, which count as errors but are not literal pass or fail judgments.</figcaption>
</figure>

Accuracy ranges from 50.0% to 59.5%. Approval bias is especially strong for the GLM reviewers: GLM-5.3 recognizes 98.7% of successful runs but only 10.1% of failures. GLM Flash recognizes all 79 successes, yet correctly rejects only 9 of 79 failures. Of the remaining 70 failed runs, it approves 69 and produces one invalid response.

GPT-5.6 Sol has the highest failure recall here, but still approves 50 of 79 failed runs. Access to recorded outputs does not make these reviewers reliable certifiers of individual executions.

This is a finding about the Full-bundle setting. It does not establish the effect of artifacts: the main panel has no matched Trace-only arm, and comparing it with TB3 would also change tasks and some model versions.

## Comparison helps ranking

Pair reviews the same successful and failed anchors together, asks for an independent verdict on each, then asks which candidate has stronger evidence. Five extends selection to the original five-run pool.

<details class="sle-instruction" markdown="1">
<summary>Show the Pair Full instruction</summary>
<div class="sle-instruction-body" markdown="1">

```text
{% include second-life-tb4/pair-full.txt %}
```

</div>
</details>

| Agentic reviewer | Single accuracy · 158 runs | Pair selection · 79 pools | Five selection · {{ tb4.five_pools }} pools |
| --- | ---: | ---: | ---: |
{% for reviewer in tb4.reviewers %}| {{ reviewer.name }} | {{ reviewer.single }}% | {{ reviewer.pair }}% | {{ reviewer.five }}% ({{ reviewer.five_wins }}/{{ tb4.five_pools }}) |
{% endfor %}| Blind baseline | 50.0% | 50.0% | {{ tb4.five_baseline }}% |

<figure class="sle-figure" markdown="0">
  <img src="/assets/img/2026-08-28-second-life-agent-evals/tb4-selection.svg" alt="Pair and Five successful-selection rates for four reviewers. Pair uses 79 pools with a 50 percent baseline; Five uses 97 pools with a 55.3 percent baseline. GPT reaches 78.4 percent on Five." loading="lazy">
  <figcaption>Selection rates conditional on mixed pools. Dashed lines show each condition's uniform-choice baseline. Pair and Five have different candidate sets, baselines, and source coverage.</figcaption>
</figure>

GLM-5.3 selects the successful Pair member 65.8% of the time, but labels both candidates correctly in only 41.8% of pairs. The corresponding GPT rates are 62.0% and 44.3%. **Choosing a better run and certifying each run's correctness are distinct capabilities.**

On Five, GPT selects a successful candidate in **{{ gpt.five_wins }}/{{ tb4.five_pools }} pools ({{ gpt.five }}%)**, {{ gpt.five_gain }} percentage points above uniform choice. GLM Flash reaches {{ flash.five }}%, even though its Single failure recall is only {{ flash.failure_recall }}%. Its Five point estimate exceeds full GLM's, but that ordering alone does not establish a reliable model advantage.

The original three-source GPT result is 64/79 (81.0%); adding the GPT-6-source batch, 12/18, gives the current 76/97 aggregate. The combined rate weights each pool equally. It is not an equal-weight average of the four sources.

These columns answer different questions. Single evaluates two balanced anchors per pool, not independent scores for all five candidates. Five can contain several successful candidates and includes an additional source. The table therefore does not measure a causal benefit of more context. On the original 79 pools, the reported paired GPT Five gain over uniform is +25.1 points, with a task-cluster 95% interval of [16.3, 33.9]; that interval should not be attached to the expanded 97-pool result. [Analysis and intervals]({{ tb4.repo }}/reports/tbench4-complete-results-2026-09-16.md).

## Ranking turns sampling into performance

Running a solver five times creates an opportunity to improve success. Oracle pass@5 tells us whether any attempt succeeded. A practical selector must identify one of those successes using only the available evidence.

<details class="sle-instruction" markdown="1">
<summary>Show the Five Full instruction</summary>
<div class="sle-instruction-body" markdown="1">

```text
{% include second-life-tb4/five-full.txt %}
```

</div>
</details>

The {{ gpt.five }}% figure above concerns mixed pools only. To estimate the effect across all 66 tasks in each source evaluation, we restore all-success and all-failure pools and use the **same GPT-5.6 Sol reviewer** across all four sources.

<figure class="sle-figure" markdown="0">
  <img src="/assets/img/2026-08-28-second-life-agent-evals/tb4-pass-at-k.svg" alt="Four panels show oracle pass at one through five and GPT reviewer selection at five. Reconstructed whole-job success is 70.0 percent for Fable, 51.2 for GPT-5.6 Sol, 45.8 for GLM, and 62.1 for GPT-6 Astra." loading="lazy">
  <figcaption>Oracle pass@k over all 66 tasks per source. Stars mark the GPT-5.6 Sol reviewer at k=5 only. Whiskers bound outcomes on excluded mixed pools; they are coverage bounds, not confidence intervals. Selector values are reconstructions, not official end-to-end benchmark scores.</figcaption>
</figure>

| Frozen source runs | Empirical pass@1 | Five + GPT reviewer | Oracle pass@5 |
| --- | ---: | ---: | ---: |
{% for source in tb4.sources %}| {{ source.name }} | {{ source.pass1 }}% | **{{ source.selected }}%** | {{ source.pass5 }}% |
{% endfor %}

For Fable, selection raises reconstructed success from 57.9% to 70.0%, a 12.1-point gain. For GPT-5.6 Sol source runs, it rises from 37.3% to 51.2%, a 13.9-point gain. The benefit is smaller on GLM and GPT-6 source runs, about 3.9 points each. The GPT-6 source has more all-success pools and less pass@5 headroom than Fable in these frozen samples.

<details class="sle-instruction" markdown="1">
<summary>How the whole-job reconstruction works</summary>
<div class="sle-instruction-body" markdown="1">

For each source, we add the all-success pool count, successful reviewed selections, and a uniform-choice fallback for excluded mixed pools, then divide by 66. Homogeneous pools were not reviewed; the calculation assumes a valid candidate is selected there.

Ten mixed pools were excluded by construction: eight had source-run exceptions and two failed artifact collection. They are distributed as 3 Fable, 5 GPT-5.6 Sol, 2 GLM, and 0 GPT-6 pools. All 97 eligible pools have been reviewed by all four reviewers. One missing GLM source reward counts as failure.

For example, Fable has 19 all-success pools, 26 successful GPT selections, and three excluded pools containing 2, 3, and 1 successful attempts:

```text
(19 + 26 + (2 + 3 + 1) / 5) / 66 = 70.0%
```

Letting every excluded-pool selection fail or succeed gives coverage bounds of 68.2–72.7% for Fable, 47.0–54.5% for GPT-5.6 Sol, and 43.9–47.0% for GLM. GPT-6 needs no fallback.

The oracle curve is the probability that a uniformly sampled subset of k frozen attempts contains a success. We did not run reviewers at k=1 through 4. [Source data and assumptions]({{ tb4.repo }}/results/tbench4-pass-at-k.json).

</div>
</details>

This builds on **LLM-as-a-Verifier** and its use of trajectory verification for test-time scaling<d-cite key="kwok2026llmverifier"></d-cite>. Here, archived runs become native, tool-using verification tasks. The saved evidence lets us measure both absolute judgment and selection without rerunning the original solvers.

## A prompt can move the choice without improving it

The Five instruction includes an example output, `{"selected_candidate":3}`. In the original 79-pool panel, DeepSeek V4.1 Flash chose candidate 3 in **64 of 79** reviews. A separate control kept evidence, order, model, and reasoning settings fixed, but replaced the numbered example with a prose schema.

<figure class="sle-figure" markdown="0">
  <img src="/assets/img/2026-08-28-second-life-agent-evals/tb4-prompt-position.svg" alt="DeepSeek selected candidate 3 in 64 of 79 original-prompt reviews. With a neutral output example it selected candidate 1 in 70 of 79 reviews; success changed from 58.2 to 59.5 percent." loading="lazy">
  <figcaption>One prompt-sensitivity control on the original 79 pools. Removing the fixed candidate example changes the position distribution substantially, while successful selection changes little.</figcaption>
</figure>

The control chose candidate 1 in **70 of 79** reviews. Success changed from 46/79 (58.2%) to 47/79 (59.5%): +1.3 points, with a paired task-cluster 95% interval of [−13.5, 16.9]. Both conditions produced valid JSON in every case.

Removing the fixed example did not produce a clear quality improvement. This single additional realization is a sensitivity check, not a definitive causal attribution independent of sampling noise. The control stays separate from the headline Five aggregate. [Prompt-control report]({{ tb4.repo }}/reports/tbench4-complete-results-2026-09-16.md#deepseek-five-prompt-sensitivity).

## Beyond verification

Verification is one use of a saved run. The same corpus could support failure diagnosis, error localization, monitoring, or recovery, provided it preserves the evidence each task requires. Error localization may need annotation; recovery may need a restorable environment, beyond the recorded artifacts used here.

The general recipe is to preserve the execution and its provenance, define a new capability question, expose only the evidence that question permits, and build a scoring rule. A benchmark's output can then become another benchmark's input.

<div class="sle-coda">
<strong>A benchmark run does not have to end when the score is computed.</strong> It can become the raw material for the next benchmark.
</div>

## Appendix

### Dataset notes and uncertainty

The labels are the original benchmark's operational verifier rewards, not fresh semantic adjudications. Task names recur across sources: 97 pools correspond to 49 task names, and the Single/Pair panel covers 48. Reported intervals resample task-name clusters, rather than treating every run as independent.

| Reviewer | Single accuracy · 95% cluster CI | Pair selection · 95% cluster CI |
| --- | ---: | ---: |
{% for reviewer in tb4.reviewers %}| {{ reviewer.name }} | {{ reviewer.single_ci }}% | {{ reviewer.pair_ci }}% |
{% endfor %}

Invalid outputs remain in the denominator as failures. Source slices have different task compositions, so their selection rates do not establish which source model's runs are intrinsically easier to verify. The GPT-6 extension has only 18 mixed pools: its GPT and GLM Flash results both equal 12/18, with broad [44.4%, 88.9%] selection intervals. A tie here does not establish equivalent reviewers. [GPT-6 extension]({{ tb4.repo }}/reports/tbench4-gpt6-source-results-2026-09-17.md).

Earlier compatible observations are reused once, based on identical trial IDs, anchors, and rewards, rather than selected for correctness. The latest GLM Flash batch completes Single and Pair while reusing its prior Five results. Automated leakage checks cover declared visible surfaces; they do not prove that arbitrary archived content contains no indirect shortcuts.

### The TB3 pilot

The earlier Terminal-Bench 3.0 study<d-cite key="terminalbench3"></d-cite> used trajectories alone: 85 mixed pools, 50 task names, and 340 derived tasks. GPT-5.6 Sol selected a successful run in 63.53% of Five pools, against 42.12% uniform choice. Across the three original 74-task source evaluations, its average reconstructed success was 41.89%, compared with 33.69% pass@1 and 55.86% oracle pass@5.

Those results remain useful historical evidence. TB3 and TB4 differ in tasks, available evidence, and some reviewer versions, so their difference is not a controlled estimate of artifact benefit. The initial 18-pool TB4 study included a matched Trace-only Single control; the expanded panel did not repeat that ablation. [TB3 report]({{ tb4.repo }}/reports/context-ladder-reviewer-comparison-2026-08-28.md) · [Initial TB4 study]({{ tb4.repo }}/reports/tbench4-run-bundle-results-2026-09-05.md).

### Recorded cost of the latest extensions

These are three distinct batches of newly paid reviews. Reused observations are not charged again in this table.

| Completed batch | New reviews | Recorded model cost |
| --- | ---: | ---: |
{% for batch in tb4.cost_batches %}| {{ batch.name }} | {{ batch.reviews }} | ${{ batch.cost }} |
{% endfor %}

The September 16 batch includes the separate DeepSeek prompt control and GLM Flash's original 79 Five reviews. These costs exclude earlier TB4 panels, the September 12 Five extension, original solver execution, and infrastructure; they are neither lifetime project spend nor provider invoices. Pricing, caching, and context lengths differ across models, so these batch totals are not a controlled efficiency comparison.

### Data and reproduction

This revision pins results to experiment commit [`6d99501`]({{ tb4.repo }}/README.md). [Local result snapshots and provenance](/assets/data/second-life-tb4/README.md) drive the tables and four TB4 figures. Regenerate them without model calls using `python scripts/generate_second_life_tb4_figures.py` with Matplotlib installed. The original TB3 plotting script and figures remain available for the pilot.

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
