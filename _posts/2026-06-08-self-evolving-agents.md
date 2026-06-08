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
      - name: UWCSE
      - name: PhyloBio
  - name: Tong Chen
    url: "https://scholar.google.com/citations?user=fOcXofAAAAAJ&hl=en"
    affiliations:
      - name: UW CSE

bibliography: 2026-06-08-self-evolving-agents.bib

toc:
  - name: "The Dual Promise"
  - name: "What Evolves"
  - name: "Learning From Experience"
  - name: "The 3x3 Evolution Matrix"
  - name: "Single Session: Online Adaptation"
  - name: "Across Sessions: Longitudinal Alignment"
  - name: "Across Users"
  - name: "When Experience Moves Inward"
  - name: "Why This Matters"
  - name: "Open Questions"
---

> **Working in progress.** This is an English draft framework. I am still refining the taxonomy, examples, and references.

## The Dual Promise

**The era of static AI agents is ending.**

The old baseline, anchored in static prompts and rigid orchestration, treated agents as fixed products that peaked at deployment. That approach has hit a wall: it is too expensive to operate, and too brittle to scale. We are now witnessing a fundamental shift toward dynamic, **self-evolving systems**.

True intelligence should not peak at deployment only to depreciate. It must appreciate. Every interaction should create pressure for the system to adapt. This paradigm shift is driven by a dual promise:

- **Motivation 1: Marginal Cost Reduction (Shrinking Costs).** Operationally, this means fewer prompt tokens, fewer tool calls, fewer retries, and less human intervention per solved task family. By compressing experience into reusable assets, the system stops paying for the same mistake twice.

- **Motivation 2: Capability Ceiling Expansion (Breaking Ceilings).** Evolution should unlock zero-day or out-of-distribution tasks that the system could not handle on day one. The agent learns to forge ad-hoc tools and strategies at runtime, making autonomy a hard systems claim rather than a behavioral illusion.

The industry is already transitioning to updateable execution substrates. OpenAI's ChatGPT memory stack now uses background "dreaming" processes to synthesize useful memory state <d-cite key="openai2026dreaming"></d-cite>; Anthropic's Agent Skills package instructions, scripts, and resources into discoverable folders that Claude can load on demand <d-cite key="anthropicagentskills2026"></d-cite>; Claude Code's new Dynamic Workflows move orchestration into runtime-executed JavaScript scripts, with `ultracode` letting Claude decide when to launch those workflows <d-cite key="anthropicdynamicworkflows2026"></d-cite>; open-source coding-agent runtimes such as OpenHands expose reusable skills and runtime context modules <d-cite key="openhandskills2026"></d-cite>; and OpenClaw-RL treats user replies, tool outputs, terminal states, and GUI changes as online learning signals <d-cite key="openclawrl2026"></d-cite>.

But merely bolting a database onto an agent is not evolution. A saved preference, project context, skill folder, patched system prompt, or rewritten tool route only matters if it prevents context bloat, redundant retrieval, extra tool calls, repeated retries, or human correction. If experience lands at the wrong layer, the agent may memorize facts without acquiring better procedures. It may retrieve a past trace without improving routing. It may add a tool without learning when to use it.

Therefore, the frontier question is not **"Does the agent have memory?"** but **"At which physical layer does experience harden into state?"**

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

## Across Users

The third time scale is population-level evolution. Here, the system learns from many users' trajectories, failures, and feedback.

### Level 3: Global Skill Libraries

At the file layer, population-level evolution looks like a shared tool ecosystem.

If one agent discovers a reliable way to call a new API, parse a tricky file format, configure a benchmark, or recover from a known error, that artifact can be validated and added to a global skill library. Other agents can retrieve it instead of rediscovering it.

This is the lowest-cost way to attack long-tail tasks. The system does not need to update the base model every time the world changes. It can add a tool, a recipe, a patch, or a verified snippet.

This cell now has strong research anchors. Agent KB builds a shared cross-framework experience base for heterogeneous agents <d-cite key="agentkb2025"></d-cite>. ReasoningBank distills generalizable reasoning strategies from both successful and failed experiences into a shared memory <d-cite key="reasoningbank2025"></d-cite>. Alita-G synthesizes and curates reusable MCP tools from successful trajectories, then retrieves them for future agent generation <d-cite key="alitag2025"></d-cite>.

The main challenge is trust. A global skill library needs provenance, tests, versioning, permission boundaries, and deprecation. Otherwise, it becomes a new supply-chain risk.

### Level 2: Collective Pipeline Optimization

At the harness layer, aggregate failure logs expose structural weaknesses.

If thousands of agents fail in the same loop, the problem may not be the base model. It may be the default system prompt, the retry policy, the tool schema, the planner, or the recovery strategy. Population logs let developers or meta-agents identify these repeated failure modes and update the default orchestration.

