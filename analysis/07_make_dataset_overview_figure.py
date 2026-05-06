from __future__ import annotations

import os
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MPLCONFIG = PROJECT_ROOT / ".cache" / "matplotlib"
MPLCONFIG.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MPLCONFIG))

import matplotlib.pyplot as plt
import seaborn as sns


DATA = PROJECT_ROOT / "data"
TABLES = PROJECT_ROOT / "tables"
FIGURES = PROJECT_ROOT / "figures" / "generated"
FIGURES.mkdir(parents=True, exist_ok=True)


def main() -> None:
    inventory = pd.read_csv(DATA / "dataset_inventory_review.csv")
    inspection = pd.read_csv(TABLES / "dataset_file_inspection.csv")

    context_counts = (
        inventory.assign(disease_context=inventory["disease_context"].str.replace("/", " / "))
        .groupby(["year", "disease_context"], as_index=False)
        .size()
    )
    file_counts = inspection.groupby("kind", as_index=False).size()

    sns.set_theme(style="whitegrid", context="paper")
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.6), gridspec_kw={"width_ratios": [1.15, 0.85]})

    sns.scatterplot(
        data=context_counts,
        x="year",
        y="disease_context",
        size="size",
        sizes=(140, 420),
        hue="disease_context",
        legend=False,
        ax=axes[0],
    )
    axes[0].set_title("Candidate human cardiac datasets")
    axes[0].set_xlabel("Publication year")
    axes[0].set_ylabel("")
    axes[0].set_xticks(sorted(inventory["year"].dropna().astype(int).unique()))
    axes[0].grid(axis="y", linestyle=":", alpha=0.5)

    sns.barplot(data=file_counts, x="kind", y="size", color="#4C78A8", ax=axes[1])
    axes[1].set_title("Downloaded file types inspected")
    axes[1].set_xlabel("")
    axes[1].set_ylabel("Number of files/archives")
    axes[1].tick_params(axis="x", rotation=25)
    for container in axes[1].containers:
        axes[1].bar_label(container, padding=3, fontsize=9)

    fig.suptitle("Reanalysis dataset register and local data audit", y=1.02)
    fig.tight_layout()

    out_png = FIGURES / "dataset_overview.png"
    out_pdf = FIGURES / "dataset_overview.pdf"
    fig.savefig(out_png, dpi=300, bbox_inches="tight")
    fig.savefig(out_pdf, bbox_inches="tight")
    print(f"Wrote {out_png}")
    print(f"Wrote {out_pdf}")


if __name__ == "__main__":
    main()
