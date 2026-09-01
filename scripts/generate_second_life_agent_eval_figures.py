#!/usr/bin/env python3
"""Generate SVG result figures for "The Second Life of Agent Evals."""

from __future__ import annotations

import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "assets" / "img" / "2026-08-28-second-life-agent-evals"

INK = "#20242D"
BODY = "#434A57"
MUTED = "#747D8B"
LINE = "#DFE4E9"
BLUE = "#4F68B3"
GREEN = "#287A68"
GREEN_SOFT = "#EAF7F2"
WARM = "#A75E3C"
PURPLE = "#7656A6"
WARM_SOFT = "#FFF1E9"
NEUTRAL_SOFT = "#F6F8FA"

FONT = "-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"


def text(
    x: float,
    y: float,
    value: str,
    *,
    size: int = 16,
    color: str = BODY,
    weight: int = 400,
    anchor: str = "middle",
    transform: str | None = None,
) -> str:
    attrs = f' transform="{transform}"' if transform else ""
    return (
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" '
        f'font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
        f'fill="{color}"{attrs}>{value}</text>'
    )


def rect(
    x: float,
    y: float,
    width: float,
    height: float,
    *,
    fill: str,
    stroke: str = "none",
    stroke_width: float = 0,
    radius: float = 0,
) -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="{radius}" fill="{fill}" stroke="{stroke}" '
        f'stroke-width="{stroke_width}"/>'
    )


def svg_document(width: int, height: int, description: str, body: list[str]) -> str:
    return "\n".join(
        [
            '<?xml version="1.0" encoding="UTF-8"?>',
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" role="img">',
            f"<title>{description}</title>",
            rect(0, 0, width, height, fill="white"),
            *body,
            "</svg>",
            "",
        ]
    )


def write_svg(stem: str, width: int, height: int, description: str, body: list[str]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / f"{stem}.svg").write_text(
        svg_document(width, height, description, body), encoding="utf-8"
    )


def render_single_confusion_matrices() -> None:
    # Rows: environment success/failure. Columns: reviewer pass/fail.
    reviewers = (
        ("GPT-5.6 Sol", "", ((69, 16), (48, 37))),
        ("GLM-5.3", "", ((83, 2), (65, 20))),
        ("DeepSeek V4 Pro", "0813 GA", ((70, 15), (60, 25))),
        ("DeepSeek V4 Flash", "0731", ((73, 12), (60, 25))),
    )
    width, height = 1440, 540
    cell_width, cell_height = 120, 108
    panel_starts = (160, 475, 790, 1105)
    grid_top = 230
    body = [
        text(
            width / 2,
            42,
            "Single-trace verification: verdicts vs. environment outcomes",
            size=22,
            color=INK,
            weight=700,
        ),
        text(
            width / 2,
            72,
            "85 successful and 85 failed traces per reviewer · false approvals are highlighted in orange",
            size=13,
            color=MUTED,
        ),
    ]

    for panel_index, ((reviewer, reviewer_detail, matrix), x_start) in enumerate(
        zip(reviewers, panel_starts)
    ):
        accuracy = 100.0 * (matrix[0][0] + matrix[1][1]) / 170
        body.extend(
            [
                text(x_start + cell_width, 112, reviewer, size=16, color=INK, weight=700),
                text(
                    x_start + cell_width,
                    134,
                    reviewer_detail,
                    size=12,
                    color=MUTED,
                    weight=600,
                ),
                text(
                    x_start + cell_width,
                    160,
                    f"{accuracy:.1f}% accuracy",
                    size=13,
                    color=MUTED,
                    weight=600,
                ),
                text(x_start + cell_width / 2, 207, "Says pass", size=13, color=BODY, weight=600),
                text(
                    x_start + 1.5 * cell_width,
                    207,
                    "Says fail",
                    size=13,
                    color=BODY,
                    weight=600,
                ),
            ]
        )

        if panel_index == 0:
            body.extend(
                [
                    text(
                        x_start - 18,
                        grid_top + cell_height / 2 + 5,
                        "Actually passed",
                        size=13,
                        color=BODY,
                        weight=600,
                        anchor="end",
                    ),
                    text(
                        x_start - 18,
                        grid_top + 1.5 * cell_height + 5,
                        "Actually failed",
                        size=13,
                        color=BODY,
                        weight=600,
                        anchor="end",
                    ),
                ]
            )

        for row in range(2):
            for column in range(2):
                value = matrix[row][column]
                correct = row == column
                false_approval = row == 1 and column == 0
                fill = GREEN_SOFT if correct else WARM_SOFT if false_approval else NEUTRAL_SOFT
                stroke = GREEN if correct else WARM if false_approval else LINE
                x = x_start + column * cell_width
                y = grid_top + row * cell_height
                row_percent = 100.0 * value / sum(matrix[row])
                body.extend(
                    [
                        rect(
                            x,
                            y,
                            cell_width,
                            cell_height,
                            fill=fill,
                            stroke=stroke,
                            stroke_width=1.6,
                            radius=5,
                        ),
                        text(
                            x + cell_width / 2,
                            y + 51,
                            str(value),
                            size=27,
                            color=INK,
                            weight=700,
                        ),
                        text(
                            x + cell_width / 2,
                            y + 78,
                            f"{row_percent:.1f}% of row",
                            size=12,
                            color=MUTED,
                        ),
                    ]
                )

    body.extend(
        [
            rect(565, 500, 13, 13, fill=GREEN_SOFT, stroke=GREEN, stroke_width=1),
            text(586, 511, "correct verdict", size=12, color=MUTED, anchor="start"),
            rect(740, 500, 13, 13, fill=WARM_SOFT, stroke=WARM, stroke_width=1),
            text(761, 511, "failed trace approved", size=12, color=MUTED, anchor="start"),
        ]
    )
    write_svg(
        "single-trace-confusion-matrices",
        width,
        height,
        "Four confusion matrices for single-trace agentic verification",
        body,
    )


