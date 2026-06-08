---
layout: distill
title: "The What & When of Self-Evolving Agents"
description: "Working in progress: a 3x3 framework for understanding self-evolving agents across files, harnesses, and weights."
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

toc:
  - name: "The Dual Promise"
  - name: "What Evolves"
  - name: "Learning From Experience"
  - name: "The 3x3 Evolution Matrix"
  - name: "Single Session: Online Adaptation"
  - name: "Across Sessions: Longitudinal Alignment"
  - name: "Across Users: Population-Level Evolution"
  - name: "When Experience Moves Inward"
  - name: "Open Questions"
---

> **Working in progress.** This is an English draft framework. I am still refining the taxonomy, examples, and references.

## The Dual Promise

**The era of static AI agents is ending.**

The old baseline, anchored in static prompts and rigid orchestration, treated agents as fixed products that peaked at deployment. That approach has hit a wall: it is too expensive to operate, and too brittle to scale. We are now witnessing a fundamental shift toward dynamic, **self-evolving systems**.

True intelligence should not peak at deployment only to depreciate. It must appreciate. Every interaction should create pressure for the system to adapt. This paradigm shift is driven by a dual promise:

- **Motivation 1: Marginal Cost Reduction (Shrinking Costs).** Operationally, this means fewer prompt tokens, fewer tool calls, fewer retries, and less human intervention per solved task family. By compressing experience into reusable assets, the system stops paying for the same mistake twice.

- **Motivation 2: Capability Ceiling Expansion (Breaking Ceilings).** Evolution should unlock zero-day or out-of-distribution tasks that the system could not handle on day one. The agent learns to forge ad-hoc tools and strategies at runtime, making autonomy a hard systems claim rather than a behavioral illusion.

Leading systems are already shifting from prompt-only baselines to updatable execution substrates. We see this across the entire stack: from ChatGPT's background state synthesis <d-cite key="openai2026dreaming"></d-cite> and Claude's dynamic runtime skills <d-cite key="anthropicagentskills2026"></d-cite><d-cite key="anthropicdynamicworkflows2026"></d-cite>, to open-source and research architectures like OpenHands <d-cite key="openhandskills2026"></d-cite> and OpenClaw-RL <d-cite key="openclawrl2026"></d-cite>.

These systems prove that agents must internalize their experience. But "learning" is not magic; it requires a physical substrate. To genuinely reduce costs and break capability ceilings, we must understand the architecture of this adaptation.

The central question is simple: **Where exactly does this evolution happen?**

Recent surveys on self-evolving agents organize the field around what evolves, when it evolves, and how it evolves <d-cite key="selfevolvingsurvey2025"></d-cite>. The 3x3 matrix below is a systems-oriented version of the same instinct: it asks which physical layer is updated, and over what lifetime the update persists.

## What Evolves

Before discussing how an agent evolves, we need to define what an agent physically is. In practice, an agent's cognitive state is distributed across three plastic layers.

### Level 1: Model Weights

The first layer is the parametric core: foundation-model weights and lightweight adapters such as LoRA modules.

This layer stores implicit knowledge. It is updated through gradient-based learning, and its updates are expensive. Weight evolution can generalize broadly across tasks, but it also carries risks such as catastrophic forgetting, regression on existing capabilities, and costly evaluation requirements.

In other words, this layer determines the agent's instincts.

### Level 2: Agent Harness

The second layer is the agent harness: orchestration logic, workflow graphs, control flow, tool invocation runtime, recovery loops, meta-prompts, and routing policies.

This layer determines how the agent thinks and acts. It can evolve without changing model tensors. A system can rewrite prompts, optimize tool-selection logic, compile repeated workflows into deterministic subroutines, add new execution nodes, or change how it recovers from errors.

