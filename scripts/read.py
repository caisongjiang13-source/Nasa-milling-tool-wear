from pathlib import Path
data_file = Path(__file__).parent/"mill.mat"
print(data_file.exists())

from scipy.io import loadmat
data = loadmat(data_file)
print(data.keys())

header = data["__header__"]
version = data["__version__"]
globals = data["__globals__"]

print(type(header))
print(type(version))
print(type(globals))
print(header)
print(version)
print(globals)
check data shape

#mill
mill = data["mill"]
print(type(mill))
print(mill.shape)
print(mill.dtype.names)

first_run = mill[0, 0]

#first run condition

print("case=",first_run["case"])
print("run =", first_run["run"])
print("VB =", first_run["VB"])
print("DOC =", first_run["DOC"])
print("feed =", first_run["feed"])
print("material =", first_run["material"])

print("time_shape=",first_run["time"].shape)
print("vib_spindle=",first_run["vib_spindle"].shape)
print("time=",first_run["time"].item())

#plot spindle vibriation

import numpy as np
import matplotlib.pyplot as plt

Duration = first_run["time"].item()
n_sample = first_run["vib_spindle"].shape[0]

#code the x-axis time interval

x_t = np.arange(n_sample)/ 250

#other data

print(first_run["smcAC"].shape)
print(first_run["smcDC"].shape)
print(first_run["vib_table"].shape)
print(first_run["AE_table"].shape)
print(first_run["AE_spindle"].shape)

print("case=",first_run["case"])
print("run=",first_run["run"])

#list all the run and case

n = np.arange(167)
n_run = mill[0,n]
for i, one_run in enumerate(n_run):
    print(
        i,
        "case=", one_run["case"].item(),
        "run=", one_run["run"].item(),
        "VB=", one_run["VB"].item()
    )
start = 0
current_case = n_run[0]["case"].item()

for i, one_run in enumerate(n_run):
    case = one_run["case"].item()

    if case != current_case:
        print(f"mill({start}-{i - 1}) : case {current_case}")
        start = i
        current_case = case

print(f"mill({start}-{len(n_run) - 1}) : case {current_case}")

#compare vib_spindle/table and AE_spindle/table

fig,axes = plt.subplots(2,2,sharex  = True)

axes[0,0].plot(x_t, first_run["vib_spindle"])
axes[0,0].set_title("vib_spindle-time")
axes[0,0].set_ylabel("vib_spindle")

axes[1,0].plot(x_t,first_run["AE_spindle"])
axes[1,0].set_title("AE_spindle-time")
axes[1,0].set_ylabel("AE_spindle")
axes[1,0].set_xlabel("time")

axes[0,1].plot(x_t, first_run["vib_table"])
axes[0,1].set_title("vib_table-time")
axes[0,1].set_ylabel("vib_table")

axes[1,1].plot(x_t,first_run["AE_table"])
axes[1,1].set_title("AE_table-time")
axes[1,1].set_ylabel("AE_table")
axes[1,1].set_xlabel("time")

plt.show()

run_4 = mill[0,3]
run_9 = mill[0,8]
run_14 = mill[0,13]

fig,axes = plt.subplots(3,2,sharex=True,sharey=True)

axes[0,0].plot(x_t, run_4["AE_spindle"])
axes[0,0].set_title("run 4 AE spindle")
axes[0,0].set_ylabel("run 4")

axes[0,1].plot(x_t, run_4["AE_table"])
axes[0,1].set_title("run 4 AE table")

axes[1,0].plot(x_t, run_9["AE_spindle"])
axes[1,0].set_title("run 9 AE spindle")
axes[1,0].set_ylabel("run 9")

axes[1,1].plot(x_t, run_9["AE_table"])
axes[1,1].set_title("run 9 AE table")

axes[2,0].plot(x_t, run_14["AE_spindle"])
axes[2,0].set_title("run 14 AE spindle")
axes[2,0].set_ylabel("run 14")
axes[2,0].set_xlabel("time")

axes[2,1].plot(x_t, run_14["AE_table"])
axes[2,1].set_title("run 14 AE table")
axes[2,1].set_xlabel("time")

plt.show()

#for range 4s-29s

cut_mask = (x_t > 4)&(x_t < 29)
AE_spindle_cut4 = run_4["AE_spindle"][cut_mask]
mean_AE_spindle_4 = np.mean(AE_spindle_cut4)
print("spindle 4 mean AE=",mean_AE_spindle_4)
AE_table_cut4 = run_4["AE_table"][cut_mask]
mean_AE_table_4 = np.mean(AE_table_cut4)
print("table 4 mean AE=",mean_AE_table_4)

AE_spindle_cut9 = run_9["AE_spindle"][cut_mask]
mean_AE_spindle_9 = np.mean(AE_spindle_cut9)
print("spindle 9 mean AE=",mean_AE_spindle_9)
AE_table_cut9 = run_9["AE_table"][cut_mask]
mean_AE_table_9 = np.mean(AE_table_cut9)
print("table 9 mean AE=",mean_AE_table_9)

AE_spindle_cut14 = run_14["AE_spindle"][cut_mask]
mean_AE_spindle_14 = np.mean(AE_spindle_cut14)
print("spindle 14 mean AE=",mean_AE_spindle_14)
AE_table_cut14 = run_14["AE_table"][cut_mask]
mean_AE_table_14 = np.mean(AE_table_cut14)
print("table 14 mean AE=",mean_AE_table_14)

gap_4 = abs(mean_AE_spindle_4 - mean_AE_table_4)
print("gap 4=",gap_4)
gap_9 = abs(mean_AE_spindle_9 - mean_AE_table_9)
print("gap 9=",gap_9)
gap_14 = abs(mean_AE_spindle_14 - mean_AE_table_14)
print("gap 14=",gap_14)































