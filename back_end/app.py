import logging

from flask import Flask, render_template
from flask_cors import CORS

from Models.calculate_service import CalculateService
from Models.data_retriever_creator import DataRetrieverCreator
from blueprints import dataAccess_bp
from infrastructure.logger import CommonLogging
from infrastructure.utilities import Utilities


def log_configuration():
    CommonLogging(Utilities.read_configuration())


def run_server():
    dist_path = "./dist"
    app = Flask(__name__,
                static_folder=dist_path,
                template_folder=dist_path
                )

    # CORS(app)
    dataset_retriever_creator = DataRetrieverCreator(logger=logging.getLogger("DataRetriever"))
    calculations_service = CalculateService(logger=logging.getLogger('CalculationService'))
    data_access_bp = dataAccess_bp.construct(dataset_retriever_creator, calculations_service)
    app.register_blueprint(data_access_bp)
    app.config.update()

    @app.route('/')
    def index():
        return render_template("index.html")

    app.logger.info("Application started")
    app.run(host="0.0.0.0", port=80, debug=True)


if __name__ == '__main__':
    log_configuration()
    run_server()