In modern coding agents, this layer includes the invisible machinery behind repeated plan-act-observe loops, terminal recovery, code editing, test execution, delegation, and runtime workflow execution. Claude Code's Dynamic Workflows are a clean recent example: the plan is no longer only a sequence of turns in the context window; it becomes a script that a separate runtime executes, while intermediate results live in script variables and subagent state <d-cite key="anthropicdynamicworkflows2026"></d-cite>.

### Level 3: External Files

The third layer is the external state: executable skill libraries, memory stores, knowledge graphs, notebooks, scratchpads, user profiles, and persistent artifacts.

This is the agent's dynamic external brain. It is not just early-stage document RAG. The most useful external memory is structured, editable, callable, and inspectable. It can store exact code, exact errors, exact user preferences, exact intermediate discoveries, and exact reusable procedures.

Evolution at this layer is cheap. It is mostly CRUD: create, read, update, delete. It also has perfect fidelity relative to model memory: a saved function, file, or note does not blur into a distribution unless the agent later summarizes it badly.

### The Blurry Boundary Between Harness and Files

The boundary between Level 2 and Level 3 is increasingly unstable.

Suppose an agent writes a Python function into a skill library. At first, that function is just an external file. But if the runtime later loads it and routes future tasks through it, the file has modified the agent's workflow. Data has become control logic.

This "code as data" property is one of the most important mechanisms in advanced self-evolving agents. External memory does not merely store facts. It can store new operators.

This is already visible in deployed agent systems. Anthropic's Agent Skills framework packages instructions, scripts, templates, and metadata inside discoverable folders <d-cite key="anthropicagentskills2026"></d-cite>. OpenHands exposes a similar skills architecture for loading reusable agent context and capability modules <d-cite key="openhandskills2026"></d-cite>. Memento-Skills turns structured markdown skills into persistent, retrievable, and evolvable agent memory <d-cite key="mementoskills2026"></d-cite>. Claude Code Dynamic Workflows show the mirror image from the harness side: runtime scripts can hold the orchestration that used to live in the model's context window <d-cite key="anthropicdynamicworkflows2026"></d-cite>. In all of these cases, external files and runtime code are no longer passive storage. They are executable capability substrates.

## Learning From Experience

At its core, self-evolution reduces to a single imperative: **learning from experience**.

Every deployed agent generates an exhaust of experience: successful trajectories, tool errors, rejected actions, and user corrections. A static agent flushes this signal the moment a task ends. A self-evolving agent captures it, routes it, and hardens it into reusable state.

This forms the **experience feedback loop**. The guiding principle for this loop is a simple cost-efficiency gradient: **internalize experience at the cheapest physical layer that prevents the error from repeating.**

To map this out, we project the three physical layers against three time scales of adaptation:

- **Single Session:** Online adaptation inside one active trajectory.
- **Across Sessions:** Longitudinal adaptation to a specific user, project, or codebase.
- **Across Users:** Population-level evolution derived from aggregate interactions.

## The 3x3 Evolution Matrix

| Time scale | Level 3: External files | Level 2: Agent harness | Level 1: Model weights |
| --- | --- | --- | --- |
| **Single session** | Working memory, scratchpads, context paging, temporary tools | Dynamic orchestration, runtime rewrites, ad-hoc tool mounting | Test-time training, fast weights, problem-specific online updates |
| **Across sessions** | Persistent skill libraries, user memory, project graphs | Prompt compilation, workflow specialization, optimized DAGs | Personal adapters, continuous fine-tuning, preference alignment |
| **Across users** | Global skill libraries, shared tool ecosystems | Collective pipeline optimization, default harness upgrades | Continual learning, RL from real interactions, model checkpoint updates |

This matrix is not meant to be a rigid classification. In real systems, the cells interact. A temporary tool created in a single session can become a persistent skill across sessions. A project-specific workflow can become a product default. A pattern discovered in millions of users' failures can eventually become a model checkpoint.

Some systems deliberately blur the cells. Recursive Language Models, for example, treat long prompts as an external environment and recursively call sub-LLMs over snippets, making them a Level 2 control strategy that manipulates Level 3 context <d-cite key="rlm2025"></d-cite>.