def render_single_failure_recall_by_source() -> None:
    reviewers = (
        ("GPT-5.6 Sol", BLUE),
        ("GLM-5.3", GREEN),
        ("DeepSeek V4 Pro 0813", WARM),
        ("DeepSeek V4 Flash 0731", PURPLE),
    )
    source_slices = (
        ("Fable +", "Claude Code · n = 33", (60.61, 27.27, 30.30, 33.33)),
        ("GPT-5.6 Sol +", "Codex · n = 29", (20.69, 10.34, 17.24, 10.34)),
        ("GLM-5.3 +", "Claude Code · n = 23", (47.83, 34.78, 43.48, 47.83)),
    )
    width, height = 1200, 545
    plot_left, plot_right = 85, 1160
    plot_top, plot_bottom = 190, 450
    plot_height = plot_bottom - plot_top
    y_max = 70.0

    def y_position(value: float) -> float:
        return plot_bottom - value / y_max * plot_height

    body = [
        text(
            width / 2,
            42,
            "Single-trace failure recall by source evaluation",
            size=22,
            color=INK,
            weight=700,
        ),
        text(
            width / 2,
            72,
            "Failed GPT-5.6 Sol + Codex traces were hardest to reject",
            size=13,
            color=MUTED,
        ),
    ]

    legend_x = (150, 375, 575, 865)
    for (reviewer, color), x in zip(reviewers, legend_x):
        body.extend(
            [
                rect(x, 112, 14, 14, fill=color, radius=2),
                text(x + 22, 124, reviewer, size=12, color=BODY, anchor="start"),
            ]
        )

    for tick in (0, 20, 40, 60):
        y = y_position(tick)
        body.extend(
            [
                f'<line x1="{plot_left}" y1="{y}" x2="{plot_right}" y2="{y}" '
                f'stroke="{LINE}" stroke-width="1"/>',
                text(plot_left - 12, y + 5, str(tick), size=12, color=MUTED, anchor="end"),
            ]
        )

    body.extend(
        [
            f'<line x1="{plot_left}" y1="{plot_top}" x2="{plot_left}" y2="{plot_bottom}" '
            f'stroke="{LINE}" stroke-width="1.3"/>',
            f'<line x1="{plot_left}" y1="{plot_bottom}" x2="{plot_right}" y2="{plot_bottom}" '
            f'stroke="{LINE}" stroke-width="1.3"/>',
            text(
                28,
                (plot_top + plot_bottom) / 2,
                "Failed traces correctly rejected (%)",
                size=13,
                color=BODY,
                transform=f"rotate(-90 28 {(plot_top + plot_bottom) / 2})",
            ),
        ]
    )

    group_centers = (250, 600, 950)
    bar_width = 44
    offsets = (-75, -25, 25, 75)
    for (source, source_detail, values), center in zip(source_slices, group_centers):
        for value, offset, (_, color) in zip(values, offsets, reviewers):
            x = center + offset - bar_width / 2
            y = y_position(value)
            body.extend(
                [
                    rect(x, y, bar_width, plot_bottom - y, fill=color, radius=3),
                    text(
                        x + bar_width / 2,
                        y - 8,
                        f"{value:.1f}",
                        size=11,
                        color=BODY,
                        weight=650,
                    ),
                ]
            )
        body.extend(
            [
                text(center, 495, source, size=13, color=INK, weight=650),
                text(center, 518, source_detail, size=12, color=MUTED),
            ]
        )

    write_svg(
        "single-failure-recall-by-source",
        width,
        height,
        "Grouped bars comparing single-trace failure recall by source evaluation",
        body,
    )


