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
- `08_build_biorxiv_submission.py`
- `09_build_preprint_pdf.py`
- `10_harmonize_metadata.py`
- `11_run_liana.py`
- `12_run_cellphonedb.md`
- `13_run_cellchat.R`
- `14_compare_methods.py`
- `15_robustness_downsampling.py`
- `16_spatial_support.py`
- `17_make_figures.py`
