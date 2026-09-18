#!/usr/bin/env python3
"""Rebuild the TB4 blog data and figures from checked-in, pinned result snapshots.

Requires matplotlib. No network access or model calls. The older
generate_second_life_agent_eval_figures.py reproduces the historical TB3 pilot.
"""

from __future__ import annotations

import json
import os
from math import comb
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/second-life-matplotlib")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "assets/data/second-life-tb4"
OUTPUT = ROOT / "assets/img/2026-08-28-second-life-agent-evals"
COMMIT = "6d99501ad21662cad4ef82c9089e15492d24e976"
REPO = f"https://github.com/XinmingTu/Agentic-Verification-Eval/blob/{COMMIT}"
REVIEWERS = {
    "gpt-5-6-sol": "GPT-5.6 Sol",
    "glm-5-3": "GLM-5.3",
    "deepseek-v4p1-flash": "DeepSeek V4.1 Flash",
    "glm-5-3-flash": "GLM-5.3 Flash",
}
SOURCES = {
    "fable-5.1": "Fable 5.1",
    "gpt-5.6-sol": "GPT-5.6 Sol",
    "glm-5.3": "GLM-5.3",
    "gpt-6-astra": "GPT-6 Astra",
}
COLORS = ["#4f68b3", "#287a68", "#a75e3c", "#8971aa"]


def read(name):
    return json.loads((INPUT / name).read_text())


def percent(value):
    return f"{value * 100:.1f}"


def save(fig, name, description):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT / f"{name}.svg", bbox_inches="tight", metadata={
        "Date": None, "Creator": "generate_second_life_tb4_figures.py",
        "Description": description,
    })
    # A local raster copy makes visual QA possible without adding another asset.
    fig.savefig(Path("/tmp") / f"{name}.png", dpi=140, bbox_inches="tight")
    plt.close(fig)


