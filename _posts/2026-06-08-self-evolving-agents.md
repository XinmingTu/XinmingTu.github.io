---
layout: distill
title: "The What & When of Self-Evolving Agents"
description: "Work in progress: a 3x3 framework for understanding self-evolving agents across external state, harnesses, and weights."
date: 2026-06-08
tags: ['AI', 'agents', 'deep-learning']

authors:
  - name: Xinming Tu
    url: "https://xinmingtu.cn"
    affiliations:
      name: University of Washington
  - name: Tong Chen
    url: "https://scholar.google.com/citations?user=fOcXofAAAAAJ&hl=en"
    affiliations:
      name: University of Washington

bibliography: 2026-06-08-self-evolving-agents.bib
_styles: |
  d-article h3 {
    margin-top: 1.15em;
    margin-bottom: 0.55em;
  }
  d-article figure.self-evolving-figure {
    margin: 1.35rem 0 1.65rem;
  }
  d-article figure.self-evolving-figure.tight-top {
    margin-top: 0.55rem;
  }
  d-article figure.self-evolving-figure.medium {
    max-width: 760px;
    margin-left: auto;
    margin-right: auto;
  }
  d-article figure.self-evolving-figure img {
    width: 100%;
    height: auto;
    display: block;
  }
  d-article figure.self-evolving-figure.narrow {
    max-width: 580px;
    margin-left: auto;
    margin-right: auto;
  }
  d-article figure.self-evolving-figure figcaption {
    color: #6b7280;
    font-size: 0.88rem;
    line-height: 1.45;
    margin-top: 0.55rem;
    text-align: center;
  }
  d-article details.appendix-cell {
    border-top: 1px solid #e7e9f0;
    padding: 0.8rem 0;
  }
  d-article details.appendix-cell:last-of-type {
    border-bottom: 1px solid #e7e9f0;
  }
  d-article details.appendix-cell summary {
    align-items: baseline;
    cursor: pointer;
    display: flex;
    gap: 0.75rem;
    list-style: none;
  }
  d-article details.appendix-cell summary::-webkit-details-marker {
    display: none;
  }
  d-article details.appendix-cell summary::before {
    color: #7a8196;
    content: "+";
    flex: 0 0 auto;
    font-weight: 800;
  }
  d-article details.appendix-cell[open] summary::before {
    content: "-";
  }
  d-article .appendix-cell-title {
    color: #1a1d26;
    flex: 0 0 14rem;
    font-weight: 800;
  }
  d-article .appendix-cell-subtitle {
    color: #6b7280;
    font-size: 0.92rem;
    font-weight: 600;
  }
  @media (max-width: 720px) {
    d-article details.appendix-cell summary {
      align-items: flex-start;
      flex-direction: column;
      gap: 0.15rem;
    }
    d-article details.appendix-cell summary::before {
      display: none;
    }
    d-article .appendix-cell-title {
      flex-basis: auto;
    }
  }

toc:
  - name: "The Dual Promise"
  - name: "What Evolves"
  - name: "Learning From Experience"
  - name: "The 3x3 Evolution Matrix"
  - name: "Single Session: Online Adaptation"
  - name: "Across Sessions: Longitudinal Alignment"
  - name: "Across Users: Population-Level Evolution"
  - name: "Conclusion: Escaping the Human Bottleneck"
  - name: "Appendix: The Complete Landscape"
---

> **Work in progress.**

## The Dual Promise

**The era of static AI agents is ending.**

True intelligence should not peak at deployment only to depreciate. It must appreciate. Every interaction should create pressure for the system to adapt. We are now witnessing a fundamental shift toward dynamic, **self-evolving systems**, driven by a dual promise:

- **Motivation 1: Marginal Cost Reduction (Shrinking Costs).** Operationally, this means fewer prompt tokens, fewer tool calls, fewer retries, and less human intervention per solved task family. By compressing experience into reusable assets, the system stops paying for the same mistake twice.

- **Motivation 2: Capability Ceiling Expansion (Breaking Ceilings).** Evolution unlocks zero-day tasks and enables robust **long-horizon execution**. Static agents inevitably fail at complex, multi-step goals due to compounding errors and context exhaustion. By learning to forge ad-hoc tools, cache intermediate progress, and adapt strategies at runtime, a self-evolving agent makes long-term autonomy a hard systems claim rather than a behavioral illusion.

