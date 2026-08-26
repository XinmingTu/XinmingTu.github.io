---
layout: distill
title: "From Data to Experience"
description: "Agentic learning shifts AI from fixed corpora toward learning loops built around tool-mediated experience."
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

<div class="exp-lede">
Language models do not learn from the world directly. They learn from traces of interaction with it. For general-purpose language models, the dominant source of those traces has been human-written text—produced after experience was filtered through attention, abstraction, and judgment about what was worth recording.
</div>

Pretraining has therefore never been only about learning text. It learns indirectly from human experience, across a long epistemic path:

$$
\text{World} \rightarrow \text{Human Experience} \rightarrow \text{Attention / Abstraction / Selection} \rightarrow \text{Text} \rightarrow \text{Model}
$$

Agents do not make this mediation disappear, nor do they give models unfiltered access to reality. They add another path: a model can act, elicit an observation, and co-produce a new trace with an environment. Once those actions begin to influence what is observed and recorded next, the model no longer merely learns from a corpus. It begins to participate in producing the corpus from which future models may learn.

The deeper shift is not simply from human data to synthetic data, or even from documents to trajectories. It is from a one-way training pipeline organized around a fixed dataset toward a learning loop organized around experience.

## Text Is Selected Experience

A real event has structure: a state, an action, a consequence, and some form of feedback. By the time it enters a document, it may have collapsed into a single sentence:

> Don't call this API concurrently.

The context that triggered the bug, the failed attempts, the error messages, and the path to the diagnosis have mostly disappeared. A trajectory has been flattened into a sequence of tokens.

Text is not only compressed experience. It is **selected experience**. What enters the training corpus is the part that someone noticed, understood, and considered worth writing down.

<div class="exp-pullquote">
Pretraining data is a lossy, selectively recorded projection of experience.
<span>The corpus preserves what survived both compression and human attention.</span>
</div>

This helps explain why next-token prediction can learn more than surface language. Text is the output of a complicated process: the world affects perception; perception shapes beliefs and intentions; those beliefs and intentions produce language. Predicting text well creates pressure to capture some of the latent regularities that produced it.

Next-token prediction is the training interface. Through predictive compression, it can learn facts, language structure, object properties, affordances, human behavior, norms, code, and action consequences. But it does not automatically produce a complete or faithful world model.

## What We Do Not Write Down

The limitation is not only compression, but selection.

People do not record everything they observe. Cups do not pass through tables. Objects fall when released. A bag usually becomes heavier as more things are placed inside it. These events are common in life but rarely worth stating because they are too obvious.

$$
P(\text{event in life}) \neq P(\text{event in text})
$$

This is reporting bias <d-cite key="gordon2013reporting"></d-cite>. Forbes and Choi illustrate it with a simple contrast: people almost never bother to write “my house is bigger than me,” even though a sentence such as “Tyler entered his house” indirectly reveals the same physical knowledge <d-cite key="forbes2017verb"></d-cite>. Commonsense knowledge is not absent from text; it is hidden in implication and represented at highly distorted frequencies.

Yejin Choi describes commonsense intelligence as intuitive reasoning about everyday situations grounded in rich background knowledge of the physical and social world <d-cite key="choi2022curious"></d-cite>. Common sense is not merely a database of propositions. It also includes object affordances, human intentions, and an understanding of when a change in context invalidates an otherwise plausible inference.

Scaling pretraining can recover some of this implicit structure, but it does not automatically remove selection bias. Shwartz and Choi found that language models can better estimate some actions, outcomes, and properties that occur frequently but are rarely stated. At the same time, they can overestimate the plausibility of rare events and amplify biases already present in the corpus <d-cite key="shwartz2020reporting"></d-cite>.

The <em>Car Wash Test</em> offers a small example. Asked, “I want to wash my car. The car wash is only 100 meters away. Should I walk or drive?”, some models choose walking because short distances are commonly associated with walking. Each local inference sounds reasonable, yet the answer misses an implicit task constraint: the car must arrive too. The failure is not universal across models or prompts, but it exposes a gap between linguistic plausibility and grounded task understanding.

Human common sense may be less like an encyclopedia of propositions than a consequence model compressed from repeated everyday interaction:

$$
f(\text{state},\ \text{action}) \rightarrow \text{likely consequence}
$$

At least for physical and practical reasoning, a useful summary is: **common sense is often the low-frequency-in-language, high-frequency-in-life part of a world model.**

## Agents Generate Their Own Traces

Learning from interaction is not new; reinforcement learning and robotics have long been organized around the agent–environment loop <d-cite key="sutton2018reinforcement"></d-cite>. What is changing is that foundation-model agents extend this interface into code, browsers, and other general digital environments, producing large volumes of structured traces as they work.

