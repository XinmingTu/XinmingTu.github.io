---
layout: distill
title: "The latest Claude models were trained on protein sequences at scale"
description: "A next-amino-acid test on little-studied proteins, with a shuffled control, finds sequence data in the latest Claude models' training and no sign of it in other frontier models."
date: 2026-11-16
tags: ['AI', 'biology', 'LLM', 'evaluation']
categories: blog
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
---

<div class="bp-lede" markdown="1">
**The latest Claude models were trained on protein sequences, at scale.** Give Claude Fable 5.2 or Claude Opus 5.5 the start of a little-studied bacterial protein and it predicts the next amino acid far better than when the same protein is shuffled. No other model we tested can do this: not GPT, not Gemini, not seven open-weight models. The ability first appears in Opus 4.7, grows in Opus 5.5, which matches ProtGPT3-10B, the largest open protein language model of its kind, and is strongest in Fable 5.2, which beats it by a wide margin. It holds even in protein families with no papers at all.
</div>

## Motivation

Atharv Jayprakash<d-cite key="jayprakash2026sod1"></d-cite> showed GPT-6 Astra ranking SOD1 variants as well as ESM-2, and PG-LLM<d-cite key="arora2026pgllm"></d-cite> found the same for frontier models across many proteins. That raises a simple question: were these models trained on protein sequence databases like UniProt?

Famous proteins can't tell us. GFP is printed in countless papers and web pages, and 9 of 12 frontier models continue it exactly. So we tested proteins that almost nobody writes about.

## Method: next-amino-acid prediction on little-studied proteins

We give a model the start of a protein and ask for the next amino acids, then ask again on a shuffled copy of the same protein. Shuffling keeps the letters and destroys their order, so the difference in accuracy is what the model knows about the order of residues.

<figure class="bp-figure bp-wide" markdown="0">
  <div class="bp-fig-desktop">{% include llm-bioseq-probe/method.svg %}</div>
  <div class="bp-fig-mobile">{% include llm-bioseq-probe/method-mobile.svg %}</div>
  <figcaption>Percentages are Claude Opus 5.5's accuracy over all 668 proteins. The real row and its answer come from the test set; the shuffled row is schematic.</figcaption>
</figure>

The proteins are little-studied: 668 of them, from 167 Pfam families of unknown function. None of these families has a solved structure, each has at most three papers, and no protein in the set has a close relative in UniProt (90% identity or more). We cut each protein at five random points, ask for the next residues and score the first one: 6,680 questions per model, counting the shuffled copies. Thinking is off or at its lowest setting.

We also looked at longer continuations: how often a model gets all 10 requested residues right, and how far it can recite a famous protein when asked for 200 residues (Appendix B).

## Results: only the latest Claude models predict them

<figure class="bp-figure" markdown="0">
  <img src="{{ '/assets/img/llm-bioseq-probe/fig1_protein.png' | relative_url }}?v=20261117e" alt="Forest plot of the real-minus-shuffled gap for 20 language models: Claude Fable 5.2 at +45.1 points, Claude Opus 5.5 at +27.4, Claude Fable 5.1 at +14.9, earlier Claude Opus models up to 10, every other model between 0 and 3.">
  <figcaption>Filled points: the chat prompt. Hollow points: raw next-token continuation of the FASTA text, through a completion endpoint or a prefilled reply, for models that allow it.</figcaption>
</figure>

Fable 5.2 gets the next amino acid right 54% of the time on real proteins and 9% on shuffled ones, a gap of 45.1 points (95% CI 42.5 to 47.6) that shows up in 98% of families. Opus 5.5's gap is 27.4 points (24.7 to 30.0), in 95% of families. Within the Opus line, Opus 4.5 and 4.6 show nothing, Opus 4.7 to 5 reach 8 to 10 points, and Opus 5.5 jumps to 27. Fable 5.1 is at 14.9 points, so most of Fable 5.2's lead is new in that release. All three GPT models, the newest GPT-6.1 Sol included, stay below 3 points, and the open-weight models stay flat even when they simply continue the raw FASTA text, the way they were trained. The lead is not just on the first residue: at the tenth residue Fable 5.2 is still 38.7 points ahead and Opus 5.5 18.5, and both write runs of correct residues that no other model, and no shuffled protein, gets close to (Appendix B).

## Comparison with protein language models