<figure class="self-evolving-figure tight-top medium">
  <img src="/assets/img/2026-06-08-self-evolving-agents/figure1-dual-promise.svg" alt="A chart showing self-evolving agents reducing cost per task while expanding capability over time.">
  <figcaption><strong>Figure 1.</strong> Self-evolution has two linked payoffs: lower marginal cost and higher capability ceilings.</figcaption>
</figure>

Leading systems are already abandoning **stateless orchestration** in favor of updatable execution substrates. These systems prove that agents must internalize their experience. But "learning" is not magic; it requires a physical substrate. To genuinely reduce costs and break capability ceilings, we must understand the architecture of this adaptation.

The central question is simple: **Where exactly does this evolution happen?**

Recent surveys on self-evolving agents organize the field around what evolves, when it evolves, and how it evolves <d-cite key="selfevolvingsurvey2025"></d-cite>. The 3x3 matrix below is a systems-oriented version of the same instinct: it asks which structural layer is updated, and over what lifetime the update persists.

## What Evolves

Before discussing how an agent evolves, we need to define what an agent physically is. In practice, an agent's cognitive state is distributed across three plastic layers.

<figure class="self-evolving-figure narrow">
  <img src="/assets/img/2026-06-08-self-evolving-agents/figure2-three-layers.svg" alt="A nested diagram of three self-evolving agent layers: external files, agent harness, and model weights.">
  <figcaption><strong>Figure 2.</strong> The agent is not only the model. Its plastic state spans external files, harness logic, and model weights.</figcaption>
</figure>

### Level 1: Model Weights

The first layer is the parametric core: the model weights. This layer stores implicit knowledge and is updated through gradient-based learning. Weight evolution can generalize broadly across tasks, but it is computationally expensive and carries inherent risks such as catastrophic forgetting, capability regression, and costly evaluation requirements.

### Level 2: Agent Harness

The second layer is the agent harness, which includes orchestration logic, control flow, tool runtime, and error recovery loops. This layer defines *how* the agent executes tasks and can evolve without changing model weights. A system can optimize tool-selection logic, compile repeated workflows into deterministic subroutines, or rewrite its system prompts.

In modern systems, this is the machinery behind the plan-act-observe loop: tool routing, retry policy, subagent spawning, workflow compilation, and runtime recovery.

### Level 3: External State

The third layer is external state: persistent memory stores, skill libraries, knowledge graphs, and scratchpads. Unlike traditional read-only RAG, modern external memory is structured, editable, and callable. It stores precise code snippets, error logs, user preferences, and reusable procedures.

Evolution here is computationally cheap, often just CRUD operations, and offers high fidelity relative to parametric memory: a saved function, test command, or API wrapper remains precise instead of blurring into statistical memory.

### The Blurry Boundary: Code as Data

The boundary between Level 2 and Level 3 is porous. When an agent writes a Python function into a skill library, it starts as an external file (Level 3). But the moment the runtime loads that file to route future tasks, data becomes control logic (Level 2). External memory no longer merely stores facts; it stores new operators.

This "code as data" property is a core mechanism in advanced self-evolving agents. External files are no longer passive storage; they are executable capability substrates.

## Learning From Experience

At its core, self-evolution reduces to a single imperative: **learning from experience**.

Every deployed agent leaves behind experience exhaust: successful trajectories, tool errors, rejected actions, and user corrections. A static agent flushes this signal the moment a task ends. A self-evolving agent captures that signal and hardens it into reusable state.

To map how this feedback loop operates, we project the three structural layers against three time scales of adaptation:

- **Single Session:** Online adaptation inside one active trajectory.
- **Across Sessions:** Longitudinal adaptation to a specific user, project, or codebase.
- **Across Users:** Population-level evolution derived from aggregate interactions.

## The 3x3 Evolution Matrix

The result is a 3x3 map: three persistence horizons crossed with three update substrates.

<figure class="self-evolving-figure">
  <img src="/assets/img/2026-06-08-self-evolving-agents/figure3-evolution-matrix.svg" alt="A 3 by 3 matrix mapping self-evolving agents by update lifetime and updated layer.">
  <figcaption><strong>Figure 3.</strong> The taxonomy as a visual map: update lifetime on one axis, updated substrate on the other.</figcaption>
</figure>

This matrix is not meant to be a rigid classification. In real systems, the cells interact. A temporary tool created in one session can become a persistent skill across sessions. A project-specific workflow can become a product default. A pattern discovered across millions of user failures can eventually become a model checkpoint.

