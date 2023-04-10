import pandas as pd
import os

class OpticalTrapData():
    def __init__(self, filename, data_dir = "JLab-Data/OpticalTrapping/"):
        self.filename = filename
        self.data_dir = data_dir

        self.initialize_parameters()

        # read the data file
        self.data = pd.read_csv(self.data_dir + filename, header = None, names = ["QPDX", "QPDY", "SGX", "SGY"], sep = "\t")
        # convert to floats
        self.data = self.data.astype(float)
        # convert the data to a numpy array
        self.QPDX = self.data.QPDX.to_numpy()
        self.QPDY = self.data.QPDY.to_numpy()
        self.SGX = self.data.SGX.to_numpy()
        self.SGY = self.data.SGY.to_numpy()

        # make sure the data file matches the settings file
        # assert self.data.shape[0] == int(self.sample_rate * self.total_seconds), "The data file does not match the settings file"





    def initialize_parameters(self):
        # if self.filename.startswith("Apr3") or self.filename.startswith("Mar"):
        #     filename_params = self.filename.split("_")
        # get laser power from filename
        file_name_params = self.filename.split("_")
        # find 'mA' in the filename
        self.laser_power = float(file_name_params[file_name_params.index("mA") - 1])


        # find the files with Settings in the name
        all_files = os.listdir(self.data_dir)
        settings_files = [file for file in all_files if "Settings" in file and file.startswith(self.filename.split('.')[:-1][0])][0]
        # read the settings file
        with open(self.data_dir + settings_files, "r") as f:
            settings = f.readlines()
            for line in settings:
                try: 
                    setting, value = line.strip().split(": ")
                    if value.replace(".", "").isdigit(): value = float(value)
                except ValueError:
                    setting = line.strip().split(": ")
                    value = None
                # make sure the value is a number
                # Sample Rate: 10000.000000
                # Stage Oscillation: 
                # Oscillation Amplitude 0.500000
                # Oscillation Frequency 0.500000
                # Axis 89.000000
                # Seconds: 30.000000
                match setting:
                    case "Sample Rate": self.sample_rate = value
                    case "Stage Oscillation": self.stage_osc = value
                    case "Oscillation Amplitude": self.osc_amplitude = value
                    case "Oscillation Frequency": self.osc_frequency = value
                    case "Axis": self.axis = value
                    case "Seconds": self.total_seconds = value
                    case _: pass
                # don't need to read the rest of the file
                if setting == "Seconds": break