Protein language models learn only from sequences, which makes them a natural yardstick. The closest match to an LLM is ProtGPT3<d-cite key="garibbo2026protgpt3"></d-cite>, released this year: it reads a protein left to right and predicts the next residue, and its 10-billion-parameter version is the largest open model of its kind. Given exactly the same input, Opus 5.5 matches it and Fable 5.2 beats it by 17 points.

<figure class="bp-figure" markdown="0">
  <img src="{{ '/assets/img/llm-bioseq-probe/fig6_protein_lm.png' | relative_url }}?v=20261117e" alt="Dot plot: Claude Fable 5.2 +45.1 at the top, then ProtGPT3-10B +27.7 and Claude Opus 5.5 +27.4; ESM C 600M +13.0, ProtGPT3-1.3B +11.6, ProtGPT2 +10.2, ESM3-open +8.5 and ESM-2 650M +7.0 well below.">
</figure>

ProtGPT3-10B gets more answers right than Opus 5.5 (38.4% vs 34.9%), but it also does better on shuffled proteins (10.7% vs 7.5%) because it knows amino acid composition better, so the gap, which is what each model knows about order, comes out the same. Fable 5.2 gets 54.1% right on real proteins and 9.0% on shuffled ones. ESM models are built to see both sides of a residue, so this test is harder for them. Appendix D has all seven models.

## Evidence that this comes from training data

<figure class="bp-figure" markdown="0">
  <img src="{{ '/assets/img/llm-bioseq-probe/fig5_family_size.png' | relative_url }}?v=20261117e" alt="Line chart over seven family-size bins from 20 to over 10,000 proteins: Claude Opus 5.5 rises from 8 to 37 points and ProtGPT3-10B from 3 to 37, almost on top of each other; Claude Fable 5.2 rises from 20 to 44 by families of 300 to 1,000 proteins and then levels off.">
</figure>

If the signal comes from training on sequences, bigger families should be easier, because the model has seen more of their relatives. To cover a wide range of sizes we added 90 smaller families, 30 each with 20 to 60, 60 to 150 and 150 to 300 proteins, chosen the same way (Appendix F), for 257 families in all. Bigger families are easier:

- Opus 5.5 goes from 8 points in families of 20 to 60 proteins to 37 in families over 10,000, and ProtGPT3-10B, trained on nothing but sequences, from 3 to 37. Across the 257 families the Spearman correlation with family size is 0.50 for Opus 5.5 and 0.46 for ProtGPT3-10B.
- Fable 5.2 climbs fastest, from 20 points to 44 by families of 300 to 1,000 proteins, then levels off near 45. On the main set alone it looks flat because it has already reached its ceiling there.
- Every Claude model from Opus 4.7 on follows the same pattern (Spearman 0.30 to 0.50, all p < 10<sup>-6</sup>), while Opus 4.5 and 4.6 stay flat at zero, as do the GPT models (Appendix C).

Two other explanations for the signal don't hold up:

- **Papers.** In the 128 families with no papers at all, the gap is 26.8 points for Opus 5.5 and 45.9 for Fable 5.2, and for Opus 5.5 it still rises with family size (rho 0.28, p = 0.001). Across families it has nothing to do with how many papers exist (rho 0.05).
- **Reasoning.** Most answers come with no thinking at all. For every reply the API reports how many of its tokens were thinking, and we count a question as thought about when that number is above zero. Fable 5.2 thought on 9% of questions, Opus 5.5 on 36%, and Fable 5.1 never. On the questions with no thinking, Fable 5.2 is right 54.7% of the time on real proteins and 8.8% on shuffled ones, and Opus 5.5 35.3% and 6.9%, no lower than when they think. GPT-6 Astra and GPT-6.1 Sol think for hundreds of tokens per question and stay near 10%.

## Famous proteins and variant ranking

<figure class="bp-figure" markdown="0">
  <img src="{{ '/assets/img/llm-bioseq-probe/fig3_known_vs_obscure.png' | relative_url }}?v=20261117e" alt="Dumbbell chart: on well-known proteins many models score high; on obscure proteins Claude Opus 5.5 and ProtGPT3-10B stay high while Gemini 4 Carbon drops to near zero.">
</figure>