## Single Session: Online Adaptation

The first time scale is intra-trajectory. How does an agent use a live execution trace to correct itself on the fly?

### Level 3: Working Memory and Context Paging

Inside a single session, external memory fights context degradation. Long reasoning traces pile up. Tool outputs introduce noise. This is the agentic version of the "lost in the middle" problem: even if the context window is technically large enough, the signal-to-noise ratio inevitably deteriorates <d-cite key="liu2023lostmiddle"></d-cite>.

The solution is OS-style context management. **MemGPT** is the canonical example here, reframing the context window as constrained RAM and external memory as virtual storage <d-cite key="memgpt2023"></d-cite>. It pages older context out, retrieves it when needed, and preserves logical clarity under long-horizon interaction.

**The caveat: Storage is not evolution.** Simply dumping context into an external database is meaningless if lossy retrieval quietly injects causal drift into the reasoning chain. A memory system only qualifies as adaptive if it improves the efficiency frontier rather than shifting the bottleneck from context length to retrieval noise.

### Level 2: Dynamic Orchestration

At the harness layer, the agent rewires its execution plan at runtime.

A static workflow dictates: *Call Tool A $\rightarrow$ Call Tool B $\rightarrow$ Summarize*.

A dynamic workflow adapts: *Tool A failed twice $\rightarrow$ inject a diagnostic node; the API wrapper is missing $\rightarrow$ synthesize a temporary function and mount it into the execution DAG.*

**Claude Code's Dynamic Workflows** make this literal: the execution plan leaves the conversation entirely. Claude writes a JavaScript orchestration script, and a separate runtime executes it in the background across subagents <d-cite key="anthropicdynamicworkflows2026"></d-cite>. The control flow - loops, branching, fan-out, error handling, resumability, and intermediate state - is compiled dynamically for that specific task.

The generated script may be temporary, but for that session, the agent has fundamentally expanded its own action space.

### Level 1: Test-Time Training

The most aggressive online adaptation modifies weights during inference. Test-time training destroys the clean boundary between training and deployment. Instead of merely using a frozen model to search longer, the system updates a subset of parameters using the exact problem at hand <d-cite key="tttdiscover2026"></d-cite>.

Whether adapting fast weights in-place <d-cite key="inplacettt2026"></d-cite> or applying a learned update rule to hidden states <d-cite key="tttlayers2024"></d-cite>, TTT is the upper edge of self-evolution. It is computationally brutal and operationally complex. But the payoff is profound: the agent does not just remember a discovery. It alters the underlying machinery that generates discoveries.

This exposes a deeper mathematical reality: the boundary between external context (Level 3) and parametric weights (Level 1) is porous. When external memory enters the inference path, it is physically materialized as dynamic tensors in the KV cache. In standard attention, $\text{Attention}(Q, K, V) = \text{softmax}(QK^T / \sqrt{d_k})V$; appending experience directly alters the computational matrix <d-cite key="vaswani2017attention"></d-cite>. At runtime, memory is not merely a database. It is a transient parameter.

## Across Sessions: Longitudinal Alignment

The second time scale is inter-session. How does an agent internalize the structural patterns of a specific user, project, or codebase over days and weeks?

### Level 3: Executable Skills

The most practical inter-session mechanism is caching executable behaviors. **Voyager** pioneered this in simulated environments by accumulating an ever-growing library of executable skills in Minecraft, storing complex routines as code to be retrieved later <d-cite key="voyager2023"></d-cite>. Today, frameworks like **OpenHands** bring the same pattern into software engineering through persistent skill directories and installable skill lifecycles <d-cite key="openhandskills2026"></d-cite>.

For a personal coding agent, this means saving an arcane project test command, storing a verified API wrapper, or locking in a strict migration recipe. The system transitions from semantic search to asset reuse. The agent simply stops paying the inference tax of rediscovering the exact same solution.

### Level 2: Meta-Programming

When an agent repeatedly solves the same class of problems, it should not reconstruct its execution plan from scratch. High-performing historical trajectories must be mined to optimize the harness itself.

This is the domain of meta-programming. **DSPy** treats language-model programs as optimizable computational graphs, tuning instructions, few-shot demonstrations, and routing rules against an evaluation metric <d-cite key="dspy2023"></d-cite>. The mechanism here is structural: a bloated, verbose explicit context collapses into a lean, project-specific DAG (Directed Acyclic Graph).

