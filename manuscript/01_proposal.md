# Manuscript Proposal

## Working Title

Robustness and biological interpretability of cell-cell communication inference in human cardiac single-cell and spatial transcriptomics

## Short Title

Benchmarking cardiac cell-cell communication inference

## Target Preprint Server

bioRxiv

## Candidate Journal Targets After Preprint

- PLOS Computational Biology
- Bioinformatics
- Cardiovascular Research
- iScience
- BMC Biology
- Briefings in Bioinformatics

## Rationale

Single-cell, single-nucleus, and spatial transcriptomics have made it possible to profile cardiac remodeling at cellular resolution. Many studies now use computational cell-cell communication inference to nominate signaling interactions between cardiomyocytes, fibroblasts, endothelial cells, vascular cells, immune cells, and adipocytes. However, these methods differ in assumptions, ligand-receptor databases, scoring models, treatment of cell abundance, and handling of spatial proximity.

For cardiac disease biology, this creates a practical problem: the same dataset can produce different inferred communication networks depending on the tool and preprocessing choices. A systematic benchmark focused on human cardiac disease datasets would help researchers distinguish robust signals from method-specific artifacts.

## Primary Objective

To benchmark the robustness, agreement, and biological interpretability of cell-cell communication inference methods across public human cardiac single-cell and spatial transcriptomics datasets.

## Specific Aims

### Aim 1

Assemble a harmonized set of public human cardiac transcriptomic datasets covering healthy adult heart, heart failure, myocardial infarction, and atrial fibrillation.

### Aim 2

Run multiple cell-cell communication inference methods on comparable cell-type annotations and disease contrasts.

Candidate methods:

- CellChat
- CellPhoneDB
- LIANA
- NicheNet
- COMMOT or similar spatial communication method for spatial datasets

### Aim 3

Quantify method agreement and robustness.

Planned tests:

- Cross-method overlap of top ligand-receptor pairs
- Cell-type pair agreement
- Pathway-level agreement
- Sensitivity to cell downsampling
- Sensitivity to cell-type annotation granularity
- Disease-vs-control reproducibility across datasets
- Spatial proximity support where spatial data are available

### Aim 4

Identify robust cardiac remodeling communication axes and translate them into practical recommendations for future cardio-omics studies.

## Expected Robust Cardiac Signals

- Fibroblast-to-cardiomyocyte extracellular matrix and TGF-beta-related signaling
- Immune-to-fibroblast inflammatory signaling
- Endothelial-to-cardiomyocyte vascular and metabolic support signals
- Pericyte/smooth muscle/endothelial vascular remodeling signals
- Chemokine signaling in injury and inflammation
- Natriuretic peptide and stress-response-associated cardiomyocyte signals

## Conservative Claims

This study will not claim clinical diagnostic or therapeutic validity. It will make computational and biological-prioritization claims based on public transcriptomic datasets.

