# Validation record

Source-preserving revision prepared on 2026-10-06.

## Source preservation

- `notebooks/Mill_phase_2_Fixed.ipynb` was compared byte for byte with the current supplied file. It is identical, including original comments, notes, metadata and saved outputs.
- The reading edition retains all 49 original cells in their original order. Source text is unchanged in 36 cells; the remaining 13 have recorded changes. This includes markdown cells as well as code. See [source_cell_map.json](source_cell_map.json) for the complete mapping and edit reasons.
- Every original comment line was checked for preservation in the corresponding reading cell, including the commented-out input experiment.
- Original markdown notes remain unchanged; clarifications are separate marked cells.
- The supplied original's existing restoration metadata is retained. These checks concern the supplied snapshot, not a pre-restoration export or later unsupplied Colab edits.

Original-file SHA-256: `e101e46e04db69b5c46f108d0bd47cfc056c06462aace2c65bac1090ce54c573`. The same fingerprint is recorded in the cell map and [provenance.json](../results/provenance.json).

## Calculations and outputs

- All 44 code cells of the reading edition, including added setup and publication cells, executed in order in one Python process against the real source `mill.mat`. The retained original notebook itself was not edited or rerun.
- The reading edition passed `nbformat` structural validation. It has saved outputs and no stored error outputs.
- Feature extraction runs directly in the original learning cells. It does not call the optional refactored script.
- Reading-edition feature tables, metrics and residuals were compared with the optional script's calculations. All numeric columns agree with absolute tolerance `1e-12`; identifier and evaluation fields agree exactly.
- The labelled Case 1 run IDs are 1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 and 17. VB = 0 is retained. Within this subset, the original global record numbers match the stored run IDs. See [case1_features.csv](../results/case1_features.csv).
- Correlations, fit coefficients and MAEs are in [baseline_metrics.csv](../results/baseline_metrics.csv). Vibration mean and standard-deviation fit code is retained from the supplied original. The AE mean fit is a labelled addition corresponding to the later result screenshots.
- The README comparison figure was generated from the reading edition's arrays and visually checked after separating crowded labels. LinkedIn figures were rebuilt from those exported arrays and checked for label legibility.
- Relative documentation links and ZIP contents were checked during final packaging. Raw data and caches are excluded. The original notebook inside the ZIP was also compared byte for byte with the supplied file.

Numerical environment: Python 3.12.14; NumPy 2.3.5; SciPy 1.17.0; pandas 2.2.3; Matplotlib 3.10.8. Notebook 7.6.3 and ipykernel 7.4.0 are installed and pinned in the requirements. Versions were read from the execution environment.

## Limits

In the earlier publication check, a separate Jupyter kernel could not start because socket creation was denied. This revision executes notebook cells directly in one Python process; a full browser-to-kernel run is not verified. Windows and Colab environments were not tested here. Instructions follow the official documentation linked in [SOURCES.md](SOURCES.md).

There is no held-out evaluation. These checks establish calculation consistency, not predictive accuracy on unseen cases, calibrated units or a physical sampling rate.

The raw dataset is not bundled. Its checksum is recorded in [provenance.json](../results/provenance.json).
