param(
    [string]$OutDir = "data/raw"
)

$ErrorActionPreference = "Stop"

New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
New-Item -ItemType Directory -Force -Path "$OutDir/GSE183852" | Out-Null
New-Item -ItemType Directory -Force -Path "$OutDir/GSE238242" | Out-Null
New-Item -ItemType Directory -Force -Path "$OutDir/GSE135805" | Out-Null
New-Item -ItemType Directory -Force -Path "$OutDir/kuppe_mi_visium" | Out-Null

$downloads = @(
    @{
        Url = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE183nnn/GSE183852/suppl/GSE183852_Integrated_Counts.csv.gz"
        Out = "$OutDir/GSE183852/GSE183852_Integrated_Counts.csv.gz"
        Label = "GSE183852 heart failure integrated counts"
    },
    @{
        Url = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE238nnn/GSE238242/suppl/GSE238242_snAF.metadata.tsv.gz"
        Out = "$OutDir/GSE238242/GSE238242_snAF.metadata.tsv.gz"
        Label = "GSE238242 AF metadata"
    },
    @{
        Url = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE238nnn/GSE238242/suppl/GSE238242_RAW.tar"
        Out = "$OutDir/GSE238242/GSE238242_RAW.tar"
        Label = "GSE238242 AF processed/raw supplementary archive"
    },
    @{
        Url = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE135nnn/GSE135805/suppl/GSE135805_RAW.tar"
        Out = "$OutDir/GSE135805/GSE135805_RAW.tar"
        Label = "GSE135805 cardiac spatial transcriptomics archive"
    },
    @{
        Url = "https://zenodo.org/records/6578047/files/Visium_control_P1.h5ad?download=1"
        Out = "$OutDir/kuppe_mi_visium/Visium_control_P1.h5ad"
        Label = "Kuppe MI Visium control P1"
    },
    @{
        Url = "https://zenodo.org/records/6578047/files/Visium_FZ_P14.h5ad?download=1"
        Out = "$OutDir/kuppe_mi_visium/Visium_FZ_P14.h5ad"
        Label = "Kuppe MI Visium fibrotic zone P14"
    },
    @{
        Url = "https://zenodo.org/records/6578047/files/Visium_IZ_P10.h5ad?download=1"
        Out = "$OutDir/kuppe_mi_visium/Visium_IZ_P10.h5ad"
        Label = "Kuppe MI Visium infarct zone P10"
    },
    @{
        Url = "https://zenodo.org/records/6578047/files/Visium_RZ_P11.h5ad?download=1"
        Out = "$OutDir/kuppe_mi_visium/Visium_RZ_P11.h5ad"
        Label = "Kuppe MI Visium remote zone P11"
    }
)

foreach ($item in $downloads) {
    if (Test-Path $item.Out) {
        Write-Host "Skipping existing: $($item.Label)"
        continue
    }

    Write-Host "Downloading: $($item.Label)"
    curl.exe --ssl-no-revoke -L --retry 3 --retry-delay 5 $item.Url -o $item.Out
}

Write-Host "Download summary:"
Get-ChildItem -Path $OutDir -Recurse -File |
    Select-Object FullName,@{Name='SizeMB';Expression={[math]::Round($_.Length / 1MB, 2)}} |
    Sort-Object FullName

