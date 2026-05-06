from __future__ import annotations

import csv
import gzip
import tarfile
from pathlib import Path

import anndata as ad
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW = PROJECT_ROOT / "data" / "raw"
TABLES = PROJECT_ROOT / "tables"
TABLES.mkdir(exist_ok=True)


def rel(path: Path) -> str:
    return str(path.relative_to(PROJECT_ROOT))


def inspect_h5ad(path: Path) -> dict[str, object]:
    dataset = ad.read_h5ad(path, backed="r")
    try:
        obs = dataset.obs
        var = dataset.var
        obs_columns = list(obs.columns)
        var_columns = list(var.columns)
        candidate_obs = [
            col
            for col in obs_columns
            if any(
                token in col.lower()
                for token in [
                    "cell",
                    "type",
                    "annotation",
                    "cluster",
                    "sample",
                    "donor",
                    "patient",
                    "disease",
                    "zone",
                    "region",
                    "condition",
                ]
            )
        ]
        return {
            "path": rel(path),
            "kind": "h5ad",
            "n_obs": dataset.n_obs,
            "n_vars": dataset.n_vars,
            "n_layers": len(dataset.layers.keys()),
            "obs_columns": "; ".join(obs_columns[:40]),
            "candidate_metadata_columns": "; ".join(candidate_obs[:30]),
            "var_columns": "; ".join(var_columns[:20]),
            "notes": "",
        }
    finally:
        dataset.file.close()


def inspect_delimited_gz(path: Path, delimiter: str) -> dict[str, object]:
    with gzip.open(path, "rt", encoding="utf-8", errors="replace", newline="") as handle:
        reader = csv.reader(handle, delimiter=delimiter)
        header = next(reader, [])
        first = next(reader, [])

    return {
        "path": rel(path),
        "kind": "compressed_table",
        "n_obs": "",
        "n_vars": len(header),
        "n_layers": "",
        "obs_columns": "; ".join(header[:40]),
        "candidate_metadata_columns": "",
        "var_columns": "",
        "notes": f"first_data_row_fields={len(first)}",
    }


def inspect_tar(path: Path) -> tuple[dict[str, object], list[dict[str, object]]]:
    with tarfile.open(path, "r:*") as archive:
        members = [member for member in archive.getmembers() if member.isfile()]

    suffix_counts: dict[str, int] = {}
    for member in members:
        suffix = "".join(Path(member.name).suffixes) or "<none>"
        suffix_counts[suffix] = suffix_counts.get(suffix, 0) + 1

    archive_row = {
        "path": rel(path),
        "kind": "tar_archive",
        "n_obs": "",
        "n_vars": "",
        "n_layers": "",
        "obs_columns": "",
        "candidate_metadata_columns": "",
        "var_columns": "",
        "notes": f"{len(members)} files; suffixes={suffix_counts}",
    }
    member_rows = [
        {
            "archive": rel(path),
            "member": member.name,
            "size_mb": round(member.size / 1024 / 1024, 3),
            "suffix": "".join(Path(member.name).suffixes),
        }
        for member in members
    ]
    return archive_row, member_rows


def main() -> None:
    rows: list[dict[str, object]] = []
    archive_members: list[dict[str, object]] = []

    for path in sorted(RAW.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix == ".h5ad":
            rows.append(inspect_h5ad(path))
        elif "".join(path.suffixes).endswith(".tsv.gz"):
            rows.append(inspect_delimited_gz(path, "\t"))
        elif "".join(path.suffixes).endswith(".csv.gz"):
            rows.append(inspect_delimited_gz(path, ","))
        elif path.suffix == ".tar":
            archive_row, member_rows = inspect_tar(path)
            rows.append(archive_row)
            archive_members.extend(member_rows)

    inspection = pd.DataFrame(rows)
    inspection_out = TABLES / "dataset_file_inspection.csv"
    inspection.to_csv(inspection_out, index=False)

    archive_out = TABLES / "archive_members.csv"
    pd.DataFrame(archive_members).to_csv(archive_out, index=False)

    print(inspection[["path", "kind", "n_obs", "n_vars", "notes"]].to_string(index=False))
    print(f"\nWrote {inspection_out}")
    print(f"Wrote {archive_out}")


if __name__ == "__main__":
    main()
