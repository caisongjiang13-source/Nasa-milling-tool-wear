# Validation record

Publication preparation date: 2026-10-06.

## Passed

- The command-line script ran against the real source `mill.mat`, producing feature, metric, residual and provenance files and data plots.
- The notebook code cells ran sequentially in a single Python process against the same source data; their outputs were saved.
- The notebook passed `nbformat` structural validation and contains no stored error outputs.
- The release contains 13 labelled Case 1 records and retains the VB = 0 record. Actual run IDs are 1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 and 17; see `results/case1_features.csv`.
- The vibration-mean correlation matches the original notebook output. The vibration-mean and AE-mean MAEs match the latest screenshot, with numerical tolerance of 1e-12. Values are in `results/baseline_metrics.csv`.
- The LinkedIn panels were visually inspected for legibility and label placement.

Numerical environment: Python 3.12.14; NumPy 2.3.5; SciPy 1.17.0; pandas 2.2.3; Matplotlib 3.10.8. Notebook 7.6.3 and ipykernel 7.4.0 were installed for checking, and are pinned in the requirements.

## Limits of verification

A separate Jupyter kernel could not start in this execution environment because socket creation was denied. The notebook's calculation cells were executed directly, but a full browser-to-kernel run was not verified. Windows and Colab execution were not tested here; installation guidance uses the documented Python and Jupyter workflows.

There is no held-out model evaluation. No predictive accuracy, generalisation to other cases, calibrated units, or physical sampling rate is established by these checks.

The raw dataset is excluded from the release package. Its SHA-256 fingerprint is recorded in `results/provenance.json`.
