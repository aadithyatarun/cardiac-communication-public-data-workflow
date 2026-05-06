# Environment Notes

This project will likely require both Python and R.

## Python Packages

- scanpy
- anndata
- pandas
- numpy
- scipy
- seaborn
- matplotlib
- liana
- cellphonedb

## Local Windows Runtime Note

On this machine, `python` is not currently available on PATH. The bundled Codex Python runtime is available at:

`C:\Users\mages\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`

Example:

```powershell
& 'C:\Users\mages\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' analysis\01_dataset_inventory.py
```

## R Packages

- Seurat
- CellChat
- NicheNet
- tidyverse
- ComplexHeatmap

## Data Storage

Large downloaded datasets should be stored under `data/raw/` or an external local data directory and excluded from git if this becomes a GitHub repository.
