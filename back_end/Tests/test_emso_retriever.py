import math
from unittest import mock
from unittest.mock import Mock

import pytest

from Models.dataset import Dataset
from Models.emso_data_retriever import EMSODataRetriever
from Tests import helper


class TestEMSORetriever:

    @pytest.fixture
    @mock.patch('Models.emso_data_retriever.EMSODataRetriever.load_data')
    def retriever(self,load_data):
        load_data.side_effect = [helper.generate_seawater_dataset()]
        logger = Mock()
        logger.info=print
        dr = EMSODataRetriever(logger)
        return dr

    def test_get_records_with_salinity_cal_return_type(self, retriever):
        records = retriever.get_records("58220")
        assert isinstance(records, Dataset)


