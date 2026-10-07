# NASA Milling: Exploring Tool Wear

I wanted to understand whether changes in milling signals could tell us something about tool wear. This project uses Python to explore that question with the NASA Milling dataset.

The work so far covers plotting signals, calculating their mean and standard deviation, and trying simple linear models to estimate wear. It is still a learning project in progress.

## Data

The data comes from the [Milling dataset in NASA's Prognostics Data Repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/), provided by the UC Berkeley BEST Lab. The original data file is `mill.mat` and needs to be downloaded separately using the links below.

The [notebook](notebooks/Mill_phase_2_Fixed.ipynb) records 167 runs in the file. The current wear analysis uses the 13 runs in Case 1 with a recorded VB value, including VB = 0. Runs without a VB value are still useful for inspecting signals, but are left out of the model fitting.

VB means flank wear, measured in millimetres. The [data dictionary](docus/data_dictionary.md) contains field notes, case ranges and recorded wear values.

## Files

| File | What it contains |
| --- | --- |
| [read.py](scripts/read.py) | Early exploration: loading the data, comparing spindle and table signals, and checking acoustic emission means in selected runs. |
| [Mill_phase_2_Fixed.ipynb](notebooks/Mill_phase_2_Fixed.ipynb) | The main analysis: signal plots, feature tables, correlations, linear fits and residual comparisons. |
| [data_dictionary.md](docus/data_dictionary.md) | Notes on the data fields and how the runs are grouped. Some details are still marked for checking. |

## Work so far

- Compared vibration and acoustic emission (AE) signals from the spindle and table.
- Plotted Case 1 spindle signals to inspect how they change between runs and investigate unusual behaviour.
- Calculated the mean and standard deviation of spindle vibration and AE using the notebook's selected time window.
- Checked their relationship with VB using scatter plots and Pearson correlation.
- Fitted separate straight-line models using vibration mean, vibration standard deviation and AE mean.
- Compared the vibration-mean and AE-mean models using residuals and mean absolute error (MAE).

The notebook also puts vibration mean and AE mean into the same table. A model using both together has not been fitted yet.

## What I found so far

In this case, spindle vibration mean tends to decrease as wear increases, while spindle AE mean tends to increase. The saved notebook outputs give the following results:

| Input used to estimate VB | Pearson correlation with VB | MAE (mm) |
| --- | ---: | ---: |
| Spindle vibration mean | -0.863 | 0.0578 |
| Spindle AE mean | 0.911 | 0.0511 |

Source: the correlation and MAE outputs in the [Mill_phase_2_Fixed notebook](notebooks/Mill_phase_2_Fixed.ipynb).

AE mean has a slightly lower fitting error here. The residuals also show that the two models make different errors on individual runs, which is why I started looking at the signals together.

These errors are calculated on the same runs used to fit the models. They do not yet tell us how well the models will work on new runs or different cutting conditions.

## How to run

The code uses NumPy, SciPy, Matplotlib and pandas. For a local Python environment, install them with:

```bash
python -m pip install numpy scipy matplotlib pandas
```

**Main notebook in Google Colab**

1. Open `Mill_phase_2_Fixed.ipynb` in Colab.
2. Put `mill.mat` in the top level of your Google Drive. The notebook currently loads `/content/drive/MyDrive/mill.mat`; change this path if you keep the data elsewhere.
3. Run the cells from top to bottom and allow Colab to mount your Drive when prompted.

**Early script on your computer**

Put mill.mat in the scripts folder, beside read.py. Open a terminal in the project’s root folder, then run:

```bash
cd scripts
python read.py
```

## Current limits

The models currently cover Case 1 only. The early script uses a 4–29 s window, while the notebook uses 10–25 s on its constructed time axis. These settings are visible in the respective files. The meaning of the dataset's `time` field is still marked for checking in the data dictionary.

The current results are a starting point for understanding the signals and their relationship with wear. More checking is needed before treating the models as reliable wear predictions.

## Data source and references

- [NASA PCoE Data Set Repository — Milling](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/): the dataset description and credit to its contributors.
- [NASA Open Data — Milling Wear](https://data.nasa.gov/dataset/milling-wear): the official dataset entry.
- [Original Milling data download](https://phm-datasets.s3.amazonaws.com/NASA/3.+Milling.zip): the archive linked from NASA's repository. Download and extract it to obtain `mill.mat` and the accompanying dataset documentation.

Dataset citation, as given by NASA: A. Agogino and K. Goebel (2007), BEST Lab, UC Berkeley. "Milling Data Set", NASA Prognostics Data Repository, NASA Ames Research Center, Moffett Field, CA.