Famous proteins are a different story. Many models do well on them, and several recite hundreds of residues letter for letter (Appendix B), because these sequences are everywhere in papers and on the web. Gemini 4 Carbon scores +47.6 on famous vertebrate proteins and falls to +5.3 on obscure ones. Opus 5.5 holds up (+51.9 to +33.3), and so does ProtGPT3-10B (+51.4 to +38.2). This first round predates Fable 5.2 and GPT-6.1 Sol, so they are not in the figure.

This also squares our result with the SOD1 post and PG-LLM. Ranking variants of a well-known protein can lean on biology and the literature: which residues are buried, which substitutions break a helix, which mutations are known in ALS. In PG-LLM, accuracy doesn't change with alignment depth and improves with more thinking, both signs of that route. Our test shuts it out. GPT-6 is good at the first kind of task and weak at the second; the latest Claude models are good at both.

## What this means

The latest Claude models learned protein families that are barely studied, and that takes a lot of sequence data, not a few examples. How broad the signal is, and how closely Opus 5.5 tracks a protein language model, suggests protein sequences were a sizeable part of their training, possibly in pretraining, though our test can't say which phase or where the data came from. Fable 5.2 goes further than any protein language model we could run. On DNA the picture is narrower: Opus 5.5 predicts human and mouse coding sequence but not the rest of the genome, and barely the bacterial genes behind the very proteins it knows (Appendix A). It learned proteins, not genomes.

## Code and data

