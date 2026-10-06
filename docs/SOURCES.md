# Sources

## Project evidence

- `results/provenance.json`: source-data checksum, record counts, window definition and evaluation scope.
- `results/case1_features.csv`: actual run labels, measured VB and extracted features.
- `results/baseline_metrics.csv`: correlations, linear coefficients and in-sample MAEs.
- `results/case1_residuals.csv`: fitted values and signed residuals.
- `notebooks/Mill_phase_2_Fixed.ipynb`: untouched supplied learning notebook, including original comments and restoration metadata.
- `notebooks/01_case1_exploration.ipynb`: original cells in sequence, with marked editorial notes and publication additions.
- `docs/source_cell_map.json`: original-file checksum and exact cell/edit mapping.
- `src/analysis.py`: optional ChatGPT-assisted refactor, cross-checked against the reading edition.

Publication values are derived from the user's source data. Figures are data plots, not illustrative or generated measurements.

## Dataset source

[NASA PCoE Data Set Repository — Milling](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)

NASA attributes the dataset to A. Agogino and K. Goebel (2007), BEST Lab, UC Berkeley, “Milling Data Set”, NASA Prognostics Data Repository, NASA Ames Research Center.

[NASA Open Data — Milling Wear](https://data.nasa.gov/dataset/milling-wear)

## Structure reference

[PatRuediger/domain_gap_milling_tool_wear](https://github.com/PatRuediger/domain_gap_milling_tool_wear): consulted for its separation of project overview, installation, data acquisition, usage and limitations. Its models and performance claims are not part of this project; no code is copied from it.

[GitHub: About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes): consulted for what a project README should communicate and relative image/file links. GitHub does not prescribe a single mandatory research-project README template.

## Installation and publishing documentation

- [Python downloads](https://www.python.org/downloads/)
- [Python packaging: pip and virtual environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
- [Python venv documentation](https://docs.python.org/3/library/venv.html)
- [Jupyter installation](https://jupyter.org/install)
- [Colab external data and Drive access](https://colab.research.google.com/notebooks/io.ipynb)
- [Matplotlib annotations](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html)
- [GitHub: Working with notebook files](https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files#working-with-jupyter-notebook-files-on-github)
- [GitHub: Create a repository](https://docs.github.com/en/get-started/start-your-journey/creating-a-repository-for-your-project-on-github)
- [GitHub: Add a file](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)
- [GitHub: Add locally hosted code](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)

These references were checked during publication preparation. Consult the live pages if interface labels change.
