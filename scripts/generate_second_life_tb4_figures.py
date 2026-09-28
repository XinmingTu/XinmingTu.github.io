#!/usr/bin/env python3
"""Rebuild the TB4 blog data and figures from checked-in, pinned result snapshots.

Requires Matplotlib and the Roboto font, which the page also uses for figure
text; set SECOND_LIFE_FONT_DIR to a folder of Roboto TTFs if it is not
installed. No network access or model calls. generate_second_life_shared.py
refreshes and validates the per-case snapshot this script reads.
The older generate_second_life_agent_eval_figures.py reproduces the TB3 pilot.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/second-life-matplotlib")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch, Patch, Rectangle
from matplotlib.ticker import FixedLocator, NullLocator

sys.dont_write_bytecode = True  # keep scripts/ free of __pycache__
sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_second_life_shared import COMMIT, LABELS, REVIEWERS, cost_table, load_records, score, shared  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "assets/data/second-life-tb4"
OUTPUT = ROOT / "assets/img/2026-08-28-second-life-agent-evals"
REPO = f"https://github.com/XinmingTu/Agentic-Verification-Eval/blob/{COMMIT}"
NAME = dict(zip(REVIEWERS, LABELS))
# Brand-anchored colors, one set for both page themes; every pair passes the
# color-vision checks against both surfaces. Anthropic orange, two OpenAI
# greens, two GLM purples (Zhipu's own blue would collide with DeepSeek's),
# DeepSeek blue. The plugin maps each to a CSS variable.
COLOR = {"opus-5-5": "#d97349", "gpt-5-6-sol": "#34a77e", "gpt-6-sol": "#1b7653",
         "glm-5-3-flash": "#b47cbb", "glm-5-3": "#8d46b9", "deepseek-v4p1-flash": "#4b72f4"}
SOURCES = ["gpt-6-astra", "fable-5.1", "glm-5.3", "gpt-5.6-sol"]  # presentation order
ORIGINAL = ["fable-5.1", "glm-5.3", "gpt-5.6-sol"]  # the three sources with Single and Pair results
SOURCE_NAME = {"gpt-6-astra": "GPT-6 Astra", "fable-5.1": "Fable 5.1", "glm-5.3": "GLM-5.3", "gpt-5.6-sol": "GPT-5.6 Sol"}
INK, BODY, MUTED, LINE, PALE = "#20242d", "#434a57", "#747d8b", "#dfe4e9", "#b0b0b0"
# Sources that are also reviewers keep their reviewer color; source-only models are gray.
SOURCE_COLOR = {"gpt-5.6-sol": COLOR["gpt-5-6-sol"], "glm-5.3": COLOR["glm-5-3"], "fable-5.1": MUTED, "gpt-6-astra": PALE}
# Wrong verdicts (Figure 1) and the heatmaps' diverging poles carry no model identity.
ERROR, ABOVE, BELOW = "#d1392e", "#2a86b8", "#d1392e"
TINT = 0.32
TOP2 = ["opus-5-5", "gpt-5-6-sol"]  # the two best Five selectors, shown in the sampling figure


def read(name):
    return json.loads((INPUT / name).read_text())


def percent(value):
    return f"{value * 100:.1f}"


def use_roboto():
    folders = [os.environ.get("SECOND_LIFE_FONT_DIR"), "~/.local/share/fonts", "~/Library/Fonts", "/Library/Fonts", "/usr/share/fonts"]
    for folder in filter(None, folders):
        for path in Path(folder).expanduser().rglob("Roboto*.ttf") if Path(folder).expanduser().is_dir() else []:
            font_manager.fontManager.addfont(str(path))
    names = {f.name for f in font_manager.fontManager.ttflist}
    if "Roboto" not in names:
        raise SystemExit("Roboto not found: install it or set SECOND_LIFE_FONT_DIR to a folder with Roboto TTFs.")


def save(fig, name, description):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT / f"{name}.svg", bbox_inches="tight", pad_inches=0.04, metadata={
        "Date": None, "Creator": "generate_second_life_tb4_figures.py", "Description": description,
    })
    # A local raster copy makes visual QA possible without adding another asset.
    fig.savefig(Path("/tmp") / f"{name}.png", dpi=140, bbox_inches="tight")
    plt.close(fig)


def label(name, mobile):
    return name.replace(" V4.1 Flash", "\nV4.1 Flash") if mobile else name


GRID = dict(color=LINE, linewidth=0.6, alpha=0.7)  # faint, value axis only


def x_grid(ax, ticks, fmt="{}%"):
    ax.set_xticks(ticks, labels=[fmt.format(t) for t in ticks])
    ax.grid(axis="x", **GRID)
    ax.set_axisbelow(True)
    ax.tick_params(length=0, pad=5)


def cell_box(ax, x, y, w, h, **kw):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.035", lw=0, **kw))


def main():
    use_roboto()
    plt.rcParams.update({
        "font.family": "Roboto", "font.size": 9.5, "text.color": INK,
        "axes.labelcolor": BODY, "axes.edgecolor": LINE, "axes.labelsize": 9,
        "xtick.labelcolor": MUTED, "ytick.labelcolor": BODY, "xtick.labelsize": 8.5, "ytick.labelsize": 9.5,
        "axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False, "axes.spines.bottom": False,
        "svg.fonttype": "none", "svg.hashsalt": "second-life-tb4",
        "figure.facecolor": "none", "axes.facecolor": "none", "savefig.transparent": True,
    })
    rows = load_records()
    select = lambda key, cond, source=None: [r for r in rows if r["reviewer"] == key and r["condition"] == cond
                                             and (source is None or r["source_key"] == source)]

    # ------------------------------------------------------------ metrics, cross-checked against the pinned summaries
    old = {r["reviewer"]: r for r in read("tbench4-complete-comparison.json") if r["condition"] == "single_pair"}
    old.update({r["reviewer"]: r for r in read("tbench4-glm-flash-complete-comparison.json")})
    frontier = {r["reviewer"]: r for r in read("tbench4-frontier-comparison.json")}
    false_pass_ci = {r["reviewer"]: r["task_cluster_bootstrap_95_ci"] for r in read("tbench4-frontier-single-failure-approval-ci.json")["reviewers"]}
    counts = {r["reviewer"]: r["confusion"] for r in read("single-verdict-counts.json")["reviewers"]}
    pass_at_k = {s["source"]: s for s in read("tbench4-frontier-pass-at-k.json")["sources"]}
    for s in read("tbench4-pass-at-k.json")["sources"]:
        assert pass_at_k[s["source"]]["pass_at_k"] == s["pass_at_k"]  # frontier file only adds reviewers
    costs = {c["key"]: c for c in cost_table(rows)}
    M, CM = {}, {}
    for key in REVIEWERS:
        single, pair, five = select(key, "single-full"), select(key, "pair-full"), select(key, "five-full")
        assert (len(single), len(pair), len(five)) == (158, 79, 97)
        for g in (1, 0):
            group = [r for r in single if r["gold_rewards"] == [g]]
            CM[key, g] = {"invalid": sum(not r["format_valid"] for r in group),
                          **{v: sum(r["format_valid"] and r["predicted_reward"] == v for r in group) for v in (1, 0)}}
            assert len(group) == 79
        five79 = [r for r in five if r["source_key"] in ORIGINAL]
        m = M[key] = {
            "single": sum(map(score, single)) / 158, "pair": sum(map(score, pair)) / 79,
            "good": CM[key, 1][1] / 79, "bad": CM[key, 0][1] / 79,
            "pair_exact": sum(r["format_valid"] and r["candidate_a_predicted_reward"] == r["gold_rewards"][0]
                              and r["candidate_b_predicted_reward"] == r["gold_rewards"][1] for r in pair) / 79,
            "five_wins": sum(map(score, five)), "five79_wins": sum(map(score, five79)),
            "by_source": {s: sum(map(score, select(key, "five-full", s))) for s in SOURCES},
            "cost": {c: costs[key][c + "_total"] / costs[key][c + "_n"] for c in ("single", "pair", "five")},
        }
        m["five"], m["five79"] = m["five_wins"] / 97, m["five79_wins"] / 79
        assert len(five79) == 79 and sum(m["by_source"].values()) == m["five_wins"]
        summary = frontier[key] if key in frontier else old[key]
        metrics = summary["metrics"]
        assert np.isclose(m["single"], metrics["single_full"]["accuracy"])
        assert np.isclose(m["good"], metrics["single_full"]["success_recall"])
        assert np.isclose(m["pair"], metrics["pair_full"]["preferred_success_rate"])
        assert np.isclose(m["pair_exact"], metrics["pair_full"]["exact_pair_classification_rate"])
        if key in frontier:
            assert np.isclose(m["five"], metrics["five_full"]["selection_success_rate"])
            assert np.isclose(m["bad"], false_pass_ci[key]["estimate"])
        else:
            assert np.isclose(m["five79"], metrics["five_full"]["selection_success_rate"])
            assert [[CM[key, g][1], CM[key, g][0], CM[key, g]["invalid"]] for g in (1, 0)] == counts[key]
        m["ci"] = summary["cluster_bootstrap_95_ci"]
        for s in SOURCES:
            assert pass_at_k[s]["reviewer_mixed_successes"][key] == m["by_source"][s]
    assert [k for k in sorted(REVIEWERS, key=lambda k: -M[k]["five"])] == REVIEWERS
    assert [k for k in sorted(REVIEWERS, key=lambda k: -M[k]["single"])] == REVIEWERS

    # ------------------------------------------------------------ sources and whole-job reconstructions
    def reconstructed(key, s):
        f = pass_at_k[s]
        return (f["all_pass_pools"] + f["reviewer_mixed_successes"][key] + sum(f["unreviewed_mixed_pools"].values()) / 5) / f["tasks"]

    assert np.isclose(reconstructed("gpt-5-6-sol", "fable-5.1"), 0.70)
    sources = []
    for s in SOURCES:
        f = pass_at_k[s]
        unreviewed = list(f["unreviewed_mixed_pools"].values())
        successes = round(f["pass_at_k"][0] * f["tasks"] * 5) - f["all_pass_pools"] * 5 - sum(unreviewed)
        uniform = successes / (f["reviewed_mixed_pools"] * 5)
        pools = [r for r in select(REVIEWERS[0], "five-full", s)]
        assert f["tasks"] == 66 and len(pools) == f["reviewed_mixed_pools"]
        assert successes == sum(sum(r["gold_rewards"]) for r in pools)
        assert np.isclose(f["pass_at_k"][-1], (f["all_pass_pools"] + f["reviewed_mixed_pools"] + len(unreviewed)) / f["tasks"])
        assert all(a <= b + 1e-12 for a, b in zip(f["pass_at_k"], f["pass_at_k"][1:]))
        assert all(reconstructed(k, s) <= f["pass_at_k"][-1] + 1e-12 for k in REVIEWERS)  # a weak selector can fall below pass@1
        sources.append({
            "key": s, "name": SOURCE_NAME[s], "pools": f["reviewed_mixed_pools"], "successes": successes,
            "uniform": percent(uniform), "uniform_rate": uniform, "tasks": f["tasks"],
            "unreviewed_mixed_pools": len(unreviewed), "pass_at_k": f["pass_at_k"],
            "pass1": percent(f["pass_at_k"][0]), "pass5": percent(f["pass_at_k"][-1]),
        })
    SRC = {s["key"]: s for s in sources}
    total_pools = sum(s["pools"] for s in sources)
    baseline = sum(s["successes"] for s in sources) / (total_pools * 5)
    baseline79 = sum(SRC[s]["successes"] for s in ORIGINAL) / (sum(SRC[s]["pools"] for s in ORIGINAL) * 5)
    assert total_pools == 97

    # ------------------------------------------------------------ page data
    ci = lambda block: f'{percent(block["lower"])}–{percent(block["upper"])}'
    data = {"commit": COMMIT, "repo": REPO, "updated": "September 26, 2026",
            "five_pools": total_pools, "source_runs": total_pools * 5,
            "candidate_successes": sum(s["successes"] for s in sources),
            "five_baseline": percent(baseline), "five79_baseline": percent(baseline79),
            "source_order": [SOURCE_NAME[s] for s in SOURCES], "reviewers": [], "sources": sources}
    for key in REVIEWERS:
        m = M[key]
        data["reviewers"].append({
            "key": key, "name": NAME[key],
            "single": percent(m["single"]), "single_ci": ci(m["ci"]["single-full"]),
            "success_recall": percent(m["good"]), "false_pass": percent(m["bad"]), "false_pass_n": CM[key, 0][1],
            "failure_recall": percent(CM[key, 0][0] / 79), "single_invalid": CM[key, 1]["invalid"] + CM[key, 0]["invalid"],
            "pair": percent(m["pair"]), "pair_ci": ci(m["ci"]["pair-full"]), "pair_exact": percent(m["pair_exact"]),
            "five": percent(m["five"]), "five_wins": m["five_wins"], "five_gain": percent(m["five"] - baseline),
            "five79": percent(m["five79"]), "five79_wins": m["five79_wins"],
            "reconstructed": [percent(reconstructed(key, s)) for s in SOURCES],
            "cost_single": f'{m["cost"]["single"]:.2f}', "cost_pair": f'{m["cost"]["pair"]:.2f}', "cost_five": f'{m["cost"]["five"]:.2f}',
        })
    (ROOT / "_data/second_life_tb4.json").write_text(json.dumps(data, indent=2) + "\n")

    # ------------------------------------------------------------ 1. Single: six confusion matrices
    alpha_of = lambda rate: 0.06 + 0.74 * rate  # wrong-verdict shading: share of the row's 79 runs
    for mobile in (False, True):
        ncol = 2 if mobile else 3
        nrow = len(REVIEWERS) // ncol
        W = 3.9 if mobile else 7.6
        left, gap = (0.74, 0.17) if mobile else (0.98, 0.3)
        cw = (W - left - (ncol - 1) * gap) / (2 * ncol)
        ch = 0.46 if mobile else 0.5
        title_h, head_h, foot_h, row_gap, key_h = (0.25, 0.2, 0.17, 0.1, 0.42) if mobile else (0.27, 0.21, 0.18, 0.06, 0.4)
        pad = 0.02
        block = title_h + head_h + 2 * ch + foot_h
        H = key_h + nrow * block + (nrow - 1) * row_gap
        fig = plt.figure(figsize=(W, H))
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis("off")
        fs = dict(title=9 if mobile else 9.5, head=7.5 if mobile else 8, pct=9.5 if mobile else 10.5, n=7 if mobile else 7.5,
                  row=8.5 if mobile else 9, sub=7 if mobile else 7.5, key=7.5 if mobile else 8)
        # Key: neutral = right verdict; red, darker with more of the row = wrong verdict.
        ky, sw = 0.13, 0.16
        kx = 0 if mobile else left + 0.02
        cell_box(ax, kx, ky, sw, sw * 0.8, color=LINE, alpha=0.75)
        ax.text(kx + sw + 0.07, ky + sw * 0.4, "Right verdict", fontsize=fs["key"], color=BODY, va="center")
        x = 1.18 if mobile else kx + 1.12
        for i, r in enumerate(np.linspace(0.1, 0.9, 5)):
            cell_box(ax, x + i * (sw + 0.03), ky, sw, sw * 0.8, color=ERROR, alpha=alpha_of(r))
        ax.text(x + 5 * (sw + 0.03) + 0.04, ky + sw * 0.4, "Wrong verdict,\ndarker = more of the row" if mobile else "Wrong verdict: darker = more of that row",
                fontsize=fs["key"], color=BODY, va="center", linespacing=1.15)
        for idx, key in enumerate(REVIEWERS):
            r, c = divmod(idx, ncol)
            x0 = left + c * (2 * cw + gap)
            y0 = key_h + r * (block + row_gap)
            ax.text(x0 + pad, y0 + title_h * 0.45, NAME[key], fontsize=fs["title"], weight="bold", color=INK, va="center")
            for j, head in enumerate(("Judged pass", "Judged fail")):
                ax.text(x0 + (j + 0.5) * cw, y0 + title_h + head_h * 0.45, head, fontsize=fs["head"], color=MUTED, ha="center", va="center")
            top = y0 + title_h + head_h
            for i, g in enumerate((1, 0)):
                for j, v in enumerate((1, 0)):
                    n = CM[key, g][v]
                    cx, cy = x0 + j * cw, top + i * ch
                    wrong = g != v
                    cell_box(ax, cx + pad, cy + pad, cw - 2 * pad, ch - 2 * pad, color=ERROR if wrong else LINE,
                             alpha=alpha_of(n / 79) if wrong else 0.75)
                    ax.text(cx + cw / 2, cy + ch * 0.43, f"{100 * n / 79:.1f}%", fontsize=fs["pct"], weight="bold" if wrong else "normal",
                            color=INK if wrong else BODY, ha="center", va="center")
                    ax.text(cx + cw / 2, cy + ch * 0.75, f"{n} of 79", fontsize=fs["n"], color=INK if wrong else BODY, ha="center", va="center")
                if c == 0:
                    ax.text(x0 - 0.08, top + (i + 0.4) * ch, "Succeeded" if g else "Failed", fontsize=fs["row"], color=BODY, ha="right", va="center")
                    ax.text(x0 - 0.08, top + (i + 0.72) * ch, "79 runs", fontsize=fs["sub"], color=MUTED, ha="right", va="center")
            invalid = [f'{CM[key, g]["invalid"]} {"succeeded" if g else "failed"}' for g in (1, 0) if CM[key, g]["invalid"]]
            if invalid:
                ax.text(x0 + pad, top + 2 * ch + foot_h * 0.5, "Invalid: " + ", ".join(invalid), fontsize=fs["sub"], color=MUTED, va="center")
        save(fig, "tb4-single-confusion" + ("-mobile" if mobile else ""),
             "Six Single confusion matrices, one per reviewer. Rows are recorded outcomes (79 succeeded, 79 failed runs); "
             "columns are Pass and Fail verdicts. Wrong-verdict cells are red, darker for a larger share of the row; right "
             "verdicts are gray. Invalid outputs are listed under a matrix and count as wrong.")

    # ------------------------------------------------------------ 2. Single accuracy versus Pair selection
    for mobile in (False, True):
        fig, ax = plt.subplots(figsize=(3.9, 3.3) if mobile else (7.6, 2.9), layout="constrained")
        for y, key in enumerate(REVIEWERS):
            c, s, p = COLOR[key], M[key]["single"] * 100, M[key]["pair"] * 100
            ax.plot([s, p], [y, y], color=c, alpha=TINT, lw=2.6, solid_capstyle="butt", zorder=2)
            ax.plot([s], [y], "o", ms=7, mfc="#ffffff", mec=c, mew=1.7, zorder=4)
            ax.plot([p], [y], "o", ms=7.5, color=c, mec="none", zorder=4)
            ax.annotate(f"{s:.1f}%", (s, y), xytext=(-7, 0), textcoords="offset points", ha="right", va="center", fontsize=8 if mobile else 8.5,
                        color=MUTED, zorder=5, bbox=dict(boxstyle="square,pad=0.1", fc="#ffffff", ec="none"))  # page-colored: hides the 50% line
            ax.annotate(f"{p:.1f}%", (p, y), xytext=(8, 0), textcoords="offset points", ha="left", va="center", fontsize=9.5, color=INK, weight="bold")
        ax.axvline(50, color=MUTED, lw=1, ls=(0, (3, 2.5)), zorder=1)
        ax.annotate("random 50%", (50, -0.55), xytext=(-4, -1), textcoords="offset points", ha="right", va="top", fontsize=8, color=MUTED)
        ax.set_yticks(range(len(REVIEWERS)), labels=[label(NAME[k], mobile) for k in REVIEWERS])
        ax.set_ylim(len(REVIEWERS) - 0.45, -0.75)
        ax.set_xlim(40, 84)
        x_grid(ax, [40, 50, 60, 70, 80])
        ax.set_xlabel("Share correct")
        fig.legend(handles=[Line2D([], [], ls="", marker="o", ms=7, mfc="none", mec=BODY, mew=1.6, label="Single: judge one run"),
                            Line2D([], [], ls="", marker="o", ms=7.5, color=BODY, mec="none", label="Pair: pick the better of two")],
                   loc="outside upper left", ncol=1 if mobile else 2, frameon=False, fontsize=9, handletextpad=0.2,
                   columnspacing=1.2, borderaxespad=0)
        save(fig, "tb4-single-pair" + ("-mobile" if mobile else ""),
             "For each reviewer, a ring marks Single accuracy on 158 runs and a dot marks how often Pair picks the "
             "successful run of two, on the same 79 pools. A dashed line marks the 50% random baseline.")

    # ------------------------------------------------------------ 3. Five by source: lollipops from the random pick
    for mobile in (False, True):
        fig, axes = plt.subplots(2 if mobile else 1, 2 if mobile else 4, figsize=(3.9, 5.4) if mobile else (7.6, 3.0),
                                 sharex=True, sharey=True, layout="constrained")
        for ax, s in zip(axes.flat, SOURCES):
            base = SRC[s]["uniform_rate"] * 100
            for y, key in enumerate(REVIEWERS):
                rate = M[key]["by_source"][s] / SRC[s]["pools"] * 100
                gain = rate - base
                ax.plot([0, gain], [y, y], color=COLOR[key], lw=2.2, solid_capstyle="butt", zorder=2)
                ax.plot([gain], [y], "o", ms=6, color=COLOR[key], mec="none", zorder=4)
                ax.annotate(f"{rate:.1f}%", (max(gain, 0), y), xytext=(6 if gain >= 0 else 5, 0), textcoords="offset points",
                            ha="left", va="center", fontsize=8, color=BODY)
            ax.axvline(0, color=MUTED, lw=0.8, alpha=0.6, zorder=1)
            ax.set_xlim(-16, 48)
            ax.set_xticks([0, 20, 40], labels=["0", "+20", "+40"])
            ax.grid(axis="x", **GRID)
            ax.set_axisbelow(True)
            ax.tick_params(length=0, pad=4)
            ax.text(0, 1.13 if mobile else 1.12, SOURCE_NAME[s], transform=ax.transAxes, fontsize=9.5, weight="bold", color=INK, ha="left", va="bottom")
            ax.text(0, 1.025, f'{SRC[s]["pools"]} pools · random {SRC[s]["uniform"]}%', transform=ax.transAxes, fontsize=8.5, color=MUTED, ha="left", va="bottom")
        axes.flat[0].set_yticks(range(len(REVIEWERS)), labels=[label(NAME[k], mobile) for k in REVIEWERS])
        axes.flat[0].set_ylim(len(REVIEWERS) - 0.5, -0.5)
        fig.supxlabel("Points above a random pick", fontsize=9, color=BODY)
        save(fig, "tb4-five-by-source" + ("-mobile" if mobile else ""),
             "Five selection by source. One panel per source, one row per reviewer; each line runs from that source's "
             "random-pick rate to the reviewer's selection rate, which is labeled. Mixed pools only.")

    # ------------------------------------------------------------ 4. Whole job: pass@1, the two best selectors, oracle pass@5
    for mobile in (False, True):
        fig, ax = plt.subplots(figsize=(3.9, 3.4) if mobile else (7.6, 3.1), layout="constrained")
        w, gap = (0.19, 0.02) if mobile else (0.18, 0.025)
        for i, s in enumerate(SOURCES):
            p1, p5 = SRC[s]["pass_at_k"][0] * 100, SRC[s]["pass_at_k"][-1] * 100
            bars = ([(p1, MUTED, 0.42, MUTED, "normal")] + [(reconstructed(k, s) * 100, COLOR[k], 1, INK, "bold") for k in TOP2]
                    + [(p5, MUTED, 0.24, MUTED, "normal")])
            xs = i + (np.arange(4) - 1.5) * (w + gap)
            for x, (v, c, a, ink, weight) in zip(xs, bars):
                ax.bar(x, v, width=w, color=c, alpha=a, zorder=2)
                ax.annotate(f"{v:.0f}" if mobile else f"{v:.1f}", (x, v), xytext=(0, 3), textcoords="offset points",
                            ha="center", va="bottom", fontsize=7 if mobile else 8.5, color=ink, weight=weight)
        ax.set_xticks(range(4), labels=[SOURCE_NAME[s].replace(" ", "\n", 1) if mobile else SOURCE_NAME[s] for s in SOURCES])
        ax.tick_params(axis="x", length=0, pad=6, labelcolor=BODY, labelsize=9 if mobile else 9.5)
        ax.set_ylim(0, 88)
        ax.set_yticks([])  # every bar carries its own label
        ax.axhline(0, color=LINE, lw=1, zorder=3)
        handles = [Patch(color=MUTED, alpha=0.42, label="pass@1 (one attempt)"),
                   Patch(color=COLOR["opus-5-5"], label="Opus 5.5 picks from five"),
                   Patch(color=COLOR["gpt-5-6-sol"], label="GPT-5.6 Sol picks from five"),
                   Patch(color=MUTED, alpha=0.24, label="Oracle pass@5")]
        fig.legend(handles=[handles[i] for i in ((0, 2, 1, 3) if mobile else range(4))],
                   loc="outside upper left", ncol=2 if mobile else 4, frameon=False, fontsize=8.5 if mobile else 9,
                   handlelength=1.2, handletextpad=0.5, columnspacing=1.2 if mobile else 1.6, borderaxespad=0)
        save(fig, "tb4-sampling-hero" + ("-mobile" if mobile else ""),
             "Whole-job success on all 66 tasks per source: pass@1, the reconstructed success when Opus 5.5 or GPT-5.6 Sol "
             "picks one of five attempts, and oracle pass@5.")

    # ------------------------------------------------------------ 5. Review cost versus performance
    ticks = [0.05, 0.1, 0.2, 0.5, 1, 2, 5]
    # Hand-placed label offsets (points) keep six names clear of each other.
    offsets = {
        "five": {"opus-5-5": (0, 11, "center"), "gpt-5-6-sol": (8, 0, "left"), "gpt-6-sol": (8, -2, "left"),
                 "glm-5-3-flash": (8, 0, "left"), "glm-5-3": (8, 0, "left"), "deepseek-v4p1-flash": (8, 0, "left")},
        "single": {"opus-5-5": (0, 11, "center"), "gpt-5-6-sol": (8, 6, "left"), "gpt-6-sol": (8, -9, "left"),
                   "glm-5-3-flash": (8, 0, "left"), "glm-5-3": (8, -7, "left"), "deepseek-v4p1-flash": (8, 8, "left")},
    }
    for mobile in (False, True):
        fig, axes = plt.subplots(2 if mobile else 1, 1 if mobile else 2, figsize=(3.9, 6.2) if mobile else (7.6, 3.3), layout="constrained")
        panels = [("five", "Five: pick one of five", "five79", baseline79, (50, 86)),
                  ("single", "Single: judge one run", "single", 0.5, (46, 66))]
        for ax, (cond, title, metric, base, ylim) in zip(axes, panels):
            pts = [(M[k]["cost"][cond], M[k][metric] * 100, k) for k in REVIEWERS]
            front, best = [], -1
            for c, v, k in sorted(pts):
                if v > best:
                    front.append((c, v)); best = v
            ax.plot(*zip(*front), color=LINE, lw=3, alpha=0.8, zorder=1, solid_capstyle="round", solid_joinstyle="round")
            for c, v, k in pts:
                ax.plot([c], [v], "o", ms=9, color=COLOR[k], mec="#ffffff", mew=1.6, zorder=4)
                dx, dy, ha = offsets[cond][k]
                ax.annotate(NAME[k], (c, v), xytext=(dx, dy), textcoords="offset points", ha=ha, va="center",
                            fontsize=8 if mobile else 8.5, color=BODY)
            ax.axhline(base * 100, color=MUTED, lw=0.9, ls=(0, (2, 3)), alpha=0.8, zorder=1)
            ax.annotate(f"random {base * 100:.1f}%" if cond == "five" else "random 50%", (3.4, base * 100), xytext=(-2, 3),
                        textcoords="offset points", ha="right", va="bottom", fontsize=8, color=MUTED)
            ax.set_xlim(-0.1, 3.4)
            ax.set_xticks([0, 1, 2, 3], labels=["$0", "$1", "$2", "$3"])
            ax.xaxis.set_minor_locator(NullLocator())
            ax.grid(axis="y", **GRID)
            ax.set_axisbelow(True)
            ax.tick_params(length=0, pad=5, labelcolor=MUTED)
            ax.set_ylim(*ylim)
            yt = list(range(int(np.ceil(ylim[0] / 5) * 5), ylim[1] + 1, 5))
            ax.set_yticks(yt, labels=[f"{t}%" for t in yt])
            ax.set_title(title, loc="left", fontsize=9.5, weight="bold", color=INK, pad=8)
            ax.set_xlabel("Mean cost per review")
        save(fig, "tb4-cost-performance" + ("-mobile" if mobile else ""),
             "Mean recorded cost per review against Five selection success and Single accuracy for each "
             "reviewer, on the 79 pools with recorded costs for every reviewer. A gray line joins reviewers that no "
             "cheaper reviewer beats.")

    # ------------------------------------------------------------ 6. DeepSeek prompt check
    neutral = next(r for r in read("tbench4-complete-comparison.json") if r["condition"] == "five_neutral")
    original = read("deepseek-five-positions.json")["original_counts"]
    control = [neutral["selected_candidate_counts"].get(str(i), 0) for i in range(1, 6)]
    for mobile in (False, True):
        fig, ax = plt.subplots(figsize=(3.9, 2.6) if mobile else (7.6, 2.6), layout="constrained")
        x = np.arange(1, 6)
        for off, vals, alpha, lab in [(-0.2, original, TINT, "Original prompt (example says 3) · 58.2% success"),
                                      (0.2, control, 1, "Neutral prompt · 59.5% success")]:
            ax.bar(x + off, vals, width=0.36, color=COLOR["deepseek-v4p1-flash"], alpha=alpha, zorder=2, label=lab)
            for xi, v in zip(x + off, vals):
                if v:
                    ax.annotate(str(v), (xi, v), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=8.5, color=BODY)
        ax.set_xticks(x, labels=[f"#{i}" for i in x])
        ax.tick_params(axis="x", length=0, labelcolor=BODY, labelsize=9)
        ax.set_ylim(0, 80)
        ax.set_yticks([])  # every bar carries its own count
        ax.axhline(0, color=LINE, lw=1, zorder=3)
        ax.set_xlabel("Candidate DeepSeek V4.1 Flash picked, out of 79 reviews")
        fig.legend(loc="outside upper left", ncol=1, frameon=False, fontsize=9, handlelength=1.2, handletextpad=0.5, borderaxespad=0)
        save(fig, "tb4-prompt-position" + ("-mobile" if mobile else ""),
             "Which candidate position DeepSeek V4.1 Flash picked in 79 Five reviews, with the original prompt (whose "
             "example output picks candidate 3) and with a neutral prompt.")

    # ------------------------------------------------------------ 7. Oracle pass@k (appendix)
    for mobile in (False, True):
        fig, ax = plt.subplots(figsize=(3.9, 3.0) if mobile else (7.6, 3.0), layout="constrained")
        for s in SOURCES:
            ys = np.array(SRC[s]["pass_at_k"]) * 100
            c = SOURCE_COLOR[s]
            ax.plot(range(1, 6), ys, "-", color=c, lw=2, solid_capstyle="round", zorder=3)
            ax.plot(range(1, 6), ys, "o", ms=5, color=c, mec="#ffffff", mew=1.2, zorder=4)
            ax.annotate(f"{SOURCE_NAME[s]}  {ys[-1]:.1f}%", (5, ys[-1]), xytext=(8, 0), textcoords="offset points",
                        ha="left", va="center", fontsize=8.5 if mobile else 9, color=BODY)
        ax.set_xticks(range(1, 6))
        ax.set_xlim(0.85, 5.1)
        ax.set_ylim(30, 84)
        ax.set_yticks([30, 40, 50, 60, 70, 80], labels=[f"{t}%" for t in (30, 40, 50, 60, 70, 80)])
        ax.grid(axis="y", **GRID)
        ax.set_axisbelow(True)
        ax.tick_params(length=0, pad=5, labelcolor=MUTED)
        ax.set_xlabel("Attempts per task (k)")
        ax.set_ylabel("Oracle pass@k")
        save(fig, "tb4-oracle-curves" + ("-mobile" if mobile else ""),
             "Oracle pass@k for k = 1 to 5 for each source, over all 66 tasks. These show what an oracle could get, "
             "not reviewer results.")

    # ------------------------------------------------------------ 8. Shared-task heatmap (appendix)
    def cell(key, s, cond, tasks):
        subset = select(key, cond, s)
        matched = [r for r in subset if r["task_name"] in tasks]
        wins, n = sum(map(score, matched)), len(matched)
        base = sum(sum(r["gold_rewards"]) for r in matched) / (5 * n) if cond == "five-full" else 0.5
        return wins, n, wins / n - base, sum(map(score, subset)) / len(subset)

    def heatmap(name, srcs, tasks, panels, mobile, description):
        # Desktop: sources are rows, reviewers columns. Mobile: transposed so the six reviewers become rows.
        n_r, n_c = (len(REVIEWERS), len(srcs)) if mobile else (len(srcs), len(REVIEWERS))
        cw, ch = (0.96 if len(srcs) == 3 else 0.74, 0.42) if mobile else (0.98, 0.46)
        left = 1.02 if mobile else 1.05
        panel_h = 0.5 + n_r * ch
        height = 0.55 + len(panels) * (panel_h + 0.28)
        width = left + n_c * cw
        fig = plt.figure(figsize=(width, height))
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(0, width); ax.set_ylim(height, 0); ax.axis("off")
        for i, d in enumerate(np.linspace(-1, 1, 41)):  # continuous legend strip, percentage points from random
            ax.add_patch(Rectangle((left + i * 0.03, 0.16), 0.03, 0.12, color=ABOVE if d >= 0 else BELOW, alpha=0.1 + 0.6 * abs(d), lw=0))
        ax.text(left - 0.08, 0.22, "vs random", ha="right", va="center", fontsize=8, color=MUTED)
        for d, lab in [(-1, "−100 pp"), (0, "0"), (1, "+100 pp")]:
            ax.text(left + (d + 1) / 2 * 1.23, 0.4, lab, ha="center", va="center", fontsize=7.5, color=MUTED)
        y0 = 0.62
        for title, cond in panels:
            ax.text(0, y0 + 0.12, title, ha="left", va="center", fontsize=9.5, weight="bold", color=INK)
            heads = [SOURCE_NAME[s] for s in srcs] if mobile else [NAME[k].replace(" V4.1 Flash", "\nV4.1 Flash").replace(" Flash", "\nFlash") for k in REVIEWERS]
            for j, head in enumerate(heads):
                ax.text(left + (j + 0.5) * cw, y0 + 0.38, head, ha="center", va="center", fontsize=7.5 if mobile else 8, color=BODY, linespacing=1.1)
            for i in range(n_r):
                key, s = (REVIEWERS[i], None) if mobile else (None, srcs[i])
                ax.text(left - 0.08, y0 + 0.56 + (i + 0.5) * ch, NAME[key] if mobile else SOURCE_NAME[s], ha="right", va="center",
                        fontsize=8 if mobile else 8.5, color=BODY)
                for j in range(n_c):
                    k2, s2 = (key, srcs[j]) if mobile else (REVIEWERS[j], s)
                    wins, n, delta, all_rate = cell(k2, s2, cond, tasks)
                    x, y = left + j * cw, y0 + 0.56 + i * ch
                    ax.add_patch(Rectangle((x + 0.02, y + 0.02), cw - 0.04, ch - 0.04, color=ABOVE if delta >= 0 else BELOW,
                                           alpha=0.08 + 0.6 * min(abs(delta), 1), lw=0))
                    ax.text(x + cw / 2, y + ch * 0.36, f"{100 * wins / n:.0f}% ({wins}/{n})", ha="center", va="center",
                            fontsize=7.5 if mobile else 8.5, color=INK, weight="bold")
                    ax.text(x + cw / 2, y + ch * 0.72, f"{100 * delta:+.0f} pp · all {100 * all_rate:.0f}%", ha="center", va="center",
                            fontsize=6.5 if mobile else 7.5, color=BODY)
            y0 += panel_h + 0.28
        save(fig, name + ("-mobile" if mobile else ""), description)

    three = shared(rows, ORIGINAL)
    assert len(three) == 6
    for mobile in (False, True):
        heatmap("tb4-shared-heatmap", ORIGINAL, three, [("Single: classify success or failure", "single-full"),
                                                         ("Pair: select the successful attempt", "pair-full"),
                                                         ("Five: select any successful attempt", "five-full")], mobile,
                "Scores on the six tasks shared by the three original sources, by source and reviewer, for Single, Pair "
                "and Five. Blue cells are above random and red cells below; each cell also gives the score on all pools.")
    print(f"Generated TB4 data and eight figure families from {COMMIT[:7]}; {total_pools} pools, baseline {baseline:.6f}.")


if __name__ == "__main__":
    main()
