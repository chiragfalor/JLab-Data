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

# Mar22, brownian
Brownian_1_files = [file for file in filename_list
        if "Settings" not in file and file.startswith("Mar22") and "ox" not in file]

print(Osc_X_files)
sample_data = OpticalTrapData(Osc_X_files[0], data_dir = data_dir)

# plot QPDX
print(sample_data.QPDX.shape)
print(sample_data.QPDX)
plt.plot(sample_data.QPDX)
plt.plot(sample_data.SGX)
# calculate PSD
f, Pxx = signal.welch(sample_data.QPDX, sample_data.sample_rate, nperseg = 1024)
plt.figure()
# log log 
plt.loglog(f, Pxx)
plt.xlabel("Frequency [Hz]")
plt.ylabel("PSD [V**2/Hz]")
plt.show()
