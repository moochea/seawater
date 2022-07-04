# get records for nonexistant key
# calculate salinity for nonexistant key
from unittest import mock
from unittest.mock import Mock

import pytest
from flask import Flask

from Models.data_retriever_creator import DataRetrieverCreator
from Models.emso_data_retriever import EMSODataRetriever
from Tests import helper
from blueprints import dataAccess_bp


class TestEndpoints:

    @pytest.fixture
    def client(self):
        class NewClass(EMSODataRetriever):
            def __init__(self):
                super().__init__()

            def api_call_to_get_data(self, reference, args_dict ):
                return helper.generate_seawater_dataset()

        app = Flask(__name__)
        retriever = DataRetrieverCreator()

        retriever._classes["EMSO"] = NewClass
        blueprint = dataAccess_bp.construct(retriever)
        app.register_blueprint(blueprint)
        app.config.update()
        return app.test_client()

    def test_get_records_for_existing_dataset(self, client):
        response = client.get("/api/dataAccess/records/EMSO/58220")
        assert response.status_code == 200

    def test_get_records_for_non_existant_dataset(self, client):
        response = client.get("/api/dataAccess/records/EMSO/12345")
        assert response.status_code == 400

    def test_calculate_salinity_for_existing_dataset(self, client):
        response = client.get("/api/dataAccess/records/EMSO/58220/salinity_calculated")
        assert response.status_code == 200

    def test_calculate_for_non_existant_source(self, client):
        response = client.get("/api/dataAccess/Schmidt/58220/salinity_calculated")
        assert response.status_code == 404
