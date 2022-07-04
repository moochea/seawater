from unittest.mock import Mock

import pandas
from pandas import DataFrame

from Models.dataset import Dataset
from Models.sensor_information import SensorInformation


def generate_seawater_dataset():
    timestamps = ["2017-01-08 00:00:00",
                  "2017-01-08 00:15:00",
                  "2017-01-08 00:30:00",
                  "2017-01-08 00:45:00",
                  "2017-01-08 01:00:00",
                  "2017-01-08 01:15:00",
                  "2017-01-08 01:29:59"
                  ]
    conductivity = [3.38080, 3.38234, 3.38599, 3.38312, 3.38360, 3.38086, 3.38067]
    temperature = [4.5782, 4.5954, 4.6405, 4.6100, 4.6160, 4.5832, 4.5826]
    pressure = [722.723, 1722.729, 1722.686, 1722.686, 1722.644, 1722.644, 1722.595]
    salinity = [34.9799, 34.9798, 34.9751, 34.9737, 34.9730, 34.9755, 34.9740]
    dataframe = DataFrame({
            'timestamps': timestamps,
            'conductivity': conductivity,
            'temperature': temperature,
            'pressure': pressure,
            'salinity': salinity})

    sensor_info = SensorInformation({
        'Firmware_Version': "1", 'Sensor_Type': "base", 'Slot': "9/2", 'SensorId': "AE12453"})
    units = pandas.Series({"conductivity":"S/m"})
    source = "Somewhere"
    return Dataset(dataFrame=dataframe, sensor_info=sensor_info, units=units, source=source)
