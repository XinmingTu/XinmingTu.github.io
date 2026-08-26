---
layout: distill
title: "The Problem Before the Model / 模型之前的问题"
description: "Before AI can solve a scientific problem, science has to make the problem solvable."
date: 2026-08-21
tags: ['AI', 'science', 'benchmarks']
categories: blog
permalink: /blog/preview/the-problem-before-the-model/
preview: true
sitemap: false
bibliography: 2026-08-21-the-problem-before-the-model.bib

authors:
  - name: Xinming Tu
    url: "https://xinmingtu.cn"
    affiliations:
      name: University of Washington

_styles: |
  d-article {
    --sci-ink: #20242b;
    --sci-body: #434a55;
    --sci-muted: #747d8b;
    --sci-line: #dfe4e8;
    --sci-soft: #f6f8f8;
    --sci-card: #ffffff;
    --sci-blue: #496aa8;
    --sci-blue-soft: #eef3fb;
    --sci-green: #2d796a;
    --sci-green-soft: #eaf6f2;
    --sci-warm: #ad6641;
    --sci-warm-soft: #fff2ea;
  }
  html[data-theme='dark'] d-article {
    --sci-ink: #edf1f4;
    --sci-body: #cbd1d8;
    --sci-muted: #9aa4b0;
    --sci-line: #41474e;
    --sci-soft: #24282c;
    --sci-card: #2a2f34;
    --sci-blue: #99b5eb;
    --sci-blue-soft: #2d384b;
    --sci-green: #7ac8b4;
    --sci-green-soft: #293e39;
    --sci-warm: #e1a17f;
    --sci-warm-soft: #45352d;
  }
  d-article p,
  d-article li {
    color: var(--sci-body);
  }
  d-article h2 {
    color: var(--sci-ink);
    margin-top: 2.2em;
  }
  d-article .sci-lede {
    border-left: 3px solid var(--sci-green);
    color: var(--sci-body);
    font-size: 1.07rem;
    line-height: 1.74;
    margin: 0.25rem 0 2rem;
    padding: 0.12rem 0 0.12rem 1rem;
  }
  d-article .sci-lede strong {
    color: var(--sci-ink);
  }
  d-article .sci-pullquote {
    color: var(--sci-ink);
    font-family: Georgia, 'Times New Roman', serif;
    font-size: clamp(1.35rem, 3vw, 1.82rem);
    font-style: italic;
    line-height: 1.42;
    margin: 2.25rem auto;
    max-width: 740px;
    text-align: center;
  }
  d-article .sci-pullquote span {
    color: var(--sci-muted);
    display: block;
    font-size: 0.61em;
    font-style: normal;
    margin-top: 0.58rem;
  }
  d-article figure.sci-figure {
    margin: 1.8rem 0 2.1rem;
  }
  d-article figure.sci-figure figcaption {
    color: var(--sci-muted);
    font-size: 0.84rem;
    line-height: 1.5;
    margin-top: 0.72rem;
    text-align: center;
  }
  d-article .sci-loops {
    background: var(--sci-soft);
    border: 1px solid var(--sci-line);
    border-radius: 15px;
    padding: 1.05rem;
  }
  d-article .sci-loop {
    align-items: center;
    display: grid;
    gap: 0.65rem;
    grid-template-columns: 7.2rem 1fr;
  }
  d-article .sci-loop + .sci-loop {
    border-top: 1px solid var(--sci-line);
    margin-top: 0.9rem;
    padding-top: 0.9rem;
  }
  d-article .sci-loop-label {
    color: var(--sci-muted);
    font-size: 0.72rem;
    font-weight: 750;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }
  d-article .sci-flow {
    align-items: center;
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
  }
  d-article .sci-node {
    background: var(--sci-card);
    border: 1px solid var(--sci-line);
    border-radius: 999px;
    color: var(--sci-ink);
    font-size: 0.81rem;
    font-weight: 650;
    padding: 0.4rem 0.64rem;
    white-space: nowrap;
  }
  d-article .sci-node.compute {
    background: var(--sci-blue-soft);
    color: var(--sci-blue);
  }
  d-article .sci-node.world {
    background: var(--sci-green-soft);
    color: var(--sci-green);
  }
  d-article .sci-node.friction {
    background: var(--sci-warm-soft);
    color: var(--sci-warm);
  }
  d-article .sci-arrow {
    color: var(--sci-muted);
    font-size: 0.86rem;
  }
  d-article .sci-questions {
    display: grid;
    gap: 0.8rem;
    grid-template-columns: repeat(3, 1fr);
  }
  d-article .sci-question {
    background: var(--sci-card);
    border: 1px solid var(--sci-line);
    border-radius: 14px;
    padding: 1rem;
  }
  d-article .sci-question-num {
    color: var(--sci-green);
    display: block;
    font-size: 0.7rem;
    font-weight: 780;
    letter-spacing: 0.1em;
    margin-bottom: 0.65rem;
    text-transform: uppercase;
  }
  d-article .sci-question strong {
    color: var(--sci-ink);
    display: block;
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 1.03rem;
    line-height: 1.35;
    margin-bottom: 0.48rem;
  }
  d-article .sci-question span:last-child {
    color: var(--sci-muted);
    display: block;
    font-size: 0.8rem;
    line-height: 1.45;
  }
  d-article .sci-equation {
    color: var(--sci-ink);
    font-family: Georgia, 'Times New Roman', serif;
    font-size: clamp(1.22rem, 2.7vw, 1.65rem);
    margin: 1.7rem auto;
    text-align: center;
  }
  d-article .sci-matrix {
    display: grid;
    gap: 0.55rem;
    grid-template-columns: repeat(2, 1fr);
  }
  d-article .sci-quadrant {
    border: 1px solid var(--sci-line);
    border-radius: 12px;
    min-height: 7rem;
    padding: 0.9rem;
  }
  d-article .sci-quadrant strong {
    color: var(--sci-ink);
    display: block;
    font-size: 0.93rem;
    margin-bottom: 0.38rem;
  }
  d-article .sci-quadrant span {
    color: var(--sci-muted);
    font-size: 0.78rem;
    line-height: 1.42;
  }
  d-article .sci-quadrant.target {
    background: var(--sci-green-soft);
    border-color: color-mix(in srgb, var(--sci-green) 34%, var(--sci-line));
  }
  d-article .sci-quadrant.engineer {
    background: var(--sci-warm-soft);
    border-color: color-mix(in srgb, var(--sci-warm) 30%, var(--sci-line));
  }
  @media (max-width: 720px) {
    d-article .sci-loop {
      align-items: start;
      grid-template-columns: 1fr;
    }
    d-article .sci-questions {
      grid-template-columns: 1fr;
    }
    d-article .sci-matrix {
      grid-template-columns: 1fr;
    }
  }
