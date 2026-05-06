# Analysis Plan

## Phase 1: Data Acquisition

1. Download processed AnnData or Seurat objects where available.
2. Store raw/large files outside git-tracked manuscript files.
3. Create a metadata table with sample, disease, tissue region, chamber, platform, and cell annotations.

## Phase 2: Harmonization

1. Convert data to a common format.
2. Standardize broad cell-type labels:
   - Cardiomyocyte
   - Fibroblast
   - Endothelial
   - Pericyte
   - Smooth muscle
   - Myeloid
   - Lymphoid
   - Adipocyte
   - Neuronal
   - Mesothelial/epicardial
3. Preserve dataset-specific fine annotations for sensitivity analyses.
4. Apply basic QC filters only when required for compatibility.

## Phase 3: Communication Inference

Run communication methods with consistent inputs:

- CellChat
- CellPhoneDB
- LIANA
- NicheNet
- Spatial method for spatial transcriptomics data where feasible

Outputs per method:

- Ligand
- Receptor
- Sender cell type
- Receiver cell type
- Score
- P value or adjusted P value when available
- Pathway or family label
- Dataset
- Disease group

## Phase 4: Benchmarking Metrics

### Network-Level Metrics

- Number of inferred interactions
- Sender-receiver edge density
- Cell-type centrality
- Disease-vs-control network shift

### Agreement Metrics

- Top-k ligand-receptor overlap
- Jaccard similarity
- Rank correlation where comparable
- Pathway-level overlap
- Sender-receiver pair overlap

### Robustness Metrics

- Downsampling stability
- Annotation granularity stability
- Bootstrap support
- Cross-dataset recurrence

### Spatial Support

- Proximity of sender and receiver cell states
- Spatial enrichment of ligand and receptor expression
- Overlap with injury/remodeling zones

## Phase 5: Biological Interpretation

Prioritize interactions that are:

1. Supported by more than one method.
2. Recurrent across datasets or disease contexts.
3. Spatially supported where spatial data exist.
4. Biologically plausible from cardiac literature.
5. Not solely explained by cell abundance changes.

## Phase 6: Reproducibility

- Use locked package versions where feasible.
- Save intermediate tables.
- Save all figure-generating scripts.
- Avoid manual figure editing except final layout.

