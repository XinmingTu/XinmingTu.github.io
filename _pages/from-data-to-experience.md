---
layout: distill
title: "From Data to Experience / 从数据到经验"
description: "Agent 改变的不只是训练数据的数量，而是模型究竟在压缩什么。"
date: 2026-08-20
tags: ['AI', 'agents', 'learning']
permalink: /preview/from-data-to-experience/
preview: true
nav: false
sitemap: false
bibliography: 2026-08-20-from-data-to-experience.bib

authors:
  - name: Xinming Tu
    url: "https://xinmingtu.cn"
    affiliations:
      name: University of Washington

_styles: |
  d-article {
    --exp-ink: #20242d;
    --exp-body: #414754;
    --exp-muted: #737b8c;
    --exp-line: #dfe3ea;
    --exp-soft: #f7f8fa;
    --exp-card: #ffffff;
    --exp-accent: #5167d9;
    --exp-accent-soft: #eef0ff;
    --exp-warm: #c56b35;
    --exp-warm-soft: #fff3eb;
    --exp-green: #278069;
    --exp-green-soft: #eaf7f2;
  }
  html[data-theme='dark'] d-article {
    --exp-ink: #edf0f5;
    --exp-body: #c9ced8;
    --exp-muted: #99a1b1;
    --exp-line: #40444d;
    --exp-soft: #24262b;
    --exp-card: #2b2e34;
    --exp-accent: #9ba8ff;
    --exp-accent-soft: #303550;
    --exp-warm: #e7a070;
    --exp-warm-soft: #463326;
    --exp-green: #72c9ae;
    --exp-green-soft: #263e37;
  }
  d-article p,
  d-article li {
    color: var(--exp-body);
  }
  d-article h2 {
    color: var(--exp-ink);
    margin-top: 2.15em;
  }
  d-article .exp-lede {
    border-left: 3px solid var(--exp-accent);
    color: var(--exp-body);
    font-size: 1.06rem;
    line-height: 1.72;
    margin: 0.25rem 0 2rem;
    padding: 0.15rem 0 0.15rem 1rem;
  }
  d-article .exp-lede strong {
    color: var(--exp-ink);
  }
  d-article .exp-pullquote {
    color: var(--exp-ink);
    font-family: Georgia, 'Times New Roman', serif;
    font-size: clamp(1.35rem, 3vw, 1.85rem);
    font-style: italic;
    line-height: 1.42;
    margin: 2.2rem auto;
    max-width: 700px;
    text-align: center;
  }
  d-article .exp-pullquote span {
    color: var(--exp-muted);
    display: block;
    font-family: inherit;
    font-size: 0.62em;
    font-style: normal;
    margin-top: 0.55rem;
  }
  d-article figure.exp-figure {
    margin: 1.6rem 0 2rem;
  }
  d-article figure.exp-figure figcaption {
    color: var(--exp-muted);
    font-size: 0.84rem;
    line-height: 1.45;
    margin-top: 0.7rem;
    text-align: center;
  }
  d-article .exp-pipelines {
    background: var(--exp-soft);
    border: 1px solid var(--exp-line);
    border-radius: 14px;
    padding: 1.1rem;
  }
  d-article .exp-pipeline {
    align-items: center;
    display: grid;
    gap: 0.55rem;
    grid-template-columns: 7.4rem 1fr;
  }
  d-article .exp-pipeline + .exp-pipeline {
    border-top: 1px solid var(--exp-line);
    margin-top: 0.9rem;
    padding-top: 0.9rem;
  }
  d-article .exp-pipeline-label {
    color: var(--exp-muted);
    font-size: 0.73rem;
    font-weight: 750;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }
  d-article .exp-flow {
    align-items: center;
    display: flex;
    flex-wrap: wrap;
    gap: 0.42rem;
  }
  d-article .exp-node {
    background: var(--exp-card);
    border: 1px solid var(--exp-line);
    border-radius: 999px;
    color: var(--exp-ink);
    font-size: 0.82rem;
    font-weight: 650;
    padding: 0.42rem 0.68rem;
    white-space: nowrap;
  }
  d-article .exp-node.human {
    background: var(--exp-warm-soft);
    border-color: color-mix(in srgb, var(--exp-warm) 32%, var(--exp-line));
    color: var(--exp-warm);
  }
  d-article .exp-node.model {
    background: var(--exp-accent-soft);
    border-color: color-mix(in srgb, var(--exp-accent) 32%, var(--exp-line));
    color: var(--exp-accent);
  }
  d-article .exp-node.evidence {
    background: var(--exp-green-soft);
    border-color: color-mix(in srgb, var(--exp-green) 32%, var(--exp-line));
    color: var(--exp-green);
  }
  d-article .exp-arrow {
    color: var(--exp-muted);
    font-size: 0.86rem;
  }
  d-article .exp-transition {
    display: grid;
    gap: 1rem;
    grid-template-columns: 1fr auto 1fr;
  }
  d-article .exp-unit {
    background: var(--exp-card);
    border: 1px solid var(--exp-line);
    border-radius: 14px;
    min-height: 10rem;
    padding: 1.05rem;
  }
  d-article .exp-unit-kicker {
    color: var(--exp-muted);
    font-size: 0.72rem;
    font-weight: 750;
    letter-spacing: 0.08em;
    margin-bottom: 0.75rem;
    text-transform: uppercase;
  }
  d-article .exp-document {
    color: var(--exp-ink);
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 1.02rem;
    line-height: 1.55;
  }
  d-article .exp-document-lines {
    display: grid;
    gap: 0.43rem;
    margin-top: 0.75rem;
  }
  d-article .exp-document-lines i {
    background: var(--exp-line);
    border-radius: 4px;
    display: block;
    height: 0.34rem;
  }
  d-article .exp-document-lines i:nth-child(2) { width: 86%; }
  d-article .exp-document-lines i:nth-child(3) { width: 64%; }
  d-article .exp-shift-arrow {
    align-self: center;
    color: var(--exp-accent);
    font-size: 1.35rem;
  }
  d-article .exp-trajectory {
    display: grid;
    gap: 0.48rem;
  }
  d-article .exp-step {
    align-items: center;
    display: grid;
    gap: 0.6rem;
    grid-template-columns: 4.3rem 1fr;
  }
  d-article .exp-step-label {
    color: var(--exp-muted);
    font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
    font-size: 0.71rem;
  }
  d-article .exp-step-value {
    background: var(--exp-soft);
    border-radius: 6px;
    color: var(--exp-ink);
    font-size: 0.79rem;
    padding: 0.34rem 0.5rem;
  }
  d-article .exp-step:last-child .exp-step-value {
    background: var(--exp-green-soft);
    color: var(--exp-green);
  }
  d-article .exp-equation {
    align-items: center;
    background: var(--exp-soft);
    border: 1px solid var(--exp-line);
    border-radius: 14px;
    display: flex;
    justify-content: center;
    margin: 1.5rem 0;
    overflow-x: auto;
    padding: 1.25rem 1rem;
    text-align: center;
  }
  d-article .exp-equation-inner {
    color: var(--exp-ink);
    font-family: Georgia, 'Times New Roman', serif;
    font-size: clamp(0.95rem, 2.5vw, 1.25rem);
    white-space: nowrap;
  }
  d-article .exp-equation .num {
    border-bottom: 1px solid var(--exp-muted);
    display: block;
    padding: 0 0.5rem 0.32rem;
  }
  d-article .exp-equation .den {
    display: block;
    padding-top: 0.32rem;
  }
  d-article .exp-ladder {
    display: grid;
    gap: 0.6rem;
    grid-template-columns: repeat(4, 1fr);
  }
  d-article .exp-rung {
    background: var(--exp-card);
    border: 1px solid var(--exp-line);
    border-radius: 12px;
    padding: 0.85rem;
  }
  d-article .exp-rung-level {
    color: var(--exp-muted);
    font-size: 0.68rem;
    font-weight: 750;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }
  d-article .exp-rung strong {
    color: var(--exp-ink);
    display: block;
    font-size: 0.9rem;
    margin: 0.32rem 0;
  }
  d-article .exp-rung span:last-child {
    color: var(--exp-muted);
    font-size: 0.76rem;
    line-height: 1.38;
  }
  d-article .exp-loop {
    align-items: center;
    display: flex;
    flex-wrap: wrap;
    gap: 0.42rem;
    justify-content: center;
    margin: 1.55rem 0;
  }
  d-article .exp-loop .exp-node {
    border-radius: 9px;
    padding: 0.6rem 0.8rem;
  }
  d-article .exp-coda {
    background: var(--exp-accent-soft);
    border-radius: 14px;
    color: var(--exp-ink);
    font-size: 1.04rem;
    line-height: 1.7;
    margin-top: 2.2rem;
    padding: 1.2rem 1.3rem;
  }
  d-article .exp-coda strong {
    color: var(--exp-accent);
  }
  @media (max-width: 720px) {
    d-article .exp-pipeline {
      align-items: start;
      grid-template-columns: 1fr;
    }
    d-article .exp-transition {
      grid-template-columns: 1fr;
    }
    d-article .exp-shift-arrow {
      justify-self: center;
      transform: rotate(90deg);
    }
    d-article .exp-ladder {
      grid-template-columns: 1fr 1fr;
    }
  }
  @media (max-width: 430px) {
    d-article .exp-ladder {
      grid-template-columns: 1fr;
    }
  }
