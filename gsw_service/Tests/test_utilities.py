import pytest

from utility import Utility


class TestiUtilities:

    @pytest.fixture
    def sample_data(self):
        return [
            {"temperature": 4.7225, "conductivity": 3.2625, "pressure": 1715.235},
            {"temperature": 4.7225, "conductivity": 3.2625, "pressure": 1715.235},
            {"temperature": 4.7225, "conductivity": 3.2625, "pressure": 1715.235},
            {"temperature": 4.7225, "conductivity": 3.2625, "pressure": 1715.235},
            {"temperature": 4.5782, "conductivity": 3.3808, "pressure": 722.723}
        ]

    def test_extract_args_to_dataframe(self, sample_data):
        dataframe = Utility.extract_args_to_dataframe(sample_data)
        assert dataframe.size == 5*3
        assert all(item in ["temperature", "conductivity", "pressure"] for item in dataframe.columns)
        assert len(dataframe.columns) == 3


    def test_calculate_psal(self, sample_data):
        dataframe = Utility.extract_args_to_dataframe(sample_data)
        psal_values = Utility.calculate_psal(dataframe)
        expected = [33.4791, 33.4791, 33.4791, 33.4791, 35.4757]
        assert (expected[x] == psal_values[x] for x in range(0,len(expected)))




