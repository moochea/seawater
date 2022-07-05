from unittest import mock
from unittest.mock import Mock
import pytest

from Models.data_retriever_base import DataRetrieverBase
from Models.data_retriever_creator import DataRetrieverCreator
from Models.dataset import Dataset
from Tests import helper


class TestDataRetrieverCreator:
    @pytest.fixture
    @mock.patch('Models.emso_data_retriever.EMSODataRetriever.load_data')
    @mock.patch("logging.getLogger")
    def creator(self, logger, load_data):
        def return_dataset(args):
            return helper.generate_seawater_dataset()
        logger = Mock()
        load_data = return_dataset
        creator = DataRetrieverCreator(logger)
        return creator

    def test_EMSO_key_exists(self, creator):
        key="EMSO"
        assert isinstance(creator.get_retriever(key), DataRetrieverBase)
        assert key in creator.keys

    def test_key_does_not_exist(self, creator):
        assert creator.get_retriever("Schmidt") is None
