import gsw
import numpy

from Models.csv_dataset_extractor import CsvDataSetExtractor
from Models.data_retriever_base import DataRetrieverBase
from Models.dataset import Dataset


class EMSODataRetriever(DataRetrieverBase):

    def __init__(self):
        self.data_ref = {"58220": "./data/58220.csv"}

    def get_records(self, reference, args_dict):
        return self.api_call_to_get_data(reference, args_dict.get('salinity_calculated', False))

    def api_call_to_get_data(self, reference, salinity_calculated):
        if reference not in self.data_ref.keys():
            return None
        loader = CsvDataSetExtractor(self.data_ref[reference])
        sensor_info = loader.extract_sensor_info()
        data, units = loader.load_data()
        if salinity_calculated:
            return Dataset(dataFrame=self.add_psalinity_column(data), sensor_info=sensor_info, units=units, source=self.data_ref[reference])
        return Dataset(dataFrame=data, sensor_info=sensor_info, units=units, source=self.data_ref[reference])

    @staticmethod
    def add_psalinity_column(dataframe):
        dataframe["pSalinity"] = dataframe.apply(lambda row: EMSODataRetriever.SP_from_C_with_Nan(
            row.conductivity, row.temperature, row.pressure), axis=1)
        return dataframe

    @staticmethod
    def SP_from_C_with_Nan(conductivity:str, temperature:str, pressure:str):
        try:
            value = gsw.SP_from_C(
                float(conductivity)*10, float(temperature), float(pressure))
            return numpy.around(value, 4)
        except:
            return None