---

{::options parse_block_html="true" /}

<div class="exp-lede">
Language models do not learn from the world directly. They learn from traces of interaction with it. Until now, most of those traces have been written by humans—after experience has already been filtered through attention, abstraction, and judgment about what was worth recording.
</div>

Pretraining 因此从来不只是“学习 text”。它在间接学习 human experience，只是中间隔着一条很长的 epistemic path：

$$
\text{World} \rightarrow \text{Human Experience} \rightarrow \text{Attention / Abstraction / Selection} \rightarrow \text{Text} \rightarrow \text{Model}
$$

Agent 带来的变化，不是让 compression 消失，也不是让模型突然直接接触未经中介的 reality。它增加了一条新的路径：模型可以通过行动主动引出 observations，并与 environment 共同产生新的 traces。本文关心的问题是：当训练从压缩 human-written records，扩展到压缩由模型自身行动触发的 consequences，什么发生了变化？

## Text Is Selected Experience

一个真实事件本来有完整的结构：当时是什么 state，做了什么 action，发生了什么 consequence，又得到了怎样的 feedback。但它写进文档时，可能只剩下一句话：

> Don't call this API concurrently.

触发 bug 的上下文、失败的尝试、报错的细节与定位答案的过程，大多消失了。一个 trajectory 被压成一串 tokens。