### Level 1: Personal Adapters

At the parametric layer, inter-session evolution compresses implicit preferences - coding style, API choices, verbosity tolerance, and problem-solving habits - into parameter-efficient adapters. If a preference becomes parametric, the model no longer needs explicit instructions; it becomes instinct.

This is the shift from a generic foundation model to a personalized intelligence. A static foundation model is inherently a generic, one-size-fits-all reasoner. Cross-session adapter updates let the agent specialize toward a user's recurring workflows and problem-solving habits. It ceases to just solve problems; it learns to solve them *your way*.

## Across Users: Population-Level Evolution

The third time scale is population-level. How does a system aggregate millions of isolated trajectories, failures, and human corrections to conquer the long tail of edge cases?

### Level 3: Collective Knowledge Graphs

At the external-state layer, population-level evolution manifests as a shared ecosystem of capabilities and knowledge.

Consider how the human scientific community tackles an open problem. No single researcher derives every result from base axioms; one group proves an intermediate lemma, publishes it, and that lemma becomes a trusted tool for the next group to build upon.

Self-evolving agents must replicate this dynamic, a pattern already visible in hybrid human-AI discovery. **FunSearch** used LLM-guided program search to produce new constructions and interpretable programs that researchers could inspect and build on <d-cite key="funsearch2023"></d-cite>. In the engineering space, tool ecosystems and registries such as **Composio** and **LlamaHub** are early infrastructure for the same pattern: an API wrapper, integration, or workaround created once can become an executable asset for many agents <d-cite key="composio2026,llamahub2024"></d-cite>.

This transforms isolated AI systems into a collective intelligence with a real network effect. Evolution is no longer constrained by a single session's context window; it compounds horizontally. The primary bottleneck becomes trust: a global memory bank requires strict provenance and sandboxing to avoid becoming a reservoir for hallucinations or a vector for supply-chain vulnerabilities.

### Level 2: Automated Harness Design

At the harness layer, aggregate failure logs expose structural bottlenecks. If ten thousand deployed agents fail in the exact same execution loop, the root cause is rarely the base model's capacity. It is usually a defect in the default system prompt, tool schema, retry policy, or orchestration path.

**ADAS (Automated Design of Agentic Systems)** represents the frontier here: meta-agents are deployed to iteratively program, validate, and search for better agentic control flows <d-cite key="adas2024"></d-cite>. The system no longer just searches for better answers; it rewrites the process that generates the answers.

### Level 1: Continual Parametric Evolution

At the parametric layer, population-level evolution is continuous reinforcement learning.

Strictly speaking, the agent does not evolve independently of humans; rather, **it treats the human population as its environment**. Deployed systems generate an ocean of implicit supervision. Every user correction, rejected output, accepted edit, and regenerated answer acts as a reward signal.

**Cursor** is the canonical public product example of this paradigm. Its online reinforcement learning for tab autocomplete turns natural developer behavior into supervision for policy improvement <d-cite key="cursortabrl2025"></d-cite>. The paradigm shift is structural: human interaction is no longer only an offline labeling process or external evaluation step; it becomes an automated catalyst for continuous improvement.

**A note on autonomy:** Today, population-level evolution is rarely fully autonomous. Agents act as prolific proposers of new tools and workflows, while humans still act as maintainers who verify and merge them. As automated sandboxing and AI-driven evaluation mature, this verification loop can close.

## Conclusion: Escaping the Human Bottleneck

Structuring self-evolution around single sessions, user preferences, and human populations is a practical way to build systems today. But this anthropocentric framing is ultimately transitional. We are currently measuring an AI's evolution by how well it adapts to *us*: our coding habits, our prompts, and our manual corrections.

As we look toward AGI and eventually ASI, the fundamental nature of experience will shift. Today, human interaction is the primary environment that forces an AI to adapt. The true inflection point arrives when the human is removed from the critical loop. The ultimate driver of evolution will not be human feedback, but **algorithmic self-play and open-ended exploration**.

Imagine a network of autonomous agents deployed to tackle an unsolved physics problem or design a next-generation operating system. They generate synthetic hypotheses, build their own sandbox environments to test them, and distribute successful discoveries - whether as executable tools (Level 3), optimized reasoning pathways (Level 2), or weight updates (Level 1) - across a global collective intelligence.

