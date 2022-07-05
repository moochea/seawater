# get records for nonexistant key
# calculate salinity for nonexistant key
from unittest import mock
from unittest.mock import Mock

import pytest
from flask import Flask

from Models.data_retriever_creator import DataRetrieverCreator
from Tests import helper
from blueprints import dataAccess_bp


class TestEndpoints:

    @pytest.fixture
    @mock.patch('Models.emso_data_retriever.EMSODataRetriever.load_data')
    def client(self, load_data):
        def calculate(arg):
            return [0,0,0,0,0,0,0]
        load_data.return_value = helper.generate_seawater_dataset()
        logger = Mock()
        app = Flask(__name__)
        retriever = DataRetrieverCreator(logger)
        calculations_service = Mock()
        calculations_service.presence_check.return_value = True
        # calculations_service.calculate_psal = Mock()
        calculations_service.calculate_psal = calculate
        blueprint = dataAccess_bp.construct(retriever, calculations_service)
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
