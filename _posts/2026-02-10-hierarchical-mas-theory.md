---
layout: distill
title: "The Work-Span of Reasoning: A Theory of Structured Test-Time Scaling in Multi-Agent Systems"
description: A work--span framework for structured test-time scaling in multi-agent systems, explaining how topology compression, scope isolation, and verification filtering yield polylogarithmic reliability overhead.
date: 2026-02-10
tags: ['agents', 'deep-learning']

authors:
  - name: Xinming Tu
    url: "https://xinmingtu.cn"
    affiliations:
      name: University of Washington

bibliography: 2026-02-10-hierarchical-mas-theory.bib

toc:
    - name: "Introduction"
    - name: "The Baseline: Why Linear Reasoning Collapses"
    - name: "Mechanism I: Architectural Compression of Span"
    - name: "Mechanism II: Scope Isolation as Active Denoising"
    - name: "Mechanism III: Verification as a Filter"
    - name: "A Unified Theory of Reliability"
    - name: "Practical Constraints"
    - name: "Conclusion"
    - name: "Related Work"
---

## Abstract

Long-horizon reasoning often collapses under linear execution because small per-step errors compound along a single dependency chain. This note reframes the reliability of multi-agent systems (MAS) through the *work--span* lens from parallel computation <d-cite key="brent1974,blumofe1999"></d-cite>. The key claim is that hierarchical (and increasingly *dynamic*) MAS improve long-horizon robustness via a *three-layer defense*: (i) **topology** compresses sequential control *span* from $\Theta(W)$ to $\tilde O(\log W)$, slowing global drift; (ii) **scope isolation** actively denoises and reduces per-leaf difficulty, lowering the *effective* atomic error rate compared to monolithic prompting (motivated by long-context brittleness such as "lost in the middle" <d-cite key="liu2023lostmiddle"></d-cite>); and (iii) **verification** acts as a filter that suppresses the residual error tail, with polylogarithmic redundant checking when false accepts are rare. We end with practical "physics" constraints---verification asymmetry, compressible interfaces, scope isolation boundaries, and managerial fan-out limits---and connect the framework to the recent shift from *static* workflows to *runtime-discovered* recursive topologies (e.g., Recursive Language Models) <d-cite key="zhang2025rlm"></d-cite>.

## Introduction

**The status quo: scale the model.**
For long-horizon tasks, a common (often implicit) response to failure is to demand that the base model's per-step error rate $\epsilon$ become arbitrarily small as the horizon grows. This is the *scale-up-the-model* narrative.

**The alternative: scale the system.**
This note argues for a complementary *scale-up-the-system* narrative. Instead of asking for unbounded improvements in $\epsilon$, reorganize computation so that the dominant error-compounding dimension is no longer the raw horizon length, but a much shorter *control depth*.

**A computation lens: work vs. span.**
We borrow the *work--span* viewpoint from parallel algorithms <d-cite key="brent1974,blumofe1999"></d-cite>. Work counts how many atomic units must be produced; span measures how long the longest sequential control chain is. A linear chain-of-thought has span $\Theta(W)$. Hierarchical MAS aim to keep span polylogarithmic while paying extra work for coordination.

**Three mechanisms that jointly buy reliability.**
The flow of the note is intentionally "enemy $\rightarrow$ defenses":

1. **Mechanism I (Topology):** hierarchy compresses span, slowing *global drift*.
2. **Mechanism II (Scope isolation):** decomposition *actively* reduces leaf difficulty and context noise, lowering the *effective* atomic error rate.
3. **Mechanism III (Verification):** cheap, sound checks suppress the remaining residual errors.

**Roadmap.**
We first define work/span and the linear-collapse baseline. Then we develop the three mechanisms. Next we synthesize them into a single reliability scaling law. Finally we list the practical constraints that determine whether the gains survive in real systems. Related work is organized as a structural evolution at the end.

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

**Static vs. dynamic hierarchies (discovered at runtime).**
The balanced tree is a pedagogical idealization. Modern agentic systems increasingly *construct* their topology on the fly: the orchestrator spawns a sub-agent only when uncertainty is high, when a check fails, or when a subproblem is detected; communication links may be rerouted round by round <d-cite key="ruan2026aorchestra,lu2026dytopo,liu2023dylan"></d-cite>. The work--span lens still applies: span is the critical-path length of the *constructed* computation DAG.