## Single Session: Online Adaptation

The first time scale is intra-trajectory. How does an agent use a live execution trace to correct itself on the fly?

### Level 3: Working Memory and Context Paging

Inside a single session, external memory fights context degradation. Long reasoning traces pile up. Tool outputs introduce noise. This is the agentic version of the "lost in the middle" problem: even if the context window is technically large enough, the signal-to-noise ratio inevitably deteriorates <d-cite key="liu2023lostmiddle"></d-cite>.

The solution is OS-style context management. MemGPT frames this as virtual memory paging across storage tiers <d-cite key="memgpt2023"></d-cite>. MEMENTO dynamically segments reasoning into blocks, compressing and evicting intermediate steps from active context so the model reasons forward over structured summaries <d-cite key="memento2026"></d-cite>. *Memory-as-Action* pushes this further, turning memory editing from a hardcoded heuristic into a learnable policy <d-cite key="memoryasaction2025"></d-cite>.

**The caveat:** Adding a database is not automatically evolution. Lossy retrieval and compression can quietly inject causal drift into the reasoning chain <d-cite key="amabench2026"></d-cite>. Ephemeral memory only counts as evolution if it strictly improves the efficiency frontier, rather than just shifting the bottleneck from context length to retrieval noise.

### Level 2: Dynamic Orchestration

At the harness layer, the agent rewires its execution plan at runtime.

A static workflow dictates: *Call Tool A $\rightarrow$ Call Tool B $\rightarrow$ Summarize*.

A dynamic workflow adapts: *Tool A failed twice $\rightarrow$ inject a diagnostic node; the API wrapper is missing $\rightarrow$ synthesize a temporary function and mount it into the execution DAG.*

Claude Code's Dynamic Workflows make this literal. Claude writes a JavaScript orchestration script for the task, and a separate runtime executes it in the background across many subagents. The plan leaves the conversation and becomes executable control state: loops, branches, fan-out, intermediate variables, resumability, and cross-checking patterns live in the workflow runtime instead of being carried turn by turn inside Claude's context window. The `ultracode` setting pushes this further by letting Claude decide when a substantive task warrants a workflow <d-cite key="anthropicdynamicworkflows2026"></d-cite>.

This requires treating next-state observations - tool outputs, terminal errors, GUI changes, user replies - as immediate directional supervision <d-cite key="openclawrl2026"></d-cite>. We see the same mechanism in ad-hoc tool creation, where agents generate, test, and mount code variants on the fly <d-cite key="latm2023,alphaevolve2025"></d-cite>. The generated script might be temporary, but for that specific session, the agent has fundamentally expanded its own action space.

### Level 1: Test-Time Training (TTT)

The most aggressive form of single-session adaptation modifies weights during inference.

Test-time training destroys the clean boundary between training and deployment. Instead of merely using a frozen model to search longer, the system updates a subset of parameters using the exact problem at hand <d-cite key="tttdiscover2026"></d-cite>.

Whether adapting fast weights in-place <d-cite key="inplacettt2026"></d-cite> or applying a learned update rule to hidden states <d-cite key="tttlayers2024"></d-cite>, TTT is the upper edge of self-evolution.

It is computationally brutal and operationally complex. But the payoff is profound: the agent does not just remember a discovery. It alters the underlying machinery that generates discoveries.

### A Note on Context and Weights

The boundary between Level 3 context and Level 1 weights is mathematically porous. When an agent writes to an external scratchpad, that file is still just a file. But the moment the scratchpad is loaded back into active context, the inference engine physically materializes it as dynamic tensors in the **KV cache**. In standard self-attention, $\text{Attention}(Q, K, V) = \text{softmax}(QK^T / \sqrt{d_k})V$; adding experience to the context means appending new key and value vectors to the computation <d-cite key="vaswani2017attention"></d-cite>.

