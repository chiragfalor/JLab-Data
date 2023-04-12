from OpticalTrapData import OpticalTrapData
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


data_dir = "JLab-Data/OpticalTrapping/"

filename_list = os.listdir(data_dir)

# categorize the files by date

# Mar22, oscillation in x
# Oscillation Amplitude 1.000000
# Oscillation Frequency 0.500000
Osc_X_files = [file for file in filename_list 
        if "Settings" not in file and file.startswith("Mar22") and "ox" in file]
Osc_X_data = [OpticalTrapData(file, data_dir = data_dir) for file in Osc_X_files]

# Mar22, brownian
Brownian_1_files = [file for file in filename_list
        if "Settings" not in file and file.startswith("Mar22") and "ox" not in file and file.endswith(".txt")]
Brownian_1_data = [OpticalTrapData(file, data_dir = data_dir) for file in Brownian_1_files]

# Apr 3, fixed beads
Fixed_beads_files = [file for file in filename_list
        if "Settings" not in file and file.startswith("Apr3")]
Fixed_beads_data = [OpticalTrapData(file, data_dir = data_dir) for file in Fixed_beads_files]

# Apr 5, brownian
Brownian_2_files = [file for file in filename_list
        if "Settings" not in file and file.startswith("Apr5")]
Brownian_2_data = [OpticalTrapData(file, data_dir = data_dir) for file in Brownian_2_files]

# onion files
Onion_files = [file for file in filename_list
        if "Settings" not in file and file.startswith("onion")]
Onion_data = [OpticalTrapData(file, data_dir = data_dir) for file in Onion_files]


# plot QPDX
# print(sample_data.QPDX.shape)
# print(sample_data.QPDX)
# plt.plot(sample_data.QPDX)
# plt.plot(sample_data.SGX)
# calculate PSD
for sample_data in Osc_X_data:
    f, Pxx = signal.welch(sample_data.QPDX, sample_data.sample_rate, nperseg = 1024)
    plt.figure()
    # log log 
    plt.loglog(f, Pxx)
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("PSD [V**2/Hz]")
    plt.show()
