# Frozen TB4 blog data

Source: [XinmingTu/Agentic-Verification-Eval at
882fcc3349f161e9bfc3c1b92ab3c49b507480cc](https://github.com/XinmingTu/Agentic-Verification-Eval/tree/882fcc3349f161e9bfc3c1b92ab3c49b507480cc),
the `main` merge that adds the audited Opus 5.5 and GPT-6 Sol reviewer results.
Snapshot date: September 26, 2026. No reviewer calls are made by the blog build.

The `tbench4-*.json` files are unchanged copies of the files with the same names
under the source repository's `results/` directory: compact metrics,
task-cluster intervals, source pass@k data, and cost ledgers. The September 16
comparison predates the GLM Flash completion, the GPT-6 Astra extension, and
the frontier reviewers; the generator combines the batches explicitly and
excludes the DeepSeek neutral-prompt control from the main results.

`shared-task-records.json` holds one minimal record per review: 334 cases for
each of the six reviewers (158 Single, 79 Pair, 97 Five), from the result files
listed in its `files` array. Single/Pair batch files also contain Five rows; the
importer skips those and loads each Five observation once, from its own file.
Raw reviewer reasoning and machine-local job paths are not copied into this
website.

`single-verdict-counts.json` and `deepseek-five-positions.json` are compact
aggregations from the earlier four-reviewer snapshot. The generator recomputes
the confusion counts for all six reviewers from the per-case records and checks
them against the first file.

The three instruction excerpts under `_includes/second-life-tb4/` are copied
verbatim from `SINGLE_FULL_INSTRUCTION`, `PAIR_INSTRUCTION`, and
`FIVE_INSTRUCTION` in the pinned `scripts/build_tbench4_run_bundle_tasks.py`.
The `harness-*.txt` files are the mini-swe-agent system prompts and the text
appended after each task instruction, copied from the recorded trajectories:
`harness-system.txt` for five reviewers, `harness-system-tool.txt` for GPT-6
Sol, and `harness-wrapper.txt` (which states the 55-step limit) for all six.

## Rebuild

From the website root, with Python, Matplotlib, and the Roboto font:

```sh
python scripts/generate_second_life_shared.py
python scripts/generate_second_life_tb4_figures.py
```

The first validates the per-case snapshot and writes
`_data/second_life_shared.json` (shared-task lists and average costs). Add
`--import-dir /path/to/Agentic-Verification-Eval` to refresh the snapshot and
the aggregate copies; files are read from the pinned commit with `git show`, so
the checkout may be on any branch. The second writes `_data/second_life_tb4.json`
and every figure, desktop and `-mobile`, under
`assets/img/2026-08-28-second-life-agent-evals/`. Set `SECOND_LIFE_FONT_DIR`
to a folder of Roboto TTFs if Roboto is not installed; its metrics set label
placement, and the page renders figure text in Roboto. PNG copies for visual
inspection go to `/tmp/`. The TB3 figure script and SVGs are retained
separately.

## Checks and conventions

The validation asserts unique observations, identical candidates, order, and
labels for all six reviewers in every case, and the Single/Pair anchor
relationship to each Five pool. The figure generator cross-checks Single
accuracy, success recall, Pair selection, exact Pair classification, Five
selection, and per-source Five counts against the pinned summaries.

Reviewer order is fixed everywhere: Opus 5.5, GPT-5.6 Sol, GPT-6 Sol, GLM-5.3
Flash, GLM-5.3, DeepSeek V4.1 Flash. That is descending Five success over all
97 pools, and it is also the Single accuracy order. Source order is GPT-6
Astra, Fable 5.1, GLM-5.3, GPT-5.6 Sol. Colors are keyed to model identifiers:
brand-anchored reviewer colors, one set for both page themes, checked for
color-vision separation on every pair. Sources that are also reviewers keep
their reviewer color; source-only models are gray. Red marks wrong verdicts in
the confusion matrices and below-random cells in the heatmaps; blue marks
above-random cells.

The confusion matrices show literal Pass and Fail verdicts with 79 runs per
row. Invalid outputs are neither: they are listed under the matrix, count as
wrong, and stay in the denominators, so such rows sum below 100%.

The 97-pool random baseline is 268/485 successful candidates, after removing
all-success and unreviewed mixed pools from each source's totals. Five totals
weight pools equally. Whole-job selection is `(all_pass_pools +
selection_successes + sum(unreviewed_success_counts) / 5) / 66` per source and
reviewer. Homogeneous pools assume a valid pick; the 3 Fable, 2 GLM, 5 GPT,
and 0 GPT-6 Astra unreviewed mixed pools use a random pick. These are
assumptions, not measured outcomes, and not leaderboard scores. One missing
GLM reward counts as a failure.

Average costs use the three-source, 79-pool population for every reviewer
(158 Single, 79 Pair, 79 Five reviews), because that is where all six have
recorded costs; the cost figure scores Five on the same 79 pools. Opus 5.5,
GPT-5.6 Sol, and GPT-6 Sol use recorded cost; the other reviewers use
max(reported, token estimate) at the rates in the pinned
`scripts/run_tbench4_complete.py`. Reused reviews count once. GPT-6 Astra
pools and the prompt control are excluded. These are experiment-accounting
figures, not invoices or total project cost.

The shared-task heatmaps fix the task set: six tasks common to the three
original sources, two common to all four. Each cell gives the shared-task
score, its difference from random in percentage points (50% for Single and
Pair; the matched candidates' success share for Five), and the score on all
available pools. The two populations are nested, not independent.