---

{::options parse_block_html="true" /}

<div class="sci-lede">
AI 的 capability 在许多方向同时提高，但它带来的 scientific progress 却极不均匀。Formal mathematics 已经出现能在 theorem prover 中 search、验证并继续学习的系统 <d-cite key="hubert2026alphaproof"></d-cite>；protein structure 有 AlphaFold；而到了 cell、tissue 或 organism，连“解决了问题”究竟意味着什么，往往都还不够清楚。最容易的解释是：<strong>biology 比 mathematics 更复杂。</strong>但 complexity 也许不是最关键的变量。
</div>

一个极其复杂的现实系统，只要找到了合适的 abstraction，也可能变得 tractable。反过来，一个看起来清楚的问题，如果 state、feedback 与 success criteria 没有对齐，也可能永远只是一个 leaderboard。

<div class="sci-pullquote">
A scientific problem is not AI-operational merely because we can benchmark it.
<span>只有当 benchmark 上的成功，确实构成 scientific progress 的证据时，问题才真正变得 AI-operational。</span>
</div>

这种差异不只是来自它们包含多少 variables。真正的问题是：我们能否把 reality 压缩成一个 AI 可以反复行动、得到可信反馈、再继续 search 的 problem。

这也是为什么“更复杂”不一定等于“更难 operationalize”。一篇讨论 generative AI 与 cell biology 的 Cell Perspective 指出，immune system 虽然跨越更多 cell types 与 spatiotemporal scales，但针对特定 immune function 做 coarse-graining 时，许多维持基础生存的 cellular machinery 未必需要被同等精细地建模 <d-cite key="dupire2026fifteen"></d-cite>。关键不是复刻全部 reality，而是保留与目标有关的 structure。

