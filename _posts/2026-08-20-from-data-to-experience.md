---
layout: distill
title: "From Data to Experience"
description: "Agentic learning shifts AI from fixed corpora toward learning loops built around tool-mediated experience."
date: 2026-08-20
tags: ['AI', 'agents', 'learning']
categories: blog
permalink: /blog/preview/from-data-to-experience/
preview: true
sitemap: false
bibliography: 2026-08-20-from-data-to-experience.bib
bilingual: true

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
    background: var(--exp-soft);
    border-left: 3px solid var(--exp-line);
    color: var(--exp-ink);
    font-family: inherit;
    font-size: 1rem;
    font-style: normal;
    font-weight: 600;
    line-height: 1.55;
    margin: 1.5rem 0;
    padding: 0.85rem 1rem;
    text-align: left;
  }
  d-article .exp-pullquote span {
    color: var(--exp-muted);
    display: block;
    font-family: inherit;
    font-size: 0.82rem;
    font-weight: 400;
    font-style: normal;
    line-height: 1.45;
    margin-top: 0.3rem;
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
  d-article .exp-flow {
    align-items: center;
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin: 1.2rem 0 1.45rem;
  }
  d-article .exp-flow-link {
    align-items: center;
    display: inline-flex;
    gap: 0.45rem;
  }
  d-article .exp-flow-step {
    background: var(--exp-card);
    border: 1px solid var(--exp-line);
    border-radius: 8px;
    color: var(--exp-ink);
    font-size: 0.82rem;
    font-weight: 600;
    line-height: 1.3;
    padding: 0.42rem 0.58rem;
    white-space: nowrap;
  }
  d-article .exp-flow-arrow {
    color: var(--exp-muted);
    flex: none;
    font-size: 0.84rem;
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
  d-article .exp-ladder {
    display: grid;
    gap: 0.6rem;
    grid-template-columns: repeat(auto-fit, minmax(8.5rem, 1fr));
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

<div class="lang-en">

<div class="exp-lede">
Language models began by compressing traces of human experience. Agents add a second channel: models can act through tools and receive consequences from environments. Once those consequences are retained, selected, and used for learning, the central object is no longer a fixed dataset but a feedback process—predict, decide, act, observe, and learn again.
</div>

Pretraining has never been only about learning text. It learns indirectly from human experience along a longer epistemic path:

<div class="exp-flow" aria-label="World to model epistemic path" markdown="0">
  <span class="exp-flow-step">World</span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Human Experience</span></span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">What Gets Recorded</span></span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Text</span></span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Model</span></span>
</div>

Human-written text is already evidence about the world, but evidence after compression and selection. Agents do not remove this mediation or gain unfiltered access to reality. They create another route by which observations can enter the learning system—and can begin to influence which observations are produced next.

The deeper shift is therefore not simply from human data to synthetic data, or even from documents to trajectories. It is from a one-way pipeline over a fixed dataset toward a learning system organized around experience.

## Text Is Selected Experience

Text is not raw experience. It is the part of experience that people chose to put into words. Before experience enters a corpus, someone has already decided what was worth recording—and left the rest out.

What survives is not a representative sample of life. Surprising events, useful conclusions, and unusual failures are more likely to be recorded than routine regularities. The corpus is shaped as much by human selection as by the world it describes.

<div class="exp-pullquote">
The training corpus is not a sample of life.
<span>It is a sample of what people found worth recording.</span>
</div>

This does not mean language contains no world structure. Text is the output of a latent process: the world affects perception; perception shapes beliefs and intentions; beliefs and intentions produce language. Predicting language well creates pressure to reverse-engineer some of the regularities that produced it.

Next-token prediction can therefore learn facts, object properties, affordances, human behavior, norms, code, action consequences, and even goal-directed behavioral regularities. **Next-token prediction is the training interface; predictive compression is the deeper operation.** But predictive compression does not guarantee a complete or faithful world model.

## What We Do Not Write Down

People do not record everything they observe. Cups do not pass through tables, yet almost nobody writes this down because it is too obvious.

$$
P_{\mathrm{life}}(e) \neq P_{\mathrm{text}}(e)
$$

This is reporting bias <d-cite key="gordon2013reporting"></d-cite>. Forbes and Choi illustrate it with a simple contrast: people almost never bother to write “my house is bigger than me,” even though a sentence such as “Tyler entered his house” indirectly reveals the same physical knowledge <d-cite key="forbes2017verb"></d-cite>. Commonsense knowledge is not absent from text; it is hidden in implication and represented at highly distorted frequencies.

The <em>Car Wash Test</em> makes the consequence concrete. Asked, “I want to wash my car. The car wash is only 100 meters away. Should I walk or drive?”, a model may choose walking because `short distance → walk` is a powerful default. The model may already know that washing a car requires bringing the car; the failure is that the familiar association wins before the goal is fully applied.

For physical and practical reasoning, a useful shorthand is that common sense often consists of **low-frequency-in-language, high-frequency-in-life structure**. Scaling can recover some of it from implication, but it does not make the frequencies in text match the frequencies in experience.

## Is Language Enough?

The wrong conclusion would be that language is detached from reality and therefore cannot support a world model. A recorded claim can transmit genuine knowledge without requiring every learner to repeat the underlying experience. A model does not need to freeze a glass of water to learn that water freezes near 0°C under ordinary pressure.

Language can also reveal more than it states explicitly. To predict what people say, a model can infer latent facts about objects, intentions, social behavior, and action consequences. Text is lossy, but it is not epistemically empty.

At the same time, perception and interaction provide a differently structured learning channel. Animals and infants acquire rich physical expectations with far less symbolic language than a foundation model sees. That observation does not prove that language models cannot learn world structure. It shows that repeated consequences can make certain regularities direct, dense, and difficult to omit.

The sharper limit appears when a consequence does not yet exist in the record. Language can encode previously observed regularities, but it cannot already contain the consequence of every action in every future state. A model can predict what will happen; interaction lets it act and observe what actually follows.

<div class="exp-pullquote">
The important step may not be from language to sensors, but from records to consequences.
<span>Interaction gives prediction something outside the model to answer to.</span>
</div>

Grounding therefore need not mean a humanoid body. The more general requirement is access to environments that return consequences independently of what the model itself chooses to generate. A compiler, browser, game, or simulator can all provide such a boundary—although each exposes a different part of the world.

## Agents Generate Their Own Traces

Learning from interaction is not new; reinforcement learning and robotics have long been organized around the agent–environment loop <d-cite key="sutton2018reinforcement"></d-cite>. What is changing is that foundation-model agents extend this interface into code, browsers, and other general digital environments, producing large volumes of structured traces as they work.

“Synthetic data” is too coarse a category for these traces. Compare model-generated text,

`Model → Text`

with agent interaction:

`Model → Action → Environment → Observation`

Both may eventually become tokens, but their epistemic provenance differs. The first primarily samples from the model's existing distribution. The second can contain information returned by an environment.

In this essay, an **experience** is not raw reality. It is a structured trace of interaction:

$$
E_t = (s_t, a_t, o_{t+1}, f_{t+1})
$$

It links a state, an action, the next observation, and the feedback returned by that transition. The trace remains a partial representation of the world, determined by what the environment and its interface make observable.

Predictive learning can estimate what usually follows an action:

$$
P(o_{t+1} \mid s_t, a_t)
$$

Interaction instead executes the action and obtains what actually happened this time. A coding agent edits a file, invokes a compiler, observes an error, revises a hypothesis, and runs a test. **Prediction extrapolates from previous experience; interaction solicits new evidence.** The model does not merely predict the world. It can ask the world.

<div class="exp-pullquote">
The actions may be synthetic; the consequences need not be.
<span>The important question is not who produced the tokens, but where the evidence came from.</span>
</div>

## Tools Mediate Experience

Agents rarely act on environments directly. A tool converts a model's intention into an action the environment can execute, then converts the consequence into an observation the model can read:

<div class="exp-flow" aria-label="Tool-mediated agent interaction" markdown="0">
  <span class="exp-flow-step">Model</span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Tool</span></span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Environment</span></span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Tool Output</span></span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Model</span></span>
</div>

A terminal passes commands to an operating system and returns stdout, errors, files, and traces. A browser turns clicks or code into web-state transitions. Scientific instruments transform otherwise inaccessible physical states into images, counts, and measurements. **Tools define an agent's action space and observation space.**

Recent work has begun to use this observation stream directly. ECHO trains terminal agents to predict the environment outputs caused by their own commands, showing that these outputs can be more than transient context for the next action: they can provide dense supervision for learning terminal dynamics <d-cite key="shrivastava2026echo"></d-cite>.

In science, tool-mediated observations have different epistemic provenance. Databases and search tools return recorded evidence. Compilers and theorem provers return consequences within formal systems. Specialized models such as AlphaFold compress structural data and regularities into predicted structures and confidence estimates <d-cite key="jumper2021alphafold"></d-cite>. Simulators return trajectories inside approximate worlds. Experiments use instruments to return new measurements from the physical world.

<figure class="exp-figure" markdown="0">
  <div class="exp-ladder">
    <div class="exp-rung"><span class="exp-rung-level">Retrieved</span><strong>Database / Search</strong><span>Previously recorded evidence</span></div>
    <div class="exp-rung"><span class="exp-rung-level">Computed</span><strong>Compiler / Prover</strong><span>Consequences of formal rules</span></div>
    <div class="exp-rung"><span class="exp-rung-level">Predicted</span><strong>AlphaFold</strong><span>A specialized model's estimate</span></div>
    <div class="exp-rung"><span class="exp-rung-level">Simulated</span><strong>Simulator</strong><span>A trajectory in an approximate world</span></div>
    <div class="exp-rung"><span class="exp-rung-level">Measured</span><strong>Experiment</strong><span>Evidence returned by the physical world</span></div>
  </div>
  <figcaption>This is not a simple ranking of quality, but a set of different epistemic relations. A tool output is an observation, not automatically truth. Its meaning depends on whether it came from retrieval, formal rules, prediction, simulation, or measurement.</figcaption>
</figure>

This also separates token novelty from epistemic novelty. A search result may be new to the model's current context while reporting old evidence; an experiment can produce an observation that did not previously exist in the record.

<div class="exp-pullquote">
Grounding does not necessarily require embodiment; it requires consequences outside the model.
<span>Every tool exposes an environment, but only through a particular representation of it.</span>
</div>

A tool can extend inference-time capability and become a source of experience. But an agent learns the environment as represented by the tool, including both the regularities it captures and the assumptions it imposes. The model must learn not only what an output says, but **what kind of claim that tool is entitled to support**.

## The Corpus Becomes a Process

Traditional pretraining begins with a relatively fixed archive: collect, freeze, then train. Agent interaction can turn corpus production into a continuing process.

These traces are not automatically useful. Most deployed models do not update their weights after each interaction. Experience must be retained with appropriate permission, filtered, verified, and used in context, memory, or optimization before it can change future predictions or actions.

**Interaction creates new observations, not automatically new knowledge.** Many observations merely confirm known regularities, expose implementation details, or add noise. Their epistemic value depends on how they are interpreted, checked, and incorporated.

<div class="exp-pullquote">
The dataset is no longer merely an input to the learning system. It becomes one of its outputs.
<span>The current model can help determine what experience a future model will see.</span>
</div>

Previously, the dataset was largely an external input to training:

$$
D \rightarrow M
$$

Increasingly, the capabilities, failures, and actions of the current model can influence the distribution generated for the next one:

$$
M_t \rightarrow D_{t+1} \rightarrow M_{t+1}
$$

The key transition is that once the current model helps determine which data are generated next, data production is no longer exogenous to training. The training distribution becomes partly **endogenous to the learning system itself**.

This makes experience shaping a central learning function. A system can search for failures, generate tasks, construct adversarial cases, use self-play, choose difficult examples, or create targeted environments. The objective is no longer simply to collect “good data,” because **high data quality is not the same as high learning value**.

A million excellent examples of a mastered task may add little; one reliable trajectory that exposes a blind spot may add much more. Once data can be generated, curriculum becomes the real data problem: **what is the best next experience for this model now?** The answer depends on capability, uncertainty, failure modes, verifier availability, and cost.

The supply is renewable, not infinite. Digital experience is constrained by compute, energy, storage, execution throughput, and reliable verification. Physical experience remains constrained by experiment latency, instrument capacity, samples, and biological time.

## The Training Pipeline Becomes a Loop

Pretraining, midtraining, posttraining, and deployment remain useful engineering labels. They describe checkpoint lifecycles, optimization regimes, objective changes, and dataset mixtures. But they tell us **when** something happens more clearly than **what** function it performs. In an adaptive learning system, the same trace can move across stages and model generations.

Four functions are more persistent:

- **Predictive or world learning** compresses regularities in experience into reusable representations. It asks: *what structure is predictable here?*
- **Policy learning** turns knowledge, goals, and constraints into behavior. It asks: *given what I know and want, what should I do?*
- **Interaction** executes actions and obtains realized consequences. It asks: *what did the environment actually return?*
- **Experience shaping** selects or generates what the model should encounter next. It asks: *what has the highest learning value now?*

Pretraining can perform predictive compression over documents or trajectories. A sequence such as `STATE → ACTION → OBSERVATION → ACTION → OBSERVATION` can still be trained with a next-token objective. Agentic data need not replace next-token prediction; it changes what next-token prediction is performed over.

World learning and policy learning are also distinct. A predictive model describes possible consequences:

`walk → person arrives, car stays home`<br>
`drive → person and car arrive`

A policy, $\pi(a \mid s, g, c)$, makes a goal-conditioned choice among them. The earlier <em>Car Wash Test</em> can now be read more precisely: it need not indicate missing world knowledge. It fails when the behavioral prior “short distance → walk” substitutes for the policy the goal requires. **Knowing what people usually do is not the same as knowing what this goal requires.** Posttraining is therefore not simply more pretraining: one of its central functions is to turn knowledge, goals, and constraints into policy.

Experience shaping is equally fundamental, but need not belong to a stage called midtraining. It may occur during pretraining, after posttraining, in deployment, between generations, or continuously. Midtraining as a stage is contingent; experience shaping as a function is fundamental.

The mapping is not exact. Pretraining learns behavioral priors; posttraining can add knowledge; interaction can be used for evaluation without any update. The point is not to rename the stages, but to replace a linear ontology with functions that recur inside a loop.

Consider a coding-agent rollout:

> state → edit → compiler error → revised hypothesis → fix → tests pass

For the current model, this may be a deployment trajectory. Once retained and verified, the same trace can become part of the training corpus for a future model—including, potentially, its predictive pretraining mixture.

<div class="exp-pullquote">
What is deployment for <em>M</em><sub>t</sub> can become training data for <em>M</em><sub>t+1</sub>.
<span>Stages belong to a training run; experience can move across stages and generations.</span>
</div>

<div class="exp-loop" aria-label="An experience-centered learning loop" markdown="0">
  <span class="exp-node evidence">Experience</span><span class="exp-arrow">→</span>
  <span class="exp-node model">Predictive Learning</span><span class="exp-arrow">→</span>
  <span class="exp-node model">Policy</span><span class="exp-arrow">→</span>
  <span class="exp-node model">Action</span><span class="exp-arrow">→</span>
  <span class="exp-node evidence">Consequence</span><span class="exp-arrow">→</span>
  <span class="exp-node evidence">New Experience</span><span class="exp-arrow">↺</span>
</div>

## From Experience to Knowledge Production

An agent producing a trace does not mean that a model has learned from it. The loop closes only when experience changes a persistent component that affects future prediction or action—weights, memory, skills, or something else.

For scientific intelligence, this distinction becomes decisive. A model can learn from every recorded discovery and still face questions whose answers do not exist in the corpus. A scientific system must eventually move beyond recorded answers and participate in generating evidence:

<div class="exp-flow" aria-label="Scientific knowledge production loop" markdown="0">
  <span class="exp-flow-step">Corpus</span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Hypothesis</span></span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Intervention</span></span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Measurement</span></span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Updated Knowledge</span></span>
</div>

A scientific agent becomes interesting when it can move from predicting an answer to causing the world to reveal an answer. That requires more than generating a hypothesis: it requires choosing an intervention, interpreting evidence, updating beliefs, and deciding what to test next.

Models began by learning from records of knowledge production. Agents can increasingly participate in the process that produces evidence—and, through experience shaping, influence which evidence is sought next.

<div class="exp-coda">
AI learning is moving from a one-way pipeline over a fixed dataset toward a feedback process in which models predict, form policies, act through tools, observe consequences, and increasingly shape what they will learn from next. For scientific intelligence, this matters most when interaction produces evidence that did not previously exist in the corpus. <strong>From dataset to experience, and from pipeline to loop.</strong>
</div>

</div>

<div class="lang-zh">

<div class="exp-lede">
语言模型最初通过压缩人类经验留下的 traces 来学习。Agent 增加了第二条通道：模型可以通过 tools 采取行动，并从环境中接收 consequences。当这些后果被保留、选择并用于学习时，核心对象就不再是一个固定 dataset，而是一个 feedback process——预测、决策、行动、观察，然后再次学习。
</div>

因此，pretraining 从来不只是学习文本。它沿着一条更长的 epistemic path，间接学习人类经验：

<div class="exp-flow" aria-label="从世界到模型的认识论路径" markdown="0">
  <span class="exp-flow-step">World</span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Human Experience</span></span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">被记录的部分</span></span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Text</span></span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Model</span></span>
</div>

人类书写的文本已经包含关于世界的 evidence，但它是经过 compression 和 selection 的证据。Agent 不会消除这种中介，也不会获得对现实的无过滤访问。它创造了另一条让 observations 进入学习系统的路径，并开始影响接下来会产生哪些 observations。

更深层的变化，不只是从 human data 转向 synthetic data，甚至也不只是从 documents 转向 trajectories，而是从围绕固定 dataset 的单向 pipeline，转向围绕 experience 组织的 learning system。

## 文本是经过选择的经验

文本不是未经处理的经验，而是人们选择写进语言的那一部分。在经验进入 corpus 之前，已经有人决定什么值得记录，其余部分则被留在了文本之外。

被保留下来的并不是生活的代表性样本。令人意外的事件、有用的结论和不寻常的失败，比日常规律更可能被写下。Corpus 因此既受它所描述的世界塑造，也受人类选择塑造。

<div class="exp-pullquote">
训练语料不是生活本身的样本。
<span>它是人们认为值得记录之事的样本。</span>
</div>

这并不意味着 language 中没有 world structure。文本是一个 latent process 的输出：世界影响感知，感知塑造信念与意图，信念与意图再产生语言。要准确预测语言，模型就有动力 reverse-engineer 产生语言的部分规律。

因此，next-token prediction 可以学习事实、物体属性、affordances、人类行为、norms、代码、行动后果，甚至 goal-directed behavioral regularities。**Next-token prediction 是 training interface；predictive compression 才是更深层的 operation。**但 predictive compression 并不保证一个完整或忠实的 world model。

## 那些我们不会写下来的东西

人们不会记录观察到的一切。杯子不会穿过桌面，但几乎没有人会把它写下来，因为这件事太显而易见。

$$
P_{\mathrm{life}}(e) \neq P_{\mathrm{text}}(e)
$$

这就是 reporting bias <d-cite key="gordon2013reporting"></d-cite>。Forbes 和 Choi 用一个简单对比说明了这一点：人们几乎不会写“我的房子比我大”，但“Tyler 走进了他的房子”这样的句子，已经间接透露出同样的物理知识 <d-cite key="forbes2017verb"></d-cite>。常识知识并没有从文本中消失；它隐藏在含义之中，并以高度失真的频率出现。

<em>Car Wash Test</em>让这种后果变得具体。面对“我想洗车，洗车店只有 100 米远，我应该走路还是开车？”这个问题，模型可能选择步行，因为 `短距离 → 步行` 是一个强大的 default。模型可能已经知道洗车需要把车带过去；失败之处在于，熟悉的关联抢在 goal 被完整应用之前主导了回答。

对于物理和实践推理，一个有用的简写是：常识往往是**在语言中低频、在生活中高频的结构**。Scaling 可以从隐含信息中恢复一部分常识，但不会让文本频率自动等同于经验频率。

## 语言足够吗？

错误的结论是：language 与现实分离，所以不可能支持 world model。一条记录下来的 claim 可以传递真正的知识，而不要求每个学习者都重复产生这条知识的 experience。模型不需要亲自冻一杯水，也能学到在普通压强下水大约在 0°C 结冰。

Language 还能透露超出字面陈述的结构。为了预测人们会说什么，模型可以推断关于物体、意图、社会行为和行动后果的 latent facts。Text 是有损的，但并不是 epistemically empty。

与此同时，perception 和 interaction 提供了另一种结构的学习通道。动物和婴儿接触的 symbolic language 远少于 foundation model，却能形成丰富的物理预期。这个观察并不能证明 language model 学不到 world structure；它说明反复出现的 consequences 能让某些规律变得直接、密集，而且不容易被省略。

更尖锐的限制出现在某个 consequence 尚未存在于 records 中的时候。Language 可以编码已经观察到的规律，却不可能预先包含每个未来状态中每个 action 的后果。模型可以预测会发生什么；interaction 则让它采取行动，并观察实际发生了什么。

<div class="exp-pullquote">
重要的跨越可能不是从 language 到 sensors，而是从 records 到 consequences。
<span>Interaction 让 prediction 必须面对来自模型之外的回答。</span>
</div>

因此，grounding 不一定意味着 humanoid body。更一般的要求，是能够访问这样的 environments：它们返回的 consequences 独立于模型自己选择生成的内容。Compiler、browser、game 和 simulator 都可以提供这样的边界，只是它们暴露的是世界的不同部分。

## Agent 生成自己的经验痕迹

从交互（interaction）中学习并不新鲜；强化学习和机器人学长期以来都围绕 agent–environment loop 展开 <d-cite key="sutton2018reinforcement"></d-cite>。正在发生变化的是，foundation-model agents 把这个接口延伸到了代码、浏览器和其他通用数字环境，并在工作过程中产生大量 structured traces（结构化痕迹）。

“Synthetic data” 对这些 traces 来说是一个过于粗糙的类别。比较 model-generated text：

`Model → Text`

和 agent interaction：

`Model → Action → Environment → Observation`

两者最终都可能变成 tokens，但 epistemic provenance 完全不同。前者主要从模型已有的 distribution 中采样；后者可以包含由 environment 返回的信息。

本文中的 **experience（经验）**并不是 raw reality，而是一条结构化的 interaction trace：

$$
E_t = (s_t, a_t, o_{t+1}, f_{t+1})
$$

它连接 state、action、下一个 observation，以及这次 transition 返回的 feedback。这条 trace 仍然只是对世界的局部表征，取决于 environment 及其 interface 允许模型观察到什么。

Predictive learning 可以估计一个行动之后通常会发生什么：

$$
P(o_{t+1} \mid s_t, a_t)
$$

Interaction 则真正执行 action，并获得这一次实际发生的结果。Coding agent 编辑文件、调用 compiler、观察报错、修改 hypothesis，再运行测试。**Prediction 从过去的 experience 外推；interaction 主动获取新的 evidence。**模型不只是预测世界，它还可以向世界提问。

<div class="exp-pullquote">
行动可以是 synthetic 的，consequences 却未必是。
<span>真正重要的问题不是谁产生了 tokens，而是其中的 evidence 来自哪里。</span>
</div>

## 工具中介经验

Agent 很少直接作用于环境。工具把模型的意图转化为环境能够执行的行动，再把行动后果转化为模型能够读取的观察：

<div class="exp-flow" aria-label="由工具中介的 agent interaction" markdown="0">
  <span class="exp-flow-step">Model</span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Tool</span></span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Environment</span></span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Tool Output</span></span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Model</span></span>
</div>

终端把命令传给操作系统，并返回 stdout、错误、文件和运行轨迹。浏览器把点击或代码转化为网页状态变化。科学仪器把原本无法直接获取的物理状态转化为图像、计数和测量值。**工具定义了 agent 的 action space 与 observation space。**

近期研究已经开始直接利用这条 observation stream。ECHO 训练 terminal agents 预测自身命令引起的环境输出，表明这些输出不只是下一步行动的临时 context，还能为学习 terminal dynamics 提供 dense supervision <d-cite key="shrivastava2026echo"></d-cite>。

在科学中，由工具中介的观察具有不同的 epistemic provenance（认识论来源）。数据库与搜索工具返回已经记录的证据；编译器与定理证明器返回形式系统中的后果；AlphaFold 等专用模型把结构数据与规律压缩为预测结构和置信度估计 <d-cite key="jumper2021alphafold"></d-cite>；模拟器返回近似世界中的轨迹；实验则通过仪器返回来自物理世界的新测量。

<figure class="exp-figure" markdown="0">
  <div class="exp-ladder">
    <div class="exp-rung"><span class="exp-rung-level">检索</span><strong>数据库 / 搜索</strong><span>先前记录的证据</span></div>
    <div class="exp-rung"><span class="exp-rung-level">计算</span><strong>编译器 / 证明器</strong><span>形式规则产生的后果</span></div>
    <div class="exp-rung"><span class="exp-rung-level">预测</span><strong>AlphaFold</strong><span>专用模型给出的估计</span></div>
    <div class="exp-rung"><span class="exp-rung-level">模拟</span><strong>模拟器</strong><span>近似世界中的轨迹</span></div>
    <div class="exp-rung"><span class="exp-rung-level">测量</span><strong>实验</strong><span>物理世界返回的证据</span></div>
  </div>
  <figcaption>这不是一个简单的质量排序，而是几种不同的认识论关系。工具输出是一项观察，不会自动成为真相；它的含义取决于其来源是检索、形式规则、预测、模拟，还是测量。</figcaption>
</figure>

这也区分了 token novelty 与 epistemic novelty。Search result 对模型当前 context 可能是新的，却仍然只是在返回旧 evidence；experiment 则可以产生此前从未存在于 records 中的 observation。

<div class="exp-pullquote">
Grounding 不一定需要 embodiment；它需要来自模型之外的 consequences。
<span>每一种 tool 都暴露了一个 environment，但只能通过对它的特定表征来暴露。</span>
</div>

Tool 既可以扩展 inference-time capability，也可以成为 experience 的来源。但 agent 学到的是“tool 所表征的 environment”，其中既包括它捕捉到的规律，也包括它施加的假设。模型不仅要理解输出说了什么，还要理解：**这个 tool 有资格支持哪一类 claim。**

## 语料库成为一个过程

传统 pretraining 从一个相对固定的 archive 开始：收集、冻结，然后训练。Agent interaction 可以把 corpus production 变成一个持续进行的过程。

这些痕迹不会自动变得有用。大多数已部署模型并不会在每次交互后更新权重。经验必须在取得适当许可的前提下被保留、过滤和验证，并被用于上下文、记忆或优化，才可能改变未来的预测或行动。

**交互产生新的观察，而不会自动产生新的知识。**许多观察只是再次确认已知规律、暴露实现细节，或增加噪声。它们的认识论价值取决于如何解释、检验和吸收这些观察。

<div class="exp-pullquote">
Dataset 不再只是 learning system 的输入，也成为它的输出之一。
<span>当前模型能够参与决定未来模型将看到什么 experience。</span>
</div>

过去，数据集在很大程度上是训练的外部输入：

$$
D \rightarrow M
$$

如今，当前模型的能力、失败与行动，可以影响下一代模型所获得的数据分布：

$$
M_t \rightarrow D_{t+1} \rightarrow M_{t+1}
$$

关键转折在于：一旦当前模型开始参与决定接下来生成哪些 data，data production 就不再 exogenous 于训练。Training distribution 开始部分 **endogenous 于 learning system 本身**。

这使 experience shaping 成为一个核心学习功能。系统可以寻找 failures、生成 tasks、构造 adversarial cases、进行 self-play、选择困难样本，或创建 targeted environments。目标不再只是收集“好数据”，因为 **high data quality 并不等于 high learning value**。

一百万条模型已经掌握的高质量样本可能增加很少；一条可靠且暴露盲点的 trajectory 反而可能重要得多。一旦 data 可以主动生成，curriculum 就成为真正的数据问题：**对当前模型而言，最好的 next experience 是什么？**答案取决于 capability、uncertainty、failure modes、verifier availability 和 cost。

这种供给是 renewable 的，却不是 infinite 的。数字 experience 受算力、能源、存储、执行吞吐量和可靠 verification 的约束；物理 experience 仍受实验延迟、仪器容量、样本和 biological time 的约束。

## 训练流程成为循环

Pretraining、midtraining、posttraining 和 deployment 仍然是有用的 engineering labels。它们描述 checkpoint lifecycle、optimization regime、objective changes 和 dataset mixture。但它们更清楚地说明事情**何时**发生，而不是它执行了**什么功能**。在 adaptive learning system 中，同一条 trace 可以跨越不同阶段和不同代模型。

四种功能更为持久：

- **Predictive / world learning** 把 experience 中的规律压缩为可以复用的 representations。它问：这里有什么 structure 是可以预测的？
- **Policy learning** 把 knowledge、goals 和 constraints 转化为 behavior。它问：根据我知道和想要的，我应该怎么做？
- **Interaction** 执行 action 并获得 realized consequences。它问：environment 实际返回了什么？
- **Experience shaping** 选择或生成模型接下来应该遇到什么。它问：现在什么 experience 具有最高 learning value？

Pretraining 可以在 documents 或 trajectories 上做 predictive compression。`STATE → ACTION → OBSERVATION → ACTION → OBSERVATION` 这样的序列依然可以使用 next-token objective。Agentic data 不一定取代 next-token prediction；它改变的是 next-token prediction 在什么对象上进行。

World learning 与 policy learning 也必须区分。Predictive model 描述可能的 consequences：

`walk → 人到了，车留在家里`<br>
`drive → 人和车都到了`

Policy $\pi(a \mid s, g, c)$ 则在这些后果之间做 goal-conditioned choice。现在可以更准确地理解前面的 <em>Car Wash Test</em>：它不一定意味着 world knowledge 缺失，而是“短距离 → 步行”的 behavioral prior 取代了目标真正要求的 policy。**知道人们通常怎么做，不等于知道这个目标要求什么。**因此，posttraining 不只是更多 pretraining；它的一个核心功能，是把 knowledge、goals 和 constraints 转化为 policy。

Experience shaping 同样 fundamental，却不一定属于一个叫作 midtraining 的阶段。它可以发生在 pretraining 中、posttraining 后、deployment 中、模型世代之间，或持续发生。Midtraining as a stage is contingent; experience shaping as a function is fundamental.

这种映射并不严格。Pretraining 会学习 behavioral priors，posttraining 也可以增加 knowledge，interaction 也可能只用于 evaluation 而不带来 update。重点不是重新命名阶段，而是用循环中反复出现的 functions 取代线性 ontology。

考虑一条 coding-agent rollout：

> 状态 → 编辑 → 编译器报错 → 修正假设 → 修复 → 测试通过

对当前模型而言，这可能是一条部署轨迹。一旦被保留和验证，同一条痕迹就可以成为未来模型训练语料的一部分——甚至可能进入它的预测性预训练混合数据。

<div class="exp-pullquote">
对 <em>M</em><sub>t</sub> 而言属于部署的内容，可以成为 <em>M</em><sub>t+1</sub> 的训练数据。
<span>阶段属于一次训练过程；经验则可以跨越阶段与模型世代流动。</span>
</div>

<div class="exp-loop" aria-label="以经验为中心的学习循环" markdown="0">
  <span class="exp-node evidence">经验</span><span class="exp-arrow">→</span>
  <span class="exp-node model">预测学习</span><span class="exp-arrow">→</span>
  <span class="exp-node model">策略</span><span class="exp-arrow">→</span>
  <span class="exp-node model">行动</span><span class="exp-arrow">→</span>
  <span class="exp-node evidence">后果</span><span class="exp-arrow">→</span>
  <span class="exp-node evidence">新经验</span><span class="exp-arrow">↺</span>
</div>

## 从经验到知识生产

Agent 生成一条 trace，并不意味着模型已经从中学到了东西。只有当 experience 改变某个会持续影响未来 prediction 或 action 的 persistent component——weights、memory、skills 或其他机制——循环才真正闭合。

对于 scientific intelligence，这个区别变得决定性。一个模型可以学完所有已经记录的 discoveries，却仍然遇到答案尚未存在于 corpus 中的问题。Scientific system 最终必须超越 recorded answers，参与生成 evidence：

<div class="exp-flow" aria-label="科学知识生产循环" markdown="0">
  <span class="exp-flow-step">Corpus</span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Hypothesis</span></span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Intervention</span></span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Measurement</span></span>
  <span class="exp-flow-link"><span class="exp-flow-arrow">→</span><span class="exp-flow-step">Updated Knowledge</span></span>
</div>

当 scientific agent 能够从 predicting an answer 走向 causing the world to reveal an answer 时，它才真正变得有趣。这不仅需要生成 hypothesis，还需要选择 intervention、解释 evidence、更新 beliefs，并决定接下来测试什么。

模型最初从 knowledge production 的 records 中学习。Agent 则开始参与产生 evidence 的过程，并通过 experience shaping 影响下一步寻找什么 evidence。

<div class="exp-coda">
AI learning 正在从固定 dataset 上的单向 pipeline，转向一个 feedback process：模型进行 prediction、形成 policy、通过 tools 行动、观察 consequences，并越来越多地塑造自己下一步将从什么 experience 中学习。对于 scientific intelligence，最重要的情形是 interaction 产生了 corpus 中此前不存在的 evidence。<strong>From dataset to experience, and from pipeline to loop.</strong>
</div>

</div>
