from __future__ import annotations

from pathlib import Path

import anndata as ad
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW = PROJECT_ROOT / "data" / "raw" / "kuppe_mi_visium"
TABLES = PROJECT_ROOT / "tables"
TABLES.mkdir(exist_ok=True)

CELLTYPE_COLUMNS = [
    "Adipocyte",
    "Cardiomyocyte",
    "Endothelial",
    "Fibroblast",
    "Lymphoid",
    "Mast",
    "Myeloid",
    "Neuronal",
    "Pericyte",
    "Cycling.cells",
    "vSMCs",
]

ZONE_BY_FILE = {
    "Visium_control_P1.h5ad": ("control", "Control"),
    "Visium_FZ_P14.h5ad": ("FZ", "Fibrotic zone"),
    "Visium_IZ_P10.h5ad": ("IZ", "Infarct zone"),
    "Visium_RZ_P11.h5ad": ("RZ", "Remote zone"),
}


def main() -> None:
    summary_rows: list[dict[str, object]] = []
    spot_rows: list[pd.DataFrame] = []

    for path in sorted(RAW.glob("*.h5ad")):
        zone_code, zone_label = ZONE_BY_FILE.get(path.name, (path.stem, path.stem))
        dataset = ad.read_h5ad(path, backed="r")
        try:
            obs = dataset.obs.copy()
        finally:
            dataset.file.close()

        available = [col for col in CELLTYPE_COLUMNS if col in obs.columns]
        missing = sorted(set(CELLTYPE_COLUMNS) - set(available))
        if missing:
            print(f"{path.name}: missing expected columns: {', '.join(missing)}")

        scores = obs[available].apply(pd.to_numeric, errors="coerce").fillna(0.0)
        dominant = scores.idxmax(axis=1)
        max_score = scores.max(axis=1)

        for cell_type in available:
            summary_rows.append(
                {
                    "file": path.name,
                    "zone_code": zone_code,
                    "zone_label": zone_label,
                    "cell_type": cell_type,
                    "n_spots": len(obs),
                    "mean_score": scores[cell_type].mean(),
                    "total_score": scores[cell_type].sum(),
                    "dominant_spots": int((dominant == cell_type).sum()),
                    "dominant_fraction": float((dominant == cell_type).mean()),
                }
            )

        spot_rows.append(
            pd.DataFrame(
                {
                    "file": path.name,
                    "zone_code": zone_code,
                    "zone_label": zone_label,
                    "spot_id": obs.index.astype(str),
                    "dominant_cell_type": dominant.astype(str).to_numpy(),
                    "dominant_score": max_score.to_numpy(),
                    "n_counts": pd.to_numeric(obs.get("n_counts"), errors="coerce"),
                    "n_genes": pd.to_numeric(obs.get("n_genes"), errors="coerce"),
                    "percent_mt": pd.to_numeric(obs.get("percent.mt"), errors="coerce"),
                }
            )
        )

    summary = pd.DataFrame(summary_rows)
    summary_out = TABLES / "kuppe_visium_celltype_summary.csv"
    summary.to_csv(summary_out, index=False)

    spot_summary = pd.concat(spot_rows, ignore_index=True)
    spot_out = TABLES / "kuppe_visium_spot_summary.csv"
    spot_summary.to_csv(spot_out, index=False)

    print(
        summary.sort_values(["zone_code", "dominant_fraction"], ascending=[True, False])
        .groupby("zone_label")
        .head(5)[
            [
                "zone_label",
                "cell_type",
                "n_spots",
                "mean_score",
                "dominant_spots",
                "dominant_fraction",
            ]
        ]
        .to_string(index=False)
    )
    print(f"\nWrote {summary_out}")
    print(f"Wrote {spot_out}")


if __name__ == "__main__":
    main()