Text 不只是 compressed experience，还是 **selected experience**。进入训练数据的，是某个人注意到、理解了，并认为值得写下来的那部分 experience。

<div class="exp-pullquote">
Pretraining data is a lossy, selectively recorded projection of experience.
<span>训练数据是经验经过有损压缩与人类筛选后留下的投影。</span>
</div>

这也解释了为什么 next-token prediction 能学到远超语言表面的东西。Text 本身是一个复杂过程的结果：世界影响人的 perception，perception 形成 belief 与 intention，最后才生成 language。要足够好地预测 text，模型就有动力捕捉一部分产生 text 的 latent regularities。

Next-token prediction 是 training interface；它可以学到 compressed predictive representations，但并不自动保证一个完整、忠实的 world model。

## What We Do Not Write Down

Text 的问题不只在于 compression，还在于 selection。

人不会记录自己看到的一切。杯子不会穿过桌面，手松开后东西会掉，袋子装得更多通常会更重——这些事件在生活中极其高频，却因为太 obvious，几乎不值得被写下来。

$$
P(\text{event in life}) \neq P(\text{event in text})
$$

这就是 reporting bias <d-cite key="gordon2013reporting"></d-cite>。Forbes 与 Choi 用一个极简例子抓住了它：人们几乎不会特意写下 “my house is bigger than me”；但 “Tyler entered his house” 又在间接泄露同一份 physical knowledge <d-cite key="forbes2017verb"></d-cite>。Text 并非没有 common sense，而是把它藏在 implication 里，并以高度偏斜的频率出现。

