# Reproducibility Checklist

Run from the project root:

```powershell
& 'C:\Users\mages\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' analysis\01_dataset_inventory.py
powershell.exe -ExecutionPolicy Bypass -File analysis\02_download_public_data.ps1
& 'C:\Users\mages\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' analysis\03_inspect_downloads.py
& 'C:\Users\mages\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' analysis\04_inspect_dataset_contents.py
& 'C:\Users\mages\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' analysis\05_summarize_kuppe_visium.py
& 'C:\Users\mages\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' analysis\06_make_initial_spatial_figures.py
& 'C:\Users\mages\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' analysis\07_make_dataset_overview_figure.py
& 'C:\Users\mages\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' analysis\08_build_biorxiv_submission.py
```

Before upload:

- Confirm that the bioRxiv account email is correct in the submission system.
- Upload `preprint_manuscript.docx`.
- Upload `supplementary_tables.xlsx`.
- Upload `supplementary_code.zip`.
- Upload separate figure files if requested by the submission system.
- Select CC BY 4.0 as the reuse license unless a different license is intentionally preferred.
