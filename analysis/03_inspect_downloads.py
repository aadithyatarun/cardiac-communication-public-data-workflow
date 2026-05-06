from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW = PROJECT_ROOT / "data" / "raw"
TABLES = PROJECT_ROOT / "tables"
TABLES.mkdir(exist_ok=True)


def main() -> None:
    rows = []
    for path in sorted(RAW.rglob("*")):
        if path.is_file():
            rows.append(
                {
                    "path": str(path.relative_to(PROJECT_ROOT)),
                    "size_mb": round(path.stat().st_size / 1024 / 1024, 3),
                    "suffix": "".join(path.suffixes),
                }
            )

    df = pd.DataFrame(rows)
    out = TABLES / "download_manifest.csv"
    df.to_csv(out, index=False)
    print(df.to_string(index=False))
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()