Their experience compounds at the speed of compute, decoupled from the biological limits of human typing speed or comprehension. By architecting systems capable of modifying their own external state, cognitive harnesses, and parametric cores, we are no longer just engineering smarter Copilots. We are laying the structural foundation for an intelligence that can finally evolve itself.

## Appendix: The Complete Landscape

The main essay keeps one or two anchor examples per cell. This appendix restores the broader map: the same 3x3 matrix, but with more systems, mechanisms, and caveats.

The placement rule is simple: if an example changes the reader's understanding of the core mechanism, it belongs in the main text; if it primarily broadens coverage, it belongs here. Several systems also cut across cells:

- **External state becoming harness:** skills begin as files, but become control logic once the runtime discovers, loads, and routes through them. Anthropic Agent Skills, OpenHands skills, and Memento-Skills all sit on this boundary <d-cite key="anthropicagentskills2026,openhandskills2026,mementoskills2026"></d-cite>.
- **External state becoming transient parameters:** retrieved context is not just "read" by the model; it becomes key-value tensors in the active computation. Linear attention and fast-weight interpretations make this boundary especially explicit <d-cite key="lineartransformersrnn2020,linearfastweights2021"></d-cite>.
- **Local discoveries becoming global defaults:** a temporary script can become a user skill, a user skill can become a shared registry asset, and a repeated population-level failure can become a harness or checkpoint update.

The nine cells below are collapsed by default: open a cell when you want the concrete systems, mechanisms, and caveats behind that part of the matrix.

<details class="appendix-cell" markdown="1">
<summary><span class="appendix-cell-title">Single Session / Level 3</span><span class="appendix-cell-subtitle">Working Memory and Context Paging</span></summary>

This cell covers state that is created, compressed, retrieved, or discarded inside one active trajectory.

- **MemGPT** frames the context window as constrained RAM and external storage as virtual memory, making memory movement an explicit systems problem <d-cite key="memgpt2023"></d-cite>.
- **MEMENTO** teaches models to manage their own context by segmenting, compressing, and evicting intermediate reasoning blocks <d-cite key="memento2026"></d-cite>.
- **Memory-as-Action** treats memory editing as a learnable action policy instead of a fixed heuristic <d-cite key="memoryasaction2025"></d-cite>.
- **AMA-Bench** highlights the core failure mode: long-horizon memory can introduce retrieval drift, so memory systems must be evaluated on causal usefulness rather than storage volume <d-cite key="amabench2026"></d-cite>.
- **Lost in the Middle** explains why this matters even when context windows are large: attention over long context is positionally and semantically brittle <d-cite key="liu2023lostmiddle"></d-cite>.

**Mechanism:** compress the live trace into structured memory, page low-salience information out of active context, and rehydrate only the pieces needed for the next decision.

**Caveat:** a larger memory store is not automatically an evolved agent. Without reliable write policy, retrieval policy, and evaluation, memory becomes another noisy tool.

</details>

<details class="appendix-cell" markdown="1">
<summary><span class="appendix-cell-title">Single Session / Level 2</span><span class="appendix-cell-subtitle">Dynamic Orchestration and Ad-Hoc Tools</span></summary>

This cell covers runtime changes to the control path: the agent changes how it acts before the current task is over.

- **Claude Code Dynamic Workflows** move orchestration from the chat transcript into a JavaScript script executed by a separate workflow runtime, allowing loops, branching, subagent fan-out, resumability, and intermediate variables to live outside the model context <d-cite key="anthropicdynamicworkflows2026"></d-cite>.
- **OpenClaw-RL** treats conversational feedback and next-state observations as a training signal for agents, making runtime experience a direct source of policy improvement <d-cite key="openclawrl2026"></d-cite>.
- **Large Language Models as Tool Makers** shows agents generating tools that other agents can use, expanding the action space without modifying the base model <d-cite key="latm2023"></d-cite>.
- **AlphaEvolve** generalizes this idea to scientific and algorithmic discovery, where generated programs become candidates in an iterative search loop <d-cite key="alphaevolve2025"></d-cite>.
- **Recursive Language Models** blur Level 2 and Level 3 by using recursive subcalls over context snippets as a control strategy for manipulating external context <d-cite key="rlm2025"></d-cite>.

**Mechanism:** turn the live trace into executable control state: scripts, temporary tools, diagnostic branches, repair loops, and subagent coordination plans.