Yejin Choi 把 commonsense intelligence 描述为：依赖关于 physical 与 social world 的丰富背景知识，对 everyday situations 做 intuitive reasoning <d-cite key="choi2022curious"></d-cite>。这也提醒我们，common sense 不只是一组静态 facts；它还包括对 object affordance、人的意图，以及 context 改变后哪些 inference 应当失效的把握。

规模化 pretraining 能补回其中一部分，但并不会自动消除 selection bias。Shwartz 与 Choi 发现，语言模型可以更好地估计一些“高频发生、很少明说”的 action、outcome 与 property；与此同时，它们也会高估极罕见事件的 plausibility，放大 corpus 中已有的偏差 <d-cite key="shwartz2020reporting"></d-cite>。

这也提供了理解 <em>Car Wash Test</em> 的一个 lens。问题是：“我想洗车。洗车店离我只有 100 米，我应该走路还是开车？”有些模型选择 walk：距离近，步行更快、更环保。局部推理都像是对的，却漏掉了 task constraint——要洗的是车，车必须到场。这个 failure 并非所有模型、所有措辞下都会出现，但它暴露了 language plausibility 与 grounded task understanding 之间仍然存在的缝隙。

人类的 common sense 也许不是一座由命题组成的百科全书。它更像从无数次日常互动中压缩出来的 consequence model：

$$
f(\text{state},\ \text{action}) \rightarrow \text{likely consequence}
$$

因此，至少对 physical 与 practical common sense，可以抓住这样一个核心：**Common sense is often the low-frequency-in-language, high-frequency-in-life part of the world model.**

## Agents Generate Their Own Traces

从 interaction 中学习并不是新事物；reinforcement learning 与 robotics 早已建立在 agent–environment loop 上 <d-cite key="sutton2018reinforcement"></d-cite>。新的地方在于，foundation-model agents 正把这条路径扩展到 code、browser 与各种通用数字环境，并持续产生大规模 traces。

一个 coding agent 不只是读到“这段代码会失败”。它编辑文件，调用 compiler，看见 error，修改假设，再运行 test。Browser agent 点击页面，遇到 modal 或 permission error，然后寻找另一条路径。它们得到的不再只是人类对 experience 的总结，而是更接近 action–consequence structure 的 experience trace。

我们可以把一个最小 experience 写成：

$$
E_t = (s_t, a_t, o_{t+1}, f_t)
$$

其中包含当前 state、采取的 action、下一步 observation，以及 success、failure 或其他 feedback。

<figure class="exp-figure" markdown="0">
  <div class="exp-transition">
    <div class="exp-unit">
      <div class="exp-unit-kicker">Old unit · Document</div>
      <div class="exp-document">“Do not call this API concurrently.”</div>
      <div class="exp-document-lines" aria-hidden="true"><i></i><i></i><i></i></div>
    </div>
    <div class="exp-shift-arrow">→</div>
    <div class="exp-unit">
      <div class="exp-unit-kicker">New unit · Experience</div>
      <div class="exp-trajectory">
        <div class="exp-step"><span class="exp-step-label">STATE</span><span class="exp-step-value">shared client</span></div>
        <div class="exp-step"><span class="exp-step-label">ACTION</span><span class="exp-step-value">parallel calls</span></div>
        <div class="exp-step"><span class="exp-step-label">OBSERVE</span><span class="exp-step-value">race condition</span></div>
        <div class="exp-step"><span class="exp-step-label">FEEDBACK</span><span class="exp-step-value">test failed</span></div>
      </div>
    </div>
  </div>
  <figcaption>数据的基本单位，从静态 document 扩展到带有 action–consequence structure 与反馈的 transition。</figcaption>
