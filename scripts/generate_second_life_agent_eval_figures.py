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
        ("GPT-5.6 Sol", ((69, 16), (48, 37))),
        ("GLM-5.3", ((83, 2), (65, 20))),
        ("DeepSeek V4 Pro 0423 preview", ((74, 11), (63, 22))),
    )
    width, height = 1200, 520
    cell_width, cell_height = 132, 112
    panel_starts = (190, 535, 880)
    grid_top = 220
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

    for panel_index, ((reviewer, matrix), x_start) in enumerate(
        zip(reviewers, panel_starts)
    ):
        accuracy = 100.0 * (matrix[0][0] + matrix[1][1]) / 170
        body.extend(
            [
                text(x_start + cell_width, 120, reviewer, size=17, color=INK, weight=700),
                text(
                    x_start + cell_width,
                    145,
                    f"{accuracy:.1f}% accuracy",
                    size=13,
                    color=MUTED,
                    weight=600,
                ),
                text(x_start + cell_width / 2, 195, "Says pass", size=13, color=BODY, weight=600),
                text(
                    x_start + 1.5 * cell_width,
                    195,
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
            rect(445, 476, 13, 13, fill=GREEN_SOFT, stroke=GREEN, stroke_width=1),
            text(466, 487, "correct verdict", size=12, color=MUTED, anchor="start"),
            rect(620, 476, 13, 13, fill=WARM_SOFT, stroke=WARM, stroke_width=1),
            text(641, 487, "failed trace approved", size=12, color=MUTED, anchor="start"),
        ]
    )
    write_svg(
        "single-trace-confusion-matrices",
        width,
        height,
        "Three confusion matrices for single-trace agentic verification",
        body,
    )


def render_pair_comparison() -> None:
    reviewers = (
        ("GPT-5.6 Sol", 43.53, 60.00, 64.71, BLUE),
        ("GLM-5.3", 23.53, 38.82, 69.41, GREEN),
        ("DeepSeek V4 Pro 0423", 25.88, 42.35, 60.00, WARM),
    )
    width, height = 1200, 590
    plot_top, plot_bottom = 175, 470
    plot_height = plot_bottom - plot_top
    y_max = 75.0
    left_x = (85, 660)
    right_x = (755, 1160)

    def y_position(value: float) -> float:
        return plot_bottom - value / y_max * plot_height

    body = [
        text(
            width / 2,
            42,
            "Comparison reveals a stronger verification signal",
            size=22,
            color=INK,
            weight=700,
        ),
        text(
            width / 2,
            72,
            "Pair reviews the same successful and failed anchors together, with neither label revealed",
            size=13,
            color=MUTED,
        ),
        text(372, 116, "Failure detection", size=17, color=INK, weight=700),
        text(958, 116, "Relative ranking", size=17, color=INK, weight=700),
        text(958, 146, "Dashed line = 50% blind selection", size=12, color=MUTED),
        rect(250, 137, 14, 14, fill="#B9BFC7", radius=2),
        text(272, 149, "Single", size=12, color=BODY, anchor="start"),
        rect(358, 137, 14, 14, fill=BLUE, radius=2),
        text(380, 149, "Pair (colored by reviewer)", size=12, color=BODY, anchor="start"),
    ]

    for panel_left, panel_right in (left_x, right_x):
        for tick in (0, 20, 40, 60):
            y = y_position(tick)
            body.extend(
                [
                    f'<line x1="{panel_left}" y1="{y}" x2="{panel_right}" y2="{y}" '
                    f'stroke="{LINE}" stroke-width="1"/>',
                    text(panel_left - 11, y + 5, str(tick), size=12, color=MUTED, anchor="end"),
                ]
            )
        body.extend(
            [
                f'<line x1="{panel_left}" y1="{plot_top}" x2="{panel_left}" y2="{plot_bottom}" '
                f'stroke="{LINE}" stroke-width="1.3"/>',
                f'<line x1="{panel_left}" y1="{plot_bottom}" x2="{panel_right}" y2="{plot_bottom}" '
                f'stroke="{LINE}" stroke-width="1.3"/>',
            ]
        )

    body.extend(
        [
            text(
                26,
                (plot_top + plot_bottom) / 2,
                "Failure recall (%)",
                size=13,
                color=BODY,
                transform=f"rotate(-90 26 {(plot_top + plot_bottom) / 2})",
            ),
            text(
                704,
                (plot_top + plot_bottom) / 2,
                "Selected success (%)",
                size=13,
                color=BODY,
                transform=f"rotate(-90 704 {(plot_top + plot_bottom) / 2})",
            ),
        ]
    )

    left_centers = (190, 372, 554)
    bar_width = 48
    for (label, single, pair, _, color), center in zip(reviewers, left_centers):
        for value, x, bar_color in (
            (single, center - 53, "#B9BFC7"),
            (pair, center + 5, color),
        ):
            y = y_position(value)
            body.extend(
                [
                    rect(x, y, bar_width, plot_bottom - y, fill=bar_color, radius=3),
                    text(x + bar_width / 2, y - 9, f"{value:.1f}", size=12, color=BODY, weight=650),
                ]
            )
        if label.startswith("DeepSeek"):
            body.extend(
                [
                    text(center, 510, "DeepSeek V4 Pro", size=13, color=INK, weight=650),
                    text(center, 531, "0423 preview", size=12, color=MUTED),
                ]
            )
        else:
            body.append(text(center, 516, label, size=13, color=INK, weight=650))

    baseline_y = y_position(50.0)
    body.extend(
        [
            f'<line x1="{right_x[0]}" y1="{baseline_y}" x2="{right_x[1]}" y2="{baseline_y}" '
            f'stroke="{MUTED}" stroke-width="1.5" stroke-dasharray="7 6"/>',
        ]
    )
    right_centers = (825, 957, 1089)
    for (label, _, _, selected, color), center in zip(reviewers, right_centers):
        bar_width = 64
        y = y_position(selected)
        body.extend(
            [
                rect(center - bar_width / 2, y, bar_width, plot_bottom - y, fill=color, radius=3),
                text(center, y - 9, f"{selected:.1f}", size=12, color=BODY, weight=650),
            ]
        )
        short_label = "DeepSeek" if label.startswith("DeepSeek") else label
        body.append(text(center, 516, short_label, size=13, color=INK, weight=650))

    body.extend(
        [
            text(372, 566, "Same 85 failures reviewed in isolation or with a contrasting trace", size=12, color=MUTED),
            text(958, 566, "Successful trace selected from each balanced Pair", size=12, color=MUTED),
        ]
    )
    write_svg(
        "pair-comparison",
        width,
        height,
        "Paired bar charts for failure recall and pairwise trace selection",
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
    render_single_confusion_matrices()
    render_pair_comparison()
    render_best_of_five_grouped_bars()


if __name__ == "__main__":
    main()
