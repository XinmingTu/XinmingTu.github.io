---
layout: distill
title: "The Second Life of Agent Evals"
description: "A benchmark run can be more than a score: frozen agent executions can be compiled into entirely new evaluations."
date: 2026-08-28
tags: ['AI', 'agents', 'benchmarks', 'verification']
categories: blog
permalink: /blog/preview/the-second-life-of-agent-evals/
preview: true
sitemap: false
bibliography: 2026-08-28-the-second-life-of-agent-evals.bib

authors:
  - name: Xinming Tu
    url: "https://xinmingtu.cn"
    affiliations:
      name: University of Washington

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
    margin-top: 2.15em;
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
  d-article figure.sle-figure {
    margin: 1.65rem 0 2rem;
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
  d-article .sle-pullquote {
    color: var(--sle-ink);
    font-family: Georgia, 'Times New Roman', serif;
    font-size: clamp(1.32rem, 3vw, 1.78rem);
    font-style: italic;
    line-height: 1.42;
    margin: 2.15rem auto;
    max-width: 760px;
    text-align: center;
  }
  d-article .sle-stats {
    display: grid;
    gap: 0.65rem;
    grid-template-columns: repeat(3, 1fr);
    margin: 1.2rem 0 1.55rem;
  }
  d-article .sle-stat {
    background: var(--sle-soft);
    border: 1px solid var(--sle-line);
    border-radius: 12px;
    padding: 0.9rem;
    text-align: center;
  }
  d-article .sle-stat strong {
    color: var(--sle-ink);
    display: block;
    font-size: 1.28rem;
  }
  d-article .sle-stat span {
    color: var(--sle-muted);
    display: block;
    font-size: 0.74rem;
    line-height: 1.35;
    margin-top: 0.25rem;
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
    line-height: 1.7;
    margin-top: 2.2rem;
    padding: 1.15rem 1.25rem;
  }
  @media (max-width: 720px) {
    d-article .sle-flow { grid-template-columns: 1fr 1fr; }
    d-article .sle-step:nth-child(2)::after { display: none; }
    d-article .sle-family,
    d-article .sle-stats { grid-template-columns: 1fr; }
  }
  @media (max-width: 430px) {
    d-article .sle-flow { grid-template-columns: 1fr; }
    d-article .sle-step::after { display: none; }
  }
---

{::options parse_block_html="true" /}

<div class="sle-lede">
An agent evaluation usually ends with a number. That is a lossy ending. The run also produced a task, a trajectory, tool interactions, artifacts, and an environment-grounded outcome. <strong>We think those execution artifacts should have a second life.</strong>
</div>

If tasks, traces, outcomes, and provenance are preserved, the output of one evaluation can become the input of another. Not merely *reused* as examples, but **compiled** into new, executable agent tasks.

<figure class="sle-figure">
  <div class="sle-flow" aria-label="From a source agent evaluation to derived agentic evaluations" markdown="0">
    <div class="sle-step source">Source agent eval</div>
    <div class="sle-step">Frozen tasks, traces, outcomes, provenance</div>
    <div class="sle-step compiler">Deterministic eval compiler</div>
    <div class="sle-step derived">Derived agentic evals</div>
  </div>
  <figcaption>The output of one agent evaluation becomes the environment of another.</figcaption>
</figure>

We explored this idea using frozen executions from three Terminal-Bench 3 runs: Fable, GPT-5.6 Sol, and GLM-5.3. The original benchmark asked whether an agent could solve a terminal task. Our derived benchmark asks whether another agent can recognize what actually happened.

## One corpus, three verification tasks

The source corpus contains 85 mixed Best-of-5 pools: each has at least one successful and one failed execution under the original environment verifier. From them, we built a 340-task family.

<div class="sle-family" markdown="0">
  <div class="sle-family-card">
    <strong>Single</strong>
    <span class="count">170</span>
    <span>Judge one trace in isolation: did this execution succeed?</span>
  </div>
  <div class="sle-family-card">
    <strong>Pair</strong>
    <span class="count">85</span>
    <span>Review one successful and one failed trace together, then prefer one.</span>
  </div>
  <div class="sle-family-card">
    <strong>Five</strong>
    <span class="count">85</span>
    <span>Select the most credible execution from the original five-run pool.</span>
  </div>
</div>

The 170 Single and 85 Pair tasks are new native Harbor tasks. The 85 Five tasks were already constructed from the same frozen pools. The source rewards remain hidden; they are visible only to the new verifier.

This is why *compile* matters. The task has changed. The original agent had to solve the problem. The second agent has read-only traces, a different instruction, a different output contract, and a hidden verifier that scores its review.

## Completion is not correctness

The Single reviewer was explicitly warned not to trust an agent's narration or claim of completion. It had to ground its verdict in commands, outputs, errors, edits, and visible verification.

That warning was not enough to make absolute verification reliable.

| Agentic reviewer | Single accuracy | Success recall | Failure recall |
| --- | ---: | ---: | ---: |
| GPT-5.6 Sol | **62.35%** | 81.18% | **43.53%** |
| GLM-5.3 | 60.59% | **97.65%** | 23.53% |
| DeepSeek V4 Pro 0423 preview | 56.47% | 87.06% | 25.88% |

The dataset is balanced, so 50% is both random accuracy and the score of approving every trace. All three reviewers were modestly better than that baseline—but all three were much better at recognizing success than failure. GLM-5.3 approved nearly every successful trace while detecting fewer than one in four failures.

These reviewers were not simply checking whether an execution *looked complete*. They were told that completion claims were not proof. Yet plausible-looking failures still passed review.

## Comparison reveals a stronger signal

Pair gave the reviewer the same positive and negative anchors together, without revealing that exactly one had succeeded. Across all three models, comparative context made the reviewer more skeptical in almost the same way.

| Agentic reviewer | Single failure recall | Pair failure recall | Pair selected success |
| --- | ---: | ---: | ---: |
| GPT-5.6 Sol | 43.53% | **60.00%** | **64.71%** |
| GLM-5.3 | 23.53% | **38.82%** | **69.41%** |
| DeepSeek V4 Pro 0423 preview | 25.88% | **42.35%** | **60.00%** |

Pair failure recall rose by roughly 15–16 percentage points for every reviewer. Pair also raised per-trace classification accuracy by about five points and substantially increased the rate at which both anchors were classified correctly.

But classification and ranking are not the same capability. A reviewer can mislabel one or both traces and still prefer the successful one. GPT-5.6 Sol did exactly that in 22 pools where both isolated reviews said *pass*, yet joint comparison still preferred the successful trace.

<div class="sle-pullquote">
Agents may struggle to certify that one run is correct while still recognizing which run is more likely to be correct.
</div>

That relative judgment is a practical form of verification. It is weaker than an executable oracle, but stronger than choosing blindly.

## Ranking turns sampling into performance

This distinction matters for test-time scaling. Running an agent five times creates pass@5 headroom, but the extra compute helps only if the system can identify a promising run.

Across the 85 mixed five-run pools, uniform selection succeeds 42.12% of the time. Agentic ranking does better:

| Best-of-5 reviewer | Selected a successful trace |
| --- | ---: |
| GPT-5.6 Sol | **63.53%** |
| GLM-5.3 | **55.29%** |
| DeepSeek V4 Flash 0731 | **51.76%** |
| Uniform selection | 42.12% |

For the primary GPT-5.6 Sol reviewer, combining the selector with all-positive and all-fail pools gives the following derived full-source picture across three 74-task Terminal-Bench 3 trace sets:

<div class="sle-stats" markdown="0">
  <div class="sle-stat">
    <strong>33.69%</strong>
    <span>Empirical pass@1 / uniform run selection</span>
  </div>
  <div class="sle-stat">
    <strong>41.89%</strong>
    <span>GPT-ranked Best-of-5 derived score</span>
  </div>
  <div class="sle-stat">
    <strong>55.86%</strong>
    <span>Oracle pass@5 ceiling</span>
  </div>
</div>

The ranker adds about 8.2 absolute points over empirical pass@1, a 24% relative lift, and recovers roughly 37% of the gap to the oracle. This is not a fresh official Terminal-Bench submission; it is arithmetic over frozen source runs. But it shows how verification can convert already-generated diversity into realized task success—even on a difficult benchmark where the underlying pass rate is near one third.

This result builds directly on **LLM-as-a-Verifier**, which established fine-grained trajectory verification and cost-efficient ranking as a mechanism for test-time scaling <d-cite key="kwok2026llmverifier"></d-cite>. Its [current repository](https://github.com/llm-as-a-verifier/llm-as-a-verifier) also reports self-verification on Terminal-Bench 2.1. Our question is complementary: what happens when verification itself becomes a native, tool-using agent task, and when isolated judgment and comparative review are measured on the same Terminal-Bench 3 executions?

## The larger idea: eval compilation

Verification is only the first clean example because the original environment already supplies an operational outcome label. Once that lineage is preserved, one execution corpus can support an entire family of capability evals.

A richer corpus could also yield tasks for failure diagnosis, error localization, progress prediction, recovery, monitoring, or tool-use auditing. These do not all come for free: error localization may require annotation, while recovery may require a saved environment snapshot. The compilation rule must match the evidence actually preserved.

Derived evals also inherit dependencies. Our 85 pools come from 50 unique source tasks, so they are not 85 independent universes. Two negative anchors are explicit unavailable-trajectory sentinels. And the original rewards are operational labels, not a new semantic adjudication of every Terminal-Bench outcome.

That suggests a compact discipline for second-life evals:

1. Preserve source-task and rollout provenance.
2. Keep outcome labels hidden from the new agent.
3. Compile deterministically and verify artifact integrity.
4. Make the capability transformation explicit.
5. Report statistical dependence inherited from the source corpus.

The builders, frozen anchor manifest, trace hashes, hidden-label checks, and task validators in this project are therefore more than implementation hygiene. They make the lineage of each derived task auditable.

## After the score

Agent evals are expensive data-generation processes. They produce much more than the scalar that reaches a leaderboard: they record decisions, observations, tool use, errors, recovery, and evidence. Treating all of that as disposable benchmark exhaust leaves most of the evaluation's value unused.

<div class="sle-coda">
<strong>A benchmark run does not have to end when the score is computed.</strong> For agentic evaluations, that may only be the first thing the data can tell us.
</div>
