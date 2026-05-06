# Analysis Scaffold

This directory will contain scripts and notebooks for the benchmark.

Recommended implementation:

- Python/Scanpy for AnnData handling and metadata harmonization
- R/Seurat where needed for source object conversion
- R packages for CellChat and NicheNet
- Python or R wrapper for LIANA
- CellPhoneDB through Python CLI

## Planned Scripts

- `00_environment_notes.md`
- `00_run_from_scratch.ps1`
- `01_dataset_inventory.py`
- `02_download_public_data.ps1`
- `03_inspect_downloads.py`
- `04_inspect_dataset_contents.py`
- `05_summarize_kuppe_visium.py`
- `06_make_initial_spatial_figures.py`
- `07_make_dataset_overview_figure.py`
- `08_harmonize_metadata.py`
- `09_run_liana.py`
- `10_run_cellphonedb.md`
- `11_run_cellchat.R`
- `12_compare_methods.py`
- `13_robustness_downsampling.py`
- `14_spatial_support.py`
- `15_make_figures.py`
