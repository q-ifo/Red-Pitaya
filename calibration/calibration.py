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
        if(ch != "in1" and ch != "in2"):
            print("Improper channel (must be in1 or in2). Setting to input 1 configs")
            ch = "in1"

        return self.calibration_configs[ch]["gain"] * voltage + self.calibration_configs[ch]["offset"]

    def correct_output(self, ch: int, voltage):
        if(ch == "off"):
            return voltage
        if(ch != "out1" and ch != "out2"):
            print("Improper channel (must be out1 or out2). Setting to output 1 configs")
            ch = "out1"

        return self.calibration_configs[ch]["gain"] * voltage + self.calibration_configs[ch]["offset"]