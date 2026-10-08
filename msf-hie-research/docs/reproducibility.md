# Reproducibility

The project is designed to support reproducible analysis through structured notebooks, modular source code, and a fixed dependency list.

## Recommended practices

- Pin dependency versions in `requirements.txt`
- Store notebook outputs and metadata with model artifacts
- Record notebook execution order and environment details
- Version the datasets and code used in each analysis run

## Suggested outputs for each run

- notebook outputs or saved figures
- model artifact files in `models/`
- metrics tables saved in `results/tables/`
- figure exports saved in `results/figures/`
