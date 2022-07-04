from unittest import mock
from unittest.mock import Mock
import pytest

from Models.data_retriever_base import DataRetrieverBase
from Models.data_retriever_creator import DataRetrieverCreator
from Models.dataset import Dataset


class TestDataRetrieverCreator:
    @pytest.fixture
    def creator(self):
        creator = DataRetrieverCreator()
        return creator

    def test_EMSO_key_exists(self, creator):
        key="EMSO"
        assert isinstance(creator.get_retriever(key), DataRetrieverBase)
        assert key in creator.keys

    def test_key_does_not_exist(self, creator):
        assert creator.get_retriever("Schmidt") is None
