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

The Single figure displays four percentage confusion matrices, with actual
outcomes in rows and literal Pass/Fail verdicts in columns. All share a 0–100%
color scale. Each row's denominator is 79, including invalid outputs, which
are omitted from the visible columns. Rows may therefore sum below 100%.
Invalid responses are never reassigned to Fail or removed from denominators.
The underlying verdict counts are retained for auditing.

The three instruction excerpts under `_includes/second-life-tb4/` are copied
verbatim from `SINGLE_FULL_INSTRUCTION`, `PAIR_INSTRUCTION`, and
`FIVE_INSTRUCTION` in the pinned `scripts/build_tbench4_run_bundle_tasks.py`.

## Rebuild

With Python and Matplotlib installed, run from the website root:

```sh
python scripts/generate_second_life_tb4_figures.py
```

This generates `_data/second_life_tb4.json` (used by the article's Liquid
tables) and six figure families under `assets/img/2026-08-28-second-life-agent-evals/`.
The four main figures and appendix oracle curves have `-mobile.svg` variants, selected with HTML
`picture` elements below 600px. Panel figures stack on mobile; the sampling
hero shows four groups of vertical bars (two groups per row on mobile). Data and scales are identical.
PNG copies for visual inspection go to `/tmp/`. The original TB3 figure script
and SVGs are retained separately.

The 97-pool uniform baseline is derived from each source's successful-run
total after subtracting all-success and excluded mixed pools: 268/485.
Combined Five counts add the original 79-pool panel and the 18 GPT-6-source
pools, weighting pools equally. Single/Pair retain their original three-source
coverage. No combined 97-pool confidence interval is inferred from the two
separate batch intervals.

The Single/Pair vertical bar panels share the same 79 source pools and
anchors, but show different metrics: judgment accuracy versus selection
success. The source-by-reviewer Five panels use the source-specific success
counts in `tbench4-pass-at-k.json`. The generator cross-checks their sums
against the separate 79- and 18-pool result files. Every source has its own
uniform baseline, computed from its reviewed candidate outcomes.

The main sampling figure shows four source groups with vertical pass@1,
selection, and oracle pass@5 bars on a shared success scale. It uses
**GPT-5.6 Sol as the reviewer for every source**,
computed from the source-specific counts. This is explicit rather than a
retrospective choice of a different best reviewer per source. In this snapshot
GPT is also tied for, or attains, the highest observed count for each source.
Selection bars are whole-job reconstructions at k=5 over **all 66 tasks per source**,
matching the task coverage of each frozen source job. The oracle curves use the
unchanged full-job pass@k values. Selection is `(all_pass_pools +
gpt_selection_successes + sum(unreviewed_success_counts)/5) / 66`.
Homogeneous pools assume valid selection; the 3 Fable, 5 GPT, 2 GLM, and 0 GPT-6
unreviewed mixed pools use uniform fallback. These are assumptions, not measured
reviewer outcomes. Gray bars encode pass@1; source-colored solid bars encode
selection; hollow dashed bars encode oracle pass@5. Bar labels show success,
and group annotations give selection gains over pass@1 in percentage points. There are no coverage whiskers. The appendix
overlays all four oracle pass@1–5 curves on one plot, with source colors and
legend order matching the main figure. Only endpoints are labeled; these do not
represent reviewer evaluations at k=2–4.
The source data records one missing GLM reward counted as failure. No tasks
are removed from the denominator. These reconstructions are not official
end-to-end leaderboard scores; direct comparisons also require matching the
benchmark version, agent setup, and scoring protocol.

Cost tables cover only three named incremental batches, including the separate
prompt control. They exclude earlier panels and source-run generation, and
must not be described as total project cost.

Display order for sources is GPT-6 Astra, Fable 5.1, GLM-5.3, then GPT-5.6 Sol,
following the requested presentation order. Colors and prose metrics are keyed
to model identifiers rather than positions, so reordering preserves their meaning.
Reviewer order is fixed by descending aggregate Five success: GPT-5.6 Sol,
GLM-5.3 Flash, GLM-5.3, DeepSeek V4.1 Flash. This same order is used in Single,
Pair, and per-source Five charts and tables; individual panels are not re-ranked.