In linear attention, this boundary becomes even more explicit: the history can be accumulated into a recurrent state, revealing the connection between Transformers and RNNs <d-cite key="lineartransformersrnn2020"></d-cite>. Linearized attention can also be interpreted as a fast-weight program, where the sequence dynamically writes key-value associations into a temporary memory matrix <d-cite key="linearfastweights2021"></d-cite>. State-space models such as Mamba push the same intuition further by collapsing sequence history into a selective recurrent state <d-cite key="mamba2023"></d-cite>.

At runtime, memory is not merely a database. Once it enters the active inference path, it becomes a transient parameter.

## Across Sessions: Longitudinal Alignment

The second time scale is inter-session. How does an agent internalize the structural patterns of a specific user, project, or operating environment over days and weeks?

### Level 3: Executable Skills and Persistent Memory

The most practical inter-session mechanism is caching executable behaviors.

Voyager pioneered this by accumulating an ever-growing library of executable skills in Minecraft, storing complex routines as code to be retrieved later <d-cite key="voyager2023"></d-cite>. Modern memory-first systems extend this beyond game environments. Memento-Skills, for instance, turns reusable capabilities into structured, evolvable markdown assets <d-cite key="mementoskills2026"></d-cite>.

For a personal coding agent, this means saving an arcane project test command, storing a verified API wrapper, or locking in a strict migration recipe. The system transitions from semantic search to asset reuse. The agent simply stops paying the inference tax of rediscovering the exact same solution.

### Level 2: Meta-Programming and Pipeline Optimization

When an agent repeatedly solves the same class of problems, it shouldn't reconstruct its execution plan from scratch. High-performing historical trajectories must be mined to optimize the harness itself.

This is the domain of meta-programming. Frameworks like DSPy <d-cite key="dspy2023"></d-cite> and MIPRO <d-cite key="mipro2024"></d-cite> treat LLM programs as optimizable computational graphs, tuning few-shot demonstrations and routing rules against an evaluation metric. AgentOptimizer <d-cite key="agentoptimizer2023"></d-cite> and ACE <d-cite key="ace2025"></d-cite> push this further by structurally revising functions and playbooks based on user satisfaction signals.

The mechanism here is structural: a bloated, verbose explicit context collapses into a lean, project-specific DAG (Directed Acyclic Graph).

### Level 1: Personal Adapters and Alignment

At the parametric layer, inter-session evolution becomes personalized alignment.

The system extracts implicit preferences - coding style, API choices, verbosity tolerance, and safety boundaries - from repeated interactions and drives them into parameter-efficient adapters. Architectures like OPPU <d-cite key="oppu2024"></d-cite>, Profile-to-PEFT <d-cite key="profiletopeft2025"></d-cite>, and PERSOMA <d-cite key="persoma2024"></d-cite> demonstrate how historical trajectories can be compressed into user-specific parametric priors.

If a preference becomes parametric, the model no longer needs to be explicitly prompted; it becomes instinct. However, the true engineering bottleneck here is governance. Personal fine-tuning demands rigorous evaluation, privacy firewalls, and rollback mechanisms to prevent the agent from fatally overfitting to yesterday's accidental typo.

## Across Users: Population-Level Evolution

The third time scale is population-level. How does a system aggregate millions of isolated trajectories, failures, and human corrections to conquer the long tail of edge cases?

### Level 3: Collective Knowledge Graphs and Shared Skills

At the file layer, population-level evolution manifests as a shared ecosystem of capabilities and knowledge.

When an agent successfully navigates an undocumented API, decrypts a complex configuration, or maps an obscure domain, that discovery should not remain isolated. It is validated and merged into a collective knowledge graph or a global skill library. Systems like Agent KB <d-cite key="agentkb2025"></d-cite>, ReasoningBank <d-cite key="reasoningbank2025"></d-cite>, and Alita-G <d-cite key="alitag2025"></d-cite> synthesize these reusable tools and strategies from the successful trajectories of heterogeneous agents.