A coding agent does not merely read that a program will fail. It edits a file, invokes a compiler, observes an error, revises a hypothesis, and runs a test. A browser agent clicks, encounters a modal or permission error, and searches for another path. These systems receive more than a human summary of experience: they produce traces with an explicit action–consequence structure.

A minimal experience can be written as:

$$
E_t = (s_t, a_t, o_{t+1}, f_t)
$$

It contains the current state, an action, the next observation, and success, failure, or another form of feedback.

The important distinction is not text versus non-text—a terminal output is still text. It is causal provenance. Human-written text records someone else's past interaction. In an agent trace, the observation is the environment's response to an action the model just took.

Prediction extrapolates from previous experience; interaction solicits new evidence. A model can predict what is likely to happen after an action, but only interaction reveals what happened in this particular case. In that sense, an agent does not merely predict the world. It can ask the world.

This is why “synthetic data” is too coarse a category. A model-generated answer and a model-generated action followed by an external consequence may both become tokens, but the evidence inside those tokens came from different places. **The actions may be synthetic; the consequences need not be.**

## Tools Mediate Experience

Agents rarely act on environments directly. A tool converts a model's intention into an action the environment can execute, then converts the consequence into an observation the model can read:

$$
\text{Model} \rightarrow \text{Tool} \rightarrow \text{Environment} \rightarrow \text{Tool Output} \rightarrow \text{Model}
$$

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

<div class="exp-pullquote">
Every tool exposes an environment, but only through a particular representation of it.
<span>A tool makes a task-relevant projection of the world available for interaction.</span>
</div>

A tool can therefore extend inference-time capability and become a source of experience. But the agent learns the environment as represented by the tool, including both the regularities the tool captures and the assumptions it imposes. The model must learn not only what an output says, but what kind of claim that output is entitled to support.

## The Corpus Becomes a Process

Traditional pretraining begins with a relatively fixed archive: collect a corpus, then train a model. Agent interaction can turn corpus production into a continuing process.

These traces are not automatically useful. Most deployed models do not update their weights after each interaction. Experience must be retained with appropriate permission, filtered, verified, and used in context, memory, or optimization before it can change future predictions or actions.

<div class="exp-pullquote">
The dataset is no longer merely an input to the learning system. It increasingly becomes one of its outputs.
<span>The current model can help determine what experience future models will see.</span>
</div>

Previously, the dataset was largely an external input to training:

$$
D \rightarrow M
$$

Increasingly, the capabilities, failures, and actions of the current model can influence the distribution generated for the next one:

$$
M_t \rightarrow D_{t+1} \rightarrow M_{t+1}
$$

This does not imply that we know the universally best next experience. Learning value is model-dependent. A million high-quality examples of a task the model has already mastered may add little; one reliable trajectory that exposes a blind spot may add much more. Once data can be generated, the question shifts from “What data is high quality?” toward “What experience is informative for this model now?”

The supply is renewable, not infinite. In digital environments, experience generation is constrained by compute, energy, storage, execution throughput, and the availability of reliable verifiers. In physical science, it remains constrained by experiment latency, instrument capacity, samples, and biological time. Digital experience becomes increasingly compute-bound; physical experience remains reality-bound.

## The Training Pipeline Becomes a Loop

Pretraining, midtraining, posttraining, and deployment remain useful engineering labels. They describe checkpoint lifecycles, optimization regimes, and dataset mixtures. But in an experience-centered system, they are not the most stable conceptual primitives, because the same trace can move across stages and model generations.

Four functions are more persistent:

- **Predictive learning** compresses regularities in experience into representations that generalize. This is a dominant function of pretraining.
- **Policy learning** turns knowledge, goals, and constraints into behavior. This is a dominant function of posttraining.
- **Interaction** executes actions and obtains realized consequences from an environment.
- **Experience shaping** selects or generates what the current model should encounter next, based on its failures, uncertainty, capabilities, and cost constraints.

The mapping is not exact. Pretraining also learns goal-directed behavioral priors; posttraining can add knowledge; interaction can be used for evaluation without any later update. The point is not to rename the stages, but to notice that experience can flow through all of them.

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

An agent producing a trace does not mean that a model has learned from it. The loop closes only when experience systematically changes a persistent component that affects future prediction or action—whether weights, memory, skills, or something else.

What changes is the direction of knowledge production. Models first learned from records of discoveries, failures, and regularities that humans considered worth writing down. Agents can now participate in the process that produces such records: acting through tools, receiving consequences, and helping determine which experiences are generated next.

<div class="exp-coda">
The deeper shift is from dataset-centered training to experience-centered learning. Models no longer merely compress what humans chose to record; they increasingly act, elicit evidence through tools, and help produce the experience from which future models learn. <strong>From dataset to experience, and from pipeline to loop.</strong>
</div>
