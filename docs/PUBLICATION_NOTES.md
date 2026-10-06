# Publication edition notes

The source was `Mill_phase_2_Fixed.ipynb`, together with the latest saved screenshots showing the AE residuals and mean-model MAEs. The calculations were rerun on the user's source `mill.mat`.

The publication edition:

- Replaces Colab-specific Drive mounting and the private Drive path with configurable local paths.
- Uses actual `run` identifiers while retaining global `record_number` as a separate field.
- Removes repeated exploratory cells from the reader-facing notebook while preserving the implemented feature and baseline choices.
- Uses consistent names for vibration-standard-deviation coefficients. The earlier notebook used `a_AEs`/`b_AEs` for that vibration fit and printed different variables; these names were misleading.
- Fixes labels that described the standard-deviation fit as a mean fit.
- Fits VB directly from a feature (`np.polyfit(feature, VB, 1)`). This avoids fitting the reverse direction or assuming that an inverted regression is the same fit.
- Adds the AE mean baseline present in the newer screenshots and verifies its MAE against the real data.
- Makes the original time-axis assumption explicit. Published plots show sample indices; no sampling-rate, frequency or calibrated-unit claims are made.
- Labels all reported MAEs as in-sample fit errors. No independent validation or multivariable model is added.
- Adds exportable tables, a clean entry point and installation instructions.

Refactoring and publication preparation were assisted by ChatGPT. Future tasks remain future tasks. The original source notebook is not overwritten.