def render_pair_comparison() -> None:
    reviewers = (
        ("GPT-5.6 Sol", 64.71, BLUE),
        ("GLM-5.3", 69.41, GREEN),
        ("DeepSeek V4 Pro", 55.29, WARM),
        ("DeepSeek V4 Flash", 52.94, PURPLE),
    )
    width, height = 1200, 540
    plot_left, plot_right = 110, 1155
    plot_top, plot_bottom = 145, 430
    plot_height = plot_bottom - plot_top
    y_max = 75.0

    def y_position(value: float) -> float:
        return plot_bottom - value / y_max * plot_height

    body = [
        text(
            width / 2,
            42,
            "Pairwise trace ranking",
            size=22,
            color=INK,
            weight=700,
        ),
        text(
            width / 2,
            73,
            "One successful and one failed run per task · labels hidden",
            size=13,
            color=MUTED,
        ),
    ]

    for tick in (0, 25, 50, 75):
        y = y_position(tick)
        body.extend(
            [
                f'<line x1="{plot_left}" y1="{y}" x2="{plot_right}" y2="{y}" '
                f'stroke="{LINE}" stroke-width="1"/>',
                text(plot_left - 14, y + 5, str(tick), size=13, color=MUTED, anchor="end"),
            ]
        )

    body.extend(
        [
            f'<line x1="{plot_left}" y1="{plot_top}" x2="{plot_left}" y2="{plot_bottom}" '
            f'stroke="{LINE}" stroke-width="1.3"/>',
            f'<line x1="{plot_left}" y1="{plot_bottom}" x2="{plot_right}" y2="{plot_bottom}" '
            f'stroke="{LINE}" stroke-width="1.3"/>',
            text(
                32,
                (plot_top + plot_bottom) / 2,
                "Successful trace selected (%)",
                size=14,
                color=BODY,
                transform=f"rotate(-90 32 {(plot_top + plot_bottom) / 2})",
            ),
        ]
    )

    baseline_y = y_position(50.0)
    body.extend(
        [
            f'<line x1="{plot_left}" y1="{baseline_y}" x2="{plot_right}" y2="{baseline_y}" '
            f'stroke="{MUTED}" stroke-width="1.8" stroke-dasharray="8 7"/>',
            text(plot_right - 5, baseline_y - 10, "50% blind selection", size=12, color=MUTED, anchor="end"),
        ]
    )

    centers = (240, 490, 740, 990)
    bar_width = 116
    for (label, selected, color), center in zip(reviewers, centers):
        y = y_position(selected)
        body.extend(
            [
                rect(center - bar_width / 2, y, bar_width, plot_bottom - y, fill=color, radius=3),
                text(center, y - 11, f"{selected:.1f}%", size=14, color=BODY, weight=700),
            ]
        )
        if label.startswith("DeepSeek"):
            release = "0813" if "Pro" in label else "0731"
            body.extend(
                [
                    text(center, 467, label, size=14, color=INK, weight=650),
                    text(center, 490, release, size=12, color=MUTED),
                ]
            )
        else:
            body.append(text(center, 474, label, size=14, color=INK, weight=650))

    write_svg(
        "pair-comparison",
        width,
        height,
        "Bar chart of pairwise successful-trace selection",
        body,
    )


TOTAL_TASKS = 74
N_TRIALS = 5

SOURCES = (
    (
        ("Fable +", "Claude Code"),
        {"histogram": {0: 29, 1: 14, 2: 10, 3: 4, 4: 5, 5: 12}, "all_pass": 12,
         "selectors": {"DeepSeek V4 Flash 0731": 20, "GLM-5.3": 22, "GPT-5.6 Sol": 23}},
    ),
    (
        ("GPT-5.6 Sol +", "Codex"),
        {"histogram": {0: 32, 1: 13, 2: 4, 3: 6, 4: 6, 5: 13}, "all_pass": 13,
         "selectors": {"DeepSeek V4 Flash 0731": 12, "GLM-5.3": 11, "GPT-5.6 Sol": 15}},
    ),
    (
        ("GLM-5.3 +", "Claude Code"),
        {"histogram": {0: 37, 1: 8, 2: 6, 3: 6, 4: 3, 5: 14}, "all_pass": 14,
         "selectors": {"DeepSeek V4 Flash 0731": 12, "GLM-5.3": 14, "GPT-5.6 Sol": 16}},
    ),
)

