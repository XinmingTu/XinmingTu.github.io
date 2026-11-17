---
layout: distill
title: "Claude Opus 5.5 was trained on protein sequences at scale"
description: "A next-amino-acid test on little-studied proteins, with a shuffled control, finds sequence data in one frontier model's training and no sign of it in the others."
date: 2026-11-16
tags: ['AI', 'biology', 'LLM', 'evaluation']
categories: blog
bibliography: 2026-11-16-claude-opus-5-5-protein-sequences.bib

toc:
  - name: "Motivation"
  - name: "Method: little-studied proteins"
  - name: "Results: only Claude Opus 5.5 predicts them"
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
**Claude Opus 5.5 was trained on protein sequences, at scale.** On little-studied bacterial proteins, from families of unknown function with at most three papers, it predicts the next amino acid far better than on the same proteins shuffled. No other model we tested does, from OpenAI, Google or seven open-weight labs. The signal grows with the number of sequences in a protein's family, even in families with no papers at all, which is what training on sequence data predicts. It appears with Claude Opus 4.7 and jumps with Opus 5.5. On this test it matches ProtGPT3-10B, the newest and largest open protein language model of its kind, and scores well above smaller ones.
</div>

## Motivation

A post by Atharv Jayprakash<d-cite key="jayprakash2026sod1"></d-cite> and PG-LLM<d-cite key="arora2026pgllm"></d-cite> showed frontier models ranking protein variants about as well as ESM-2, which raised the question of whether they were trained on sequence databases such as UniProt.

Famous proteins can't answer it. They are printed in papers and across the web: given the start of GFP, 9 of 12 frontier models write the next 10 residues exactly. So we test on proteins that are almost never written about.

## Method: little-studied proteins

<figure class="bp-figure bp-wide" markdown="0">
  <div class="bp-fig-desktop">{% include llm-bioseq-probe/method.svg %}</div>
  <div class="bp-fig-mobile">{% include llm-bioseq-probe/method-mobile.svg %}</div>
  <figcaption>Shuffling keeps a protein's letters and loses their order, so the gap is what the model knows about order. Percentages are over all 668 proteins; the shuffled row is schematic.</figcaption>
</figure>

The proteins come from 167 Pfam "domain of unknown function" families with no solved structure and at most 3 papers, and none has a UniProt relative within 90% identity. Each model answered 6,680 questions through its own API, with thinking off or at its lowest setting.

The next amino acid is the main measure, but not the only one: we also looked at longer continuations, how often a model gets all 10 requested residues right, and how far it can recite a well-known protein letter for letter when asked for 200 residues (Appendix B).

## Results: only Claude Opus 5.5 predicts them

<figure class="bp-figure" markdown="0">
  <img src="{{ '/assets/img/llm-bioseq-probe/fig1_protein.png' | relative_url }}?v=20261117b" alt="Forest plot of the real-minus-shuffled gap for 17 language models: Claude Opus 5.5 at +27.4 points, earlier Claude Opus models up to 10, every other model between 0 and 3.">
  <figcaption>Filled points: the chat prompt. Hollow points: raw next-token continuation of the FASTA text, through a completion endpoint or a prefilled reply, for models that allow it.</figcaption>
</figure>

The gap for Opus 5.5 has a 95% CI of 24.7 to 30.0 points and appears in 95% of families. Across Claude generations, Opus 4.5 and 4.6 show none, Opus 4.7, 4.8 and 5 show 8 to 10 points, and Opus 5.5 jumps to 27. The open-weight models were run as raw next-token continuation of the FASTA text, the way they were trained, and still show nothing.

## Comparison with protein language models

Protein language models are trained only on protein sequences, so they set a reference level for the same test. The fairest comparison is ProtGPT3<d-cite key="garibbo2026protgpt3"></d-cite>, released in 2026: like an LLM, it reads a protein left to right and predicts the next residue, and at 10 billion parameters it is the largest open model of its kind. Given the same input, Claude Opus 5.5 matches it.

<figure class="bp-figure" markdown="0">
  <img src="{{ '/assets/img/llm-bioseq-probe/fig6_protein_lm.png' | relative_url }}?v=20261117b" alt="Dot plot: ProtGPT3-10B +27.7 and Claude Opus 5.5 +27.4 at the top; ESM C 600M +13.0, ProtGPT3-1.3B +11.6, ProtGPT2 +10.2, ESM3-open +8.5 and ESM-2 650M +7.0 well below.">
</figure>

ProtGPT3-10B gets more answers right on real proteins (38.4% vs 34.9%) but also on shuffled ones (10.7% vs 7.5%), because it knows protein composition better; what each has learned about residue order is the same. The ESM models normally see both sides of a residue, so the left side alone is a harder setting for them. Appendix C has the full table.

