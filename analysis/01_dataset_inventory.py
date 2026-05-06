from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INVENTORY = PROJECT_ROOT / "data" / "dataset_inventory_template.csv"
OUTPUT = PROJECT_ROOT / "data" / "dataset_inventory_review.csv"


REQUIRED_COLUMNS = [
    "dataset_id",
    "citation",
    "year",
    "disease_context",
    "tissue_or_chamber",
    "platform",
    "data_type",
    "processed_data_url",
    "accession",
    "license_or_terms",
    "status",
    "notes",
]


def main() -> None:
    df = pd.read_csv(INVENTORY)
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df = df.sort_values(["status", "year", "dataset_id"], ascending=[True, False, True])
    df.to_csv(OUTPUT, index=False)

    print(f"Loaded {len(df)} candidate datasets")
    print(df[["dataset_id", "year", "disease_context", "accession", "status"]].to_string(index=False))
    print(f"\nWrote review table to {OUTPUT}")


if __name__ == "__main__":
    main()