SERIES = (
    ("pass1", "pass@1 (uniform)", "#B9BFC7"),
    ("DeepSeek V4 Flash 0731", "DeepSeek V4 Flash 0731", WARM),
    ("GLM-5.3", "GLM-5.3", GREEN),
    ("GPT-5.6 Sol", "GPT-5.6 Sol", BLUE),
    ("pass5", "pass@5 (oracle)", INK),
)


def pass_at_k(histogram: dict[int, int]) -> list[float]:
    values = []
    for k in range(1, N_TRIALS + 1):
        solved = 0.0
        for positive_count, tasks in histogram.items():
            fail_probability = (
                math.comb(N_TRIALS - positive_count, k) / math.comb(N_TRIALS, k)
                if N_TRIALS - positive_count >= k
                else 0.0
            )
            solved += tasks * (1.0 - fail_probability)
        values.append(100.0 * solved / TOTAL_TASKS)
    return values


def render_pass_at_k_curves() -> None:
    series = (
        ("Fable + Claude Code", WARM, SOURCES[0][1]),
        ("GPT-5.6 Sol + Codex", BLUE, SOURCES[1][1]),
        ("GLM-5.3 + Claude Code", GREEN, SOURCES[2][1]),
    )
    width, height = 1200, 540
    plot_left, plot_right = 105, 1015
    plot_top, plot_bottom = 155, 440
    plot_width = plot_right - plot_left
    plot_height = plot_bottom - plot_top
    y_min, y_max = 20.0, 65.0

    def x_position(k: int) -> float:
        return plot_left + (k - 1) / (N_TRIALS - 1) * plot_width

    def y_position(value: float) -> float:
        return plot_bottom - (value - y_min) / (y_max - y_min) * plot_height

    body = [
        text(
            width / 2,
            42,
            "Terminal-Bench 3.0 pass@k across three agent evaluations",
            size=25,
            color=INK,
            weight=700,
        ),
        text(
            width / 2,
            72,
            "Estimated from five frozen runs per task",
            size=15,
            color=MUTED,
        ),
    ]

    legend_x = (235, 500, 785)
    for (label, color, _), x in zip(series, legend_x):
        body.extend(
            [
                f'<line x1="{x}" y1="116" x2="{x + 30}" y2="116" '
                f'stroke="{color}" stroke-width="3"/>',
                f'<circle cx="{x + 15}" cy="116" r="4" fill="{color}"/>',
                text(x + 40, 121, label, size=14, color=BODY, anchor="start"),
            ]
        )

    for tick in (20, 30, 40, 50, 60):
        y = y_position(tick)
        body.extend(
            [
                f'<line x1="{plot_left}" y1="{y}" x2="{plot_right}" y2="{y}" '
                f'stroke="{LINE}" stroke-width="1"/>',
                text(plot_left - 12, y + 5, str(tick), size=14, color=MUTED, anchor="end"),
            ]
        )

    body.extend(
        [
            f'<line x1="{plot_left}" y1="{plot_top}" x2="{plot_left}" y2="{plot_bottom}" '
            f'stroke="{LINE}" stroke-width="1.3"/>',
            f'<line x1="{plot_left}" y1="{plot_bottom}" x2="{plot_right}" y2="{plot_bottom}" '
            f'stroke="{LINE}" stroke-width="1.3"/>',
            text(
                28,
                (plot_top + plot_bottom) / 2,
                "Tasks solved (%)",
                size=15,
                color=BODY,
                transform=f"rotate(-90 28 {(plot_top + plot_bottom) / 2})",
            ),
        ]
    )

    for k in range(1, N_TRIALS + 1):
        x = x_position(k)
        body.extend(
            [
                f'<line x1="{x}" y1="{plot_bottom}" x2="{x}" y2="{plot_bottom + 6}" '
                f'stroke="{LINE}" stroke-width="1.2"/>',
                text(x, plot_bottom + 29, f"pass@{k}", size=14, color=BODY, weight=650),
            ]
        )

    for label, color, spec in series:
        values = pass_at_k(spec["histogram"])
        points = " ".join(
            f"{x_position(k):.2f},{y_position(value):.2f}"
            for k, value in enumerate(values, start=1)
        )
        body.append(
            f'<polyline points="{points}" fill="none" stroke="{color}" '
            f'stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
        )
        for k, value in enumerate(values, start=1):
            body.append(
                f'<circle cx="{x_position(k)}" cy="{y_position(value)}" r="5" '
                f'fill="white" stroke="{color}" stroke-width="3"/>'
            )
        body.append(
            text(
                plot_right + 18,
                y_position(values[-1]) + 5,
                f"{values[-1]:.1f}%",
                size=14,
                color=color,
                weight=700,
                anchor="start",
            )
        )

    write_svg(
        "terminal-bench-3-0-pass-at-k",
        width,
        height,
        "Pass at k curves for three Terminal-Bench 3.0 source evaluations",
        body,
    )


