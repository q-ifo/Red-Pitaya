import json
import types

class Calibrator:
    def __init__(self, config_file: str = "calibration_configs.json"):
        try:
            with open(config_file, 'r') as config_file:
                self.calibration_configs = json.load(config_file)
        except FileNotFoundError:
            print("Voltage config file not found, using default (no gain/offset) settings!")
            self.calibration_configs = dict(
                name = "default",
                input1 = dict(gain = 1, offset = 0),
                input2 = dict(gain = 1, offset = 0)
            )

    def correct_input(self, ch: int, voltage):
        if(ch != 1 and ch != 2):
            print("Improper channel (must be 1 or 2). Setting to input 1 configs")
            ch = 1

        return self.calibration_configs[f"input{ch}"]["gain"] * voltage + self.calibration_configs[f"input{ch}"]["offset"]

    def correct_output(self, ch: int, voltage):
        if(ch != 1 and ch != 2):
            print("Improper channel (must be 1 or 2). Setting to output 1 configs")
            ch = 1

        return self.calibration_configs[f"output{ch}"]["gain"] * voltage + self.calibration_configs[f"output{ch}"]["offset"]