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

> **Working in progress.**

## The Dual Promise

**The era of static AI agents is ending.**

True intelligence should not peak at deployment only to depreciate. It must appreciate. Every interaction should create pressure for the system to adapt. We are now witnessing a fundamental shift toward dynamic, **self-evolving systems**, driven by a dual promise:

- **Motivation 1: Marginal Cost Reduction (Shrinking Costs).** Operationally, this means fewer prompt tokens, fewer tool calls, fewer retries, and less human intervention per solved task family. By compressing experience into reusable assets, the system stops paying for the same mistake twice.

- **Motivation 2: Capability Ceiling Expansion (Breaking Ceilings).** Evolution should unlock zero-day tasks and enable robust **long-horizon execution**. Static agents inevitably fail at complex, multi-step goals due to compounding errors and context exhaustion. By learning to forge ad-hoc tools, cache intermediate progress, and adapt strategies at runtime, a self-evolving agent makes long-term autonomy a hard systems claim rather than a behavioral illusion.

Leading systems are already abandoning **stateless orchestration** in favor of updatable execution substrates. We see this transition across the stack: from the accumulation of **persistent skill libraries** in systems like OpenHands <d-cite key="openhandskills2026"></d-cite>, to Claude's ability to compile **dynamic runtime scripts** on the fly <d-cite key="anthropicdynamicworkflows2026"></d-cite>, and deep reinforcement learning loops in OpenClaw-RL <d-cite key="openclawrl2026"></d-cite>.

These systems prove that agents must internalize their experience. But "learning" is not magic; it requires a physical substrate. To genuinely reduce costs and break capability ceilings, we must understand the architecture of this adaptation.

The central question is simple: **Where exactly does this evolution happen?**

Recent surveys on self-evolving agents organize the field around what evolves, when it evolves, and how it evolves <d-cite key="selfevolvingsurvey2025"></d-cite>. The 3x3 matrix below is a systems-oriented version of the same instinct: it asks which physical layer is updated, and over what lifetime the update persists.

## What Evolves

Before discussing how an agent evolves, we need to define what an agent physically is. In practice, an agent's cognitive state is distributed across three plastic layers.

### Level 1: Model Weights

The first layer is the parametric core: the model weights.

This layer stores implicit knowledge. It is updated through gradient-based learning, which makes updates computationally expensive. While weight evolution can generalize broadly across tasks, it carries inherent risks such as catastrophic forgetting, regression on existing capabilities, and costly evaluation requirements.

### Level 2: Agent Harness

The second layer is the agent harness, which includes the orchestration logic, control flow, tool runtime, and error recovery loops.

This layer defines how the agent executes tasks and can evolve without changing model weights. A system can optimize tool-selection logic, compile repeated workflows into deterministic subroutines, or rewrite its system prompts.

In modern systems, this is the machinery driving the plan-act-observe loop. Claude Code's Dynamic Workflows provide a clean example: the execution plan is no longer just a sequence of text turns in the context window. Instead, it becomes an executable script managed by a separate runtime, handling intermediate variables and subagent states entirely outside the model <d-cite key="anthropicdynamicworkflows2026"></d-cite>.

### Level 3: External Files

The third layer is external state: persistent memory stores, skill libraries, knowledge graphs, and scratchpads.

Unlike traditional read-only RAG, modern external memory is structured, editable, and callable. It stores precise code snippets, error logs, user preferences, and reusable procedures.

Evolution at this layer is computationally cheap: primarily CRUD (create, read, update, delete) operations. It also offers high fidelity relative to parametric memory: a saved function or specific configuration remains exact, rather than blurring into a statistical distribution.

### The Blurry Boundary: Code as Data

The boundary between Level 2 (Harness) and Level 3 (Files) is increasingly porous.

When an agent writes a Python function into a skill library, it starts as an external file. But the moment the runtime loads that file to route future tasks, data becomes control logic. External memory no longer merely stores facts; it stores new operators.