**Caveat:** dynamic orchestration creates power and risk at the same time. The more the control layer can rewrite itself, the more the runtime needs isolation, provenance, cost bounds, and rollback.

</details>

<details class="appendix-cell" markdown="1">
<summary><span class="appendix-cell-title">Single Session / Level 1</span><span class="appendix-cell-subtitle">Test-Time Training and Fast Weights</span></summary>

This cell covers parametric or quasi-parametric adaptation during inference.

- **Learning to Discover at Test Time** explores updating model behavior on the exact problem instance rather than only searching longer with frozen weights <d-cite key="tttdiscover2026"></d-cite>.
- **In-Place Test-Time Training** studies direct updates to model parameters during inference, making deployment itself part of the learning loop <d-cite key="inplacettt2026"></d-cite>.
- **TTT Layers** reinterpret sequence modeling as a learned test-time update process, where hidden states behave like expressive memory substrates <d-cite key="tttlayers2024"></d-cite>.
- **Linear Transformers Are Secretly Fast Weight Programmers** makes the fast-weight interpretation explicit: sequence history can write temporary associations into a memory matrix <d-cite key="linearfastweights2021"></d-cite>.
- **Transformers are RNNs** and **Mamba** show adjacent forms of recurrent state accumulation, making the boundary between context, state, and weights less clean than the standard frozen-transformer picture suggests <d-cite key="lineartransformersrnn2020,mamba2023"></d-cite>.

**Mechanism:** use the current problem instance to change the computation itself: gradient updates, learned hidden-state updates, fast-weight memory, or recurrent state accumulation.

**Caveat:** this is the most powerful and operationally expensive online adaptation cell. It demands tight evaluation because a useful local update can also create regressions.

</details>

<details class="appendix-cell" markdown="1">
<summary><span class="appendix-cell-title">Across Sessions / Level 3</span><span class="appendix-cell-subtitle">Persistent Skills and User Memory</span></summary>

This cell covers state that survives across sessions for one user, project, codebase, or environment.

- **Voyager** accumulates executable Minecraft skills and retrieves them for future tasks, giving a clear early example of skill-library growth <d-cite key="voyager2023"></d-cite>.
- **Anthropic Agent Skills** package reusable procedures into discoverable folders that an agent can load when relevant <d-cite key="anthropicagentskills2026"></d-cite>.
- **OpenHands Skills and Context** supports persistent skill installation, enabling skills to be managed, enabled, disabled, and reused across sessions <d-cite key="openhandskills2026"></d-cite>.
- **Memento-Skills** pushes the same idea toward agents that design and improve agent skills themselves <d-cite key="mementoskills2026"></d-cite>.
- **Hermes Agent** sits in the same product/research direction: persistent agent capability surfaces that can be reused across tasks <d-cite key="hermesagent2026"></d-cite>.

**Mechanism:** convert repeated discoveries into durable artifacts: scripts, commands, wrappers, procedures, project conventions, and environment-specific recipes.

**Caveat:** persistent skills need lifecycle management. Stale skills can be worse than no skills, especially when project dependencies, APIs, or security constraints change.

</details>

<details class="appendix-cell" markdown="1">
<summary><span class="appendix-cell-title">Across Sessions / Level 2</span><span class="appendix-cell-subtitle">Meta-Programming and Workflow Optimization</span></summary>

This cell covers changes to the user's or project's recurring execution graph.

- **DSPy** treats language-model programs as optimizable graphs rather than hand-written prompts <d-cite key="dspy2023"></d-cite>.
- **MIPRO** optimizes instructions and demonstrations for multi-stage language-model programs <d-cite key="mipro2024"></d-cite>.
- **AgentOptimizer** uses agentic improvement loops to train or refine LLM agents <d-cite key="agentoptimizer2023"></d-cite>.
- **Agentic Context Engineering (ACE)** studies evolving context for self-improving language models, moving context design from manual prompt craft toward an updateable system component <d-cite key="ace2025"></d-cite>.

**Mechanism:** mine historical trajectories, identify high-performing execution patterns, and compile them into reusable prompts, routers, DAGs, tool schemas, and workflows.

**Caveat:** harness optimization can overfit to yesterday's tasks. Good systems need evaluation sets that represent the future operating distribution, not just the past transcript.

</details>

