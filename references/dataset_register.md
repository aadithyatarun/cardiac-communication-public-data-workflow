# Dataset Register

This register tracks candidate datasets for inclusion. Final inclusion requires confirming data accessibility, license, processed file availability, metadata completeness, and disease/control labels.

## Priority 1: Human Adult Heart Reference

### Cells of the adult human heart

- Citation: Litvinukova et al., Nature, 2020
- DOI: 10.1038/s41586-020-2797-4
- Data type: human adult heart single-cell/single-nucleus RNA-seq
- Use: healthy reference cell types and baseline cardiac cell communication
- Source: Human Cell Atlas / cellxgene resources
- Notes: widely cited cardiac reference atlas

## Priority 2: Human Myocardial Infarction Spatial Multiomics

### Spatial multi-omic map of human myocardial infarction

- Citation: Kuppe et al., Nature, 2022
- DOI: 10.1038/s41586-022-05060-x
- Data type: snRNA-seq, snATAC-seq, spatial transcriptomics
- Disease: myocardial infarction, injury/remodeling zones, controls
- Use: spatial support for inferred communication networks
- Data availability: cellxgene, Zenodo, Human Cell Atlas Data Portal
- Notes: strong anchor dataset for spatial validation and injury-zone biology

## Priority 3: Human Heart Failure

### Single-cell transcriptomics reveals cell-type-specific diversification in human heart failure

- Citation: Nature Cardiovascular Research, 2022
- DOI: 10.1038/s44161-022-00028-6
- GEO accession: GSE183852
- Data type: integrated sc/snRNA-seq
- Disease: dilated cardiomyopathy / heart failure
- Use: disease-vs-healthy communication comparison
- Notes: large and highly cited; important for fibroblast and cardiomyocyte remodeling

### Spatial Transcriptomics of Human Cardiac Tissue

- Accession: GSE135805
- Data type: spatial transcriptomics
- Disease: normal, hypertrophic, dilated, and ischemic cardiomyopathy
- Use: early spatial cardiac heart failure dataset
- Notes: may require careful preprocessing due to older platform and metadata format

## Priority 4: Human Atrial Fibrillation

### Single-nucleus multi-omics implicates androgen receptor signaling in cardiomyocytes and NR4A1 regulation in fibroblasts during atrial fibrillation

- Citation: Leblanc et al., Nature Cardiovascular Research, 2025
- DOI: 10.1038/s44161-025-00626-0
- GEO accession: GSE238242
- Data type: paired snRNA-seq and snATAC-seq multiome
- Disease: persistent atrial fibrillation vs sinus rhythm controls
- Use: atrial disease context, fibroblast/cardiomyocyte communication, validation of AF-specific signals
- Notes: authors provide code at https://github.com/lebf3/scAF_multiome/

### Large-scale single-nuclei profiling identifies role for ATRNL1 in atrial fibrillation

- Citation: Nature Communications, 2024
- Data type: single-nucleus RNA-seq
- Disease: atrial fibrillation
- Use: independent AF replication dataset if processed data are accessible

## Inclusion Criteria

- Human cardiac tissue preferred
- Processed count matrix or AnnData/Seurat object available
- Cell-type annotations available or recoverable
- Disease/control metadata available
- Public access without controlled clinical identifiers
- Permissive enough terms for reanalysis and preprint reporting

## Exclusion Criteria

- No usable metadata
- No disease/control labels for disease analyses
- Data access requires lengthy controlled-access approval
- Dataset is too small for stable communication inference
