"""Reproduce the existing Case 1 exploration; no held-out validation is performed."""

from pathlib import Path
import argparse
import hashlib
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.io import loadmat

FEATURES = ["vib_mean", "vib_std", "AE_mean", "AE_std"]
BASELINES = ["vib_mean", "vib_std", "AE_mean"]
# These fractions preserve the original (10 < assumed_time < 25) mask.
# Physical seconds / sampling rate have not been independently verified.
WINDOW_START = 10 / 36
WINDOW_END = 25 / 36


def window_mask(length):
    position = np.arange(length) / length
    return (position > WINDOW_START) & (position < WINDOW_END)


def load_features(data_path, case_id=1):
    mill = loadmat(data_path)["mill"].ravel()
    rows = []
    for index, record in enumerate(mill):
        case = int(record["case"].item())
        vb = float(record["VB"].item())
        if case != case_id or not np.isfinite(vb):
            continue
        row = {"record_number": index + 1, "case": case,
               "run": int(record["run"].item()), "VB": vb}
        for channel, prefix in [("vib_spindle", "vib"), ("AE_spindle", "AE")]:
            signal = np.asarray(record[channel], dtype=float).ravel()
            segment = signal[window_mask(len(signal))]
            if not len(segment) or not np.isfinite(segment).all():
                raise ValueError(f"Invalid signal in record {index + 1}: {channel}")
            row[prefix + "_mean"] = float(np.mean(segment))
            row[prefix + "_std"] = float(np.std(segment, ddof=0))
        rows.append(row)
    if len(rows) < 3:
        raise ValueError("At least three labelled records are needed.")
    return mill, pd.DataFrame(rows)


def fit_baselines(features):
    metrics, residuals = [], features[["record_number", "case", "run", "VB"]].copy()
    for feature in BASELINES:
        x, y = features[feature].to_numpy(), features["VB"].to_numpy()
        if np.ptp(x) == 0:
            raise ValueError(f"Constant feature: {feature}")
        slope, intercept = np.polyfit(x, y, 1)
        estimate = slope * x + intercept
        residual = y - estimate
        residuals[feature + "_estimate"] = estimate
        residuals[feature + "_residual"] = residual
        metrics.append({"feature": feature,
                        "pearson_r": float(np.corrcoef(x, y)[0, 1]),
                        "slope": float(slope), "intercept": float(intercept),
                        "fit_MAE": float(np.mean(np.abs(residual))),
                        "evaluation": "in-sample; no independent test set"})
    return pd.DataFrame(metrics), residuals


def style_axes(ax):
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.16)


def save_figures(mill, features, metrics, residuals, destination):
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    colors = {"vib_mean": "#2563eb", "AE_mean": "#0f766e"}
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), constrained_layout=True)
    for ax, feature, title in zip(axes, ["vib_mean", "AE_mean"],
                                  ["Spindle vibration mean", "Spindle AE mean"]):
        ax.scatter(features[feature], features.VB, color=colors[feature], s=48)
        row = metrics.set_index("feature").loc[feature]
        x = np.linspace(features[feature].min(), features[feature].max(), 100)
        ax.plot(x, row.slope * x + row.intercept, color=colors[feature], alpha=0.65)
        for _, point in features.iterrows():
            offset = (5, 5)

            if feature == "vib_mean":
                if int(point.run) == 8:
                    offset = (5, 10)
                elif int(point.run) == 9:
                    offset = (-12, -13)
                elif int(point.run) == 13:
                    offset = (-18, 8)
                elif int(point.run) == 14:
                    offset = (5, 12)

            ax.annotate(
                str(int(point.run)),
                (point[feature], point.VB),
                xytext=offset,
                textcoords="offset points",
                fontsize=9,
            )
        ax.set(title=f"{title} | r = {row.pearson_r:+.3f}",
               xlabel="Mean signal (dataset units)", ylabel="Flank wear VB (dataset units)")
        style_axes(ax)
    fig.suptitle("Case 1: individual linear fits on the same labelled records")
    fig.savefig(destination / "feature_relationships.png", dpi=180)
    plt.close(fig)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), constrained_layout=True, sharey=True)
    for ax, feature, title in zip(axes, ["vib_mean", "AE_mean"],
                                  ["Vibration mean baseline", "AE mean baseline"]):
        ax.axhline(0, color="#64748b", linestyle="--", linewidth=1)
        x, y = residuals[feature + "_estimate"], residuals[feature + "_residual"]
        ax.scatter(x, y, color=colors[feature], s=48)
        for run, xx, yy in zip(features.run, x, y):
            ax.annotate(str(run), (xx, yy), xytext=(5, 5),
                        textcoords="offset points", fontsize=9)
        ax.set(title=title, xlabel="Fitted VB (dataset units)",
               ylabel="Measured VB - fitted VB")
        ax.margins(x=0.12, y=0.16)
        style_axes(ax)
    fig.suptitle("Residuals: points are labelled with Case 1 run IDs")
    fig.savefig(destination / "residual_comparison.png", dpi=180)
    plt.close(fig)

    fig, axes = plt.subplots(2, 1, figsize=(10, 7), constrained_layout=True, sharex=True)
    for ax, channel, label in zip(axes, ["vib_spindle", "AE_spindle"],
                                  ["Spindle vibration", "Spindle acoustic emission"]):
        for run_id, color in [(11, "#94a3b8"), (12, "#ea580c"), (13, "#2563eb")]:
            record = next(r for r in mill if int(r["case"].item()) == 1
                          and int(r["run"].item()) == run_id)
            signal = np.asarray(record[channel]).ravel()
            ax.plot(np.arange(len(signal)), signal, color=color, alpha=0.7,
                    linewidth=0.65, label=f"Run {run_id}")
        mask_indices = np.flatnonzero(window_mask(len(signal)))
        ax.axvspan(mask_indices[0], mask_indices[-1], color="#0f766e", alpha=0.08,
                   label="Feature window")
        ax.set(title=label, ylabel="Signal (dataset units)")
        ax.legend(ncol=4, frameon=False, fontsize=9)
        style_axes(ax)
    axes[-1].set_xlabel("Sample index (zero-based; physical time not verified)")
    fig.savefig(destination / "signal_window.png", dpi=180)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    root = Path(__file__).resolve().parents[1]
    parser.add_argument("--data", type=Path, default=root / "data" / "mill.mat")
    args = parser.parse_args()
    if not args.data.is_file():
        parser.error("mill.mat is missing. Download NASA Milling data and place it in data/.")
    mill, features = load_features(args.data)
    metrics, residuals = fit_baselines(features)
    results = root / "results"
    results.mkdir(exist_ok=True)
    features.to_csv(results / "case1_features.csv", index=False)
    metrics.to_csv(results / "baseline_metrics.csv", index=False)
    residuals.to_csv(results / "case1_residuals.csv", index=False)
    metadata = {"dataset_shape": [1, len(mill)], "case": 1,
                "labelled_records": len(features),
                "window_fraction": [WINDOW_START, WINDOW_END],
                "window_boundary": "strictly greater / strictly less",
                "std_ddof": 0, "retains_zero_VB": True,
                "time_axis": "original 36-second assumption is unverified; use sample indices",
                "data_sha256": hashlib.sha256(args.data.read_bytes()).hexdigest(),
                "evaluation": "in-sample; no held-out data"}
    (results / "provenance.json").write_text(json.dumps(metadata, indent=2) + "\n")
    save_figures(mill, features, metrics, residuals, root / "figures")
    print(metrics.to_string(index=False))
    print("Saved results/ and figures/. These are fitting diagnostics, not test results.")


if __name__ == "__main__":
    main()