## Evidence that this comes from training data

<figure class="bp-figure" markdown="0">
  <img src="{{ '/assets/img/llm-bioseq-probe/fig5_family_size.png' | relative_url }}?v=20261117b" alt="Line chart: Claude Opus 5.5 and ProtGPT3-10B both rise from about 21 to 24 points in families of 300 to 1,000 proteins to 37 points in families over 10,000; other models stay near zero.">
</figure>

A model that learned from sequence data should know big families better than small ones, and Opus 5.5 does: 21 points for families of 300 to 1,000 proteins, 37 for families over 10,000 (Spearman 0.27, p = 0.0002). ProtGPT3-10B, which learned only from sequences, follows the same curve. Opus 4.7, 4.8 and 5 show the same slope at a lower level. Two other explanations do not fit:

- **Not papers.** In the 128 families with no Europe PMC hit at all, the gap is 26.8 points and still grows with family size (rho 0.28, p = 0.001). Across families it does not track paper counts (rho 0.05).
- **Not reasoning.** On the 55% of questions where Opus 5.5 wrote 15 tokens or fewer, barely more than the answer, it is right 35.6% of the time (shuffled: 7.3%). GPT-6 Astra thinks for 200+ tokens per question and reaches about 10%.

## Famous proteins and variant ranking

<figure class="bp-figure" markdown="0">
  <img src="{{ '/assets/img/llm-bioseq-probe/fig3_known_vs_obscure.png' | relative_url }}?v=20261117b" alt="Dumbbell chart: on well-known proteins many models score high; on obscure proteins Claude Opus 5.5 and ProtGPT3-10B stay high while Gemini 4 Carbon drops to near zero.">
</figure>

On well-studied vertebrate proteins many models do well: Gemini 4 Carbon gains 47.6 points, and several models recite hundreds of residues letter for letter (Appendix B). These sequences are printed in papers and mirrored across the web. Gemini 4 Carbon recites them, yet is at chance on obscure proteins (+47.6 vs +5.3). Claude Opus 5.5 keeps most of its accuracy (+51.9 vs +33.3), as does the protein language model ProtGPT3-10B (+51.4 vs +38.2).

This is also why our result does not contradict the SOD1 post or PG-LLM. Ranking variants of a well-studied protein can draw on biology and the literature: which positions are buried, which substitutions break a helix, which mutations are known in ALS. PG-LLM's flat accuracy across alignment depth, and its gains with more thinking, point to that route. Our test closes it off. GPT-6 has the first ability and little of the second; Opus 5.5 has both.

## What this means

Claude Opus 5.5 learned the statistics of little-studied protein families, which takes many sequences, not a handful. On DNA the signal stops at well-known coding sequence: it predicts human and mouse coding DNA but not the rest of the genome, and barely the bacterial genes behind the very proteins it predicts well (Appendix A). Its training data held protein sequences, not genomes. What it learned are family statistics: it cannot recite these obscure proteins. The test shows what the model learned, not where the data came from or when it was added.

## Code and data