**The question is not how complex reality is. The question is whether we know how to compress it into a problem.**

Scientific representation 本身就是一种 compression。Temperature、gene、protein structure、cell state 都不是 reality 本身；它们是为了某类 prediction 与 intervention 而保留信息的 abstraction。

## 1. AI Compounds Where Reality Can Answer Back

AI 最容易 compound 的环境有一个共同结构。Coding、games 与 formal mathematics 之所以对 AI 格外友好，并不只是因为它们是 digital，而是因为 generation 可以迅速遇到 consequence：

$$
\text{Generate} \rightarrow \text{Verify} \rightarrow \text{Update} \rightarrow \text{Search again}
$$

Formal mathematics 是一个 extreme case。Candidate proof 与 formal verifier 存在于同一个 computational substrate 中；proof 对不对，可以低成本、并行、近乎即时地得到反馈。AlphaProof 正是通过与 Lean environment 交互，从 verified proof attempts 中持续学习 <d-cite key="hubert2026alphaproof"></d-cite>。

现实科学的 loop 更长：prediction 要变成 intervention，intervention 要穿过 physical world，最后才成为 measurement。中间每一段都有 latency、noise 与 cost。

<figure class="sci-figure" markdown="0">
  <div class="sci-loops">
    <div class="sci-loop">
      <div class="sci-loop-label">Formal loop</div>
      <div class="sci-flow">
        <span class="sci-node compute">Model</span><span class="sci-arrow">→</span>
        <span class="sci-node compute">Candidate proof</span><span class="sci-arrow">→</span>
        <span class="sci-node world">Formal verifier</span><span class="sci-arrow">↺</span>
      </div>
    </div>
    <div class="sci-loop">
      <div class="sci-loop-label">Physical loop</div>
      <div class="sci-flow">
        <span class="sci-node compute">Model</span><span class="sci-arrow">→</span>
        <span class="sci-node compute">Prediction</span><span class="sci-arrow">→</span>
        <span class="sci-node friction">Experiment</span><span class="sci-arrow">→</span>
        <span class="sci-node world">Measurement</span><span class="sci-arrow">↺</span>
      </div>
    </div>
  </div>
  <figcaption>AI progress depends not only on the quality of generation, but on how quickly and reliably the domain can answer back.</figcaption>
</figure>

可以把这种能力叫作 **Verification Bandwidth**：一个 scientific loop 在单位时间与成本下，可以返回多少可靠、可归因的新信息。作为直觉：

$$
B_{\text{verify}} \propto \frac{\text{Throughput} \times \text{Reliability}}{\text{Cost} \times \text{Latency}}
$$

这不是一个需要精确估计的 universal metric，而是一个 design principle：**AI progresses fastest where science can return high-bandwidth, trustworthy feedback.**

## 2. A Benchmark Is Not Yet a Scientific Problem

但 verification bandwidth 仍然不够。一个 verifier 可以非常 objective，却验证了错误的 object。

Dupire 等人的 Cell Perspective 很清楚地看到了现有 biology benchmarks 的问题：retrospective statistical superiority 经常被误认为 biological progress。于是作者提出 15 个 grand challenges、purpose-built perturbational datasets、blinded prospective evaluation，并把快速迭代的 Tier 1 methods benchmarks 与强调 experimental actionability 的 Tier 2 discovery benchmarks 分开 <d-cite key="dupire2026fifteen"></d-cite>。这是重要的一步。

