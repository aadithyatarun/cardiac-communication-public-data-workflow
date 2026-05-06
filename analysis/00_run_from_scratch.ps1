param(
    [string]$Python = "C:\Users\mages\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $ProjectRoot

& $Python analysis\01_dataset_inventory.py
powershell.exe -ExecutionPolicy Bypass -File analysis\02_download_public_data.ps1
& $Python analysis\03_inspect_downloads.py
& $Python analysis\04_inspect_dataset_contents.py
& $Python analysis\05_summarize_kuppe_visium.py
& $Python analysis\06_make_initial_spatial_figures.py
& $Python analysis\07_make_dataset_overview_figure.py
& $Python analysis\08_build_biorxiv_submission.py