This "code as data" property is a core mechanism in advanced self-evolving agents. Frameworks like Anthropic's Agent Skills <d-cite key="anthropicagentskills2026"></d-cite>, OpenHands <d-cite key="openhandskills2026"></d-cite>, and Memento-Skills <d-cite key="mementoskills2026"></d-cite> all package capabilities into discoverable folders or structured markdown. In these systems, external files are no longer passive storage; they are executable capability substrates.

## Learning From Experience

At its core, self-evolution reduces to a single imperative: **learning from experience**.

Every deployed agent leaves behind experience exhaust: successful trajectories, tool errors, rejected actions, and user corrections. A static agent flushes this signal the moment a task ends. A self-evolving agent captures that signal and hardens it into reusable state.

To map how this feedback loop operates, we project the three structural layers against three time scales of adaptation:

- **Single Session:** Online adaptation inside one active trajectory.
- **Across Sessions:** Longitudinal adaptation to a specific user, project, or codebase.
- **Across Users:** Population-level evolution derived from aggregate interactions.

## The 3x3 Evolution Matrix

| Time scale | Level 3: External state (Files/Memory) | Level 2: Agent harness (Control/Logic) | Level 1: Model weights (Parametric) |
| --- | --- | --- | --- |
| **Single session**<br><br>*Online* | Working memory, active scratchpads, context paging | Dynamic orchestration, runtime rewrites, ad-hoc tool mounting | Test-time training, fast weights, in-place updates |
| **Across sessions**<br><br>*Longitudinal* | Persistent skill libraries, user memory, executable assets | Meta-programming, workflow optimization, specialized DAGs | Personal adapters, continuous fine-tuning, preference alignment |
| **Across users**<br><br>*Population* | Collective knowledge graphs, shared global skills | Collective pipeline optimization, automated harness design | Continual RL, learning from interaction, checkpoint updates |

This matrix is not meant to be a rigid classification. In real systems, the cells interact. A temporary tool created in a single session can become a persistent skill across sessions. A project-specific workflow can become a product default. A pattern discovered in millions of users' failures can eventually become a model checkpoint.

Some systems deliberately blur the cells. Recursive Language Models, for example, treat long prompts as an external environment and recursively call sub-LLMs over snippets, making them a Level 2 control strategy that manipulates Level 3 context <d-cite key="rlm2025"></d-cite>.

## Single Session: Online Adaptation

The first time scale is intra-trajectory. How does an agent use a live execution trace to correct itself on the fly?

### Level 3: Working Memory and Context Paging

Inside a single session, external memory fights context degradation. Long reasoning traces pile up. Tool outputs introduce noise. This is the agentic version of the "lost in the middle" problem: even if the context window is technically large enough, the signal-to-noise ratio inevitably deteriorates <d-cite key="liu2023lostmiddle"></d-cite>.

The solution is OS-style context management. MemGPT frames this as virtual memory paging across storage tiers <d-cite key="memgpt2023"></d-cite>. MEMENTO dynamically segments reasoning into blocks, compressing and evicting intermediate steps from active context so the model reasons forward over structured summaries <d-cite key="memento2026"></d-cite>. *Memory-as-Action* pushes this further, turning memory editing from a hardcoded heuristic into a learnable policy <d-cite key="memoryasaction2025"></d-cite>.

**The caveat: Storage is not evolution.** Simply dumping context into an external database is meaningless if lossy retrieval quietly injects causal drift into the reasoning chain <d-cite key="amabench2026"></d-cite>. Ephemeral memory only qualifies as evolution if it strictly improves the efficiency frontier, rather than just shifting the system's bottleneck from context length to retrieval noise.

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

