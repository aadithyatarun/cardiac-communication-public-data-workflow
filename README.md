# Cardiac Communication Public Data Workflow

Reproducible workflow for auditing public human cardiac single-cell, single-nucleus, multiome, and spatial transcriptomics datasets before downstream cell-cell communication analysis.

The project currently includes a dataset register, public-data download script, local file inspection, a myocardial infarction Visium spatial composition analysis, generated figures, derived tables, and a preprint-ready manuscript package.

## Research Question

Which public human cardiac transcriptomic datasets are analysis-ready for spatially grounded cell-cell communication studies, and what initial tissue-zone composition signals are visible in myocardial infarction spatial transcriptomics data?

## Current Scope

- Human adult heart reference atlas
- Human myocardial infarction spatial multi-omics
- Human heart failure and dilated cardiomyopathy single-cell/single-nucleus transcriptomics
- Human atrial fibrillation single-nucleus multiome
- Human cardiac spatial transcriptomics from heart failure etiologies

The current analysis intentionally stops short of claiming completed CellChat, CellPhoneDB, LIANA, or NicheNet benchmarking. Those methods require additional harmonization of count matrices and cell-type annotations.

## Repository Structure

- `analysis/`: reproducible scripts, including the from-scratch runner
- `data/`: dataset inventory and metadata only; large public data are ignored
- `tables/`: generated audit and summary tables
- `figures/generated/`: generated PNG/PDF figures
- `manuscript/`: proposal, outline, and preprint notes
- `references/`: dataset and literature source notes
- `deliverables/preprint/`: manuscript, supplementary tables, cover note, metadata, and code archive

## Reproduce

Run from the project root:

```powershell
powershell.exe -ExecutionPolicy Bypass -File analysis\00_run_from_scratch.ps1
```

The runner downloads or skips existing public raw files, regenerates tables and figures, and rebuilds the preprint deliverables.

## Key Outputs

- `tables/dataset_file_inspection.csv`
- `tables/archive_members.csv`
- `tables/kuppe_visium_celltype_summary.csv`
- `tables/kuppe_visium_spot_summary.csv`
- `figures/generated/dataset_overview.png`
- `figures/generated/kuppe_visium_celltype_overview.png`
- `deliverables/preprint/preprint_manuscript.docx`
- `deliverables/preprint/supplementary_tables.xlsx`
- `deliverables/preprint/supplementary_code.zip`

## Data Policy

Large public datasets are not committed to GitHub. They are downloaded into `data/raw/` by `analysis/02_download_public_data.ps1` and are ignored by git. Dataset accessions and source information are tracked in `data/dataset_inventory_review.csv` and `references/dataset_register.md`.

## Author

Tarun Aadithya Magesh Raghavan  
Department of Health Science, McMaster University, Hamilton, Ontario, Canada