但同一篇文章也暴露了更深的 difficulty。比如 “organismal responses” 被落成：根据 vaccination 前的 immune profile，预测之后的 antibody 与 T cell responses；“cell state reprogramming” 被落成：实施 perturbation，再比较 molecular 与 phenotypic readouts。为了让它们可评估，Table 2 必须进一步给出 AUROC、Pearson $r$、sensitivity 与 specificity 等 thresholds。

这些都是 legitimate experiments。问题是：**通过这些 benchmarks，是否就意味着我们理解了标题所指向的 scientific object？**一次 vaccination response 不等于 organismal behavior；一个 molecular readout 也未必完整刻画 cell fate。

这并不是 paper 的错误。作者自己明确把这些 challenges 称为 broad、open-ended programmatic goals，而不是具有 unambiguous resolution criteria 的数学问题。这个 tension 揭示了 science operationalization 最难的一层：

<div class="sci-pullquote">
The easiest thing to standardize is often not the thing we most want to understand.
<span>可测量，不等于测到了我们真正声称已经理解的东西。</span>
</div>

因此，除了“能不能 measure”，还需要问 **Verifier Alignment**：observable metric 与 scientific claim 之间的 correspondence 到底有多强？Benchmarkability 只保证系统能得到一个 score；scientific operationalization 还要求这个 score 是科学进展的有效证据。

## 3. Three Questions for Making Science Operational

在训练更大的 model 之前，一个 scientific problem 至少需要回答三个 questions：

<figure class="sci-figure" markdown="0">
  <div class="sci-questions">
    <div class="sci-question">
      <span class="sci-question-num">01 · State</span>
      <strong>What is the state?</strong>
      <span>Representation preserves what matters and makes the problem effectively closed.</span>
    </div>
    <div class="sci-question">
      <span class="sci-question-num">02 · Feedback</span>
      <strong>Can reality answer back?</strong>
      <span>Verification is affordable, timely, reliable, and scalable.</span>
    </div>
    <div class="sci-question">
      <span class="sci-question-num">03 · Meaning</span>
      <strong>Does the answer mean what we think?</strong>
      <span>The verifier and its coverage match the scientific claim.</span>
    </div>
  </div>
  <figcaption>Representation makes a question computable; feedback makes learning possible; alignment makes the result scientifically meaningful.</figcaption>
</figure>

### 1. What is the state?

我们需要一个 representation，使它为当前问题保留足够的信息。这里的 closure 不是说世界真的封闭，而是：给定这个 state，未被表示的 variables 不会持续主导我们想预测的 outcome。

**A scientific representation is a claim about what can safely be ignored.**

Virtual Cell 的难点并不是 cell 有很多 variables，而是：**we do not yet know the sufficient statistics of a cell.**什么需要被保留——transcriptome、protein activity、spatial organization、history、microenvironment——取决于问题本身。AI Virtual Cell 的愿景因此把 universal state representations、dynamics 与 in-silico perturbation 同时列为核心能力 <d-cite key="bunne2024virtualcell"></d-cite>；但 representation 是否 sufficient，最终仍要由目标 experiment 来回答。

### 2. Can reality answer back?

Prediction 之后，能否进行真正区分 hypotheses 的 intervention？实验需要多久、多少钱？measurement 有多 noisy？能否 automate、parallelize，并把结果归因到具体 action？Observation 可以提供 evidence；intervention 更进一步，让模型看到 action 的 consequence。

当 hypothesis generation 逐渐接近免费时，稀缺的就不再是 ideas，而是 contact with reality。

**As hypothesis generation becomes cheap, contact with reality becomes the scarce resource.**

Faster models do not automatically create faster science if reality still runs at biological speed.

### 3. Does the answer mean what we think it means?

即使 experiment 返回一个清楚的 number，仍要检查 coverage：一个 cell line 的结果能否代表 primary tissue？一个 cohort 能否覆盖 intended population？一个短期 molecular proxy 能否代表长期 function？

**A verifier can be objective and still be scientifically misaligned.**

Operationalization fails when the benchmark becomes easier to optimize than the scientific claim it was supposed to represent.

