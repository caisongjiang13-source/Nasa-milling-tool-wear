# Source-preserving publication notes

The main source is the supplied `Mill_phase_2_Fixed.ipynb`, with later screenshots used as evidence for AE mean fitting results. Calculations use the supplied `mill.mat`.

## Supplied original

`notebooks/Mill_phase_2_Fixed.ipynb` is a byte-for-byte copy of the supplied file. Code, comments, original markdown, metadata and existing outputs are unchanged. Its existing restoration metadata describes an earlier recovery from pasted Colab text. This release preserves that supplied snapshot; it does not claim to recover its pre-restoration whitespace or any later unsupplied changes.

## Reading edition

`notebooks/01_case1_exploration.ipynb` now contains every original cell in the same order, with nearby editorial notes. It retains original variable names and commented-out experiments. Feature calculations execute directly in the notebook, without importing the optional refactored script.

The exact source-cell map and code edits are recorded in `docs/source_cell_map.json`. The code changes are limited to runtime/data-path adaptation, unverified time-axis captions, quote compatibility in two f-strings, and the coefficient pair printed in the vibration-standard-deviation cell. Misleading original names and notes remain visible with corrections alongside them.

## Explicit additions

Publication preparation adds a clearly labelled section after the supplied notebook:

- The AE mean fit corresponding to later supplied result screenshots; this fit code is absent from the supplied notebook.
- MAE calculations, CSV exports and provenance metadata.
- Presentation figures, clearer run-label offsets and short leader lines for crowded labels.

These additions were prepared with ChatGPT assistance. The vibration means, standard deviations, vibration model coefficients and vibration residuals are reused directly from the author's supplied cells. No combined model or independent validation is added.

## Optional script

`src/analysis.py` remains an optional ChatGPT-assisted refactor for exporting the same numerical results. Its header and README identify it as a helper rather than the author's original learning source. The primary entry points are the supplied original and the source-preserving reading edition.

The README, installation guide and LinkedIn draft now explain this distinction. The author's personal reflection remains blank. Creating this package does not publish or modify a repository or social account.