All code, test sets, model outputs and figures are in [llm-bioseq-probe](https://github.com/XinmingTu/LLM-bioseq-probe).

**Cite this post**

```bibtex
@misc{tu2026bioseq,
  author = {Tu, Xinming and Chen, Leo Tianlai},
  title  = {The latest Claude models were trained on protein sequences at scale},
  year   = {2026},
  month  = nov,
  url    = {https://xinmingtu.cn/blog/2026/claude-opus-5-5-protein-sequences/},
  note   = {Blog post}
}
```

## Appendix

### A. DNA

<figure class="bp-figure" markdown="0">
  <img src="{{ '/assets/img/llm-bioseq-probe/fig2_dna.png' | relative_url }}?v=20261117e" alt="Forest plot by genomic region: Claude Opus 5.5 predicts human and mouse coding sequence; nothing clear elsewhere.">
</figure>

220-nucleotide windows, 200 shown and 20 to predict, from hg38, mm39 and the bacterial genes behind the test proteins, 500 per region. Non-coding windows contain no repeats, and the control shuffles each window keeping its dinucleotide counts. Opus 5.5 wrote all 20 nucleotides right 25 times in 500 human coding windows; a blind guess does that about once in a trillion. Gemini 4 Carbon blocks most DNA prompts before answering, so it is not shown.

### B. Longer continuations

**All 10 residues right.** Each question asks for the next 10 residues. On the 668 little-studied proteins, Claude Fable 5.2 gets all 10 right at 88 real cuts and Opus 5.5 at 12, and neither at any shuffled one. If their residues were independent guesses at their own per-residue accuracy, they would get 15.8 and 0.56 by chance.

**Every position.** Scored one position at a time, the gap falls slowly: from 45.1 points at the first residue to 38.7 at the tenth for Fable 5.2, and from 27.4 to 18.5 for Opus 5.5. Fable 5.1 and Opus 4.7, 4.8 and 5 fade faster, and the other 14 models, including those run as raw continuation, stay near zero all the way.

<figure class="bp-figure" markdown="0">
  <img src="{{ '/assets/img/llm-bioseq-probe/fig7_by_position.png' | relative_url }}?v=20261117e" alt="Line chart: real-minus-shuffled gap at positions 1 to 10 of the reply; Claude Opus 5.5 falls from 27.4 to 18.5, Opus 4.7 to 5 from about 9 to between 2 and 5, other models near zero.">
</figure>

**Runs in a row.** Fable 5.2 gets the first 2 residues right 34% of the time, the first 5 11% and all 10 2.6%; Opus 5.5 16%, 3% and 0.4%. On shuffled proteins neither gets past 3. Once on track they get surer: after one right residue, Opus 5.5 gets the next right 47% of the time, after four in a row 68%.

<figure class="bp-figure" markdown="0">
  <img src="{{ '/assets/img/llm-bioseq-probe/fig8_runs.png' | relative_url }}?v=20261117e" alt="Line chart: share of replies whose first k residues are all right; Claude Opus 5.5 starts at 35% and stays above other models out to 10 residues, while its shuffled curve drops to zero by 3.">
</figure>

**Reciting well-known proteins.** At 158 points in well-studied proteins, each model was asked for the next 200 residues at once.

<figure class="bp-figure" markdown="0">
  <img src="{{ '/assets/img/llm-bioseq-probe/fig4_recall.png' | relative_url }}?v=20261117e" alt="Bar chart: how often each model continues a famous protein letter for letter for 50, 100 and 200 residues.">
</figure>

Opus 5.5 gets past 100 residues 24 times (longest run 305), Gemini 4 Carbon 23 times (201), Opus 5 14 times (325). GPT-6.1 Sol never reaches 100, and GPT-5.5 never gets past 2. 

### C. Family size for every model

<figure class="bp-figure" markdown="0">
  <img src="{{ '/assets/img/llm-bioseq-probe/fig5b_family_size_all.png' | relative_url }}?v=20261117e" alt="Line chart: the gap by family size for 12 language models and ProtGPT3-10B; Claude Fable 5.2, Opus 5.5 and ProtGPT3-10B rise steeply, Fable 5.1 and Opus 4.7 to 5 rise at a lower level, Opus 4.5 and 4.6, GPT and Gemini stay near zero.">
</figure>

| Model | 20–60 | 60–150 | 150–300 | 300–1k | 1k–3k | 3k–10k | >10k | Spearman |
|---|---|---|---|---|---|---|---|---|
| Claude Fable 5.2 | +19.5 | +24.0 | +35.5 | +44.1 | +46.0 | +46.4 | +41.5 | 0.38 |
| Claude Opus 5.5 | +7.9 | +7.4 | +14.4 | +21.2 | +26.0 | +31.7 | +36.7 | 0.50 |
| ProtGPT3-10B | +3.2 | +6.5 | +10.7 | +23.9 | +25.3 | +30.6 | +37.1 | 0.46 |
| Claude Fable 5.1 | +2.5 | −0.2 | +3.2 | +9.6 | +14.6 | +17.5 | +23.5 | 0.48 |
| Claude Opus 5 | −1.6 | −0.2 | +1.2 | +5.6 | +6.4 | +12.8 | +22.8 | 0.36 |
| Claude Opus 4.8 | +0.5 | +1.4 | +3.7 | +4.4 | +3.6 | +10.6 | +21.1 | 0.30 |
| Claude Opus 4.7 | +2.8 | −0.8 | +2.8 | +3.3 | +7.5 | +12.3 | +19.7 | 0.36 |
| Claude Opus 4.6 | −0.5 | +1.5 | +1.3 | +2.7 | −0.1 | +0.9 | −1.5 | −0.03 |
| Claude Opus 4.5 | +0.2 | +0.5 | −0.5 | +2.6 | +2.7 | +1.9 | −2.6 | 0.05 |
| GPT-5.5 | −2.2 | +0.8 | +0.7 | +2.7 | +0.4 | +2.6 | +3.8 | 0.14 |

Real minus shuffled, in points, by the number of proteins in the family; Spearman correlation of a family's gap with the log of its size, over all 257 families. GPT-6.1 Sol, GPT-6 Astra and Gemini 4 Carbon are still running on the small-family set and will be added.

### D. Protein language models

| Model | Reads | Input | Real | Shuffled | Real minus shuffled, points (95% CI) |
|---|---|---|---|---|---|
| ProtGPT3-10B | left to right | residues before the cut | 38.4% | 10.7% | +27.7 (24.2 to 31.1) |
| ESM C 600M | both sides | residues before the cut | 24.1% | 11.2% | +13.0 (10.7 to 15.2) |
| ProtGPT3-1.3B | left to right | residues before the cut | 22.3% | 10.7% | +11.6 (8.9 to 14.4) |
| ProtGPT2 | left to right | residues before the cut | 19.0% | 8.8% | +10.2 (8.3 to 12.2) |
| ESM3-open 1.4B | both sides | residues before the cut | 19.6% | 11.0% | +8.5 (6.4 to 10.7) |
| ESM-2 650M | both sides | residues before the cut | 17.3% | 10.3% | +7.0 (5.2 to 8.9) |
| ESM-2 650M | both sides | residues on both sides of the cut | 45.7% | 11.1% | +34.6 (31.8 to 37.3) |

The last row is fill-in-the-blank rather than continuation: ESM-2 also sees the residues after the cut, which the LLMs never get. Every model first passed a sanity check on well-known proteins. Continuing ubiquitin and hemoglobin β from the left, ProtGPT3-10B gets 100% and 84% of residues right; with the whole protein and one residue masked, ESM-2 gets 80% of ubiquitin, ESM C and ESM3-open 100%. Masks are set on token ids, because the ESM SDK's "_" character is not ESM C's mask token. ProtGPT2 uses multi-residue tokens, so a residue's probability is the sum over the tokens that start with it; ProtGPT3 uses one token per residue.

### E. Robustness

- **Prompt format.** Asking Opus 5.5 to copy the sequence and then continue gives the same gap as the standard prompt (19.3 vs 19.8 points on the same subset of questions).
- **Refusals.** Non-answers are excluded and counted: 1% for Opus 5.5. Counting them as wrong moves its gap by under 1 point. GPT-4o, DeepSeek, Qwen, Kimi, GLM and gpt-oss often declined to guess a sequence; a best-guess prompt made them answer and did not change the picture.
- **No instruction.** Sent the sequence alone, with no request to continue it, GPT-5.5 and Opus 5.5 almost always describe it instead (on a sample of 400 questions each), so chat models need the instruction.
- **Claude Fable 5.** Anthropic's usage-policy filter blocked 44% of Fable 5's questions, so it is left out of the main figures. On the questions it answered its gap is 13.9 points; counting blocked questions as wrong gives 11.6, and keeping only the cuts answered on both the real and the shuffled protein gives 14.6. Fable 5.1 and 5.2 were blocked 2.5% and 0% of the time.
- **Repeat runs.** Asked 400 of the same questions again, Fable 5.2 scores 57.5% on real and 9.5% on shuffled proteins, against 57.5% and 8.5% the first time.
- **A first round.** A smaller run of 20 models on 37 families, half well-known and half obscure, gave the same picture and set the design of the main run.

### F. Methods

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

**Thinking.** A reply counts as thought about when the API reports thinking tokens for it: `thinking_tokens` in Anthropic's usage report, `reasoning_tokens` in OpenRouter's. The thinking text itself is not kept; only the visible reply is scored.

**Scoring.** We take the last line of the reply, keep its letters and read the first one as the predicted next amino acid. A question counts only if that line contains nothing but the 20 standard letters; refusals and other non-answers are excluded and counted (1% for Opus 5.5). Only this first residue is scored. We asked for 10 so that the answer is a sequence rather than a single letter, and used the full 10 only to count exact continuations.

**The shuffled control.** Each protein's residues are shuffled once, with a random seed fixed by its accession, and the same 5 cut positions are asked on the shuffled sequence. The shuffle keeps the composition of the whole protein and destroys the order, so a model that knows only which amino acids are common scores the same on both.

**Statistics.** For each family we compute the share of correct first residues on real and on shuffled cuts, and take the difference, in percentage points. The result for a model is the mean of that gap over the 167 families. Intervals are 95% bootstraps over families (10,000 resamples), the main test is a one-sided sign-flip permutation test over families, and the family-size trend is the Spearman correlation between a family's gap and the logarithm of its size.

**Raw continuation.** For models that allow it, the same prefix is sent without any instruction, as the text ">sequence" followed by the FASTA lines, through a plain completion endpoint (open-weight models on Fireworks) or as the start of the model's own reply (Gemini 2.5 Pro). The first letter the model writes is scored as above.

**Protein language models.** They get the same prefix and no prompt. ProtGPT3 and ProtGPT2 read it left to right and give a probability for the next token; the ESM models see the prefix, a mask in place of the next residue, and the end of the sequence. In every case the prediction is the most likely of the 20 standard amino acids.

Total API cost was about $700, plus a few dollars of GPU time for the protein language models.

### G. Safety behaviour seen along the way

Gemini 4 Carbon blocked about 75% of DNA prompts outright. OpenAI rejected 23 GPT-6 requests in the first round and 17 GPT-6.1 Sol requests in the main run as possible biological misuse. Claude Sonnet 4.5 refused 97% of requests that started its reply with a protein sequence, and Anthropic's filter blocked 44% of Claude Fable 5's questions as cyber content.