def source_values(spec: dict) -> dict[str, float]:
    curve = pass_at_k(spec["histogram"])
    values = {"pass1": curve[0], "pass5": curve[-1]}
    values.update(
        {
            reviewer: 100.0 * (spec["all_pass"] + selected_mixed) / TOTAL_TASKS
            for reviewer, selected_mixed in spec["selectors"].items()
        }
    )
    return values


def render_best_of_five_grouped_bars() -> None:
    width, height = 1200, 700
    plot_left, plot_right = 105, 1165
    plot_top, plot_bottom = 175, 565
    plot_height = plot_bottom - plot_top
    group_centers = (285, 635, 985)
    bar_width = 34
    offsets = (-88, -44, 0, 44, 88)
    y_max = 66.0
    source_data = [(labels, source_values(spec)) for labels, spec in SOURCES]

    def y_position(value: float) -> float:
        return plot_bottom - value / y_max * plot_height

    body = [
        text(
            width / 2,
            42,
            "Terminal-Bench 3.0: Best-of-5 trace selection",
            size=22,
            color=INK,
            weight=700,
        ),
        text(
            width / 2,
            72,
            "Agentic reviewers choose one of five frozen runs without seeing environment rewards",
            size=13,
            color=MUTED,
        ),
    ]

    legend_widths = (155, 225, 115, 145, 150)
    legend_total = sum(legend_widths)
    legend_x = (width - legend_total) / 2
    for (_, label, color), item_width in zip(SERIES, legend_widths):
        body.extend(
            [
                rect(legend_x, 105, 14, 14, fill=color, radius=2),
                text(legend_x + 21, 117, label, size=11, color=BODY, anchor="start"),
            ]
        )
        legend_x += item_width

    for tick in range(0, 61, 10):
        y = y_position(tick)
        body.extend(
            [
                f'<line x1="{plot_left}" y1="{y}" x2="{plot_right}" y2="{y}" '
                f'stroke="{LINE}" stroke-width="1"/>',
                text(plot_left - 12, y + 5, str(tick), size=12, color=MUTED, anchor="end"),
            ]
        )

    body.extend(
        [
            f'<line x1="{plot_left}" y1="{plot_top}" x2="{plot_left}" y2="{plot_bottom}" '
            f'stroke="{LINE}" stroke-width="1.3"/>',
            f'<line x1="{plot_left}" y1="{plot_bottom}" x2="{plot_right}" y2="{plot_bottom}" '
            f'stroke="{LINE}" stroke-width="1.3"/>',
            text(
                27,
                (plot_top + plot_bottom) / 2,
                "Selected positive-reward rate (%)",
                size=13,
                color=BODY,
                transform=f"rotate(-90 27 {(plot_top + plot_bottom) / 2})",
            ),
        ]
    )

    for (labels, values), group_center in zip(source_data, group_centers):
        for (key, _, color), offset in zip(SERIES, offsets):
            value = values[key]
            x = group_center + offset - bar_width / 2
            y = y_position(value)
            body.extend(
                [
                    rect(x, y, bar_width, plot_bottom - y, fill=color, radius=2),
                    text(x + bar_width / 2, y - 8, f"{value:.1f}", size=11, color=BODY, weight=600),
                ]
            )
        body.extend(
            [
                text(group_center, 603, labels[0], size=14, color=INK, weight=650),
                text(group_center, 625, labels[1], size=13, color=MUTED, weight=500),
            ]
        )

    body.append(
        text(width / 2, 671, "Trace pool (solver model + agent)", size=13, color=BODY)
    )
    write_svg(
        "terminal-bench-3-0-best-of-five-selection",
        width,
        height,
        "Grouped bars comparing pass at one, three agentic selectors, and oracle pass at five",
        body,
    )


def main() -> None:
    render_pass_at_k_curves()
    render_single_confusion_matrices()
    render_single_failure_recall_by_source()
    render_pair_comparison()
    render_best_of_five_grouped_bars()


if __name__ == "__main__":
    main()
