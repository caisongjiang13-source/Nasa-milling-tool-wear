from pathlib import Path
data_file = Path(__file__).parent/"mill.mat"

from scipy.io import loadmat
data = loadmat(data_file)
print(data.keys())

import numpy as np
import matplotlib.pyplot as plt

mill = data["mill"]

run_4 = mill[0,3]
run_9 = mill[0,8]
run_14 = mill[0,13]

# print("case=",run_14["case"])
# print("run =", run_14["run"])
# print("VB =", run_14["VB"])
# print("DOC =", run_14["DOC"])
# print("feed =", run_14["feed"])
# print("material =", run_14["material"])

