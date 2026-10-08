# MSF HIE Research

A research project focused on malaria forecasting, hotspot analysis, and healthcare accessibility modeling for MSF operational planning.

## Project structure

- `notebooks/` contains reproducible analysis workflow notebooks
- `src/` contains reusable Python modules for preprocessing, feature generation, modeling, and evaluation
- `data/` stores raw and sample datasets and documentation
- `models/` stores trained model artifacts and metadata
- `results/` stores figures and tabular outputs
- `docs/` stores methodology and reproducibility documentation

## Getting started

```bash
cd msf-hie-research
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then open the notebooks in `notebooks/` or run scripts from the project root.

## Typical workflow

1. Validate and clean the raw data in `notebooks/01_data_validation.ipynb`
2. Explore patterns in `notebooks/02_exploratory_analysis.ipynb`
3. Run spatiotemporal and environmental analyses in the subsequent notebooks
4. Train and evaluate forecasting models using the modules in `src/`
5. Save outputs to `results/` and model artifacts to `models/`