This is the ultimate strategy for attacking out-of-distribution tasks: **crowdsourcing both executable tools and structured world knowledge.** The primary bottleneck is no longer generation, but trust. A global memory bank requires strict provenance and sandboxing to prevent it from becoming a reservoir for hallucinations or a vector for supply-chain vulnerabilities.

### Level 2: Collective Pipeline Optimization

At the harness layer, aggregate failure logs expose structural bottlenecks.

If ten thousand deployed agents fail in the exact same execution loop, the root cause is rarely the base model's capacity. It is usually a defect in the default system prompt, a brittle tool schema, or a malformed retry policy. By mining these population-level deadlocks, developers - or automated meta-agents - can refactor the default orchestration logic.

We see this frontier in automated harness design. Frameworks like ADAS <d-cite key="adas2024"></d-cite> and Darwin Godel Machine <d-cite key="dgm2025"></d-cite> use meta-agents to iteratively program and validate better agentic control flows. This allows the control layer to evolve aggressively, pushing product improvements without waiting for the next massive model checkpoint.

### Level 1: Continual Parametric Evolution

At the parametric layer, population-level evolution is continuous reinforcement learning.

Deployed systems generate an ocean of implicit supervision. Every user correction, rejected output, and accepted code edit is a high-fidelity reward signal. WildChat <d-cite key="wildchat2024"></d-cite> and WildFeedback <d-cite key="wildfeedback2024"></d-cite> demonstrate how in-situ feedback can be converted directly into alignment data, while RLHI <d-cite key="rlhi2025"></d-cite> learns from real-world conversational trajectories.

Cursor's online RL for autocomplete is the canonical product example: user-validated suggestions are converted into reward gradients to continuously update the policy <d-cite key="cursortabrl2025"></d-cite>. The endgame is clear: **human interaction is no longer just a source of training data. It is the direct catalyst for the next generation of model intelligence.**

## When Experience Moves Inward

The practical design question is not simply *whether* an agent should learn, but **where the learning should land.**

The physical layers form a strict cost-efficiency gradient. Weight updates are expensive and opaque; harness updates are powerful but risky; file updates are cheap and inspectable. This dictates a conservative lifecycle for promoting agentic experience:

1. **Incident to Asset (Level 3):** If an experience is rare, highly specific, or tied to a local environment, cache it externally as a skill or memory block.
2. **Asset to Workflow (Level 2):** If a cached pattern proves structural and procedural, promote it. Compile it into the orchestration graph as a new routing rule or recovery loop.
3. **Workflow to Weights (Level 1):** Only when a pattern is stable, broadly applicable, and privacy-safe should it be distilled into the parametric core.

This inward movement of experience yields the ultimate engineering heuristic for self-evolving systems:

> **Do not train what you can compile. Do not compile what you can cache. Do not cache what you can solve once and discard.**

## Open Questions

This framework is just the beginning. The transition from static interfaces to living, self-evolving systems exposes several unsolved frontiers:

- **Credit Assignment:** When a trajectory fails, which layer is at fault? Was it missing memory, a brittle tool schema, weak model capacity, or user ambiguity? Blaming the wrong layer creates toxic updates.

- **Evaluation:** How do we prove an evolution is a genuine upgrade rather than local overfitting? We need temporal and causal evaluation metrics, not just static benchmarks.

- **Safety and Rollback:** Self-modification requires strict version control. If a compiled DAG or personal adapter introduces a performance regression, the system must be able to cleanly roll back.

- **Contamination:** Memory poisoning, reward hacking, and tool supply-chain attacks are inherent risks when systems learn from deployment traces. Evolution demands rigorous quarantine, not just blind accumulation.

- **Privacy Boundaries:** Across-session and across-user learning require hard firewalls. A personal memory must never leak into a global skill; a global parametric update must never memorize a private trajectory.

Self-evolving agents are not defined by any single technique or paper. They are defined by a feedback loop: by a system's ability to mutate its own future behavior at the right layer, over the right time scale, with the right cost.
