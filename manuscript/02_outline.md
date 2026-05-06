# Manuscript Outline

## Title

Robustness and biological interpretability of cell-cell communication inference in human cardiac single-cell and spatial transcriptomics

## Abstract Draft

Single-cell and spatial transcriptomic studies increasingly use computational cell-cell communication inference to nominate mechanisms of cardiac remodeling. However, the reproducibility of inferred ligand-receptor interactions across methods, datasets, disease contexts, and preprocessing choices remains unclear. Here, we benchmark multiple communication inference frameworks across public human cardiac transcriptomic datasets spanning healthy adult heart, heart failure, myocardial infarction, and atrial fibrillation. We quantify agreement at the ligand-receptor, pathway, and cell-type-pair levels, and assess robustness to downsampling, annotation granularity, and spatial proximity support. Across datasets, method-specific ligand-receptor rankings vary substantially, whereas pathway-level signals are more stable and converge on fibroblast, endothelial, immune, and cardiomyocyte remodeling axes. Spatial data provide additional support for a subset of inferred interactions, particularly those involving injury-associated fibroblast, myeloid, endothelial, and stressed cardiomyocyte states. These results provide practical guidance for interpreting cardiac cell-cell communication analyses and highlight robust signaling programs for future mechanistic studies.

## Main Sections

### Introduction

- Cardiac remodeling is multicellular.
- Single-cell and spatial omics provide cell-type resolution.
- Cell-cell communication inference is popular but method-dependent.
- Cardiology needs a practical benchmark using human cardiac datasets.

### Results

1. Public human cardiac datasets capture complementary disease contexts.
2. Communication tools differ in ligand-receptor prioritization and network density.
3. Pathway-level signals are more reproducible than individual ligand-receptor pairs.
4. Robust remodeling axes recur across heart failure, myocardial infarction, and atrial fibrillation.
5. Spatial transcriptomics supports a subset of inferred communication events.
6. Downsampling and annotation granularity affect rare-cell and fibroblast-state interactions.
7. Practical recommendations for cardiac communication inference.

### Discussion

- Interpreting tool-specific vs robust signals.
- Why pathway-level agreement may be more reliable than individual pair ranking.
- Cardiac biology implications.
- Limitations: public data heterogeneity, tissue region differences, sample size, computational inference cannot prove signaling.
- Recommendations for future studies.

### Methods

- Dataset search and inclusion criteria
- Preprocessing and harmonization
- Cell-type annotation mapping
- Communication inference methods
- Robustness analyses
- Spatial validation
- Statistical summaries
- Reproducibility and code availability

## Planned Figures

### Figure 1

Study design and dataset overview.

### Figure 2

Cross-method agreement in inferred cardiac communication networks.

### Figure 3

Disease-associated communication axes in heart failure, myocardial infarction, and atrial fibrillation.

### Figure 4

Spatial support for selected inferred interactions in myocardial injury and heart failure tissue.

### Figure 5

Robustness to downsampling and annotation granularity.

### Figure 6

Practical decision framework for cardiac cell-cell communication analysis.

