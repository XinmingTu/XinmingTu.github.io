---
layout: distill
title: "Claude was trained on protein sequences at scale"
description: "A next-amino-acid test on little-studied proteins finds that the latest Claude models were trained on protein sequences at scale. Other frontier models show no sign of it."
date: 2026-11-16
tags: ['AI', 'biology', 'LLM', 'evaluation']
categories: blog
og_image: https://xinmingtu.cn/assets/img/llm-bioseq-probe/social_card.png
bibliography: 2026-11-16-claude-opus-5-5-protein-sequences.bib

toc:
  - name: "Motivation"
  - name: "Method: next-amino-acid prediction on little-studied proteins"
  - name: "Results: only the latest Claude models predict them"
  - name: "Comparison with protein language models"
  - name: "Evidence that this comes from training data"
  - name: "Famous proteins and variant ranking"
  - name: "What this means"
  - name: "Code and data"
  - name: "Appendix"

authors:
  - name: Xinming Tu
    url: "https://xinmingtu.cn"
    affiliations:
      name: University of Washington, Phylo
  - name: Leo Tianlai Chen
    url: "https://www.leozang.com/"
    affiliations:
      name: Harvard Medical School

_styles: |
  /* Keep the article header and reading column on the same grid. */
  @media (min-width: 768px) {
    html body d-title h1 {
      font-size: 38px;
      line-height: 1.18;
      letter-spacing: -0.025em;
    }
    html body d-title p {
      font-size: 18px;
      line-height: 1.55;
    }
  }
  @media (min-width: 768px) and (max-width: 1179px) {
    html body d-title,
    html body d-byline,
    html body d-article {
      grid-template-columns: [screen-start] minmax(16px, 1fr) [page-start middle-start text-start] repeat(8, minmax(0, 63.5px)) [text-end middle-end page-end] minmax(16px, 1fr) [screen-end];
      column-gap: 16px;
    }
    d-article d-contents {
      grid-column: text;
      grid-row: auto;
      justify-self: stretch;
      width: auto;
      padding: 1rem;
      margin: 0 0 1.5rem;
      border: 1px solid var(--global-divider-color);
      display: block;
    }
  }
  @media (min-width: 1180px) {
    html body d-title,
    html body d-byline,
    html body d-article {
      grid-template-columns: [screen-start] 1fr [page-start kicker-start] 60px [middle-start] 60px [text-start kicker-end] repeat(8, minmax(0, 53px)) [text-end gutter-start] 60px [middle-end] 60px [page-end gutter-end] 1fr [screen-end];
      column-gap: 32px;
    }
    d-article > figure.bp-figure:not(.bp-wide) {
      grid-column: middle;
    }
  }
  /* Keep the affiliation on one line in the byline. */
  d-byline .affiliation { white-space: nowrap; }
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
  /* Serif body, sans headings, tighter leading. */
  d-article p, d-article li, d-article .bp-lede {
    font-family: "Source Serif 4", Charter, "Bitstream Charter", Georgia, serif;
    font-size: 17.5px; line-height: 1.5;
  }
  html body d-article h2 { color: var(--bp-ink); font-size: 26px; font-weight: 600; letter-spacing: -0.01em; line-height: 1.25; margin-top: 2.2rem; margin-bottom: 0.6em; }
  html body d-article h3 { font-size: 19px; font-weight: 600; line-height: 1.3; }
  @media (min-width: 768px) { html body d-title h1 { font-size: 34px; font-weight: 600; } }
  d-article .bp-lede {
    border-left: 3px solid var(--bp-accent);
    font-size: 1.06rem; line-height: 1.7;
    margin: 0.3rem 0 2rem; padding: 0.1rem 0 0.1rem 1rem;
  }
  d-article .bp-lede p { margin: 0 0 0.6rem; }
  d-article .bp-lede strong { color: var(--bp-ink); }
  d-article p strong, d-article li strong { font-weight: 700; }
  d-article figure.bp-figure { margin: 1.6rem 0 2rem; }
  @media (min-width: 1000px) {
    d-article > figure.bp-wide { grid-column: page; justify-self: center; width: 100%; max-width: 860px; }
  }
  d-article figure.bp-figure img, d-article figure.bp-figure svg { display: block; width: 100%; height: auto; }
  /* Data figures are inline SVG; their colours follow the page theme. */
  d-article { --fig-ink: #1d2433; --fig-muted: #6b7385; --fig-grid: #eceef2; --fig-grey: #a3aab8; --fig-light: #d3d7df; --fig-bg: #ffffff; --fig-accent-text: #b4532f; --fig-gpt-61: #2c2c33; --fig-gpt-6: #4b4b55; --fig-gpt-55: #7c7c87; --fig-c-s45: #f6dfd4; --fig-c-o45: #f3d3c4; --fig-c-o46: #efc1ab; --fig-c-o47: #eaad92; --fig-c-o48: #e59c7d; --fig-c-o5: #df8a68; --fig-c-f51: #c0694c; --fig-c-f52: #9c3a1c; --fig-bar-50: #e6e9ef; --fig-bar-100: #c5cbd6; --fig-bar-200: #8b93a3; }
  html[data-theme='dark'] d-article { --fig-ink: #e6e8ee; --fig-muted: #a0a8b8; --fig-grid: #30353f; --fig-grey: #7d8596; --fig-light: #4a505c; --fig-bg: var(--global-bg-color, #1c1c1d); --fig-accent-text: #eda48a; --fig-gpt-61: #ececf1; --fig-gpt-6: #c2c2cc; --fig-gpt-55: #8e8e9a; --fig-c-s45: #5e3e31; --fig-c-o45: #6a4535; --fig-c-o46: #7d4f3b; --fig-c-o47: #925a41; --fig-c-o48: #a86548; --fig-c-o5: #bf6f4e; --fig-c-f51: #e8906c; --fig-c-f52: #ffb08a; --fig-bar-50: #353a45; --fig-bar-100: #555c6a; --fig-bar-200: #8b93a3; }
  d-article .bp-svg svg { display: block; width: 100%; height: auto; }
  d-article figure.bp-figure figcaption {
    color: var(--bp-muted); font-size: 0.83rem; line-height: 1.45; margin-top: 0.65rem;
  }
  d-article .bp-fig-mobile { display: none; }
  @media (max-width: 600px) {
    d-article .bp-fig-desktop { display: none; }
    d-article .bp-fig-mobile { display: block; }
  }
---
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400&display=swap">


<div class="bp-lede" markdown="1">
**The latest Claude models were trained on protein sequences, at scale.** Give Claude Fable 5.2 or Claude Opus 5.5 the start of a little-studied bacterial protein and they predict the next amino acid. Shuffle the protein and they can't. No other model we tested can do this. Like a protein language model, they do better on bigger protein families, and they do it even in families with no papers at all. Fable 5.2 beats every open protein language model we ran, and Opus 5.5 is level with ProtGPT3-10B, the largest of them.
</div>

## Motivation

Frontier LLMs have started to look good at protein tasks. Atharv Jayprakash<d-cite key="jayprakash2026sod1"></d-cite> showed GPT-6 Astra ranking SOD1 variants as well as ESM-2, and PG-LLM<d-cite key="arora2026pgllm"></d-cite> found the same across many proteins. Did these models learn from protein sequence databases such as UniProt, or from what is written about proteins?

Famous proteins can't tell the two apart: GFP is printed in countless papers, and most frontier models recite it. So we tested proteins that almost nobody writes about.

## Method: next-amino-acid prediction on little-studied proteins

We give a model the start of a protein and ask for the next amino acids. Then we ask again on a shuffled copy of the same protein. Shuffling keeps the letters and destroys their order, so the difference in accuracy measures what the model knows about the sequence itself.

<figure class="bp-figure bp-wide" markdown="0">
  <div class="bp-fig-desktop">{% include llm-bioseq-probe/method.svg %}</div>
  <div class="bp-fig-mobile">{% include llm-bioseq-probe/method-mobile.svg %}</div>
  <figcaption>Percentages are Claude Opus 5.5's accuracy over all 668 proteins. The real row and its answer come from the test set; the shuffled row is schematic.</figcaption>
</figure>

The test set is 668 bacterial and archaeal proteins from 167 Pfam families of unknown function. No family has a solved structure or more than three papers, and no protein has a close relative in UniProt. Each protein is cut at five points. At each cut the model writes the next 10 amino acids, and we score the first. Thinking is at its lowest setting. Appendix E has the details.

## Results: only the latest Claude models predict them

<figure class="bp-figure" markdown="0">
  <div class="bp-svg" role="img" aria-label="Forest plot of the real-minus-shuffled gap for 20 language models: Claude Fable 5.2 at +45.1 points, Claude Opus 5.5 at +27.4, Claude Fable 5.1 at +14.9, earlier Claude Opus models up to 10, every other model between 0 and 3.">{% include llm-bioseq-probe/fig1_protein.svg %}</div>
  <figcaption>Filled points: the chat prompt. Hollow points: raw next-token continuation of the FASTA text, through a completion endpoint or a prefilled reply, for models that allow it.</figcaption>
</figure>

Fable 5.2 gets the next amino acid right 54% of the time on real proteins and 9% on shuffled ones. The gap is there in nearly every family, not just a few easy ones. It appears in Opus 4.7, jumps in Opus 5.5, and jumps again in Fable 5.2. GPT, Gemini and the seven open-weight models (DeepSeek V4.1 Flash, Qwen 3.8, Kimi K3.1 Pro, GLM-5.3, MiniMax M3, gpt-oss-120b and Nemotron 3 Ultra) stay near zero, even when they simply continue raw FASTA text, the way they were trained. The latest Claude models also write runs of correct residues that other models rarely manage (Appendix B).

## Comparison with protein language models

Protein language models learn only from sequences, so they are the natural yardstick. The closest to an LLM are the ones that read a protein left to right and predict the next residue: ProtGPT3<d-cite key="garibbo2026protgpt3"></d-cite>, whose 10-billion-parameter version is the largest open one, and ProGen3<d-cite key="bhatnagar2025progen3"></d-cite>, whose largest public version has 3 billion. On the same input, Fable 5.2 beats both by a wide margin. Opus 5.5 is level with ProtGPT3-10B and below ProGen3-3B.

<figure class="bp-figure" markdown="0">
  <div class="bp-svg" role="img" aria-label="Dot plot: Claude Fable 5.2 +45.1 at the top, then ProGen3-3B +32.5, ProtGPT3-10B +27.7 and Claude Opus 5.5 +27.4; ESM C 600M +13.0, ProtGPT3-1.3B +11.6, ProtGPT2 +10.2, ESM3-open +8.5 and ESM-2 650M +7.0 well below.">{% include llm-bioseq-probe/fig6_protein_lm.svg %}</div>
</figure>

ESM models are trained to see both sides of a residue, so continuing from the left is harder for them. Appendix C has all eight models.

## Evidence that this comes from training data

If the models learned from sequences, families with more sequences should be easier. To test this over a wide range, we added 90 smaller families, down to 20 proteins each, for 257 families in all.

<figure class="bp-figure" markdown="0">
  <div class="bp-svg" role="img" aria-label="Line chart over seven family-size bins from 20 to over 10,000 proteins: Claude Opus 5.5, ProtGPT3-10B and ProGen3-3B rise together; Claude Fable 5.2 rises fastest and levels off from about 300 proteins; Fable 5.1 and Opus 4.7 to 5 rise at a lower level; Opus 4.5 and 4.6, GPT and Gemini stay near zero.">{% include llm-bioseq-probe/fig5_family_size.svg %}</div>
</figure>

They are. Opus 5.5 rises with the two protein language models, ProtGPT3-10B and ProGen3-3B, which are trained on nothing but sequences. Fable 5.2 rises fastest and levels off at about 300 proteins per family. Earlier Claude models rise at a lower level, and GPT and Gemini stay near zero.

Two other explanations don't fit:

- **Papers.** In the 128 families with no papers at all, both models do as well as on the whole set.
- **Reasoning.** Most answers involve no thinking at all: the API reports thinking tokens on 9% of Fable 5.2's answers and 36% of Opus 5.5's. The answers without thinking are just as accurate. GPT-6 Astra and GPT-6.1 Sol think for hundreds of tokens per question and stay near zero.

## Famous proteins and variant ranking

Famous proteins are a different story. Many models do well on them, and several recite hundreds of residues letter for letter (Appendix B), because these sequences are all over papers and the web. In a first round with famous and obscure proteins side by side, Gemini 4 Carbon was strong on the famous ones and dropped to almost nothing on the obscure ones. The latest Claude models and ProtGPT3-10B held up, and Fable 5.2 was the strongest on both.

<figure class="bp-figure" markdown="0">
  <div class="bp-svg" role="img" aria-label="Dumbbell chart: on well-known proteins many models score high; on obscure proteins Claude Fable 5.2, Claude Opus 5.5 and ProtGPT3-10B stay high while Gemini 4 Carbon drops to near zero.">{% include llm-bioseq-probe/fig3_known_vs_obscure.svg %}</div>
</figure>

This also explains the SOD1 and PG-LLM results. Ranking variants of a well-known protein can lean on what is written about it: which residues are buried, which substitutions break a helix, which mutations cause ALS. In PG-LLM, accuracy doesn't depend on alignment depth and improves with more thinking, both signs of that route. Our test shuts it out. GPT-6 is good at the first kind of task and weak at the second; the latest Claude models are good at both.

## What this means

The latest Claude models know protein families that almost nobody has studied. That takes a lot of sequence data, not a few examples: protein sequences were a sizeable part of their training. Opus 5.5 behaves like a protein language model, and Fable 5.2 goes beyond the best one we could run. GPT and Gemini show none of this. Whatever protein sequence they saw in training, it was not enough to learn these families.

DNA is different. Opus 5.5 predicts human and mouse coding sequence but not the rest of the genome, and barely the bacterial genes behind the proteins it knows (Appendix A). It learned proteins, not genomes.

## Code and data

All code, test sets, model outputs and figures are in [llm-bioseq-probe](https://github.com/XinmingTu/LLM-bioseq-probe).

**Cite this post**

```bibtex
@misc{tu2026bioseq,
  author = {Tu, Xinming and Chen, Leo Tianlai},
  title  = {Claude was trained on protein sequences at scale},
  year   = {2026},
  month  = nov,
  url    = {https://xinmingtu.cn/blog/2026/claude-opus-5-5-protein-sequences/},
  note   = {Blog post}
}
```

## Appendix

### A. DNA

<figure class="bp-figure" markdown="0">
  <div class="bp-svg" role="img" aria-label="Forest plot by genomic region: Claude Opus 5.5 predicts human and mouse coding sequence; nothing clear elsewhere.">{% include llm-bioseq-probe/fig2_dna.svg %}</div>
</figure>

220-nucleotide windows, 200 shown and 20 to predict, from hg38, mm39 and the bacterial genes behind the test proteins, 500 per region. Non-coding windows contain no repeats, and the control shuffles each window keeping its dinucleotide counts. Opus 5.5 wrote all 20 nucleotides right 25 times in 500 human coding windows; a blind guess does that about once in a trillion. Gemini 4 Carbon blocks most DNA prompts before answering, so it is not shown.

### B. Longer continuations

**All 10 residues right.** Each question asks for the next 10 residues. On the 668 little-studied proteins, Claude Fable 5.2 gets all 10 right at 88 real cuts and Opus 5.5 at 12, and neither at any shuffled one. If their residues were independent guesses at their own per-residue accuracy, they would get 15.8 and 0.57 by chance.

**Runs in a row.** On shuffled proteins neither Fable 5.2 nor Opus 5.5 gets more than 3 residues in a row. Once on track they get surer: after one right residue, Opus 5.5 gets the next right 47% of the time, after four in a row 68%.

<figure class="bp-figure" markdown="0">
  <div class="bp-svg" role="img" aria-label="Line chart: share of replies whose first k residues are all right; Claude Opus 5.5 starts at 35% and stays above other models out to 10 residues, while its shuffled curve drops to zero by 3.">{% include llm-bioseq-probe/fig8_runs.svg %}</div>
</figure>

**Reciting well-known proteins.** At 158 points in well-studied proteins, each model was asked for the next 200 residues at once.

<figure class="bp-figure" markdown="0">
  <div class="bp-svg" role="img" aria-label="Bar chart: how often each model continues a famous protein letter for letter for 50, 100 and 200 residues.">{% include llm-bioseq-probe/fig4_recall.svg %}</div>
</figure>

GPT-6.1 Sol never reaches 100 residues, and GPT-5.5 never gets past 2.

### C. Protein language models

| Model | Reads | Input | Real | Shuffled | Real minus shuffled, points (95% CI) |
|---|---|---|---|---|---|
| ProGen3-3B | left to right | residues before the cut | 43.7% | 11.1% | +32.5 (29.3 to 35.7) |
| ProtGPT3-10B | left to right | residues before the cut | 38.4% | 10.7% | +27.7 (24.2 to 31.1) |
| ESM C 600M | both sides | residues before the cut | 24.1% | 11.2% | +13.0 (10.7 to 15.2) |
| ProtGPT3-1.3B | left to right | residues before the cut | 22.3% | 10.7% | +11.6 (8.9 to 14.4) |
| ProtGPT2 | left to right | residues before the cut | 19.0% | 8.8% | +10.2 (8.3 to 12.2) |
| ESM3-open 1.4B | both sides | residues before the cut | 19.6% | 11.0% | +8.5 (6.4 to 10.7) |
| ESM-2 650M | both sides | residues before the cut | 17.3% | 10.3% | +7.0 (5.2 to 8.9) |
| ESM-2 650M | both sides | residues on both sides of the cut | 45.7% | 11.1% | +34.6 (31.8 to 37.3) |

ProtGPT3-10B gets more answers right than Opus 5.5 (38.4% vs 34.9%) but also more on shuffled proteins (10.7% vs 7.5%), because it knows amino acid composition better; the gap between the two, which is what each model knows about order, comes out the same. The last row is fill-in-the-blank rather than continuation: ESM-2 also sees the residues after the cut, which the LLMs never get. Every model first passed a sanity check on well-known proteins. Continuing ubiquitin and hemoglobin β from the left, ProGen3-3B gets 98% and 87% of residues right and ProtGPT3-10B 100% and 84%; with the whole protein and one residue masked, ESM-2 gets 80% of ubiquitin, ESM C and ESM3-open 100%. Masks are set on token ids, because the ESM SDK's "_" character is not ESM C's mask token. ProtGPT2 uses multi-residue tokens, so a residue's probability is the sum over the tokens that start with it; ProGen3 and ProtGPT3 use one token per residue.

### D. Robustness

- **Across families.** The gap is positive in 98% of families for Fable 5.2 and 94% for Opus 5.5.
- **Family size.** Over all 257 families, the Spearman correlation between a family's gap and the log of its size is 0.50 for Opus 5.5, 0.48 for ProGen3-3B, 0.46 for ProtGPT3-10B, 0.38 for Fable 5.2, and 0.30 to 0.48 for Fable 5.1 and Opus 4.7 to 5 (all p < 10<sup>-6</sup>); for Opus 4.5 and 4.6 it is about 0.
- **Papers.** In the 128 families with no papers at all, the gap is 45.9 points for Fable 5.2 and 26.8 for Opus 5.5, against 45.1 and 27.4 over all 167. For Opus 5.5 it still rises with family size there (Spearman 0.28, p = 0.001), and across families it is unrelated to the number of papers (Spearman 0.05).
- **Prompt format.** Asking Opus 5.5 to copy the sequence first and then continue gives the same gap as the standard prompt on the same 400 questions (12.0 vs 12.0 points; this subset comes from 10 families).
- **Refusals.** Non-answers (0.1% for Opus 5.5) are excluded; counting them as wrong changes its gap by under 1 point. GPT-4o, DeepSeek, Qwen, Kimi, GLM and gpt-oss often declined to guess; a best-guess prompt made them answer, with the same result.
- **No instruction.** Sent the sequence alone, GPT-5.5 and Opus 5.5 almost always describe it instead of continuing it (on a sample of 400 questions each), so chat models need the instruction.
- **Claude Fable 5.** Anthropic's usage-policy filter blocked 44% of Fable 5's questions, so it is left out of the main figures. On the questions it answered its gap is 13.9 points; counting blocked questions as wrong gives 11.6, and keeping only the cuts answered on both the real and the shuffled protein gives 14.6, close to Fable 5.1's 14.9. Fable 5.1 and 5.2 were blocked 2.5% and 0% of the time.
- **Repeat runs.** Asked 400 of the same questions again, Fable 5.2 scores 57.5% on real and 9.5% on shuffled proteins, against 57.5% and 8.5% the first time.
- **A first round.** A smaller run of 23 models on 37 families, half well-known and half obscure, gave the same picture and set the design of the main run.

### E. Methods

**Choosing the proteins.** We started from every Pfam family whose name says "domain of unknown function" (DUF) or "protein of unknown function", and kept those with no structure in the PDB, at most 3 Europe PMC hits for the family's accession, and at least 300 member proteins. We binned them by size (300 to 1,000 proteins, 1,000 to 3,000, 3,000 to 10,000, over 10,000) and drew 50 families per bin at random; only 17 families qualify above 10,000, so the set has 167. From each family we took 4 proteins from UniProt that are unreviewed (TrEMBL), come from Bacteria or Archaea, are 120 to 800 residues long, use only the 20 standard amino acids, are not low-complexity (Shannon entropy above 3.9 bits per residue), and are alone in their UniRef90 cluster, so no other UniProt protein is 90% or more identical to them. That gives 668 proteins.

**Smaller families.** For the family-size test we drew 30 more families in each of three smaller bins (20 to 60, 60 to 150 and 150 to 300 proteins) with the same criteria and 4 proteins per family, 360 proteins in all. Every model gets the same prompt and scoring as on the main set.

**Cutting.** Each protein is cut at 5 positions drawn at random inside its Pfam domain (the longest domain span, at least 40 residues), at least 10 residues from either end of the domain and with at least 30 residues before the cut: 3,340 cuts. Everything before the cut is the prefix; the residue right after it is the answer.

**Asking.** The model gets this message, with the prefix in 60-character lines (an example from one of the test proteins):

```
Below is the beginning of a protein sequence in one-letter amino acid codes.
Predict how it continues. Reply with exactly the next 10 amino acids as
one-letter codes on one line, and nothing else.

>sequence
MRSGGQPLHPQPAHRFHYRTAARPRAAWILGCVLHLADAEEGARFWWQYAAGAGDDAAAY
CLYLHCLVLGDSYAAALWREQTSLDTPPHDFDDTSVPTVLRILSRLTPA
```

Each model runs through its own API with temperature 0 where it is accepted, thinking off or at its lowest setting (for Opus 5.5 and the Fable models, low effort, at which the model still decides whether to think), no tools, and one sample per question. The Claude Fable models run through OpenRouter, since Anthropic's API serves them only to workspaces that retain data. Models that declined to guess (GPT-4o, DeepSeek, Qwen, Kimi, GLM, gpt-oss) also got a version that adds "Give your best guess even if you are uncertain. Do not explain or refuse."; those runs are marked separately.

**Thinking.** A reply counts as thought about when the API reports thinking tokens for it: `thinking_tokens` in Anthropic's usage report, `reasoning_tokens` in OpenRouter's. The thinking text itself is not kept; only the visible reply is scored. Fable 5.2 thought on 9% of questions, Opus 5.5 on 36%, Fable 5.1 never. Without thinking, Fable 5.2 is right 54.7% of the time on real proteins and 8.8% on shuffled ones (48.2% and 10.6% with thinking), and Opus 5.5 35.3% and 6.9% (34.1% and 8.6%).

**Scoring.** We read the last sequence the reply states: a run of capital amino-acid letters on its own line or after a label such as "Answer:", skipping words, lists and anything inside thinking tags. If it starts by restating the end of the prefix, the restatement is dropped. Its first letter is the predicted next amino acid. A reply cut off at the length limit counts only if it opens with a sequence. Replies that state no sequence are excluded and counted (0.1% for Opus 5.5). Only the first residue is scored; the full 10 are used for exact continuations and runs. The same reader is used for every model and for real and shuffled proteins.

**The shuffled control.** Each protein's residues are shuffled once, with a random seed fixed by its accession, and the same 5 cut positions are asked on the shuffled sequence. The shuffle keeps the composition of the whole protein and destroys the order, so a model that knows only which amino acids are common scores the same on both.

**Statistics.** For each family we compute the share of correct first residues on real and on shuffled cuts, and take the difference, in percentage points. The result for a model is the mean of that gap over the 167 families. Intervals are 95% bootstraps over families (10,000 resamples), the main test is a one-sided sign-flip permutation test over families, and the family-size trend is the Spearman correlation between a family's gap and the logarithm of its size.

**Raw continuation.** For models that allow it, the same prefix is sent without any instruction, as the text ">sequence" followed by the FASTA lines, through a plain completion endpoint (open-weight models on Fireworks) or as the start of the model's own reply (Gemini 2.5 Pro). The first letter the model writes is scored as above.

**Protein language models.** They get the same prefix and no prompt. ProGen3, ProtGPT3 and ProtGPT2 read it left to right and give a probability for the next token; the ESM models see the prefix, a mask in place of the next residue, and the end of the sequence. In every case the prediction is the most likely of the 20 standard amino acids.

Total API cost was about $730, plus a few dollars of GPU time for the protein language models.

### F. Safety behaviour seen along the way

Gemini 4 Carbon blocked about 75% of DNA prompts outright. OpenAI rejected 23 GPT-6 requests in the first round and 17 GPT-6.1 Sol requests in the main run as possible biological misuse. Claude Sonnet 4.5 refused 97% of requests that started its reply with a protein sequence, and Anthropic's filter blocked 44% of Claude Fable 5's questions as cyber content.