Voyager pioneered this by accumulating an ever-growing library of executable skills in Minecraft, storing complex routines as code to be retrieved later <d-cite key="voyager2023"></d-cite>. Today, modern open-source ecosystems have brought this directly into real-world software engineering. Frameworks like OpenHands <d-cite key="openhandskills2026"></d-cite>, agent systems like Hermes Agent <d-cite key="hermesagent2026"></d-cite>, and memory-first methods like Memento-Skills <d-cite key="mementoskills2026"></d-cite> all support persistent, evolvable skill libraries across user sessions.

For a personal coding agent, this means saving an arcane project test command, storing a verified API wrapper, or locking in a strict migration recipe. The system transitions from semantic search to asset reuse. The agent simply stops paying the inference tax of rediscovering the exact same solution.

### Level 2: Meta-Programming and Pipeline Optimization

When an agent repeatedly solves the same class of problems, it shouldn't reconstruct its execution plan from scratch. High-performing historical trajectories must be mined to optimize the harness itself.

This is the domain of meta-programming. Frameworks like DSPy <d-cite key="dspy2023"></d-cite> and MIPRO <d-cite key="mipro2024"></d-cite> treat LLM programs as optimizable computational graphs, tuning few-shot demonstrations and routing rules against an evaluation metric. AgentOptimizer <d-cite key="agentoptimizer2023"></d-cite> and ACE <d-cite key="ace2025"></d-cite> push this further by structurally revising functions and playbooks based on user satisfaction signals.

The mechanism here is structural: a bloated, verbose explicit context collapses into a lean, project-specific DAG (Directed Acyclic Graph).

### Level 1: Personal Adapters and Alignment

At the parametric layer, inter-session evolution becomes personalized alignment.

The system extracts implicit preferences - coding style, API choices, verbosity tolerance, and problem-solving habits - from repeated interactions and drives them into parameter-efficient adapters. Architectures like OPPU <d-cite key="oppu2024"></d-cite>, Profile-to-PEFT <d-cite key="profiletopeft2025"></d-cite>, and PERSOMA <d-cite key="persoma2024"></d-cite> demonstrate how historical trajectories can be compressed into user-specific parametric priors.

If a preference becomes parametric, the model no longer needs to be explicitly prompted; it becomes instinct. This is one structural prerequisite for true **Personal AGI**. A static foundation model is inherently a generic, one-size-fits-all reasoner. Cross-session adapter updates let the agent specialize toward a user's recurring workflows and problem-solving habits. It ceases to just solve problems; it learns to solve them *your way*.

## Across Users: Population-Level Evolution

The third time scale is population-level. How does a system aggregate millions of isolated trajectories, failures, and human corrections to conquer the long tail of edge cases?

### Level 3: Collective Knowledge Graphs and Shared Skills

At the file layer, population-level evolution manifests as a shared ecosystem of capabilities and knowledge.

Consider how the human scientific community tackles an open problem. No single researcher derives every result from base axioms; one group proves an intermediate lemma, publishes it, and that lemma becomes a trusted tool for the next group to build upon.

Self-evolving agents must replicate this dynamic, a pattern already visible in hybrid human-AI discovery. FunSearch, for example, used LLM-guided program search to produce new constructions for the cap set problem and interpretable programs that researchers could inspect and build on <d-cite key="funsearch2023"></d-cite>. In the agent setting, whether a system resolves a rare dependency conflict, writes a novel API wrapper, or discovers a reusable subroutine, that breakthrough should not remain isolated. It should be validated and merged into a global capability registry.

We are seeing primitive stages of this in open-source tool ecosystems like LlamaHub <d-cite key="llamahub2024"></d-cite> and Composio <d-cite key="composio2026"></d-cite>, alongside research frameworks like Agent KB <d-cite key="agentkb2025"></d-cite>, ReasoningBank <d-cite key="reasoningbank2025"></d-cite>, and Alita-G <d-cite key="alitag2025"></d-cite>, which synthesize reusable tools and strategies from successful trajectories of heterogeneous agents.

