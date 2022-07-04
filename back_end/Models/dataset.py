import gsw
import numpy
from pandas import DataFrame
from Models.sensor_information import SensorInformation


class Dataset:
    def __init__(self, dataFrame: DataFrame, sensor_info: SensorInformation, units: {}, source: str):
        self._dataframe = dataFrame
        self._sensor_info = sensor_info
        self._units = units
        self._source = source

    @property
    def empty(self):
        return self._dataframe.empty

    @property
    def number_of_records(self):
        return int(self._dataframe.size/self._dataframe.columns.size)

    @property
    def sensor_info(self):
        return self._sensor_info

    @property
    def units(self):
        return self._units.to_dict()

    @property
    def source(self):
        return self._source

    @property
    def data(self):
        return self._dataframe.to_dict('records')