</figure>

关键差别不在于 text versus non-text——terminal output 仍然是 text。区别在于 causal provenance：human-written text 是他人过去留下的记录；agent trace 中的 observation，则是 environment 对模型刚刚采取的 action 所作的回应。

<figure class="exp-figure" markdown="0">
  <div class="exp-pipelines">
    <div class="exp-pipeline">
      <div class="exp-pipeline-label">Recorded experience</div>
      <div class="exp-flow">
        <span class="exp-node evidence">World</span><span class="exp-arrow">→</span>
        <span class="exp-node human">Human experience</span><span class="exp-arrow">→</span>
        <span class="exp-node human">Text</span><span class="exp-arrow">→</span>
        <span class="exp-node model">Model</span>
      </div>
    </div>
    <div class="exp-pipeline">
      <div class="exp-pipeline-label">Generated experience</div>
      <div class="exp-flow">
        <span class="exp-node model">Model</span><span class="exp-arrow">→</span>
        <span class="exp-node model">Action</span><span class="exp-arrow">→</span>
        <span class="exp-node evidence">Environment</span><span class="exp-arrow">→</span>
        <span class="exp-node evidence">Observation</span><span class="exp-arrow">↺</span>
      </div>
    </div>
  </div>
  <figcaption>Agent 没有取代 recorded experience；它增加了一条通过自身 action 主动引出 environment observation 的路径。</figcaption>
</figure>

## Tools Mediate Experience

Agent 通常不会直接作用于 environment。Tool 把模型的 intention 变成 environment 可以执行的 action，再把 consequence 变成模型可以读取的 observation：

$$
\text{Model} \rightarrow \text{Tool} \rightarrow \text{Environment} \rightarrow \text{Tool Output} \rightarrow \text{Model}
$$

Terminal 把 command 交给 operating system，并返回 stdout、errors、files 与 traces；browser 把 clicks 或 code 变成 web state transitions；scientific instruments 把不可直接读取的 physical state 转换成 images、counts 或 measurements。**Tools define an agent's action space and observation space.**

Recent work 也开始直接利用这条 observation stream。ECHO 让 terminal agent 预测自身 commands 所引起的 environment outputs，结果显示这些 outputs 不只是下一步 action 的 transient context，也可以作为 dense supervision，帮助模型学习 terminal dynamics <d-cite key="shrivastava2026echo"></d-cite>。

在 science 中，tool-mediated observations 有不同的 epistemic provenance。Database 与 search tool 返回已经记录的 evidence；compiler 与 theorem prover 返回 formal consequence；AlphaFold 这样的 specialized model 把 structural data 与规律压缩成 predicted structure 与 confidence <d-cite key="jumper2021alphafold"></d-cite>；simulator 返回近似世界中的 trajectory；experiment 则通过 instrument 返回新的 measurement。

<figure class="exp-figure" markdown="0">
  <div class="exp-ladder">
    <div class="exp-rung"><span class="exp-rung-level">Retrieved</span><strong>Database / Search</strong><span>过去记录的 evidence</span></div>
    <div class="exp-rung"><span class="exp-rung-level">Computed</span><strong>Compiler / Prover</strong><span>formal system 的 consequence</span></div>
    <div class="exp-rung"><span class="exp-rung-level">Predicted</span><strong>AlphaFold / Simulator</strong><span>specialized model 中的 world</span></div>
    <div class="exp-rung"><span class="exp-rung-level">Measured</span><strong>Real Experiment</strong><span>physical world 返回的 evidence</span></div>
  </div>
  <figcaption>这不是简单的质量排序，而是不同的 epistemic relations。Tool output 是 observation，不自动等于 truth；模型还需要理解它来自 retrieval、formal rules、prediction、simulation，还是 measurement。</figcaption>
</figure>

<div class="exp-pullquote">
Every tool exposes an environment, but only through a particular representation of it.
<span>Tool 不是 world 本身，而是让某个 task-relevant projection of the world 变得可交互。</span>
</div>

