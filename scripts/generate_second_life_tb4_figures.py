#!/usr/bin/env python3
"""Rebuild the TB4 blog data and figures from checked-in, pinned result snapshots.

Requires matplotlib. No network access or model calls. The older
generate_second_life_agent_eval_figures.py reproduces the historical TB3 pilot.
"""

from __future__ import annotations

import json
import os
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
            "single_invalid": cm[0][2] + cm[1][2],
            "pair": percent(m["pair_full"]["preferred_success_rate"]),
            "pair_exact": percent(m["pair_full"]["exact_pair_classification_rate"]),
            "five": percent(wins / n), "five_wins": wins,
            "five_gain": percent(wins / n - baseline),
            "single_ci": f'{percent(ci["single-full"]["lower"])}–{percent(ci["single-full"]["upper"])}',
            "pair_ci": f'{percent(ci["pair-full"]["lower"])}–{percent(ci["pair-full"]["upper"])}',
        })
    for s in sources:
        fallback = sum(s["unreviewed_mixed_pools"].values()) / 5
        effective = (s["all_pass_pools"] + s["reviewer_mixed_successes"]["gpt-5-6-sol"] + fallback) / s["tasks"]
        data["sources"].append({
            "name": SOURCES[s["source"]], "pools": s["reviewed_mixed_pools"],
            "pass1": percent(s["pass_at_k"][0]), "pass5": percent(s["pass_at_k"][-1]),
            "selected": percent(effective), "gain": percent(effective - s["pass_at_k"][0]),
            "coverage_bounds": f'{percent(s["missing_pool_lower_bound"])}–{percent(s["missing_pool_upper_bound"])}',
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

    # Recall retains all 79 anchors in each class, including invalid outputs.
    recall = np.array([[panels[key]["metrics"]["single_full"][metric] * 100
                        for metric in ("success_recall", "failure_recall")]
                       for key in REVIEWERS])
    fig, ax = plt.subplots(figsize=(7.6, 3.8), layout="constrained")
    cmap = LinearSegmentedColormap.from_list("recall", ["#f3f6fb", "#3757a6"])
    heatmap = ax.imshow(recall, cmap=cmap, vmin=0, vmax=100, aspect="auto")
    for i in range(4):
        for j in range(2):
            value = recall[i, j]
            ax.text(j, i, f"{value:.1f}%", ha="center", va="center",
                    fontsize=18, weight="bold", color="white" if value >= 60 else "#20242d")
    ax.set(xticks=[0, 1], xticklabels=["Success recall", "Failure recall"],
           yticks=range(4), yticklabels=list(REVIEWERS.values()))
    ax.xaxis.tick_top()
    ax.tick_params(length=0, pad=12)
    ax.set_xticks([.5], minor=True)
    ax.set_yticks([.5, 1.5, 2.5], minor=True)
    ax.grid(which="minor", color="white", linewidth=3)
    ax.tick_params(which="minor", length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    colorbar = fig.colorbar(heatmap, ax=ax, fraction=.045, pad=.04, ticks=[0, 25, 50, 75, 100])
    colorbar.set_label("Correctly identified (%)", labelpad=10)
    colorbar.outline.set_visible(False)
    save(fig, "tb4-single-recall", "Single Full success and failure recall. Each class has 79 anchors per reviewer. Invalid outputs count as errors; the shared color scale spans 0 to 100 percent.")

    fig, axes = plt.subplots(2, 1, figsize=(8, 7), layout="constrained")
    for ax, metric, title, base in zip(axes, ["pair", "five"], ["Pair · 79 pools / 3 sources", "Five · 97 pools / 4 sources"], [50, baseline * 100]):
        vals = [float(r[metric]) for r in data["reviewers"]]
        ax.barh(range(4), vals, color=COLORS, height=.55)
        ax.axvline(base, color="#747d8b", linestyle="--", linewidth=1.4)
        for i, v in enumerate(vals):
            ax.text(v + 1, i, f"{v:.1f}%", va="center", fontsize=11, weight="bold")
        ax.set(yticks=range(4), yticklabels=list(REVIEWERS.values()), xlim=(0, 100), xlabel="Successful selection (%)", title=title)
        ax.set_xticks([0, 25, 50, 75, 100])
        ax.text(.02, -.24, f"Dashed line: uniform choice ({base:.1f}%)", transform=ax.transAxes, fontsize=10, color="#747d8b")
        ax.set_axisbelow(True)
        ax.grid(axis="x", alpha=.15)
        ax.invert_yaxis()
    save(fig, "tb4-selection", "Pair and Five selection rates; different source coverage and chance baselines, not a causal context ladder.")

    fig, axes = plt.subplots(2, 2, figsize=(10, 7.5), layout="constrained", sharex=True, sharey=True)
    for ax, s, item, color in zip(axes.flat, sources, data["sources"], COLORS):
        ys = np.array(s["pass_at_k"]) * 100
        fallback = sum(s["unreviewed_mixed_pools"].values()) / 5
        mid = (s["all_pass_pools"] + s["reviewer_mixed_successes"]["gpt-5-6-sol"] + fallback) / s["tasks"] * 100
        lo, hi = s["missing_pool_lower_bound"] * 100, s["missing_pool_upper_bound"] * 100
        ax.plot(range(1, 6), ys, "o-", color=color, linewidth=2, label="Oracle pass@k")
        ax.errorbar(5, mid, yerr=[[mid-lo], [hi-mid]], fmt="*", color="#20242d", markersize=14, capsize=5, label="GPT-5.6 Sol selector at k=5")
        ax.annotate(f"{mid:.1f}% selected", (5, mid), xytext=(-12, -19), textcoords="offset points", ha="right", fontsize=10, weight="bold")
        ax.annotate(f"{ys[-1]:.1f}% oracle", (5, ys[-1]), xytext=(-10, 10), textcoords="offset points", ha="right", fontsize=10, color=color)
        ax.set(title=SOURCES[s["source"]], xticks=range(1, 6), xlim=(.7, 5.5), ylim=(30, 87), yticks=[30, 40, 50, 60, 70, 80])
        ax.grid(alpha=.18)
    for ax in axes[:, 0]:
        ax.set_ylabel("Whole-job success (%)")
    for ax in axes[1]:
        ax.set_xlabel("Number of frozen attempts (k)")
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="outside lower center", ncol=2, frameon=False)
    save(fig, "tb4-pass-at-k", "All 66 tasks per source. Stars use the same GPT-5.6 Sol reviewer. Error bars bound excluded mixed pools, not statistical uncertainty.")

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
    print(f"Generated TB4 data and four figures from {COMMIT}; {total_pools} pools, baseline {baseline:.6f}.")


if __name__ == "__main__":
    main()
