from Models.calculate_service import CalculateService
import gsw
import numpy

from Models.csv_dataset_extractor import CsvDataSetExtractor
from Models.data_retriever_base import DataRetrieverBase
from Models.dataset import Dataset
from infrastructure.utilities import Utilities


class EMSODataRetriever(DataRetrieverBase):

    def __init__(self, logger):
        self.logger = logger
        key = "58220"
        self.datasets = {key: EMSODataRetriever.load_data()}
        self.logger.info("EMSO data retriever created")

    def get_records(self, reference: str, args_dict={}):
        if reference in self.datasets.keys():
            dataset = self.datasets[reference]
            return dataset

    # def calculated_salinity(self, dataset):
    #     presence_check = self.client.check_present()
    #     self.logger.info(f"gsw service operational: {presence_check}")
    #     if presence_check:
    #         psal_list = self.client.calculate_psal(dataset.data)
    #         new_dataframe = Utilities.dict_list_to_dataframe(dataset.data)
    #         new_dataframe['pSalinity'] = psal_list
    #         return dataset.updated_dataframe(new_dataframe)

    @staticmethod
    def load_data():
        filepath = "./data/58220.csv"
        loader = CsvDataSetExtractor(filepath)
        sensor_info = loader.extract_sensor_info()
        data, units = loader.load_data()
        return Dataset(dataFrame=data, sensor_info=sensor_info, units=units, source=filepath)