All code, test sets, model outputs and figures are in [llm-bioseq-probe](https://github.com/XinmingTu/LLM-bioseq-probe).

**Cite this post**

```bibtex
@misc{tu2026bioseq,
  author = {Tu, Xinming and Chen, Leo Tianlai},
  title  = {Claude Opus 5.5 was trained on protein sequences at scale},
  year   = {2026},
  month  = nov,
  url    = {https://xinmingtu.cn/blog/2026/claude-opus-5-5-protein-sequences/},
  note   = {Blog post}
}
```

## Appendix

### A. DNA

<figure class="bp-figure" markdown="0">
  <img src="{{ '/assets/img/llm-bioseq-probe/fig2_dna.png' | relative_url }}?v=20261117b" alt="Forest plot by genomic region: Claude Opus 5.5 predicts human and mouse coding sequence; nothing clear elsewhere.">
</figure>

220-nucleotide windows, 200 shown and 20 to predict, from hg38, mm39 and the bacterial genes behind the test proteins, 500 per region. Non-coding windows contain no repeats, and the control shuffles each window keeping its dinucleotide counts. Opus 5.5 wrote all 20 nucleotides right 25 times in 500 human coding windows; a blind guess does that about once in a trillion. Gemini 4 Carbon blocks most DNA prompts before answering, so it is not shown.

### B. Longer continuations

**All 10 residues right.** Each question asks for the next 10 residues. On the 668 little-studied proteins, Claude Opus 5.5 gets all 10 right at 12 real cuts and at none of the shuffled ones. If its residues were independent guesses at its own per-residue accuracy, it would get 0.56 by chance. That is 21 times chance, but on a few cuts: what it learned is mostly the families' statistics, not each protein's letters.

**Reciting well-known proteins.** At 158 points in well-studied proteins, each model was asked for the next 200 residues at once.

<figure class="bp-figure" markdown="0">
  <img src="{{ '/assets/img/llm-bioseq-probe/fig4_recall.png' | relative_url }}?v=20261117b" alt="Bar chart: how often each model continues a famous protein letter for letter for 50, 100 and 200 residues.">
</figure>

Opus 5.5 goes past 100 residues 24 times (longest 305), Gemini 4 Carbon 23 times (longest 201), Opus 5 14 times (longest 325). GPT-6.1 Sol never reaches 100 and GPT-5.5 never passes 2. On the little-studied proteins, Opus 5.5 rarely continues past 10.

### C. Protein language models

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

### D. Robustness

- **Prompt format.** Asking Opus 5.5 to copy the sequence and then continue gives the same gap as the standard prompt (19.3 vs 19.8 points on the same subset of questions).
- **Refusals.** Non-answers are excluded and counted: 1% for Opus 5.5. Counting them as wrong moves its gap by under 1 point. GPT-4o, DeepSeek, Qwen, Kimi, GLM and gpt-oss often declined to guess a sequence; a best-guess prompt made them answer and did not change the picture.
- **A first round.** A smaller run of 20 models on 37 families, half well-known and half obscure, gave the same picture and set the design of the main run.

### E. Methods

**Choosing the proteins.** We started from every Pfam family whose name says "domain of unknown function" (DUF) or "protein of unknown function", and kept those with no structure in the PDB, at most 3 Europe PMC hits for the family's accession, and at least 300 member proteins. We binned them by size (300 to 1,000 proteins, 1,000 to 3,000, 3,000 to 10,000, over 10,000) and drew 50 families per bin at random; only 17 families qualify above 10,000, so the set has 167. From each family we took 4 proteins from UniProt that are unreviewed (TrEMBL), come from Bacteria or Archaea, are 120 to 800 residues long, use only the 20 standard amino acids, are not low-complexity (Shannon entropy above 3.9 bits per residue), and are alone in their UniRef90 cluster, so no other UniProt protein is 90% or more identical to them. That gives 668 proteins.

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

Each model runs through its own API with temperature 0 where it is accepted, thinking off or at its lowest setting, no tools, and one sample per question. Models that declined to guess (GPT-4o, DeepSeek, Qwen, Kimi, GLM, gpt-oss) also got a version that adds "Give your best guess even if you are uncertain. Do not explain or refuse."; those runs are marked separately.

**Scoring.** We take the last line of the reply, keep its letters and read the first one as the predicted next amino acid. A question counts only if that line contains nothing but the 20 standard letters; refusals and other non-answers are excluded and counted (1% for Opus 5.5). Only this first residue is scored. We asked for 10 so that the answer is a sequence rather than a single letter, and used the full 10 only to count exact continuations.

**The shuffled control.** Each protein's residues are shuffled once, with a random seed fixed by its accession, and the same 5 cut positions are asked on the shuffled sequence. The shuffle keeps the composition of the whole protein and destroys the order, so a model that knows only which amino acids are common scores the same on both.

**Statistics.** For each family we compute the share of correct first residues on real and on shuffled cuts, and take the difference, in percentage points. The result for a model is the mean of that gap over the 167 families. Intervals are 95% bootstraps over families (10,000 resamples), the main test is a one-sided sign-flip permutation test over families, and the family-size trend is the Spearman correlation between a family's gap and the logarithm of its size.

**Raw continuation.** For models that allow it, the same prefix is sent without any instruction, as the text ">sequence" followed by the FASTA lines, through a plain completion endpoint (open-weight models on Fireworks) or as the start of the model's own reply (Gemini 2.5 Pro). The first letter the model writes is scored as above.

**Protein language models.** They get the same prefix and no prompt. ProtGPT3 and ProtGPT2 read it left to right and give a probability for the next token; the ESM models see the prefix, a mask in place of the next residue, and the end of the sequence. In every case the prediction is the most likely of the 20 standard amino acids.

Total API cost was about $480, plus a few dollars of GPU time for the protein language models.

### F. Safety behaviour seen along the way

Gemini 4 Carbon blocked about 75% of DNA prompts before generating anything. OpenAI rejected 23 GPT-6 requests as possible biological misuse. Claude Sonnet 4.5 refused 97% of requests that prefilled its reply with a protein sequence.