**Transition: span is not the whole story.**
Reducing span mitigates global drift, but it does not automatically guarantee correctness of the $W$ leaf-level units. Even if the top-level plan stays coherent, the system can still fail if too many leaves are wrong. This leads to our second mechanism: *make the leaves easier and cleaner.*

## Mechanism II: Scope Isolation as Active Denoising

**Decomposition is not only parallelism.**
A common story says hierarchy helps because it parallelizes work. A second (often implicit) story is that decomposition *improves accuracy* by changing the distribution of subproblems each model instance faces.

**A simple model: error depends on difficulty and noise.**
Let $L$ denote intrinsic subproblem complexity and $N$ denote context "noise" or distraction. Write the base model's unit error rate as $\epsilon(L, N)$. A monolithic run tends to induce large $(L, N)$, yielding

$$
\epsilon_{\mathrm{mono}} = \epsilon(L_{\mathrm{root}}, N_{\mathrm{root}}).
$$

A good decomposition aims to create leaves with smaller scope and cleaner context:

$$
L_{\mathrm{leaf}} \ll L_{\mathrm{root}}, \qquad N_{\mathrm{leaf}} \ll N_{\mathrm{root}},
$$

so

$$
\epsilon_{\mathrm{leaf}} = \epsilon(L_{\mathrm{leaf}}, N_{\mathrm{leaf}}) \ll \epsilon_{\mathrm{mono}}.
$$

The motivation is empirical: long contexts and distraction can degrade how LMs use evidence (e.g., "lost in the middle" <d-cite key="liu2023lostmiddle"></d-cite>), so physically isolating scope can raise the signal-to-noise ratio each leaf agent sees.

**The trade: communication work for lower atomic error.**
Scope isolation typically increases coordination and integration work. But it can *pay for itself* by lowering $\epsilon_{\mathrm{leaf}}$ enough that the system succeeds with light explicit verification on moderate $W$. This explains a practical observation: many dynamic MAS appear to "work" even without heavy formal verification because they keep subproblems inside the base model's comfortable regime.

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

**How the mechanisms cooperate.**
The unified equation makes the collaboration explicit:

- Topology shrinks the dangerous control path from $W$ to $D$, making drift scale with depth rather than horizon.
- Scope isolation lowers the base unit error rate from $\epsilon_{\mathrm{mono}}$ to $\epsilon_{\mathrm{leaf}}$ by reducing $(L, N)$ at the leaves.
- Verification suppresses the remaining tail so that $Wq$ stays bounded even when $W$ is large.

**Regimes (why "no heavy verification" can still work).**
The same equation explains an empirical spectrum:

- **Isolation-dominated regime:** if $W \epsilon_{\mathrm{leaf}}$ is not large on the workload, modest or even zero explicit checking can succeed.
- **Verification-dominated regime:** if $W \epsilon_{\mathrm{leaf}}$ becomes large, the system must grow $m$ so that $\delta_+^m$ drives $q$ down to $O(1/W)$.

**Dynamic topology as just-in-time optimization.**
Modern systems can be read as searching for a good operating point of the unified equation *at runtime*. AOrchestra spawns sub-agents on demand with explicit context control <d-cite key="ruan2026aorchestra"></d-cite>; DyTopo reroutes communication edges round by round to match stage-dependent information needs <d-cite key="lu2026dytopo"></d-cite>; DyLAN selects and reforms agent teams dynamically <d-cite key="liu2023dylan"></d-cite>. In this view, "create a sub-agent", "route a message", and "increase checking" are inference-time actions that trade work for lower span, lower $\epsilon_{\mathrm{leaf}}$, or lower residual error.

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

Linear long-horizon reasoning fails not because errors exist, but because a linear topology forces them to accumulate along a length-$W$ control chain. Hierarchical MAS change the computation:

- they compress span so that drift scales with depth ($D$) rather than horizon ($W$);
- they actively reduce the effective unit error rate via scope isolation (cleaner, smaller contexts);
- and they use verification as a filter to suppress residual errors with only polylogarithmic overhead under a verification advantage.

The resulting picture is that reliability is not only a function of model capability, but also of the system's computation graph: topology, interfaces, context routing, and checking.

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

Unlike baselines that scale a single dimension, Hierarchical MAS provides a **unified framework** to jointly optimize topology, scope, and verification under work--span constraints.