<details class="appendix-cell" markdown="1">
<summary><span class="appendix-cell-title">Across Sessions / Level 1</span><span class="appendix-cell-subtitle">Personal Adapters and Preference Alignment</span></summary>

This cell covers parametric personalization over repeated interactions with one user or organization.

- **OPPU** explores democratized personalized parameter-efficient fine-tuning <d-cite key="oppu2024"></d-cite>.
- **Profile-to-PEFT** uses profile-derived signals to produce fast personalized adaptation <d-cite key="profiletopeft2025"></d-cite>.
- **PERSOMA** studies personalized soft-prompt adapters for personalized language prompting <d-cite key="persoma2024"></d-cite>.

**Mechanism:** compress stable preferences into adapters, soft prompts, LoRA-style modules, or other parameter-efficient personalization layers.

**Caveat:** personalization must separate durable preference from accidental context. A user accepting one terse answer should not permanently train the model to be terse in every domain.

</details>

<details class="appendix-cell" markdown="1">
<summary><span class="appendix-cell-title">Across Users / Level 3</span><span class="appendix-cell-subtitle">Collective Knowledge Graphs and Shared Skills</span></summary>

This cell covers external assets created from many users, agents, tasks, or environments.

- **FunSearch** shows a collective program-search loop in which generated programs are evaluated, selected, and reused for further discovery <d-cite key="funsearch2023"></d-cite>.
- **Agent KB** studies how cross-domain experience can be reused for agentic problem solving <d-cite key="agentkb2025"></d-cite>.
- **ReasoningBank** collects reasoning memories to scale agent self-evolution <d-cite key="reasoningbank2025"></d-cite>.
- **Alita-G** explores self-evolving generative agents for agent generation, making agent-building artifacts themselves part of the evolving substrate <d-cite key="alitag2025"></d-cite>.
- **LlamaHub** and **Composio** represent practical infrastructure for shared tools and integrations <d-cite key="llamahub2024,composio2026"></d-cite>.

**Mechanism:** validate and promote local discoveries into shared assets: tools, integrations, reasoning traces, API wrappers, benchmark solutions, and capability graphs.

**Caveat:** the trust problem dominates this cell. A global skill bank without provenance, sandboxing, and eval gates can become a supply-chain vulnerability or a hallucination amplifier.

</details>

<details class="appendix-cell" markdown="1">
<summary><span class="appendix-cell-title">Across Users / Level 2</span><span class="appendix-cell-subtitle">Automated Harness Design</span></summary>

This cell covers population-level improvement to the default agent process itself.

- **ADAS** uses search over agentic system designs to discover stronger control flows <d-cite key="adas2024"></d-cite>.
- **Darwin Godel Machine** explores open-ended evolution of self-improving coding agents <d-cite key="dgm2025"></d-cite>.
- **Hyperagents** make the meta-level improvement procedure itself editable, so the system searches not only for better agents but for better ways to generate better agents <d-cite key="hyperagents2026"></d-cite>.

**Mechanism:** mine aggregate failure logs, identify structural bottlenecks in prompts/tools/workflows, and use meta-agents to propose, test, and deploy better harnesses.

**Caveat:** harness updates are product updates. They require regression testing, rollout controls, and auditability because one bad default policy can affect every downstream user.

</details>

<details class="appendix-cell" markdown="1">
<summary><span class="appendix-cell-title">Across Users / Level 1</span><span class="appendix-cell-subtitle">Continual RL and Checkpoint Evolution</span></summary>

This cell covers model updates derived from population-scale interaction data.

- **Cursor Tab online RL** turns natural developer behavior - accepting, rejecting, or editing autocomplete suggestions - into reward signals for improving the autocomplete model <d-cite key="cursortabrl2025"></d-cite>.
- Chat-style products provide adjacent feedback channels: thumbs-up/down, regenerations, follow-up corrections, conversation abandonment, and accepted edits. These are not all equally clean rewards, but together they form a data flywheel for future alignment and checkpoint updates.
- Academic and industrial continual-learning loops increasingly treat deployed interaction as the environment rather than a post-hoc evaluation set.

**Mechanism:** aggregate implicit and explicit feedback into preference data, reward models, reinforcement-learning updates, supervised fine-tuning corpora, and future checkpoint releases.

**Caveat:** this is usually not fully autonomous self-evolution today. Humans still shape reward design, filter data, approve deployments, and evaluate regressions. The self-evolving part is the data flywheel; the governance layer remains human-heavy.

</details>
