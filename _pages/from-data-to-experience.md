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
  d-article .exp-rung:last-child {
    background: var(--exp-green-soft);
    border-color: color-mix(in srgb, var(--exp-green) 35%, var(--exp-line));
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
早期语言模型偶尔会给出一种听起来完全合理、但又明显不对的建议：<strong>“你可以走路去洗车。”</strong>每个词都对，句法也对；可如果目的是洗车，你得把车带过去。这个小错误暴露了一个更大的问题：模型读过大量关于世界的文字，却没有经历过世界本身。
</div>

这不是说 pretraining 与 experience 无关。恰恰相反，传统 pretraining 一直在学习 experience——只是这些 experience 已经先经过了人类的注意、理解、筛选与表达。

$$
\text{World} \rightarrow \text{Human Experience} \rightarrow \text{Abstraction} \rightarrow \text{Text} \rightarrow \text{Model}
$$

Agent 带来的变化，不只是更多数据，而是一条新的 epistemic path：

$$
\text{Model} \rightarrow \text{Action} \rightarrow \text{Consequence} \rightarrow \text{Experience} \rightarrow \text{Model}
$$

**真正改变的是 what gets compressed。**

## Text Is Compressed Experience

互联网不是世界的随机样本。它是人类认为“值得说”的那部分世界。

一个真实事件本来有完整的结构：当时是什么 state，做了什么 action，发生了什么 consequence，又得到了怎样的 feedback。但写进文档时，它往往只剩下一句话：

> Don't call this API concurrently.

触发 bug 的上下文、失败的尝试、报错的细节、定位答案的过程，都消失了。一个 trajectory 被压成了一串 tokens。

所以，更准确的说法不是“text 是 experience 的简化版”，而是：

<div class="exp-pullquote">
Pretraining data is a lossy, flattened projection of experience.
<span>训练数据是真实经验经过有损压缩后留下的平面投影。</span>
</div>

这也解释了为什么 next-token prediction 能学到远超语言表面的东西。Text 本身是一个复杂过程的结果：世界影响人的 perception，perception 形成 belief 与 intention，最后才生成 language。要足够好地预测 text，模型就不得不反向捕捉一部分产生 text 的 latent structure。

Next-token prediction 是 training interface；它学到的，可能是一个 compressed predictive model。

<figure class="exp-figure">
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
      <div class="exp-pipeline-label">Model experience</div>
      <div class="exp-flow">
        <span class="exp-node model">Model</span><span class="exp-arrow">→</span>
        <span class="exp-node model">Action</span><span class="exp-arrow">→</span>
        <span class="exp-node evidence">Environment</span><span class="exp-arrow">→</span>
        <span class="exp-node evidence">Consequence</span><span class="exp-arrow">↺</span>
      </div>
    </div>
  </div>
  <figcaption>Agent 没有取代 recorded experience；它增加了一条从行动后果获得信息的路径。</figcaption>
</figure>

## The Missing Obvious

Text 的问题不只在于 compression，还在于 selection。

人不会记录自己看到的一切。杯子不会穿过桌面，手松开后东西会掉，袋子装得更多通常会更重——这些事件在生活中极其高频，却因为太 obvious，几乎不值得被写下来。

$$
P(\text{event in life}) \neq P(\text{event in text})
$$

这就是 reporting bias。它让互联网擅长保存罕见、抽象、值得讨论的知识，却系统性地漏掉 mundane reality。

人类的 common sense 也许并不是一座由命题组成的百科全书。它更像从无数次日常互动中压缩出来的 consequence model：

$$
f(\text{state},\ \text{action}) \rightarrow \text{likely consequence}
$$

于是可以得到一个简洁的定义：**Common sense is the low-frequency-in-language, high-frequency-in-life part of the world model.**

## The New Unit of Learning

Agent 让模型第一次可以大规模接触 human compression 之前的数据。

一个 coding agent 不只是读到“这段代码会失败”。它编辑文件，调用 compiler，看见 error，修改假设，再运行 test。Browser agent 点击页面，遇到 modal 或 permission error，然后寻找另一条路径。它们得到的不是关于 experience 的描述，而是 experience trajectory 本身。

我们可以把一个最小 experience 写成：

$$
E_t = (s_t, a_t, o_{t+1}, f_t)
$$

其中包含当前 state、采取的 action、下一步 observation，以及 success、failure 或其他 feedback。

<figure class="exp-figure">
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
  <figcaption>学习的基本单位，从静态 document 走向带有因果结构与反馈的 transition。</figcaption>
</figure>

这里需要区分三个概念：

- **Experience** 是发生过什么。
- **Knowledge** 是从许多 experience 中压缩出的、可复用的规律。
- **Intelligence** 是把 experience 变成 knowledge，再用 knowledge 指导下一次行动的能力。

三者连起来，才构成 learning loop：

<div class="exp-loop" aria-label="Experience, knowledge, and action learning loop">
  <span class="exp-node evidence">Experience</span><span class="exp-arrow">→</span>
  <span class="exp-node model">Compression</span><span class="exp-arrow">→</span>
  <span class="exp-node model">Knowledge</span><span class="exp-arrow">→</span>
  <span class="exp-node human">Action</span><span class="exp-arrow">→</span>
  <span class="exp-node evidence">New experience</span><span class="exp-arrow">↺</span>
</div>

## Abundance Is Not Knowledge

Agent 可以生成近乎无限的 trajectories，但这不等于可以生成无限的 knowledge。

如果模型已经把同一类任务做过一百万次，第一百万零一次成功不会提供多少新信息。最有价值的时刻通常是：模型预测会发生 $X$，世界却返回了 $Y$。这个 discrepancy 才是 surprise，也是真正减少 uncertainty 的地方。

因此，未来训练数据的价值不应只按 token 数量计算。一个更有用的直觉是：

<div class="exp-equation" aria-label="Experience value equation">
  <div class="exp-equation-inner">
    <span class="num">Novelty × Reliability × Generalizability</span>
    <span class="den">Compute Cost</span>
  </div>
</div>

这意味着 data wall 没有消失，只是换了形态：从寻找更多高质量文本，变成在海量 interaction 中寻找少数 grounded、可信、能迁移的 surprise。

**Data scarcity becomes information scarcity.** 我们或许不会耗尽 tokens，但会耗尽廉价而可信的新发现。

## Tools as Teachers

这也让 synthetic data 这个词显得过于粗糙。

模型生成一段文字再拿来训练，仍然可能只是在自己的 distribution 内循环。真正重要的区别，不是 synthetic versus real，而是 **closed loop versus grounded loop**：系统外部有没有一个 source of truth，能告诉模型“你刚才错了”。

<figure class="exp-figure">
  <div class="exp-ladder">
    <div class="exp-rung"><span class="exp-rung-level">Closed</span><strong>Model → Text</strong><span>重新组合已有 distribution</span></div>
    <div class="exp-rung"><span class="exp-rung-level">Verified</span><strong>Compiler / Solver</strong><span>得到可检查的反馈</span></div>
    <div class="exp-rung"><span class="exp-rung-level">Simulated</span><strong>Simulator</strong><span>观察 intervention 的后果</span></div>
    <div class="exp-rung"><span class="exp-rung-level">Grounded</span><strong>Real experiment</strong><span>由 measurement 更新模型</span></div>
  </div>
  <figcaption>越往右，经验越可能引入模型自身无法凭空生成的新信息。</figcaption>
</figure>

在这个框架下，compiler、theorem prover、simulator 和 scientific model 都有两种身份：它们既是 inference-time extension，也是 training-time teacher。

模型可以在不会时调用工具；也可以通过大量带验证的 interaction，把工具暴露出来的一部分规律重新 distilled into weights。由此形成一个 flywheel：

$$
\text{Model} \rightarrow \text{Tools} \rightarrow \text{Evidence} \rightarrow \text{Training} \rightarrow \text{Better Model}
$$

但这并不意味着所有工具最终都要被塞回 model weights。更自然的分工也许是：weights 保存缓慢变化的 compressed knowledge，memory 保存 episodic experience，tools 充当 specialized cognitive organs，而 environment 持续提供 evidence。

模型真正需要学会的是：什么时候回答，什么时候行动，什么时候调用工具，以及面对冲突的 evidence 时应该相信什么。

## From Observation to Intervention

Text 大多保存 observational knowledge：模型看到 $X$ 与 $Y$ 一起出现。Agent 则可以做出 intervention：执行 $do(X)$，再观察 $Y$ 是否发生。

这一步对 causal knowledge 尤其重要。进入 science 后，learning loop 会变成：

$$
\text{Hypothesis} \rightarrow \text{Experiment} \rightarrow \text{Measurement} \rightarrow \text{Updated Model}
$$

此时，prediction 不再只是“下一个 token 是什么”，而是一个更一般的问题：

<div class="exp-pullquote">
Given what I know, if I do X, what will happen?
<span>在我已知的一切之上，如果采取这个行动，世界将如何变化？</span>
</div>

Common sense、agent planning、program execution、biology 与 scientific discovery，都可以被放进这个 consequence-prediction 的框架。模型从预测下一段描述，走向预测 action-conditioned next state。

## A New Epistemic Loop

Foundation model 的历史可以粗略分成三个阶段：

1. **Human experience**：人类与世界互动，从中形成经验。
2. **Recorded experience**：人类把经验压缩成文本，模型再压缩这些记录。Internet 像 humanity's giant offline replay buffer。
3. **Model experience**：模型开始行动、观察、验证，并写入自己的 replay buffer。

Pretraining 让 AI 学会压缩 humanity's records of the world。Agentic learning 则开始让它压缩 what the world—and its tools—reveal through interaction。

<div class="exp-coda">
这场 shift 最深的含义，不是“我们突然有了更多 training data”。而是 <strong>AI training 正在从学习人类积累的知识，走向参与知识产生的过程本身。</strong>
</div>