Tool 因而既可能扩展模型的 inference-time capability，也可能成为 experience 的来源。但 agent 学到的是 environment as represented by the tool，其中同时包含 tool 捕捉到的规律与它施加的 assumptions。模型需要知道的不只是 output 是什么，还包括这个 tool 有资格支持什么样的 claim。

## The Corpus Becomes a Process

传统 pretraining 从一个相对固定的 archive 开始：先收集 human-written corpus，再训练 model。Agent interaction 则把 corpus 变成一个可以持续运行的 process：

<div class="exp-loop" aria-label="A continuously generated interaction corpus" markdown="0">
  <span class="exp-node model">Model</span><span class="exp-arrow">→</span>
  <span class="exp-node model">Interaction</span><span class="exp-arrow">→</span>
  <span class="exp-node evidence">New Trace</span><span class="exp-arrow">→</span>
  <span class="exp-node human">Training</span><span class="exp-arrow">→</span>
  <span class="exp-node model">Updated Model</span><span class="exp-arrow">↺</span>
</div>

这也说明为什么 synthetic data 这个词过于粗糙。模型生成一段文字再训练自己，可能只是在已有 distribution 内循环；agent self-play 或 tool use 则可以产生另一种 data：**actions 由 model 生成，consequences 由 environment 返回。**

<div class="exp-pullquote">
The actions may be synthetic; the consequences need not be.
<span>Self-play 产生 actions 与 questions；environment 提供 constraints 与 consequences。</span>
</div>

从规模看，这已经不只是一个理论上的 data source。Google 在 2026 年报告其产品与 APIs 每月处理约 3.2 quadrillion tokens；作为数量级参照，Llama 3.1 的公开 pretraining 规模约为 15 trillion tokens <d-cite key="google2026tokens,meta2024llama31"></d-cite>。这个比较并非 apples-to-apples：processed tokens 包含重复 inputs 与 context，大量 interaction 也受隐私、授权和质量限制，不能直接变成 training data。但它说明，interaction throughput 已经可以迅速超过一个固定 corpus 的规模。

这些 data 不是 infinite，而是 **renewable**。只要继续投入 inference compute、运行 environments 与 verifiers，系统就能产生下一轮 traces。Data generation 本身开始成为 inference workload：compute 不再只是在 training 时消费 data，也可以在 interaction 时生产未来的 data。

新的边界因此不是“还有多少 text 没有抓取”。在 digital environments 中，experience generation 受到 GPU、CPU、energy、storage 与 execution throughput 的限制；在 physical science 中，它仍受到 experiment latency、instrument capacity、sample availability 与 biological timescale 的限制。

**In digital environments, experience becomes compute-bound. In physical science, it remains reality-bound.**

## From Experience to Knowledge Production

最后仍需要一个重要的 distinction：**Agent 产生 trace，不等于 model 已经从 trace 中 learning。**只有当 experience 系统性地改变了模型未来的 prediction 或 action，learning loop 才真正闭合。至于这种变化最终存在 weights、memory、skills 还是其他 persistent component 中，是 implementation question，而不是这里最重要的 conceptual boundary。

可以把这条演化理解为三个彼此重叠的层次，而不是严格替代的历史阶段：

1. **Human experience**：人类与世界互动，从中形成经验。
2. **Recorded experience**：人类把认为值得记录的部分压缩成 text，模型再压缩这些 traces。
3. **Generated experience**：模型通过 tools 行动，environment 返回 observations；这些 action-conditioned traces 又成为未来 learning 的原料。

Pretraining 让模型压缩 what humans found worth writing down。Agentic learning 则可能让 training corpus 从固定 archive 变成 renewable process：model 产生 actions，environment 产生 consequences，interaction 本身开始产生新的 experience。

<div class="exp-coda">
The deeper shift is from passively compressing human-written records to actively producing and compressing tool-mediated experience. <strong>AI training 开始从学习人类积累的知识，扩展到参与知识产生的过程本身。</strong>
</div>
