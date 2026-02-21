---
layout: distill
title: "The Redistribution of Human Intelligence / 人类智能的重分配"
description: "AI's core impact isn't replacing human intelligence but redistributing it — from execution to decision-making, enabling unprecedented scale."
date: 2026-02-18
tags: ['AI', 'agents', 'future']
bilingual: true

authors:
  - name: Xinming Tu
    url: "https://xinmingtu.cn"
    affiliations:
      name: University of Washington

toc:
  - name: "Two Dimensions of Intelligence"
    name_zh: "智能的两个维度"
  - name: "Agent Task Horizon Growth"
    name_zh: "Agent 任务时间跨度的增长"
  - name: "Redistribution Is Scale"
    name_zh: "重分配即扩展"
  - name: "Time Scale Matching"
    name_zh: "时间尺度的匹配"
  - name: "The Limit of Redistribution"
    name_zh: "重分配的极限"
  - name: "AI Build Better AI"
    name_zh: "AI 构建更好的 AI"
  - name: "Personal Positioning"
    name_zh: "个人的定位"
  - name: "Current Limitations"
    name_zh: "当前的局限"
  - name: "References"
    name_zh: "参考文献"
---

{::options parse_block_html="true" /}

<div class="lang-en">

<a href="javascript:void(0)" onclick="document.getElementById('lang-toggle').click()">中文版</a>

I've been thinking about a question lately: what does AI really mean for humanity?

AI's core impact is not replacing human intelligence, but **redistributing** it. And redistribution itself means the scale of human intelligence — an exponential amplification of individual capability.

</div>

<div class="lang-zh">

<a href="javascript:void(0)" onclick="document.getElementById('lang-toggle').click()">Read in English</a>

最近一直在思考一个问题：AI 对人类到底意味着什么？

AI 的核心影响不是取代人类智能，而是**重分配**人类智能。而重分配本身，就意味着人类智能的 scale——个体能力的指数放大。

</div>

<div id="two-dimensions-of-intelligence" style="height:0;margin:0;padding:0;overflow:hidden;"></div>

<div class="lang-en">

## Two Dimensions of Intelligence

Intelligence can be broken down into two dimensions: the **breadth** of knowledge and the **depth** of thinking.

In terms of breadth, AI has indisputably surpassed humans. Any LLM commands a knowledge base far exceeding that of any individual person — this hardly needs elaboration.

