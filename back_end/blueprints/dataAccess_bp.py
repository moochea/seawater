import logging
from http import HTTPStatus

from flask import jsonify, Blueprint


def construct(dataset_retriever_creator):
    dataAccess_bp = Blueprint('dataAccess', __name__, url_prefix="/api/dataAccess")

    logger = logging.getLogger('DataRetrieval')

    @dataAccess_bp.route('/records/<key>/<data_ref>', methods=('GET',))
    def get_records(key, data_ref):
        return get_data(key, data_ref, salinity_calculated=False)

    @dataAccess_bp.route('/records/<key>/<data_ref>/salinity_calculated', methods=('GET',))
    def calculate_salinity(key, data_ref):
        return get_data(key, data_ref, salinity_calculated=True)

    def get_data(key, data_ref, salinity_calculated):
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
                dataset = retriever.get_records(data_ref, {'salinity_calculated': salinity_calculated})
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

    return dataAccess_bp
