from Models.calculate_service import CalculateService
import gsw
import numpy

from Models.csv_dataset_extractor import CsvDataSetExtractor
from Models.data_retriever_base import DataRetrieverBase
from Models.dataset import Dataset


class EMSODataRetriever(DataRetrieverBase):

    def __init__(self, logger):
        self.logger = logger
        key = "58220"
        self.datasets = {key: EMSODataRetriever.load_data(key)}
        self.client = CalculateService(logger)
        self.logger.info("EMSO data retriever created")

    def get_records(self, reference: str, args_dict: dict):
        if reference in self.datasets.keys():
            dataset = self.datasets[reference]
        if args_dict and args_dict.get("salinity_calculated", False):
            dataset = self.calculated_salinity(dataset)
        return dataset

    def calculated_salinity(self, dataset):
        self.client.check_present()
        self.logger.info("Present!")
        return dataset 

    @staticmethod
    def load_data(reference):
        filepath = "./data/58220.csv"
        loader = CsvDataSetExtractor(filepath)
        sensor_info = loader.extract_sensor_info()
        data, units = loader.load_data()
        return Dataset(dataFrame=data, sensor_info=sensor_info, units=units, source=filepath)

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
