# Frozen TB4 blog data

Source: [XinmingTu/Agentic-Verification-Eval at
6d99501ad21662cad4ef82c9089e15492d24e976](https://github.com/XinmingTu/Agentic-Verification-Eval/tree/6d99501ad21662cad4ef82c9089e15492d24e976).
Snapshot date: September 18, 2026. No reviewer calls are made by the blog build.

The `tbench4-*.json` files are unchanged copies of the files with the same names
under the source repository's `results/` directory. They contain compact
metrics, task-cluster intervals, source pass@k data, and incremental cost ledgers.
The September 16 comparison predates the GLM Flash completion and GPT-6
extension; the generator combines the three batches explicitly and excludes
the DeepSeek neutral-prompt control from the main result.

`single-verdict-counts.json` and `deepseek-five-positions.json` are compact
aggregations of the pinned per-review JSONL files identified inside them.
Single verdict columns are **pass, fail, invalid**, with original successes and
failures as rows. These counts retain invalid outputs as errors without
misrepresenting them as pass/fail judgments. Raw reviewer reasoning and
machine-local job paths are not copied into this website.

The Single figure displays success/failure recall as a percentage heatmap,
with a shared 0–100% color scale. Each pool supplies one anchor per class, so
each cell's denominator is 79, including invalid outputs as errors. The
underlying verdict counts are retained for auditing.

The three instruction excerpts under `_includes/second-life-tb4/` are copied
verbatim from `SINGLE_FULL_INSTRUCTION`, `PAIR_INSTRUCTION`, and
`FIVE_INSTRUCTION` in the pinned `scripts/build_tbench4_run_bundle_tasks.py`.

## Rebuild

With Python and Matplotlib installed, run from the website root:

```sh
python scripts/generate_second_life_tb4_figures.py
```

This generates `_data/second_life_tb4.json` (used by the article's Liquid
tables) and four SVGs under `assets/img/2026-08-28-second-life-agent-evals/`.
PNG copies for visual inspection go to `/tmp/`. The original TB3 figure script
and SVGs are retained separately.

The 97-pool uniform baseline is derived from each source's successful-run
total after subtracting all-success and excluded mixed pools: 268/485.
Combined Five counts add the original 79-pool panel and the 18 GPT-6-source
pools, weighting pools equally. Single/Pair retain their original three-source
coverage. No combined 97-pool confidence interval is inferred from the two
separate batch intervals.

The pass@k figure uses **GPT-5.6 Sol as the reviewer in every source panel**,
computed from the source-specific counts. This is explicit rather than a
retrospective choice of a different best reviewer per source. In this snapshot
GPT is also tied for, or attains, the highest observed count in each panel.
Stars are whole-job reconstructions at k=5; whiskers bound unreviewed mixed
pool outcomes and are not statistical confidence intervals. Homogeneous pools
assume valid selection; excluded mixed pools use uniform fallback. The source
data records one missing GLM reward counted as failure.

Cost tables cover only three named incremental batches, including the separate
prompt control. They exclude earlier panels and source-run generation, and
must not be described as total project cost.
