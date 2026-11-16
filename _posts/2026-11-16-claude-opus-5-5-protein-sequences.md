---
layout: distill
title: "Claude Opus 5.5 was trained on protein sequence data"
description: "A next-amino-acid test on proteins nobody has studied, with a shuffled control, finds sequence data in one frontier model's training and no sign of it in the others."
date: 2026-11-16
tags: ['AI', 'biology', 'LLM', 'evaluation']
categories: blog
permalink: /blog/preview/claude-opus-5-5-protein-sequences/
preview: true
sitemap: false
bibliography: 2026-11-16-claude-opus-5-5-protein-sequences.bib

toc:
  - name: "Why famous proteins don't count"
  - name: "The test"
  - name: "Only Claude Opus 5.5 shows it"
  - name: "The fingerprint of training data"
  - name: "Famous proteins prove little"
  - name: "What this shows, and what it does not"
  - name: "Appendix"

authors:
  - name: Xinming Tu
    url: "https://xinmingtu.cn"
    affiliations:
      name: University of Washington, Phylo

_styles: |
  d-article {
    --bp-panel: #f6f7f9; --bp-ink: #1d2433; --bp-body: #3c4454; --bp-muted: #6b7385;
    --bp-faint: #b4bac6; --bp-line: #d9dde4; --bp-bead: #ffffff;
    --bp-accent: #d97757; --bp-accent-text: #b4532f; --bp-accent-soft: #fbeee8;
    --bp-good: #2f8a5f; --bp-bad: #c2453d; --bp-chip: #1d2433; --bp-chip-text: #ffffff;
  }
  html[data-theme='dark'] d-article {
    --bp-panel: #20242c; --bp-ink: #eef0f4; --bp-body: #cdd2db; --bp-muted: #9aa2b2;
    --bp-faint: #6c7484; --bp-line: #3a404c; --bp-bead: #2a2f39;
    --bp-accent: #e08a6c; --bp-accent-text: #eda48a; --bp-accent-soft: #4a3229;
    --bp-good: #6cc398; --bp-bad: #e58a82; --bp-chip: #eef0f4; --bp-chip-text: #1d2433;
  }
  d-article p, d-article li { color: var(--bp-body); }
  d-article h2 { color: var(--bp-ink); margin-top: 1.9rem; margin-bottom: 0.7em; }
  d-article .bp-lede {
    border-left: 3px solid var(--bp-accent);
    font-size: 1.06rem; line-height: 1.7;
    margin: 0.3rem 0 2rem; padding: 0.1rem 0 0.1rem 1rem;
  }
  d-article .bp-lede p { margin: 0 0 0.6rem; }
  d-article .bp-lede strong { color: var(--bp-ink); }
  d-article figure.bp-figure { margin: 1.6rem 0 2rem; }
  @media (min-width: 1000px) {
    d-article > figure.bp-wide { grid-column: page; justify-self: center; width: 100%; max-width: 860px; }
  }
  d-article figure.bp-figure img, d-article figure.bp-figure svg { display: block; width: 100%; height: auto; }
  html[data-theme='dark'] d-article figure.bp-figure img { background: #ffffff; border-radius: 10px; padding: 10px; }
  d-article figure.bp-figure figcaption {
    color: var(--bp-muted); font-size: 0.83rem; line-height: 1.45; margin-top: 0.65rem;
  }
  d-article .bp-fig-mobile { display: none; }
  @media (max-width: 600px) {
    d-article .bp-fig-desktop { display: none; }
    d-article .bp-fig-mobile { display: block; }
  }
  d-article .bp-cmd {
    background: var(--bp-panel); border: 1px solid var(--bp-line); border-radius: 8px;
    font-size: 0.85rem; padding: 0.7rem 0.9rem;
  }
---

<div class="bp-lede" markdown="1">
**Claude Opus 5.5 was trained on protein sequences. No other model we tested shows it.**

On 668 bacterial proteins that no paper describes, we asked models for the next amino acid, then asked again on the same protein shuffled. The gap between the two is what a model learned about these sequences:

- **Claude Opus 5.5: +27.4 points** (34.9% vs 7.5%)
- OpenAI: GPT-6 Astra +2.9, GPT-5.5 +2.1
- Google: Gemini 4 Carbon +0.9, Gemini 2.5 Pro +1.1
- Open-weight: DeepSeek, Qwen, Kimi, GLM, MiniMax, gpt-oss and Nemotron, 0 to +1.9

The gap grows with the number of sequences in a protein's family, including families with no papers at all: the fingerprint of training data. It is new: Opus 4.6 +0.9, Opus 4.8 +7.7, Opus 5 +9.7, Opus 5.5 +27.4.
</div>

## Why famous proteins don't count

A post by Atharv Jayprakash<d-cite key="jayprakash2026sod1"></d-cite> and PG-LLM<d-cite key="arora2026pgllm"></d-cite> showed frontier models ranking protein variants about as well as ESM-2, which raised the question of whether they were trained on sequence databases such as UniProt.

Famous proteins can't answer it. They are printed in papers and across the web: given the start of GFP, 9 of 12 frontier models write the next 10 residues exactly. So we test on proteins nobody writes about.

## The test

<figure class="bp-figure bp-wide" markdown="0">
  <div class="bp-fig-desktop">{% include llm-bioseq-probe/method.svg %}</div>
  <div class="bp-fig-mobile">{% include llm-bioseq-probe/method-mobile.svg %}</div>
  <figcaption>Shuffling keeps a protein's letters and loses their order, so the gap is what the model knows about order. Percentages are over all 668 proteins; the shuffled row is schematic.</figcaption>
</figure>

The proteins come from 167 Pfam "domain of unknown function" families with no solved structure and at most 3 papers, and none has a UniProt relative within 90% identity. Each model answered 6,680 questions through its own API, with thinking off or at its lowest setting.

## Only Claude Opus 5.5 shows it

<figure class="bp-figure" markdown="0">
  <img src="{{ '/assets/img/llm-bioseq-probe/fig1_protein.png' | relative_url }}" alt="Forest plot of the real-minus-shuffled gap for 17 models; Claude Opus 5.5 at +27.4 points, every non-Claude model between 0 and 3.">
  <figcaption>Filled points: the chat prompt. Hollow points: raw next-token continuation of the FASTA text, through a completion endpoint or a prefilled reply, for models that allow it.</figcaption>
</figure>

The gap for Opus 5.5 has a 95% CI of 24.7 to 30.1 points and appears in 95% of families. The open-weight models were run as raw next-token continuation of the FASTA text, the way they were trained, and still show nothing.

## The fingerprint of training data

<figure class="bp-figure" markdown="0">
  <img src="{{ '/assets/img/llm-bioseq-probe/fig5_family_size.png' | relative_url }}" alt="Line chart: Claude Opus 5.5's gap rises from 21 points in families of 300 to 1,000 proteins to 37 points in families over 10,000; other models stay near zero.">
</figure>

A model that learned from sequence data should know big families better than small ones, and Opus 5.5 does: 21 points for families of 300 to 1,000 proteins, 37 for families over 10,000 (Spearman 0.27, p = 0.0002). Opus 4.8 and Opus 5 show the same slope at a lower level. Two other explanations do not fit:

- **Not papers.** In the 128 families with no Europe PMC hit at all, the gap is 26.8 points and still grows with family size (rho 0.28, p = 0.001). Across families it does not track paper counts (rho 0.05).
- **Not reasoning.** On the 55% of questions where Opus 5.5 wrote 15 tokens or fewer, barely more than the answer, it is right 35.6% of the time (shuffled: 7.3%). GPT-6 Astra thinks for 200+ tokens per question and reaches about 10%.

## Famous proteins prove little

<figure class="bp-figure" markdown="0">
  <img src="{{ '/assets/img/llm-bioseq-probe/fig3_known_vs_obscure.png' | relative_url }}" alt="Dumbbell chart: on well-known proteins many models score high; on obscure proteins only recent Claude Opus models do.">
</figure>

On well-studied vertebrate proteins many models do well: Gemini 4 Carbon gains 47.6 points, and several models recite hundreds of residues letter for letter (Appendix B). These sequences are printed in papers and mirrored across the web. Gemini 4 Carbon recites them, yet is at chance on the obscure bacterial set.

This is also why our result does not contradict the SOD1 post or PG-LLM. Ranking variants of a well-studied protein can draw on biology and the literature: which positions are buried, which substitutions break a helix, which mutations are known in ALS. PG-LLM's flat accuracy across alignment depth, and its gains with more thinking, point to that route. Our test closes it off. GPT-6 has the first ability and little of the second; Opus 5.5 has both.

## What this shows, and what it does not

- **Shows:** Claude Opus 5.5 was trained on protein sequence data at scale, enough to learn the statistics of families no paper describes. The signal starts small in Opus 4.8 and Opus 5 and jumps in Opus 5.5.
- **Shows:** on DNA the signal stops at well-known coding sequence. Opus 5.5 predicts human and mouse coding DNA but not promoters, introns or intergenic DNA, and barely the bacterial genes behind the very proteins it predicts well (+6 points as DNA against +27 as protein). Its training data held protein sequences, not the genomes they come from (Appendix A).
- **Does not show:** whether the data was a deliberate sequence corpus or crawled database pages, or whether it entered in pretraining or a later phase.
- **Does not show:** that other models never saw sequences, only that we find no sign of it.
- **Does not show:** verbatim memory of these obscure proteins. Asked for 200 more residues, Opus 5.5 rarely gets past 10 in a row. Training left it the families' statistics, not each protein's letters.

### Test your own model

Code, test sets, every model reply and the figures are in [llm-bioseq-probe](https://github.com/XinmingTu/LLM-bioseq-probe). One command scores a new model:

<div class="bp-cmd" markdown="1">
`uv run probe-model --model <id> --provider <anthropic | openai_chat | openai_responses | gemini | fireworks> --run`
</div>

**Cite this post**

```bibtex
@misc{tu2026bioseq,
  author = {Tu, Xinming},
  title  = {Claude Opus 5.5 was trained on protein sequence data},
  year   = {2026},
  month  = nov,
  url    = {https://xinmingtu.cn/blog/preview/claude-opus-5-5-protein-sequences/},
  note   = {Blog post}
}
```

## Appendix

### A. DNA

<figure class="bp-figure" markdown="0">
  <img src="{{ '/assets/img/llm-bioseq-probe/fig2_dna.png' | relative_url }}" alt="Forest plot by genomic region: Claude Opus 5.5 predicts human and mouse coding sequence; nothing clear elsewhere.">
</figure>

220-nucleotide windows, 200 shown and 20 to predict, from hg38, mm39 and the bacterial genes behind the test proteins, 500 per region. Non-coding windows contain no repeats, and the control shuffles each window keeping its dinucleotide counts. Opus 5.5 wrote all 20 nucleotides right 25 times in 500 human coding windows; a blind guess does that about once in a trillion. Gemini 4 Carbon blocks most DNA prompts before answering, so it is not shown.

### B. Reciting famous proteins

<figure class="bp-figure" markdown="0">
  <img src="{{ '/assets/img/llm-bioseq-probe/fig4_recall.png' | relative_url }}" alt="Bar chart: how often each model continues a famous protein letter for letter for 50, 100 and 200 residues.">
</figure>

At 158 points in well-studied proteins, each model was asked for the next 200 residues. Opus 5.5 goes past 100 residues 24 times (longest 305), Gemini 4 Carbon 23 times (longest 201), Opus 5 14 times (longest 325). GPT-6.1 Sol never reaches 100 and GPT-5.5 never passes 2.

### C. Robustness

- **Prompt format.** Asking Opus 5.5 to copy the sequence and then continue gives the same gap as the standard prompt (19.3 vs 19.8 points on the same subset of questions).
- **Refusals.** Non-answers are excluded and counted: 1% for Opus 5.5. Counting them as wrong moves its gap by under 1 point. GPT-4o, DeepSeek, Qwen, Kimi, GLM and gpt-oss often declined to guess a sequence; a best-guess prompt made them answer and did not change the picture.
- **A first round.** A smaller run of 20 models on 37 families, half well-known and half obscure, gave the same picture and set the design of the main run.

### D. Methods

Each protein is cut at 5 random points inside its Pfam domain; the model sees the start in FASTA format (60-character lines) and returns the next 10 residues; only the first is scored. The shuffled copy uses a fixed seed per protein. Intervals are 95% bootstraps over families (10,000 resamples), the main test a one-sided sign-flip permutation test over families. The analysis plan for the main run was written before it. Total API cost was about $450.

### E. Safety behaviour seen along the way

Gemini 4 Carbon blocked about 75% of DNA prompts before generating anything. OpenAI rejected 23 GPT-6 requests as possible biological misuse. Claude Sonnet 4.5 refused 97% of requests that prefilled its reply with a protein sequence.