如果这三个条件能在一个有意义的 instance family 中同时成立，solution 才可能被 amortize：一次学习，不只解决一个样本，而是反复解决同一类 scientific problems。

## 4. AlphaFold Inherited a Well-Specified Problem

AlphaFold 的意义不只是 model architecture 的成功。它继承了一个被 structural biology 长期打磨过的问题：input 是 sequence，target 是相对标准化的 3D structure；数十年的实验积累形成了 Protein Data Bank（PDB）；CASP 又用尚未公开的 experimental structures 进行 blind assessment <d-cite key="jumper2021alphafold"></d-cite>。

换成前面的三个 questions：

1. **State** 相对清楚：sequence 与 atomic coordinates 提供了强而可计算的 representations——尽管它们仍不能覆盖所有 dynamics、ligands 与 cellular contexts。
2. **Reality could answer back**：experimental structural biology 很昂贵，但几十年的结果已经被持续标准化、共享并积累。
3. **Verifier alignment 很强**：对 structure-prediction 这个 claim，predicted coordinates 与 blinded experimental structure 的 correspondence 相对直接。

这使得 progress 能在广大的 protein family 上被 amortize。AlphaFold 不只是解决了一个 structure；一个 learned system 开始重复解决整个 problem family。

<div class="sci-pullquote">
Before there was AlphaFold, there had to be an AlphaFold-shaped problem.
<span>AlphaFold 不只解决了一个 scientific problem；它继承了一个已经被异常清楚地 specified 的问题。</span>
</div>

## 5. The Next AlphaFold May Begin as Problem Engineering

所以寻找 “the next AlphaFold”，不能只问哪个 scientific problem 最重要。更有用的问题是：**哪个重要问题最接近变得 AlphaFold-shaped？**

<div class="sci-equation">Scientific opportunity = Importance × Operationalizability</div>

<figure class="sci-figure" markdown="0">
  <div class="sci-matrix">
    <div class="sci-quadrant engineer">
      <strong>Important · Not yet operational</strong>
      <span>Engineer representations, measurements, interventions, and aligned verifiers.</span>
    </div>
    <div class="sci-quadrant target">
      <strong>Important · Operational</strong>
      <span>High-leverage target for model building and amortized scientific search.</span>
    </div>
    <div class="sci-quadrant">
      <strong>Lower importance · Not operational</strong>
      <span>Rethink the object before investing in scale.</span>
    </div>
    <div class="sci-quadrant">
      <strong>Lower importance · Operational</strong>
      <span>Useful testbed, but not automatically scientific progress.</span>
    </div>
  </div>
  <figcaption>The next breakthrough may sit one step left of “ready”: scientifically important, with problem engineering as the remaining bottleneck.</figcaption>
</figure>

这改变了 AI for Science 的 investment logic。除了 more models、more compute 与 more generic data，我们还需要 purpose-built perturbational datasets、standardized representations、automated experiments、better measurements，以及 truly blinded prospective benchmarks。Cell Perspective 的最大价值也正在这里：它要求数据围绕具体 questions 被重新生成，而不是继续聚合 originally collected for other purposes 的 public datasets <d-cite key="dupire2026fifteen"></d-cite>。

**The next AlphaFold may begin as a problem-engineering project, not a model project.**

Scientific infrastructure determines where intelligence can compound.

## 6. Who Formulates the Problem?

到目前为止，我们仍默认 humans 决定 objects、state space、measurement 与 success criteria，然后让 AI 在其中 search：**Humans formulate. AI searches.**

这已经可能带来巨大的 progress，但它还不是 science 的全部。更远的 frontier，是 AI 开始参与 formulation：发现当前 representation 丢失了关键变量，指出 benchmark 正在优化错误的 proxy，或者设计一个能区分两种 competing abstractions 的 experiment。这不是跳过 verification；恰恰相反，它是把 verification loop 用在 problem definition 本身。

Today, we make parts of reality legible to AI, and AI searches them. Tomorrow: **can AI help decide how reality should be made legible?**

**The deepest frontier in AI for Science may not be solving the problems we give AI, but learning whether AI can help us discover what the right problems are.**