What's more interesting is depth. AI's recent performance on IMO gold medals, Erdős open problems, [First Proof](https://www.scientificamerican.com/article/mathematicians-launch-first-proof-a-first-of-its-kind-math-exam-for-ai/), and other frontier mathematics has astonished many. Since last October, AI tools have helped solve roughly [100 Erdős problems](https://www.scientificamerican.com/article/ai-uncovers-solutions-to-erdos-problems-moving-closer-to-transforming-math/), with [Erdős Problem #728](https://arxiv.org/abs/2601.07421) considered the first Erdős open problem solved entirely autonomously by an AI system. But we need to understand precisely what this means — it demonstrates that **in well-defined settings with sufficient data and feedback signals**, AI can already reach extremely high levels. This is not the same as AI possessing general "deep thinking" ability.

IMO problems, while extremely difficult, have clear problem definitions, correct answers, and abundant historical training data. The real research frontier is often nothing like this — you don't even know how to formulate the problem, or which direction to think in. The hard part of deep thinking may not be the quality of each reasoning step, but the **sense of direction** when facing infinite possibilities. This is precisely the core gap between well-defined problems and open-ended research.

Even so, AI's rate of progress on the depth dimension remains astonishing — and accelerating.

</div>

<div class="lang-zh">

## 智能的两个维度

智能，或者说智慧，某种程度上可以分为两个维度：**知识的广度**和**思考的深度**。

广度上，AI 超越人类已经毫无争议。任何一个 LLM 所掌握的知识面都远超任何一个人类个体。

对于深度而言，最近一年 AI 在 IMO 金牌、Erdős 开放问题、[First Proof](https://www.scientificamerican.com/article/mathematicians-launch-first-proof-a-first-of-its-kind-math-exam-for-ai/) 等前沿数学上的表现让很多人惊叹。自去年十月以来，AI 工具已经帮助解决了大约 [100 个 Erdős 问题](https://www.scientificamerican.com/article/ai-uncovers-solutions-to-erdos-problems-moving-closer-to-transforming-math/)，其中 [Erdős Problem #728](https://arxiv.org/abs/2601.07421) 被认为是第一个由 AI 系统完全自主解决的 Erdős 开放问题。但我们需要准确理解这意味着什么——它说明的是，在**定义明确的场景（well-defined setting）下、有充足数据和反馈信号**的问题中，AI 已经可以达到极高水平。这并不等同于 AI 已经具备了通用的"深度思考"能力。

IMO 的题目（甚至是 Erdős 开放问题）虽然极其困难，但它们有明确的问题定义、有正确答案、有大量历史训练数据。真正的科研前沿往往不是这样的——你甚至不知道问题该怎么提，不知道该往哪个方向想。深度思考（deep thinking）的难点也许不在于单步推理的质量，而在于面对无限可能性时的**方向感**。这恰好是定义明确的问题（well-defined problem）和开放性研究（open-ended research）之间最核心的差距。

但即便如此，AI 在深度维度上的进展速度仍然惊人，而且还在加速。

</div>

<div id="agent-task-horizon-growth" style="height:0;margin:0;padding:0;overflow:hidden;"></div>

<div class="lang-en">

## Agent Task Horizon Growth

[METR's research](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) tracks a key metric: the time scale of tasks that AI agents can complete autonomously. While there is [some debate](https://www.technologyreview.com/2026/02/05/1132254/this-is-the-most-misunderstood-graph-in-ai/) about whether this growth strictly follows an exponential curve, the trend is clear — from minutes, to hours, and likely soon to days. METR's data shows the doubling time for AI agent task horizons is roughly 7 months.

<figure markdown="0">
<img src="/assets/img/2026-02-18-ai-redistribution/time-horizon-1-vs-1-1-hybrid.png" style="width: 100%;">
<figcaption>Source: METR, "Measuring AI Ability to Complete Long Tasks" (TH1.1 Update, Jan 2026)</figcaption>
</figure>

Most people focus on "AI is getting stronger," but I think what's more worth paying attention to is the implication behind this trend: **the "granularity" of tasks AI can complete autonomously is getting larger.**

What does larger granularity mean? It means humans need to intervene less frequently. It means the cost of human intelligence in the overall task pipeline is dropping. And when that cost drops below a certain threshold, the task is no longer bottlenecked by human time and attention — it can be scaled with compute resources.

This logic is entirely consistent with natural language programming. Writing code used to require allocating intelligence to every implementation detail — syntax, debugging, boilerplate, edge cases. Now with tools like Claude Code and Codex, you only need to invest thinking at the top-level design; the implementation is handed off to AI. The same applies to making presentations, data analysis, and document writing.

It's all the same thing at its core: **human intelligence withdraws from the execution layer and concentrates on the decision layer.**

"Everyone is a builder" sounds like a slogan, but the mechanism behind it is precisely the redistribution of human intelligence — you no longer need to invest intelligence in programming details, so non-programmers can build things too. The emergence of various agent assistants follows the same logic. It's not that humans have become smarter — it's that human intelligence no longer needs to be wasted on those tasks.

</div>

<div class="lang-zh">

## Agent 任务时间跨度的增长

[METR 的研究](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)追踪了一个关键指标：AI agent 能够自主完成的任务的时间尺度。尽管对这个增长是否严格符合指数曲线[存在一些争议](https://www.technologyreview.com/2026/02/05/1132254/this-is-the-most-misunderstood-graph-in-ai/)，但趋势是清晰的——从最初的以分钟为单位，到以小时为单位，估计很快就会到达以天为单位。METR 的数据显示，大约每隔七个月，AI agent 能自主完成的任务的时间尺度翻倍。

<figure markdown="0">
<img src="/assets/img/2026-02-18-ai-redistribution/time-horizon-1-vs-1-1-hybrid.png" style="width: 100%;">
<figcaption>Source: METR, "Measuring AI Ability to Complete Long Tasks" (TH1.1 Update, Jan 2026)</figcaption>
</figure>

**AI 能自主完成的任务"时间尺度"在变大。**

时间尺度变大意味着什么？意味着人类需要介入的频率在降低。意味着人类智能在整个任务流程（pipeline）中的成本在降低。而当人类智能的成本降低到一定程度，这个任务就不再受限于人类的时间和注意力，而是可以被计算资源来扩展（scale）了。

这个逻辑其实和自然语言编程是完全一致的。以前写代码，你需要把智能分配到实现（implementation）的每一个细节上——语法、调试、模板代码（boilerplate）、边界情况（edge case）。现在有了 Claude Code、Codex 这样的工具，你只需要在顶层设计（top-level design）上投入思考，实现的部分交给 AI 就好。做 PPT 也一样，数据分析也一样，文档写作也一样。

本质上都是同一件事：**人类智能从执行层撤出，集中到决策层。**

"人人都是建设者（builder）"这句话听起来像口号，但它背后的机制正是人类智能的重分配——不需要在编程细节上投入智能了，所以非程序员也能构建东西。各种 agent 助手的出现也是同样的道理。不是说人类变聪明了，而是人类的智能不需要被浪费在那些地方了。

</div>

<div id="redistribution-is-scale" style="height:0;margin:0;padding:0;overflow:hidden;"></div>

<div class="lang-en">

## Redistribution Is Scale

What's the direct result of redistribution? It's the **amplification** of human intelligence.

A person's time and energy used to be limited. Your intelligence was scattered across a mass of execution details — you spent 70% of your time on implementation, 20% on debugging, and maybe only 10% actually doing high-level thinking. Now if the execution layer no longer needs you, 100% of your intelligence can be directed toward the most valuable thinking. One person can supervise five, ten, or even dozens of parallel projects.

That's scale.

More fundamentally, **human intellectual labor is essentially computation**. What our brains do — processing information, reasoning, making decisions — is computation from an information-theoretic perspective. Since it's computation, it can naturally be measured in compute, and naturally scaled with compute. What AI does is transfer computation that previously could only run on "human brain time" onto silicon-based compute.

Think of it with a simple framing: if completing a project requires X units of "intelligence compute," nearly 100% of that used to require human compute. Now perhaps it only needs 10% human + 90% AI compute. That means the same human resources can produce ten times the output. The impact on societal productivity is already enormous — and we're just getting started.

</div>

<div class="lang-zh">

## 重分配即扩展

重分配带来的直接结果是什么？是对人类智能的**放大**。

以前一个人的时间有限，精力有限。你的智能被分散在大量的执行细节上——你花 70% 的时间在实现（implementation），20% 在调试（debugging），可能只有 10% 真正在做高层级思考。现在如果执行层的工作不再需要你了，那你 100% 的智能都可以投入到最有价值的思考上。你一个人可以监督五个、十个、甚至几十个并行的项目。

这就是扩展（scale）。

更根本地说，**人类的智力劳动本质上是一种计算**。我们的大脑在做的事情——处理信息、推理、决策——从信息论的角度看就是计算。既然是计算，就自然可以用算力来衡量，也自然可以用算力来扩展（scale）。AI 做的，就是把原本只能用"人脑时间"来执行的计算，转移到硅基算力上。

用一个简单的框架来想：如果完成一个项目需要 X 单位的"智能计算量"，以前几乎 100% 需要人类算力。现在也许只需要 10% 人类算力 + 90% AI 算力。那意味着同样的人力资源可以产出十倍的成果。这对社会生产力的改变已经是巨大的了——而且一切才刚刚开始。

</div>

<div id="time-scale-matching" style="height:0;margin:0;padding:0;overflow:hidden;"></div>

<div class="lang-en">

## Time Scale Matching

So far, the redistribution we've discussed has mainly occurred in the digital world — writing code, doing analysis, writing documents. But a much larger tipping point is approaching.

The growth of AI agent capabilities isn't just about "being able to do harder things" — it's about "being able to manage workflows across longer time spans." This expansion of the task horizon has a profoundly important implication:

When an agent's task horizon is only minutes, it can only orchestrate operations at the granularity of "run a piece of code" or "call an API." But when the horizon extends to days or even weeks, an entirely new possibility emerges — **running an experiment itself can become a "tool call" within an agent's workflow.**

Think about it: today's AI agents invoke code execution, wait a few seconds for results, then continue reasoning. Future agents could just as easily dispatch a standardized wet lab experiment, wait a few days for results, then proceed to the next step. Experiments shift from "external processes the agent can't manage" to "asynchronous steps the agent can orchestrate."

Previously, the time scales were mismatched: agents could only "live" for minutes, while experiments take days to run. This mismatch prevented AI from incorporating experiments into its loop. Now that the time scales are aligned, physical-world operations are naturally being "absorbed" into AI's orchestration scope.

**This is a key threshold for AI moving from the purely digital world to influencing the physical world.**

And this is still the logic of "redistribution." The research loop — design experiment → run experiment → interpret results → plan next experiment — previously required humans at every cognitive step. Not because AI wasn't smart enough for experiment design or data interpretation, but because AI's task horizon was too short to maintain a coherent workflow across the time gap of "waiting for experimental results." Now that the horizon is long enough, humans can step out of this loop and instead supervise more parallel experimental threads.

A scientist's intelligence, scaled — just like that.

</div>

<div class="lang-zh">

## 时间尺度的匹配

到目前为止，我们讨论的重分配主要发生在数字世界——写代码、做分析、写文档。但有一个更大的临界点正在到来。

AI agent 能力的增长不仅仅是"能做更难的事"，更是"能管理更长时间跨度的工作流（workflow）"。这个任务时间跨度（task horizon）的扩展有一个非常深远的含义：

当 agent 的任务时间跨度只有以分钟为单位的时候，它能编排的只是"跑一段代码"、"调一个 API"这种粒度的操作。但当时间跨度扩展到以天甚至周为单位，一个全新的可能性出现了——**和物理世界交互（比如做实验）本身可以变成 agent 工作流里的一个步骤**。

想想看：现在的 AI agent 调用代码执行，等几秒拿到结果，然后继续推理。未来的 agent 完全可以发起一个湿实验室（wet lab）的标准化实验，等几天拿到结果，然后继续推进下一步。实验从"agent 管不了的外部流程"变成了"agent 可以编排的一个异步步骤"。

以前两者的时间尺度不匹配：agent 只能"思考/活"几分钟，而实验要跑几天。这个不匹配使得 AI 没法把实验纳入自己的循环。现在时间尺度对齐了，物理世界的操作就自然地被"吸纳"进了 AI 的编排范围。

**这是 AI 从纯数字世界走向影响物理世界的一个关键门槛。**

而且这仍然是"重分配"的逻辑。以前科研的循环——设计实验 → 执行实验 → 解读结果 → 规划下一步实验——其中每一个认知环节都需要人类。不是因为 AI 不够聪明做不了实验设计或数据解读，而是因为 AI 的任务时间跨度太短，没法跨越"等实验结果"这个时间间隔来维持连贯的工作流。现在时间跨度够长了，人类就可以从这个循环中退出来，转而去监督更多条并行的实验线。

一个科学家的智能，就这样被扩展（scale）了。

</div>

<div id="the-limit-of-redistribution" style="height:0;margin:0;padding:0;overflow:hidden;"></div>

<div class="lang-en">

## The Limit of Redistribution

Following the logic of redistribution naturally leads to a fundamental question: **will the portion that still requires human intelligence eventually approach zero?**

My personal judgment is that reaching this extreme is unlikely in the short term (say, two to three years). But the trend is certain: human intelligence will increasingly concentrate on fewer, higher-level problems.

The likely progression looks something like this: first, withdrawing from implementation (happening now), then from design (beginning to happen), and finally from goal-setting and value alignment (still quite far off). The difficulty at each step probably doesn't increase linearly — the higher you go, the more the required judgment involves taste, intuition, and values, things AI still isn't particularly good at.

But one point is worth emphasizing: **even if human contribution doesn't reach zero, just dropping from 90% to 10% would already be transformative for society.** We don't need to wait for AGI to fully replace humans to feel the upheaval — redistribution itself is already profoundly changing everything.


</div>

<div class="lang-zh">

## 重分配的极限

沿着重分配的逻辑自然会追问一个根本性的问题：**人类智能最终需要做的部分，会不会趋近于零？**

我个人的判断是，短期内（比如两三年）应该不太可能达到这个极端。但趋势是确定的：人类智能会越来越集中在更少、更高层级的问题上。

可能的渐进路径大概是这样的：先从实现（implementation）退出（正在发生），再从设计（design）退出（开始发生），最后从目标设定（goal-setting）和价值对齐（value alignment）退出（还比较远）。每一步的难度可能不是线性递增的——越往上走，需要的判断越是涉及品味、直觉、价值观这些目前 AI 还不太擅长的东西。

不过有一点值得强调：**即使人类的贡献不归零，只要从 90% 降到 10%，对社会的冲击已经是变革性的。** 我们不需要等到 AGI 完全取代人类才会感受到剧变，重分配本身就已经在深刻改变一切了。


</div>

<div id="ai-build-better-ai" style="height:0;margin:0;padding:0;overflow:hidden;"></div>

<div class="lang-en">

## AI Build Better AI

Dario Amodei recently stated on the [Dwarkesh Podcast (2026.2.13)](https://www.dwarkesh.com/p/dario-amodei-2) that he has 90% confidence in achieving "a country of geniuses in a data center" within ten years, and personally estimates it's more likely within one to three years. He believes we are approaching the end of the exponential growth phase.

If this prediction is correct, then a natural follow-up question arises: **what happens if AI can fully build better AI?**

That would mean the growth of intelligence is no longer constrained by human biological limits — no longer constrained by our brain capacity, our learning speed, our lifespan. Intelligence would enter a self-accelerating loop. That would be human civilization stepping into an entirely new world — the changes would be earth-shattering.

Of course, this is unlikely to happen fully in the short term. But it's worth noting that **partial self-improvement is already underway**. AI is assisting its own training processes, automating RLHF pipelines, and writing code to improve its own infrastructure. A fully autonomous closed loop hasn't formed yet, but the direction is clear.

For a more detailed outlook on AI's positive potential, I recommend Dario's long essay from last year, [*Machines of Loving Grace*](https://www.darioamodei.com/essay/machines-of-loving-grace), in which he envisions transformations AI could bring to biology, medicine, economic development, and more.

</div>

<div class="lang-zh">

## AI 构建更好的 AI

Dario Amodei 在最近的 [Dwarkesh Podcast（2026.2.13）](https://www.dwarkesh.com/p/dario-amodei-2)中表示，他对十年内实现 "a country of geniuses in a data center" 有 90% 的信心，并且个人估计更可能在一到三年内实现。他认为我们正在接近指数增长阶段的尾声。

如果这个预判是对的，那接下来一个自然的问题就是：**如果 AI 能完全自主地构建更好的 AI，会怎样？**

那将意味着智能的增长不再受限于人类的生物学约束——不再受限于我们的大脑容量、我们的学习速度、我们的寿命。智能将进入一个自我加速的循环。那就是人类文明迈向一个彻底的全新世界，变化将是天翻地覆的。

当然，短期内这不太可能完全发生。但值得注意的是，**部分自我改进（partial self-improvement）其实已经在进行中了**。AI 在辅助自身的训练流程、自动化 RLHF 流程、写代码来改进自身的基础设施。完全自主的闭环还没有形成，但方向是清楚的。

关于 AI 积极前景的更详细展望，推荐阅读 Dario 去年的长文 [*Machines of Loving Grace*](https://www.darioamodei.com/essay/machines-of-loving-grace)，他在其中描绘了 AI 在生物学、医学、经济发展等领域可能带来的变革。

</div>

<div id="personal-positioning" style="height:0;margin:0;padding:0;overflow:hidden;"></div>

<div class="lang-en">

## Personal Positioning

Coming back to a more personal level. Where should individual effort be directed?

**The first direction** is using AI to boost your own productivity — doing your next project better and faster. This is intuitive and what most people are doing right now. But this direction carries an implicit risk: work that takes months now might only take days a year or two from now. Pure application-layer efficiency gains may be rapidly devalued by the fast growth of AI capabilities.

**The second direction** is accelerating the improvement of AI itself — pushing the frontier of AI capabilities, or using AI to accelerate scientific discovery. This path assumes AI won't hit a wall soon, or at least that the wall isn't very close. If that assumption holds, this path may have more lasting value, because science itself is constantly opening new frontiers.

**The third direction** is thinking beyond AGI itself — toward the post-AGI world. If AI truly achieves recursive self-improvement, many of today's intellectual bottlenecks will dissolve. What remains are problems that are fundamentally *not* about intelligence but about the physical and biological world: aging, disease. These are domains where no amount of AI reasoning can substitute for the constraints of biology and physics. Studying aging, for instance, could become one of the most valuable long-term research directions.

Regardless of which direction you take, the core question is the same: "where should human intelligence be allocated?"

In an era of rapid AI progress, work that is "close to AI's capability frontier" gets caught up to faster. Work that "defines meaningful new problems" may have more lasting value.

One last reminder, also to myself: even when AI can think better than us, it still can't exercise for us. In a world where cognitive labor is increasingly automated, your physical health becomes your most irreplaceable asset. Stay active, sleep well, exercise regularly — so that when the AI revolution fully arrives, you're actually in good shape to embrace it.

</div>

<div class="lang-zh">

## 个人的定位

回到更个人的层面。个人的努力应该投向哪里？

**第一个方向**是用 AI 提高自己的生产力，更好更快地做下一个项目。这很直觉，也是大多数人当下在做的。但这个方向有一个隐含的风险：现在花几个月做的工作，也许一两年后只需要几天就能完成。纯粹的应用层提效，可能会被 AI 能力的快速增长迅速贬值。

**第二个方向**是加速提高 AI 的能力——去推动 AI 能力的前沿，或者用 AI 来加速科学发现本身。这条路的前提是 AI 不会很快碰壁，或者说这个瓶颈目前还不是很近。如果前提成立，这条路可能有更持久的价值，因为科学本身在不断开拓新前沿。

**第三个方向**是跳出 AGI 本身，去思考 Post-AGI 时代的问题。如果 AI 真的实现了递归式自我改进，今天很多认知层面的瓶颈都会被打破。那时候真正剩下的，是那些本质上*不是*认知问题、而是物理世界和生物学的问题：衰老、疾病。这些领域，再强的 AI 推理也无法替代生物学和物理学的约束。比如研究衰老，可能会成为最有长期价值的研究方向之一。

无论走哪个方向，核心问题都是一样的："人类智能该分配到哪里？"

在一个 AI 快速进步的时代，越是"离 AI 能力前沿近"的工作，被 AI 追上的速度越快。越是"定义有意义的新问题"的工作，可能越有持久的价值。

最后一个提醒，也是给自己的：AI 再怎么发展，也没法替我们锻炼。在认知劳动越来越自动化的世界里，身体健康反而成了最不可替代的资产。规律运动、好好睡觉、保持健康——这样当 AI 革命真正到来的时候，你才有足够好的状态去拥抱它。

</div>

<div id="current-limitations" style="height:0;margin:0;padding:0;overflow:hidden;"></div>

<div class="lang-en">

## Current Limitations

Demis Hassabis recently described current AI as a kind of "jagged intelligence" at the [India AI Impact Summit (2026.2.18)](https://www.storyboard18.com/brand-makers/google-deepmind-ceo-says-agi-not-here-yet-calls-current-ai-jagged-intelligence-90028.htm). I think this description is remarkably precise, manifesting in two ways:

First, **AI has inherent uncertainty**. It is highly sensitive to prompts and context — unlike a calculator that always produces the same output for the same input. The same question phrased differently can yield dramatically different answers.

Second, **AI's difficulty distribution has a different shape from the human difficulty distribution**. As Hassabis noted, AI can win an IMO gold medal yet make mistakes on basic math problems when posed in certain ways. It can write elegant mathematical proofs but stumble on simple logical reasoning. AI's intelligence profile has a fundamentally different shape from that of humans.

These limitations are real, but I believe they **can be addressed through system design**.

The key insight is: we don't need to pursue a perfect single LLM. Instead, we need to build an **LLM-based system** — incorporating tools, environments, and multi-agent architectures, using system-level design to compensate for individual model unreliability. (I discuss the specific design of Multi-Agent systems in more detail in [another blog post](/blog/2026/hierarchical-mas-theory/).)

</div>

<div class="lang-zh">

## 当前的局限

Demis Hassabis 在最近的 [India AI Impact Summit（2026.2.18）](https://www.storyboard18.com/brand-makers/google-deepmind-ceo-says-agi-not-here-yet-calls-current-ai-jagged-intelligence-90028.htm)上形容当前的 AI 是一种"参差不齐的智能"（jagged intelligence）。我觉得这个描述非常精准，具体体现在两个方面：

第一，**AI 具有内在的不确定性**。它对提示词（prompt）和上下文（context）是高度敏感的，不像计算器那样给同样的输入一定得到同样的输出。同一个问题换一种问法，可能得到截然不同的回答。

第二，**AI 的难度分布和人类的难度分布形状不同**。正如 Hassabis 所说，AI 能拿到 IMO 金牌，却可能在以特定方式提出的基础数学题上犯错。它可以写出优雅的数学证明，但可能在一个简单的逻辑推理上犯错。AI 的智能分布（intelligence profile）和人类是不同形状的。

这些局限是真实的，但我认为它们**可以被系统设计解决**。

关键思路是：我们不需要追求一个完美的单一 LLM，而是需要构建一个**基于 LLM 的系统（LLM-based system）**——加入工具、环境、多智能体（multi-agent）架构，用系统层面的设计来弥补单个模型的不可靠性。（关于多智能体系统的具体设计，我在[另一篇博客](/blog/2026/hierarchical-mas-theory/)中有更详细的讨论。）

</div>

<div id="references" style="height:0;margin:0;padding:0;overflow:hidden;"></div>

<div class="lang-en">

## References

- Dario Amodei, [*"We are near the end of the exponential"*](https://www.dwarkesh.com/p/dario-amodei-2) — Dwarkesh Podcast, Feb 2026
- Dario Amodei, [*Machines of Loving Grace*](https://www.darioamodei.com/essay/machines-of-loving-grace) — Essay, Oct 2024
- Demis Hassabis on "Jagged Intelligence" — [India AI Impact Summit](https://www.storyboard18.com/brand-makers/google-deepmind-ceo-says-agi-not-here-yet-calls-current-ai-jagged-intelligence-90028.htm), Feb 2026
- METR, [*Measuring AI Ability to Complete Long Tasks*](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/), Mar 2025 ([TH1.1 Update](https://metr.org/blog/2026-1-29-time-horizon-1-1/), Jan 2026)
- MIT Technology Review, [*This is the most misunderstood graph in AI*](https://www.technologyreview.com/2026/02/05/1132254/this-is-the-most-misunderstood-graph-in-ai/), Feb 2026
- Scientific American, [*AI uncovers solutions to Erdős problems*](https://www.scientificamerican.com/article/ai-uncovers-solutions-to-erdos-problems-moving-closer-to-transforming-math/), Feb 2026
- Scientific American, [*Mathematicians launch First Proof*](https://www.scientificamerican.com/article/mathematicians-launch-first-proof-a-first-of-its-kind-math-exam-for-ai/), Feb 2026
- Terence Tao, [*The story of Erdős problem #1026*](https://terrytao.wordpress.com/2025/12/08/the-story-of-erdos-problem-126/), Dec 2025
- [Amy Tam's thread on the cost of staying](https://x.com/amytam01/status/2023593365401636896)

</div>

<div class="lang-zh">

## 参考文献

- Dario Amodei, [*"We are near the end of the exponential"*](https://www.dwarkesh.com/p/dario-amodei-2) — Dwarkesh Podcast, Feb 2026
- Dario Amodei, [*Machines of Loving Grace*](https://www.darioamodei.com/essay/machines-of-loving-grace) — Essay, Oct 2024
- Demis Hassabis on "Jagged Intelligence" — [India AI Impact Summit](https://www.storyboard18.com/brand-makers/google-deepmind-ceo-says-agi-not-here-yet-calls-current-ai-jagged-intelligence-90028.htm), Feb 2026
- METR, [*Measuring AI Ability to Complete Long Tasks*](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/), Mar 2025 ([TH1.1 Update](https://metr.org/blog/2026-1-29-time-horizon-1-1/), Jan 2026)
- MIT Technology Review, [*This is the most misunderstood graph in AI*](https://www.technologyreview.com/2026/02/05/1132254/this-is-the-most-misunderstood-graph-in-ai/), Feb 2026
- Scientific American, [*AI uncovers solutions to Erdős problems*](https://www.scientificamerican.com/article/ai-uncovers-solutions-to-erdos-problems-moving-closer-to-transforming-math/), Feb 2026
- Scientific American, [*Mathematicians launch First Proof*](https://www.scientificamerican.com/article/mathematicians-launch-first-proof-a-first-of-its-kind-math-exam-for-ai/), Feb 2026
- Terence Tao, [*The story of Erdős problem #1026*](https://terrytao.wordpress.com/2025/12/08/the-story-of-erdos-problem-126/), Dec 2025
- [Amy Tam's thread on the cost of staying](https://x.com/amytam01/status/2023593365401636896)

</div>