This transforms isolated AI systems into a **collective intelligence** with a real network effect. If one agent discovers a robust workaround, that executable knowledge can be propagated to the broader ecosystem. Evolution is no longer constrained by a single session's context window; it compounds horizontally, mirroring the collaborative accumulation of human knowledge. The primary bottleneck becomes trust: a global memory bank requires strict provenance and sandboxing to avoid becoming a reservoir for hallucinations or a vector for supply-chain vulnerabilities.

### Level 2: Collective Pipeline Optimization

At the harness layer, aggregate failure logs expose structural bottlenecks.

If ten thousand deployed agents fail in the exact same execution loop, the root cause is rarely the base model's capacity. It is usually a defect in the default system prompt, a brittle tool schema, or a malformed retry policy. By mining these population-level deadlocks, developers - or automated meta-agents - can refactor the default orchestration logic.

We see this frontier in automated harness design. Frameworks like ADAS <d-cite key="adas2024"></d-cite> and Darwin Godel Machine <d-cite key="dgm2025"></d-cite> use meta-agents to iteratively program and validate better agentic control flows. Hyperagents push this further by making the meta-level modification procedure itself editable: the system no longer only searches for better agents, but also rewrites the process that generates future improvements <d-cite key="hyperagents2026"></d-cite>. This allows the control layer to evolve aggressively, pushing product improvements without waiting for the next massive model checkpoint.

### Level 1: Continual Parametric Evolution

At the parametric layer, population-level evolution is continuous reinforcement learning.

Strictly speaking, the agent does not evolve independently of humans; rather, **it treats the human population as its environment**. Deployed systems generate an ocean of implicit supervision. Every user correction, rejected output, and accepted code edit acts as a high-fidelity reward signal.

This is the open secret of frontier AI labs. Long before academic benchmarks attempted to simulate this loop, products like ChatGPT were already functioning as data flywheels: converting thumbs-ups, regenerations, and follow-up corrections into preference signals for subsequent alignment runs.

Today, this mechanism is moving from explicit feedback buttons to implicit behavioral RL. Cursor's online RL for autocomplete is the canonical product example: when a user accepts a suggestion or manually edits it away, that natural human action is converted into an automated reward signal to continuously update the model's policy <d-cite key="cursortabrl2025"></d-cite>.

The paradigm shift is structural: human interaction is no longer an external evaluation step or a costly offline data-labeling process. It becomes the automated catalyst for continuous model improvement.

**A Note on Autonomy:** Today, population-level evolution is rarely fully autonomous. At this scale, agents act as prolific *proposers* of new tools and workflows, while humans still act as *maintainers* who verify and merge them. However, this is a current engineering bottleneck, not a permanent ceiling. As automated sandboxing and AI-driven evaluation mature, this verification loop will close, paving the way for truly autonomous, population-scale self-evolution.

## Conclusion: Escaping the Human Bottleneck

Structuring self-evolution around single sessions, user preferences, and human populations is a practical way to build systems today. But this anthropocentric framing is ultimately transitional. We are currently measuring an AI's evolution by how well it adapts to *us*: our coding habits, our prompts, and our manual corrections.

As we look toward Artificial General Intelligence (AGI) and eventually ASI, the fundamental nature of experience will shift.

Today, human interaction is the primary environment that forces an agent to adapt. But the true inflection point arrives when the human is removed from the critical loop. The ultimate driver of evolution will not be human feedback, but **algorithmic self-play and open-ended exploration**.

Imagine a network of autonomous agents deployed to tackle an unsolved physics problem or design a next-generation operating system. They generate synthetic hypotheses, build their own sandbox environments to test them, and distribute successful discoveries - whether as executable tools (Level 3), optimized reasoning pathways (Level 2), or weight updates (Level 1) - across a global collective intelligence.

Their experience compounds at the speed of compute, decoupled from the biological limits of human typing speed or comprehension. By architecting systems capable of modifying their own external files, cognitive harnesses, and parametric cores, we are no longer just engineering smarter Copilots. We are laying the structural foundation for an intelligence that can finally evolve itself.
