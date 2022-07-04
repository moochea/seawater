import math

from Models.emso_data_retriever import EMSODataRetriever
from Tests import helper


class TestEMSORetriever:

    def test_salinity_calc(self):
        allowable_difference_percent = 5.0
        dataset = helper.generate_seawater_dataset()
        new_dataframe = EMSODataRetriever.add_psalinity_column(dataset._dataframe)
        pSalinity = new_dataframe['pSalinity'].tolist()
        assert all(item is not None for item in pSalinity)
        percent_diff = new_dataframe.apply(lambda row: (math.fabs(float(row['salinity'])-float(row['pSalinity']))*100/float(row['salinity'])), axis=1).tolist()
        assert all(value is not None and value < allowable_difference_percent for value in percent_diff)

