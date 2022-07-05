from http import HTTPStatus
from flask import Blueprint, request, jsonify, json

from utility import Utility


def construct():
    calc_bp = Blueprint("calculations", __name__, url_prefix="/api/calculations")

    @calc_bp.route('/practical_salinity', methods=('POST',))
    def process_data():
        data = request.data
        data = json.loads(data)
        dataframe = Utility.extract_args_to_dataframe(data)
        psal = Utility.calculate_psal(dataframe)
        response = jsonify(psal)
        response.status = HTTPStatus.OK
        return response

    return calc_bp
