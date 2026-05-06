from __future__ import annotations

import os
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TABLES = PROJECT_ROOT / "tables"
FIGURES = PROJECT_ROOT / "figures" / "generated"
FIGURES.mkdir(parents=True, exist_ok=True)

MPLCONFIG = PROJECT_ROOT / ".cache" / "matplotlib"
MPLCONFIG.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MPLCONFIG))

import matplotlib.pyplot as plt
import seaborn as sns

ZONE_ORDER = ["Control", "Remote zone", "Fibrotic zone", "Infarct zone"]
CELLTYPE_ORDER = [
    "Cardiomyocyte",
    "Fibroblast",
    "Endothelial",
    "Myeloid",
    "Lymphoid",
    "Mast",
    "Pericyte",
    "vSMCs",
    "Adipocyte",
    "Cycling.cells",
    "Neuronal",
]


def main() -> None:
    summary = pd.read_csv(TABLES / "kuppe_visium_celltype_summary.csv")
    summary["zone_label"] = pd.Categorical(summary["zone_label"], ZONE_ORDER, ordered=True)
    summary["cell_type"] = pd.Categorical(summary["cell_type"], CELLTYPE_ORDER, ordered=True)
    summary = summary.sort_values(["zone_label", "cell_type"])

    sns.set_theme(style="whitegrid", context="paper")
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), gridspec_kw={"width_ratios": [1.1, 1]})

    stacked = summary.pivot(
        index="zone_label", columns="cell_type", values="dominant_fraction"
    ).fillna(0.0)
    stacked = stacked[CELLTYPE_ORDER]
    colors = sns.color_palette("tab20", n_colors=len(stacked.columns))
    bottom = pd.Series(0.0, index=stacked.index)
    for color, cell_type in zip(colors, stacked.columns):
        axes[0].bar(
            stacked.index.astype(str),
            stacked[cell_type],
            bottom=bottom,
            label=cell_type,
            color=color,
            width=0.75,
        )
        bottom += stacked[cell_type]

    axes[0].set_ylabel("Dominant spot fraction")
    axes[0].set_xlabel("")
    axes[0].set_ylim(0, 1)
    axes[0].tick_params(axis="x", rotation=25)
    axes[0].set_title("Dominant deconvolved cell type")

    heatmap = summary.pivot(index="cell_type", columns="zone_label", values="mean_score").fillna(0.0)
    heatmap = heatmap.loc[CELLTYPE_ORDER, ZONE_ORDER]
    sns.heatmap(
        heatmap,
        ax=axes[1],
        cmap="viridis",
        linewidths=0.3,
        linecolor="white",
        cbar_kws={"label": "Mean score"},
    )
    axes[1].set_xlabel("")
    axes[1].set_ylabel("")
    axes[1].set_title("Mean cell-type score")

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(
        handles,
        labels,
        loc="lower center",
        ncol=6,
        frameon=False,
        bbox_to_anchor=(0.5, -0.03),
    )
    fig.suptitle("Human myocardial infarction Visium cell-type composition", y=1.02)
    fig.tight_layout(rect=[0, 0.08, 1, 1])

    out_png = FIGURES / "kuppe_visium_celltype_overview.png"
    out_pdf = FIGURES / "kuppe_visium_celltype_overview.pdf"
    fig.savefig(out_png, dpi=300, bbox_inches="tight")
    fig.savefig(out_pdf, bbox_inches="tight")
    print(f"Wrote {out_png}")
    print(f"Wrote {out_pdf}")


if __name__ == "__main__":
    main()
