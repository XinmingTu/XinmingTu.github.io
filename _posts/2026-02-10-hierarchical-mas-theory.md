---
layout: distill
title: "Structured Test-Time Scaling: A Theoretical Framework for Multi-Agent Systems"
description: A theoretical framework for structured test-time scaling through multi-agent systems, showing how topology compression, scope isolation, and decoupled verification bypass the linear collapse of long-horizon reasoning.
date: 2026-02-10
tags: ['agents', 'deep-learning']

authors:
  - name: Xinming Tu
    url: "https://xinmingtu.cn"
    affiliations:
      name: University of Washington
  - name: Guanghao Ye
    affiliations:
      name: TBD

bibliography: 2026-02-10-hierarchical-mas-theory.bib

toc:
    - name: "Introduction"
    - name: "The Baseline: Why Linear Reasoning Collapses"
    - name: "Mechanism I: Architectural Compression of Span"
    - name: "Mechanism II: Scope Isolation via State Virtualization"
    - name: "Mechanism III: Verification as a Filter"
    - name: "A Unified Theory of Reliability"
    - name: "Practical Constraints"
    - name: "Conclusion"
    - name: "Related Work"
---

> **Note:** This post is a work in progress and may be updated frequently. We are currently working on experiments.

## Abstract

The current paradigm of test-time scaling often relies on unstructured, linear generation (e.g., long chains-of-thought). However, long-horizon reasoning inevitably collapses under this linear execution because small per-step errors compound exponentially along a single dependency chain. This note proposes a theoretical framework for *structured* test-time scaling through the lens of multi-agent systems (MAS). We argue that hierarchical and dynamically orchestrated MAS bypass linear collapse via a *three-layer defense*: (i) **topology** (analyzed via the *work--span* lens of parallel computation) compresses the sequential control span from $\Theta(W)$ to $\tilde O(\log W)$, slowing global drift; (ii) **scope isolation** actively denoises context via explicit state virtualization, transforming uncheckable semantic drift into verifiable atomic failures; and (iii) **verification** (such as strict decoupled filters seen in frontier systems like Google's Aletheia) acts as an error-correction code that suppresses the residual tail. We conclude with practical "physics" constraints---bandwidth, context hygiene, and fan-out---mapping the recent shift from static workflows to runtime-discovered recursive topologies (e.g., Recursive Language Models).

## Introduction

**The shift to test-time scaling and its unstructured bottleneck.**
As the AI community seeks to solve increasingly complex, long-horizon tasks, focus has shifted toward *test-time scaling*---spending more compute during inference. However, the default approach of simply prompting a model to "think longer" via long, linear Chains-of-Thought (CoT) is fundamentally *unstructured*. Mathematically, a single continuous reasoning path forces per-step errors to compound exponentially. To avoid collapse, the base model would need an impossibly low atomic error rate, posing a strict limit on unstructured scaling.

**The empirical success of Multi-Agent Systems (MAS).**
In practice, the community has bypassed this bottleneck by scaling the *system* rather than just the context window. Multi-agent frameworks and dynamic reasoning topologies---ranging from static role-playing teams <d-cite key="hong2023metagpt,wu2023autogen"></d-cite> to dynamic orchestrators <d-cite key="ruan2026aorchestra"></d-cite> and Recursive Language Models (RLMs) <d-cite key="zhang2025rlm"></d-cite>---have demonstrated remarkable empirical success on long-horizon tasks. By decomposing tasks, delegating sub-problems, and managing context, these systems successfully harness test-time compute where linear CoT fails.

**The gap: heuristics vs. theory.**
Despite their effectiveness, the design of modern agentic systems remains largely driven by heuristics and empirical trial-and-error. System prompts, hierarchical structures, and routing mechanisms are often engineered based on intuition rather than first principles. We lack a unified theoretical framework to explain *why* certain multi-agent topologies scale reliably, what limits their performance, and how to systematically design them.

**Our contribution: A theory of structured test-time scaling.**
This note bridges that gap. We propose a theoretical framework for *structured* test-time scaling by borrowing the *work--span* lens from classical parallel computation <d-cite key="brent1974"></d-cite>. We formalize how MAS bypass linear collapse not merely by throwing more compute at the problem, but by structurally reorganizing the computation graph through a *three-layer defense*:

1. **Mechanism I (Topology):** Dynamic hierarchy compresses the sequential control *span*, transforming global drift from a function of total work ($W$) to a function of logarithmic depth ($D$).
2. **Mechanism II (Scope isolation):** Explicit state management actively reduces leaf difficulty and context noise, lowering the intrinsic atomic error rate ($\epsilon_{\mathrm{leaf}}$).
3. **Mechanism III (Verification):** Decoupled filtering (as seen in recent models like Gemini Deep Think's Aletheia) suppresses the residual error tail ($\delta_+$), preventing local hallucinations from contaminating global state.

**Roadmap.**
Section 2 defines work/span and the linear-collapse baseline. Sections 3--5 develop the three mechanisms. Section 6 synthesizes them into a single reliability scaling law. Section 7 lists the practical constraints that determine whether the gains survive in real systems. Related work is organized as a structural evolution in the appendix.

## The Baseline: Why Linear Reasoning Collapses

**Work and span.**
Consider a task whose solution requires producing and correctly composing $W$ atomic units (facts, sub-proofs, code edits, tests, etc.). We distinguish:

- **Work $W$:** total required atomic units.
- **Span $S$:** the length of the longest sequential dependency/control path (critical path).

**Notation (quick reference).**

| Symbol | Meaning |
|--------|---------|
| $W$ | total atomic units (work) |
| $S$ | sequential control span / critical path |
| $k$ | branching factor / manager fan-out |
| $D$ | hierarchy depth (idealized $\lceil \log_k W \rceil$) |
| $\epsilon_{\mathrm{mono}}$ | unit error rate in monolithic (no isolation) setting |
| $\epsilon_{\mathrm{leaf}}$ | unit error rate after scope isolation at leaves |
| $\eta$ | per-layer drift probability (global intent/spec distortion) |
| $q$ | residual leaf error after all local gates |
| $\delta_+, \delta_-$ | verifier false accept / false reject |
| $m$ | redundant checks per unit |
| $c_g, c_v$ | cost of generation / verification |

**Linear execution forces $S = W$.**
A single-agent linear execution induces a sequential chain:

$$
U_1 \to U_2 \to \dots \to U_W,
$$

so the span is $S = W$.

**Exponential collapse under small per-step error.**
Let $\epsilon_{\mathrm{mono}}$ be the probability that a generated atomic unit is incorrect in a way that is not repaired. In the simplest brittle model (independent failures; any critical failure ruins the run),

$$
P_{\mathrm{linear}} = (1-\epsilon_{\mathrm{mono}})^W \;\approx\; e^{-\epsilon_{\mathrm{mono}} W}.
$$

**The "physical" limit of the linear topology.**
To keep $P_{\mathrm{linear}}$ bounded away from $0$ as $W$ grows, one needs $\epsilon_{\mathrm{mono}} = O(1/W)$. That is, the base model would have to become arbitrarily reliable as the horizon lengthens. This is the core brittleness critique of long chains.

**What the baseline teaches.**
The enemy is not "multi-step reasoning" per se; it is the *linear span* that forces errors and drift to accumulate along a length-$W$ control path. The rest of the note asks: can we change the topology so that the dominant compounding path is much shorter, and then keep the remaining errors local?

## Mechanism I: Architectural Compression of Span

**From a chain to a tree/DAG.**
Replace the linear chain with a roughly balanced $k$-ary hierarchy: a manager decomposes work into $k$ subproblems, sub-managers repeat, and leaves produce outputs. In the idealized balanced case,

$$
D = \left\lceil \log_k W \right\rceil,
$$

and the sequential control span scales like $S \approx \Theta(D)$ rather than $\Theta(W)$.

**A concrete contrast (linear vs. hierarchical).**
A useful mental model is that hierarchy keeps total work large (still $\Theta(W)$), but shortens the single most dangerous path:

$$
\underbrace{\text{Linear: } S=W}_{\text{one long control chain}}
\qquad\Rightarrow\qquad
\underbrace{\text{Hierarchy: } S \approx D = \Theta(\log_k W)}_{\text{short control depth}}.
$$

**Global drift becomes depth-driven.**
Let $\eta$ be the per-layer probability that intent or constraints are distorted in a way that is not fully corrected (semantic drift, spec distortion). A simple coherence model is

$$
P_{\mathrm{coherence}} \approx (1-\eta)^D \approx e^{-\eta D}.
$$

Compared to the linear analogue $e^{-\eta W}$, span compression makes drift decay extremely slowly with problem size.

**Dynamic Topology as Runtime Compilation (The Control Stack).**
The balanced tree is a pedagogical idealization. Modern agentic systems construct their topology *just-in-time*, operating like a dynamic **call stack**.

- **Explicit Orchestration:** Frameworks like **AOrchestra** <d-cite key="ruan2026aorchestra"></d-cite> formalize the sub-agent not as a fixed role, but as a runtime tuple $\langle \text{Instruction}, \text{Context}, \text{Tools} \rangle$, spawned only when uncertainty peaks.
- **Implicit Recursion:** **Recursive Language Models (RLMs)** <d-cite key="zhang2025rlm"></d-cite> achieve span compression via functional recursion, where the model invokes itself on sub-problems.

In both cases, the system trades integration work for reduced span by managing a *stack* of ephemeral agents, effectively "compiling" the optimal computation graph on the fly.

**Transition: span is not the whole story.**
Reducing span mitigates global drift, but it does not automatically guarantee correctness of the $W$ leaf-level units. Even if the top-level plan stays coherent, the system can still fail if too many leaves are wrong. This leads to our second mechanism: *make the leaves easier and cleaner.*

## Mechanism II: Scope Isolation via State Virtualization

**Decomposition is not only parallelism.**
A common story says hierarchy helps because it parallelizes work. A second, deeper story is that decomposition *improves accuracy* by changing the distribution of subproblems each model instance faces.

**A simple model: error depends on difficulty and noise.**
Let $L$ denote intrinsic subproblem complexity and $N$ denote context "noise" or distraction. Write the base model's unit error rate as $\epsilon(L, N)$. A monolithic run tends to induce large $(L, N)$, yielding $\epsilon_{\mathrm{mono}} = \epsilon(L_{\mathrm{root}}, N_{\mathrm{root}})$. A good decomposition aims to create leaves with smaller scope and cleaner context:

$$
L_{\mathrm{leaf}} \ll L_{\mathrm{root}}, \qquad N_{\mathrm{leaf}} \ll N_{\mathrm{root}}.
$$

The motivation is empirical: long contexts degrade reasoning ("lost in the middle" <d-cite key="liu2023lostmiddle"></d-cite>). The goal of isolation is to physically ensure $N_{\mathrm{leaf}}$ is minimal, keeping the base model in its reliable regime.

**Implementing Isolation: The Agentic Von Neumann Architecture.**
How do we physically guarantee $N_{\mathrm{leaf}} \ll N_{\mathrm{root}}$? Reliable MAS achieve this by adopting a *virtualized state architecture*, mirroring the separation of execution and storage in classical computing:

1. **Transient Isolation (The Call Stack):** Frameworks like AOrchestra <d-cite key="ruan2026aorchestra"></d-cite> and RLMs <d-cite key="zhang2025rlm"></d-cite> manage *control flow* via a programmatic call stack---sub-agents are spawned through code-level invocations (function calls, API calls), not conversational prompting. Each invocation creates a fresh, ephemeral context window (a "stack frame") with an explicit input/output contract. Once the sub-agent returns, its noisy internal reasoning trace is garbage-collected, preventing noise accumulation in the parent process.
2. **Persistent Isolation (The File System):** To manage long-term state that exceeds any single context window, systems like RLMs <d-cite key="zhang2025rlm"></d-cite>, native agentic frameworks <d-cite key="liu2026pensieve"></d-cite>, and OS-Agents <d-cite key="packer2023memgpt,wang2023voyager"></d-cite> use the file system directly to manage context. Instead of passing a linear chat log that grows unboundedly, agents read and write to structured artifacts (e.g., `spec.md`, `memory.json`). This forces the agent to explicitly "page in" only relevant data, keeping the working context clean and bounded within the context window---reducing the effective context from "everything that happened" to "only the files currently open."

**The trade: communication work for lower atomic error.**
Scope isolation is not free. It converts implicit context attention into explicit coordination work (reading/writing files, managing stack frames). However, it pays for itself by lowering $\epsilon_{\mathrm{leaf}}$ drastically. This explains why dynamic MAS work: they trade cheap token generation (extra work) for a structurally lower error rate (robustness).

**Qualitative Shift: From Drift to Checkability.**
Beyond reducing the error *rate* $\epsilon$, scope isolation transforms the *nature* of errors. In a monolithic context, failures often manifest as subtle semantic drift or hallucination, which are notoriously difficult to detect automatically. By enforcing strict input/output boundaries (e.g., function signatures or file schemas), isolation forces errors to manifest as discrete, local failures---such as syntax errors, type mismatches, or factual contradictions within a small window. This transformation is crucial: it converts *unverifiable* global drift into *verifiable* atomic failures, setting the stage for the rigorous filtering of Mechanism III.

**Transition: isolation lowers error, but does not eliminate tails.**
Even after scope isolation, probabilistic errors occur. As $W$ grows, the system must prevent these local errors from being sealed into upstream state. This motivates our third mechanism: verification as a filter.

## Mechanism III: Verification as a Filter

**Why false accept is the system killer.**
Verification error is not monolithic. We separate:

- $\delta_+$: *false accept* (accepting an incorrect candidate).
- $\delta_-$: *false reject* (rejecting a correct candidate).

False reject primarily increases cost via retries. False accept is more dangerous: it seals wrong work into shared state, making later correction difficult or impossible.

**The verification advantage assumption.**
Let $c_g$ be the cost of generating a candidate and $c_v$ the cost of verifying it. The regime where verification is useful is

$$
c_v \ll c_g \quad\text{and}\quad \delta_+ \text{ is small (or reducible by redundancy).}
$$

**Redundant checking gives logarithmic suppression.**
Suppose the leaf generator has unit error probability $\epsilon_{\mathrm{leaf}}$ after scope isolation. Run $m$ independent (or effectively de-correlated) checks and accept only if all checks accept. An incorrect candidate passes with probability at most $\delta_+^m$, so a simple bound on residual leaf error is

$$
q \;\lesssim\; \epsilon_{\mathrm{leaf}}\,\delta_+^m.
$$

To prevent work-driven collapse we want $Wq = O(1)$, i.e.,

$$
\epsilon_{\mathrm{leaf}}\,\delta_+^m \;\lesssim\; \frac{1}{W}.
$$

Solving gives

$$
m \;\gtrsim\; \frac{\ln(W\epsilon_{\mathrm{leaf}})}{-\ln(\delta_+)} \;=\; O(\log W),
$$

so only logarithmically many redundant checks are sufficient under a verification advantage.

**Correlation caveat.**
The $\delta_+^m$ behavior assumes checks are not perfectly correlated. In practice, de-correlation may require diversified prompts, randomized perturbations, tool-based tests, cross-model critics, or heterogeneous verifiers.

**Case Study: Decoupling for Strict Verification (Gemini's Aletheia).**
The necessity of minimizing $\delta_+$ is central to recent breakthroughs in inference-time scaling for scientific reasoning, such as Google DeepMind's math-research agent **Aletheia**, built on **Gemini Deep Think** <d-cite key="deepmind2026aletheia"></d-cite>. In domains where false accepts can permanently contaminate long-horizon proofs or scientific hypotheses, Aletheia implements a strict *Reason → Verify → Revise* loop that explicitly decouples the Generator from the Verifier. This architectural separation mitigates "confirmation bias"---where a monolithic model blindly accepts its own flawed logic. By forcing candidate solutions through an independent natural language Verifier that checks for logical gaps and citation hallucinations, the system drastically lowers its false accept rate $\delta_+$. Crucially, this strict filtering enables "intelligent failure": if the Verifier rejects all candidate paths, the system outputs "no solution" rather than sealing a hallucination into the state. This demonstrates the exact trade-off of Mechanism III: dynamically expending compute on retries ($m$) to convert catastrophic generation errors into explicit aborts, thereby bounding the residual error $q$ under a verification advantage.

## A Unified Theory of Reliability

**Two failure channels: drift vs. residual leaf errors.**
Combine the global-drift channel (span/depth-driven) with the local-error channel (work-driven). A compact approximation is

$$
P_{\mathrm{success}} \;\approx\; \exp\Big( -\big(\underbrace{\eta D}_{\text{span / drift}} + \underbrace{W q}_{\text{work / residual}}\big) \Big).
$$

Substituting the verification bound $q \lesssim \epsilon_{\mathrm{leaf}} \delta_+^m$ yields the "three-layer" decomposition:

$$
-\ln P_{\mathrm{success}} \;\approx\;
\underbrace{\eta D}_{\textbf{Topology (span)}}
\;+\;
\underbrace{W \epsilon_{\mathrm{leaf}}}_{\textbf{Scope isolation (node error)}}
\;\times\;
\underbrace{\delta_+^m}_{\textbf{Verification (filter)}}.
$$

**The governing law of structured test-time scaling.**
The unified equation formalizes the transition from heuristic MAS design to a predictable scaling law. It shows exactly how structured test-time compute should be allocated:

- **Topology** allocates compute to build hierarchy, shrinking the dangerous control path from $W$ to $D$, making drift scale with depth rather than horizon.
- **Scope isolation** allocates compute to explicit state management, lowering the base unit error rate from $\epsilon_{\mathrm{mono}}$ to $\epsilon_{\mathrm{leaf}}$.
- **Verification** allocates compute to redundant checking, suppressing the remaining tail so that $Wq$ stays bounded.

**Synthesis: The Agentic Von Neumann Architecture.**
This framework suggests that reliable MAS converge towards a classic computer architecture:

- **Mechanism I (The Stack):** Dynamic topology acts as the *Control Plane*, using recursion/spawning to compress execution span.
- **Mechanism II (The File System):** Scope isolation acts as the *Data Plane*, using virtualized state to decouple local reasoning from global history.
- **Mechanism III (The Filter):** Verification acts as the *Error Correction Code*, suppressing the residual tail.

Just as modern OS designs separate stack memory from file storage, robust agentic systems separate ephemeral reasoning traces from persistent state artifacts.

**Regimes (why "no heavy verification" can still work).**
The same equation explains an empirical spectrum:

- **Isolation-dominated regime:** if $W \epsilon_{\mathrm{leaf}}$ is not large on the workload, modest or even zero explicit checking can succeed.
- **Verification-dominated regime:** if $W \epsilon_{\mathrm{leaf}}$ becomes large, the system must grow $m$ so that $\delta_+^m$ drives $q$ down to $O(1/W)$.

## Practical Constraints

Hierarchy is not a free lunch. The following constraints determine whether the scaling story behind the unified equation survives contact with reality.

### Constraint 1: Verification advantage (cost and soundness)

$$
c_v \ll c_g \quad\text{and}\quad \delta_+ \text{ is small (or reducible by redundancy).}
$$

The strongest requirement is not simply "verification is accurate," but that *false accepts are rare enough* that wrong work does not routinely pass gates.

### Constraint 2: Compressible interfaces (bounded bandwidth)

A manager must control sub-agents through a low-bandwidth interface. An engineering version is:

$$
\mathrm{Comm}(u \to v) \le B \quad \text{for each edge.}
$$

If modules require exchanging full internal state (strong coupling), coordination cost and coordination error explode, negating span compression.

### Constraint 3: Scope isolation boundaries (active atomic tractability)

The system must actively *manufacture* tractable leaves by isolating scope and cleaning context:

- **Context hygiene:** keep $N_{\mathrm{leaf}}$ low (avoid long noisy threads).
- **Complexity reduction:** keep $L_{\mathrm{leaf}}$ within the base model's reliable regime.
- **Non-leaky boundaries:** prevent irrelevant constraints and unvetted partial solutions from leaking across modules.

If scope isolation fails, $\epsilon_{\mathrm{leaf}}$ rises toward $\epsilon_{\mathrm{mono}}$, pushing the burden back onto heavy verification.

### Constraint 4: Managerial fan-out limits

Although larger $k$ reduces depth $D = \lceil \log_k W \rceil$, it increases each manager's integration and verification load. In practice,

$$
k \le k_{\max}(\text{manager}),
$$

limited by attention, context window, tool latency, and integration complexity. Dynamic systems partially address this by allocating fan-out and depth *just in time* based on uncertainty and progress <d-cite key="ruan2026aorchestra,lu2026dytopo"></d-cite>.

## Conclusion

The paradigm of scaling test-time compute is hitting the physical limits of linear, unstructured generation. Long-horizon reasoning fails not merely because base models make errors, but because an unstructured topology ($\Theta(W)$ span) forces those errors to compound exponentially.

This note has proposed that the empirical success of modern Multi-Agent Systems is not magic, but the necessary result of *structured test-time scaling*. By viewing MAS through a theoretical lens, we see that they systematically reorganize computation:

- they compress span via dynamic topology so that global drift scales with logarithmic depth ($D$);
- they actively reduce the effective atomic error rate via strict scope isolation;
- and they deploy decoupled verification (as seen in frontier systems like Aletheia) to suppress residual errors with polylogarithmic overhead.

Ultimately, the next frontier of reliable reasoning lies not just in training more capable base models, but in the rigorous, theory-guided design of the inference-time computation graph.

## Related Work

We organize related work as a *structural evolution* in how inference-time computation is arranged, viewed through the work--span lens. The phases below are not mutually exclusive, but they capture a clear shift from fixed topologies to adaptive, recursive computation graphs.

### Foundations: work--span and critical-path viewpoints

Our work--span decomposition is inspired by classic results in parallel computation and scheduling, where *work* captures total operations and *span* (critical-path length) captures the irreducible sequential bottleneck <d-cite key="brent1974,blumofe1999"></d-cite>.

### Phase I: Static pipelines and role-fixed teams (fixed topology)

Early LLM multi-agent systems often mimic human organizational charts or encode SOP-style workflows with a *fixed* communication graph. Examples include CAMEL <d-cite key="li2023camel"></d-cite>, MetaGPT <d-cite key="hong2023metagpt"></d-cite>, ChatDev <d-cite key="qian2023chatdev"></d-cite>, and broader orchestration frameworks such as AutoGen <d-cite key="wu2023autogen"></d-cite>. Empirical failure analyses highlight brittleness modes such as mis-specification, weak termination, and leaky coordination <d-cite key="cemri2025whyfail"></d-cite>.

### Phase II: Inference-time search and internal deliberation (single-context scaling)

A second wave of work treats "more thinking at test time" as a way to increase reliability without changing model weights. Chain-of-thought prompting <d-cite key="wei2022cot"></d-cite> primarily increases *depth* (and thus span), while self-consistency <d-cite key="wang2022selfconsistency"></d-cite> improves reliability via *breadth* (sampling and aggregation). Tree-of-Thoughts <d-cite key="yao2023tot"></d-cite> makes exploration explicit. Iterative refinement methods such as Self-Refine <d-cite key="madaan2023selfrefine"></d-cite> and Reflexion <d-cite key="shinn2023reflexion"></d-cite> introduce local retry loops. Tool-augmented paradigms like ReAct <d-cite key="yao2022react"></d-cite> strengthen verification signals. A practical limitation is that much computation is still bound to a single long context, motivating explicit context hygiene and isolation <d-cite key="liu2023lostmiddle"></d-cite>.

### Phase III: Dynamic and recursive topology (topology discovered at runtime)

Most relevant to our "scale-up-the-system" narrative is the rise of systems that *construct* their computation graph during inference. AOrchestra formalizes sub-agents as dynamically creatable executors via a unified four-tuple interface $\langle \text{Instruction, Context, Tools, Model} \rangle$ and delegates execution via on-the-fly agent creation <d-cite key="ruan2026aorchestra"></d-cite>. DyTopo reconstructs sparse directed communication graphs round by round via semantic matching of lightweight "need/offer" descriptors <d-cite key="lu2026dytopo"></d-cite>. DyLAN selects teams and adapts collaboration structures dynamically via an explicit team-optimization stage <d-cite key="liu2023dylan"></d-cite>. Recursive Language Models (RLMs) offer a complementary single-model instantiation of recursion by allowing the model to programmatically inspect, decompose, and call itself over prompt snippets <d-cite key="zhang2025rlm"></d-cite>.

### Verification, debate, and process supervision

Debate <d-cite key="irving2018debate"></d-cite> and multi-agent debate <d-cite key="du2023debate,yang2025revisitingmad"></d-cite> can be interpreted as structured breadth-plus-verification. Process supervision and stepwise verification target the same failure channel by reducing false accepts and residual errors <d-cite key="lightman2023verify"></d-cite>.

### Internalization and mechanistic perspectives

A complementary direction internalizes external deliberation into a single model via RL or distillation <d-cite key="samanta2025maca,liu2026sdrl,luo2026agentark"></d-cite>. Mechanistic work suggests strong reasoning models may instantiate multiple heterogeneous internal perspectives and reconcile them during reasoning <d-cite key="kim2026societies,andreas2022agentmodels"></d-cite>.

### Fault-tolerance analogies and correlation caveats

Our emphasis on false accept and correlation echoes lessons from fault-tolerant computing. N-version programming formalizes redundancy but can fail under correlated design faults <d-cite key="avizienis1985nversion,knight1986independence"></d-cite>. Byzantine fault tolerance studies robust aggregation under faulty participants <d-cite key="lamport1982byzantine,castro1999pbft"></d-cite>.

### Synthesis: Mapping Inference Patterns to Scaling Axes

The table below summarizes how different inference patterns align with the work--span framework proposed in this note. While prior methods typically scale a single axis (depth, breadth, or verification), Hierarchical MAS uniquely combines topology control with scope isolation to minimize the effective error compounding path.

| Inference Pattern | Primary Scaling Axis | Span ($S$) | Mechanism & Limit |
| --- | --- | --- | --- |
| Linear CoT / Reflection | Depth | $\Theta(W)$ | *Increases span.* Prone to global drift; linear failure rate. |
| Best-of-$N$ / Ensembles | Breadth | $\Theta(W)$ | *Parallel samples.* Reduces variance; limited by selection reliability. |
| Tool-based Checks | Verification | $\Theta(W)$ | *Filters output.* Targets false accepts ($\delta_+$); needs cheap verifiers. |
| **Hierarchical MAS** | **Unified (All Axes)** | $\tilde O(\log W)$ | **Joint Optimization.** Structures Depth (Topology), Breadth (Isolation), and Verification (Filter) to minimize total failure cost. |

*Mapping common inference patterns to the scaling axes. Unlike baselines that scale a single dimension (depth, breadth, or checks), Hierarchical MAS provides a **unified framework** to jointly optimize topology, scope, and verification under work--span constraints.*
