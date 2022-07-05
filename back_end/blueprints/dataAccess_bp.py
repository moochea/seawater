import logging
from http import HTTPStatus

from flask import jsonify, Blueprint

from infrastructure.utilities import Utilities


def construct(dataset_retriever_creator, calculations_service):
    dataAccess_bp = Blueprint('dataAccess', __name__, url_prefix="/api/dataAccess")

    logger = logging.getLogger('DataRetrieval')

    @dataAccess_bp.route('/records/<key>/<data_ref>', methods=('GET',))
    def get_records(key, data_ref):
        return get_data(key, data_ref, salinity_calculated=False)

    @dataAccess_bp.route('/records/<key>/<data_ref>/salinity_calculated', methods=('GET',))
    def get_records_with_psal(key, data_ref):
        return get_data(key, data_ref, salinity_calculated=True)

    def get_data(key, data_ref, salinity_calculated):
        logger.info("get data")
        msg = "unknown error"
        response = jsonify(msg)
        response.status = HTTPStatus.BAD_REQUEST

        if key:
            logger.info(f"get {key} records with salinity calculated" if salinity_calculated else f"get {key} records")
            retriever = dataset_retriever_creator.get_retriever(key)
            if not retriever:
                msg = f"{key} source not supported"
                response = jsonify(msg)
                response.status = HTTPStatus.BAD_REQUEST
                return response
            try:
                dataset = retriever.get_records(data_ref)
                if salinity_calculated:
                    dataset = calculate_salinity(dataset)
                status = {
                    'status': 'success',
                    'data': dataset.data,
                    'units': dataset.units,
                    'source': dataset.source,
                    'totalRecords': int(dataset.number_of_records)
                }
                logger.info(f"dataset size: {dataset.number_of_records}")
                response = jsonify(message=status)
                response.status = HTTPStatus.OK
            except:
                msg = f"{data_ref} not accessible at {key}"
                response = jsonify(msg)
                response.status = HTTPStatus.BAD_REQUEST
            finally:
                return response
        else:
            return response

    def calculate_salinity(dataset):
        presence_check = calculations_service.check_present()
        logger.info(f"gsw service operational: {presence_check}")
        if presence_check:
            psal_list = calculations_service.calculate_psal(dataset.data)
            new_dataframe = Utilities.dict_list_to_dataframe(dataset.data)
            new_dataframe['pSalinity'] = psal_list
            return dataset.updated_dataframe(new_dataframe)

    return dataAccess_bp