def main():
    plt.rcParams.update({
        "font.family": "sans-serif", "font.sans-serif": ["Arial", "DejaVu Sans"], "font.size": 11,
        "text.color": "#20242d", "axes.labelcolor": "#434a57",
        "xtick.color": "#434a57", "ytick.color": "#434a57",
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.edgecolor": "#dfe4e9", "svg.fonttype": "none",
        "svg.hashsalt": "second-life-tb4", "figure.facecolor": "white",
    })
    complete = read("tbench4-complete-comparison.json")
    panels = {r["reviewer"]: r for r in complete if r["condition"] == "single_pair"}
    panels.update({r["reviewer"]: r for r in read("tbench4-glm-flash-complete-comparison.json")})
    gpt6 = {r["reviewer"]: r for r in read("tbench4-gpt6-source-comparison.json")}
    sources = read("tbench4-pass-at-k.json")["sources"]
    counts = {r["reviewer"]: r["confusion"] for r in read("single-verdict-counts.json")["reviewers"]}
    total_pools = sum(s["reviewed_mixed_pools"] for s in sources)
    candidate_successes = sum(round(s["pass_at_k"][0] * s["tasks"] * 5)
                              - s["all_pass_pools"] * 5
                              - sum(s["unreviewed_mixed_pools"].values()) for s in sources)
    baseline = candidate_successes / (total_pools * 5)
    data = {"commit": COMMIT, "repo": REPO, "updated": "September 18, 2026",
            "five_pools": total_pools, "source_runs": total_pools * 5,
            "five_baseline": percent(baseline), "candidate_successes": candidate_successes,
            "reviewers": [], "sources": []}

    for key, label in REVIEWERS.items():
        m = panels[key]["metrics"]
        cm = counts[key]
        assert sum(map(sum, cm)) == m["single_full"]["n"] == 158
        assert all(sum(row) == 79 for row in cm)
        assert np.isclose(cm[0][0] / 79, m["single_full"]["success_recall"])
        assert np.isclose(cm[1][1] / 79, m["single_full"]["failure_recall"])
        assert cm[0][0] + cm[1][1] == round(m["single_full"]["accuracy"] * 158)
        assert cm[0][2] + cm[1][2] == m["single_full"]["confusion"]["invalid_outputs"]
        n = m["five_full"]["n"] + gpt6[key]["metrics"]["five_full"]["n"]
        wins = round(m["five_full"]["selection_success_rate"] * m["five_full"]["n"])
        wins += round(gpt6[key]["metrics"]["five_full"]["selection_success_rate"] * 18)
        assert n == total_pools
        ci = panels[key]["cluster_bootstrap_95_ci"]
        data["reviewers"].append({
            "key": key, "name": label, "single": percent(m["single_full"]["accuracy"]),
            "success_recall": percent(m["single_full"]["success_recall"]),
            "failure_recall": percent(m["single_full"]["failure_recall"]),
            "false_pass": percent(cm[1][0] / 79),
            "single_invalid": cm[0][2] + cm[1][2],
            "pair": percent(m["pair_full"]["preferred_success_rate"]),
            "pair_exact": percent(m["pair_full"]["exact_pair_classification_rate"]),
            "five": percent(wins / n), "five_wins": wins,
            "five_gain": percent(wins / n - baseline),
            "single_ci": f'{percent(ci["single-full"]["lower"])}–{percent(ci["single-full"]["upper"])}',
            "pair_ci": f'{percent(ci["pair-full"]["lower"])}–{percent(ci["pair-full"]["upper"])}',
        })
        assert sum(s["reviewer_mixed_successes"][key] for s in sources) == wins
    for s in sources:
        excluded = list(s["unreviewed_mixed_pools"].values())
        included_tasks = s["tasks"] - len(excluded)
        # Remove the same excluded pools from both the oracle curve and selection.
        pass_at_k = [
            (rate * s["tasks"] - sum(1 - comb(5 - c, k) / comb(5, k) for c in excluded)) / included_tasks
            for k, rate in enumerate(s["pass_at_k"], start=1)
        ]
        effective = (s["all_pass_pools"] + s["reviewer_mixed_successes"]["gpt-5-6-sol"]) / included_tasks
        successes = round(s["pass_at_k"][0] * s["tasks"] * 5) - s["all_pass_pools"] * 5 - sum(excluded)
        uniform = successes / (s["reviewed_mixed_pools"] * 5)
        assert np.isclose(pass_at_k[0], (successes + s["all_pass_pools"] * 5) / (included_tasks * 5))
        assert np.isclose(pass_at_k[-1], (s["all_pass_pools"] + s["reviewed_mixed_pools"]) / included_tasks)
        assert all(a <= b + 1e-12 for a, b in zip(pass_at_k, pass_at_k[1:]))
        assert effective <= pass_at_k[-1] + 1e-12
        data["sources"].append({
            "name": SOURCES[s["source"]], "pools": s["reviewed_mixed_pools"],
            "uniform": percent(uniform), "uniform_rate": uniform,
            "reviewer_rates": [percent(s["reviewer_mixed_successes"][key] / s["reviewed_mixed_pools"]) for key in REVIEWERS],
            "gpt_selection_gain": percent(s["reviewer_mixed_successes"]["gpt-5-6-sol"] / s["reviewed_mixed_pools"] - uniform),
            "included_tasks": included_tasks, "excluded_pools": len(excluded), "pass_at_k": pass_at_k,
            "pass1": percent(pass_at_k[0]), "pass5": percent(pass_at_k[-1]),
            "selected": percent(effective), "gain": percent(effective - pass_at_k[0]),
            "selected_rate": effective,
        })
    data["cost_batches"] = []
    for label, filename in [
        ("September 16 completion + prompt control", "tbench4-complete-progress.json"),
        ("GPT-6-source Five extension", "tbench4-gpt6-source-progress.json"),
        ("GLM Flash Single/Pair completion", "tbench4-glm-flash-complete-progress.json"),
    ]:
        ledger = read(filename)
        data["cost_batches"].append({"name": label,
            "reviews": sum(p["completed_new"] for p in ledger["progress"]),
            "cost": f'{ledger["accounted_new_cost_usd"]:.2f}'})
    (ROOT / "_data/second_life_tb4.json").write_text(json.dumps(data, indent=2) + "\n")

    # Show literal pass/fail predictions. Invalid mass stays in the denominator
    # but is not assigned to either visible column, so rows may sum below 100%.
    for mobile in (False, True):
        fig, axes = plt.subplots(4 if mobile else 2, 1 if mobile else 2, figsize=(4.4, 9.4) if mobile else (8.4, 5.6), layout="constrained")
        cmap = LinearSegmentedColormap.from_list("predictions", ["#f3f6fb", "#3757a6"])
        for ax, (key, label) in zip(axes.flat, REVIEWERS.items()):
            rates = np.array(counts[key])[:, :2] / 79 * 100
            heatmap = ax.imshow(rates, cmap=cmap, vmin=0, vmax=100, aspect="auto")
            for i in range(2):
                for j in range(2):
                    value = rates[i, j]
                    ax.text(j, i, f"{value:.1f}%", ha="center", va="center",
                            fontsize=19, weight="bold", color="white" if value >= 60 else "#20242d")
            ax.set(xticks=[0, 1], xticklabels=["Pass", "Fail"],
                   yticks=[0, 1], yticklabels=["Succeeded", "Failed"], xlabel="Reviewer verdict")
            ax.set_title(label, weight="bold", pad=10)
            ax.tick_params(length=0, pad=7)
            ax.set_xticks([.5], minor=True)
            ax.set_yticks([.5], minor=True)
            ax.grid(which="minor", color="white", linewidth=3)
            ax.tick_params(which="minor", length=0)
            for spine in ax.spines.values():
                spine.set_visible(False)
        colorbar = fig.colorbar(heatmap, ax=axes, fraction=.035, pad=.035, ticks=[0, 25, 50, 75, 100])
        colorbar.set_label("Share of each outcome class (%)", labelpad=10)
        colorbar.outline.set_visible(False)
        save(fig, "tb4-single-confusion" + ("-mobile" if mobile else ""), "Single: source outcomes in rows, reviewer verdicts in columns. Percentages use 79 anchors per row. Invalid outputs are omitted from columns, retained in denominators. Shared 0–100% scale.")

    short_labels = ["GPT-5.6\nSol", "GLM-5.3", "DeepSeek\nV4.1 Flash", "GLM-5.3\nFlash"]
    for mobile in (False, True):
        fig, axes = plt.subplots(2 if mobile else 1, 1 if mobile else 2, figsize=(4.4, 6.7) if mobile else (8.4, 4), layout="constrained", sharey=True)
        for ax, metric, title, ylabel in zip(axes, ["single", "pair"],
                                           ["Single · 158 runs", "Pair · 79 pools"],
                                           ["Correct judgments (%)", "Successful selections (%)"]):
            vals = [float(r[metric]) for r in data["reviewers"]]
            bars = ax.bar(range(4), vals, color=COLORS, width=.65)
            ax.bar_label(bars, labels=[f"{v:.1f}%" for v in vals], padding=5, fontsize=10, weight="bold", bbox={"facecolor": "white", "edgecolor": "none", "pad": .3})
            ax.axhline(50, color="#747d8b", linestyle="--", linewidth=1.4, clip_on=False, zorder=4)
            ax.spines["bottom"].set_visible(False)
            ax.set(xticks=range(4), xticklabels=short_labels, ylim=(50, 100), yticks=[50, 60, 70, 80, 90, 100], ylabel=ylabel, title=title)
            ax.tick_params(axis="x", labelsize=9)
            ax.set_axisbelow(True)
            ax.grid(axis="y", alpha=.15)
        save(fig, "tb4-single-pair" + ("-mobile" if mobile else ""), "Single accuracy (79 successful and 79 failed runs) and Pair successful selection on the same 79 pools. Axes start at the dashed 50% baselines. Different metrics, not a causal context-gain estimate.")

    for mobile in (False, True):
        fig, axes = plt.subplots(4 if mobile else 2, 1 if mobile else 2, figsize=(4.4, 11.8) if mobile else (8.4, 6.6), layout="constrained", sharey=True)
        for ax, s in zip(axes.flat, data["sources"]):
            vals = [float(v) for v in s["reviewer_rates"]]
            bars = ax.bar(range(4), vals, color=COLORS, width=.65)
            ax.bar_label(bars, labels=[f"{v:.1f}%" for v in vals], padding=5, fontsize=10, weight="bold", bbox={"facecolor": "white", "edgecolor": "none", "pad": .3})
            ax.axhline(s["uniform_rate"] * 100, color="#747d8b", linestyle="--", linewidth=1.4)
            ax.set(xticks=range(4), xticklabels=short_labels, ylim=(0, 103), yticks=[0, 25, 50, 75, 100])
            ax.set_title(f'{s["name"]} · {s["pools"]} pools\nUniform choice: {s["uniform"]}%', fontsize=11, pad=12)
            ax.tick_params(axis="x", labelsize=9)
            ax.set_axisbelow(True)
            ax.grid(axis="y", alpha=.15)
        for ax in (axes if mobile else axes[:, 0]):
            ax.set_ylabel("Successful selections (%)")
        save(fig, "tb4-five-by-source" + ("-mobile" if mobile else ""), "Five selection by source and reviewer; fixed reviewer colors and order, source-specific uniform baselines, invalid outputs counted as failures. Source task sets differ.")

    for mobile in (False, True):
        fig, axes = plt.subplots(4 if mobile else 2, 1 if mobile else 2, figsize=(4.8, 12.6) if mobile else (8.8, 7), layout="constrained", sharex=True, sharey=True)
        for ax, item in zip(axes.flat, data["sources"]):
            ys = np.array(item["pass_at_k"]) * 100
            mid = item["selected_rate"] * 100
            color = COLORS[0]
            ax.plot(range(1, 6), ys, "o-", color=color, linewidth=2, label="Oracle pass@k")
            ax.hlines(ys[0], 1, 5, color="#b8c0ce", linestyle=":", linewidth=1)
            ax.plot(5, mid, "*", color="#20242d", markersize=14, label="GPT-5.6 Sol reviewer at k=5")
            ax.annotate(f"{mid:.1f}% selected", (5, mid), xytext=(-12, -19), textcoords="offset points", ha="right", fontsize=10, weight="bold", bbox={"facecolor": "white", "edgecolor": "none", "pad": .3})
            ax.annotate(f"{ys[-1]:.1f}% oracle", (5, ys[-1]), xytext=(-10, 10), textcoords="offset points", ha="right", fontsize=10, color=color)
            ax.annotate(f"{ys[0]:.1f}%", (1, ys[0]), xytext=(6, -17), textcoords="offset points", fontsize=10, color="#747d8b")
            ax.set_title(f'{item["name"]} · {item["included_tasks"]} tasks\n+{item["gain"]} pp over pass@1', fontsize=12, pad=12)
            ax.set(xticks=range(1, 6), xlim=(.7, 5.5), ylim=(30, 88), yticks=[30, 40, 50, 60, 70, 80])
            ax.grid(alpha=.18)
        for ax in (axes if mobile else axes[:, 0]):
            ax.set_ylabel("Success on included tasks (%)")
        for ax in ([axes[-1]] if mobile else axes[1]):
            ax.set_xlabel("Number of frozen attempts (k)")
        handles, labels = axes.flat[0].get_legend_handles_labels()
        fig.legend(handles, labels, loc="outside lower center", ncol=1 if mobile else 2, frameon=False)
        save(fig, "tb4-sampling-hero" + ("-mobile" if mobile else ""), "Oracle pass@1–5 and reconstructed selection stars using GPT-5.6 Sol at k=5, on the same included tasks per source. Excludes 3 Fable, 5 GPT, 2 GLM, and 0 GPT-6 mixed pools from both curves and stars. Homogeneous pools assume valid selection; no fallback is used.")

    neutral = next(r for r in complete if r["condition"] == "five_neutral")
    original_rows = read("deepseek-five-positions.json")
    fig, ax = plt.subplots(figsize=(9, 3.6), layout="constrained")
    x = np.arange(1, 6)
    original = original_rows["original_counts"]
    control = [neutral["selected_candidate_counts"].get(str(i), 0) for i in x]
    for offsets, vals, color, label in [(x-.18, original, COLORS[2], "Original example · 58.2% success"), (x+.18, control, COLORS[0], "Neutral example · 59.5% success")]:
        bars = ax.bar(offsets, vals, width=.36, color=color, label=label)
        ax.bar_label(bars, padding=3, fontsize=10)
    ax.set(xlabel="Selected candidate position", ylabel="Selections (out of 79)", xticks=x, ylim=(0, 87))
    ax.legend(frameon=False, loc="upper right", fontsize=10)
    save(fig, "tb4-prompt-position", "DeepSeek V4.1 Flash changes position preference after removing the numbered output example; the success difference is inconclusive.")
    print(f"Generated TB4 data and five figures from {COMMIT}; {total_pools} pools, baseline {baseline:.6f}.")


if __name__ == "__main__":
    main()