This is how an agent product can improve without every improvement becoming a model checkpoint. The control layer can evolve faster than the weights.

For coding agents, examples include better terminal recovery, better patch validation, better context selection, safer file-edit policies, and better delegation. These improvements often feel like "the model got smarter," but the actual change may be in the harness.

The frontier version is automated harness design. ADAS searches for new agentic systems by having a meta-agent program better agents in code <d-cite key="adas2024"></d-cite>. Darwin Godel Machine goes further by iteratively modifying its own code and validating improvements on coding benchmarks <d-cite key="dgm2025"></d-cite>. PromptWizard and related prompt optimizers show the lighter-weight variant: prompts can be optimized through feedback-driven self-evolution without changing weights <d-cite key="promptwizard2024"></d-cite>.

### Level 1: Continual Learning From Real Interaction

At the weight layer, population-level evolution becomes continual learning.

WildChat provides a public million-conversation substrate for studying real user interactions with ChatGPT-like systems <d-cite key="wildchat2024"></d-cite>. WildFeedback shows how in-situ feedback from those kinds of interactions can be converted into preference data for alignment <d-cite key="wildfeedback2024"></d-cite>. RLHI extends this idea by learning from in-the-wild user conversations, including user-guided rewrites and persona-conditioned rewards <d-cite key="rlhi2025"></d-cite>.

The broader implication is straightforward: deployed systems generate supervision. User corrections, rejected outputs, accepted edits, repeated prompts, tool errors, and recovery traces are all training signals. Cursor's online-RL work on Tab is a concrete product example: accepted and rejected suggestions are converted into rewards and used to improve the policy <d-cite key="cursortabrl2025"></d-cite>.

This does not mean every product is already doing safe, high-frequency online RL. In many cases, public evidence is limited, privacy constraints are significant, and production learning loops are deliberately conservative. But as a systems direction, it is clear: the outer loop of human interaction can become the inner loop of model improvement.

## When Experience Moves Inward

The practical design question is not simply whether an agent should learn. It is where the learning should land.

The cost gradient suggests a conservative promotion rule:

1. **Incident to memory.** If an experience is rare, local, exact, or tied to a specific environment, keep it in Level 3 as a note, trace, skill, or artifact.
2. **Memory to workflow.** If the same pattern recurs and has a procedural structure, promote it into Level 2 as a compiled prompt, tool route, recovery loop, or optimized DAG.
3. **Workflow to weights.** If the pattern is stable, broad, privacy-safe, and distributional, internalize it into Level 1 through adapters, continual learning, or checkpoint updates.

This is the engineering version of the inward movement described above:

**Do not train what you can compile. Do not compile what you can remember. Do not remember what you can solve once and discard.**

The rule is intentionally conservative. Weight updates are not morally or technically superior to memory updates. The right layer is the cheapest layer that preserves the useful signal without creating unacceptable risk.

## Why This Matters

The 3x3 matrix clarifies the dual promise of self-evolving agents.

First, it explains **marginal cost reduction**. If the agent can store a solved procedure as a file, compile it into a workflow, or distill it into a model prior, then repeated tasks become cheaper. The system stops paying full price for the same mistake.

Second, it explains **capability ceiling expansion**. If the agent can create tools, explore at test time, collect failures across users, and eventually train on those signals, then it can solve tasks that were not anticipated by the original prompt or harness.

This is the difference between an agent as a static interface and an agent as a living system.

A static agent has a fixed ceiling and a growing maintenance burden. A self-evolving agent has a feedback loop. The system can move experience inward:

1. From incident to memory.
2. From memory to workflow.
3. From workflow to weights.

That movement is the core mechanism of appreciation.

## Open Questions

This framework is still incomplete. Several problems need sharper treatment.

**Credit assignment.** When an agent succeeds or fails, which layer deserves the update? A bad result could come from missing memory, bad orchestration, weak model capability, tool failure, or user ambiguity.

**Evaluation.** How do we test whether an evolution improves the agent rather than overfitting to a local artifact? File updates are easy to inspect; weight updates are not. Memory systems also need causal and temporal evaluation, not just semantic retrieval scores.

**Safety and rollback.** Self-modification requires versioning. A skill library, harness, or adapter must be reversible when it introduces regressions.

**Contamination.** Memory poisoning, bad skill propagation, reward hacking, and tool supply-chain attacks are all natural failure modes once the system can learn from deployment traces. Evolution needs provenance and quarantine, not just accumulation.

**Privacy.** Across-session and across-user learning require different data boundaries. A personal memory should not leak into a global skill. A global model update should not memorize a private trajectory.

**Economics.** The matrix has a cost gradient. File updates are cheap; harness updates are moderate; weight updates are expensive. A practical agent should usually evolve at the cheapest layer that solves the problem.

Self-evolving agents are not defined by one technique. They are defined by whether experience changes future behavior at the right layer, over the right time scale, with the right cost.
