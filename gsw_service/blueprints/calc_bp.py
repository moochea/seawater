from http import HTTPStatus

import gsw as gsw
import numpy
import pandas as pandas
from flask import Blueprint, request, jsonify, json
# import flask_swagger_ui


def construct():
    calc_bp = Blueprint("calculations", __name__, url_prefix="/api/calculations")

    @calc_bp.route('/practical_salinity', methods=('POST',))
    def process_data():
        print("calculate_psal")
        data=request.data
        data = json.loads(data)
        dataframe = extract_args_to_dataframe(data)
        psal = calculate_psal(dataframe)
        response = jsonify(psal)
        response.status = HTTPStatus.OK
        return response

    def extract_args_to_dataframe(list_of_dict):
        conductivity="conductivity"
        pressure="pressure"
        temperature="temperature"
        conductivity_values=[]
        temperature_values=[]
        pressure_values=[]
        for item in list_of_dict:
            conductivity_values.append(item[conductivity])
            pressure_values.append(item[pressure])
            temperature_values.append(item[temperature])
        return pandas.DataFrame(data={conductivity: conductivity_values, temperature: temperature_values, pressure: pressure_values })

    def calculate_psal(dataframe):
        '''
        :param dataframe:
        :return: list: list of float values
        '''
        pSalinity = dataframe.apply(lambda row: SP_from_C_with_Nan(
            row.conductivity, row.temperature, row.pressure), axis=1)
        return pSalinity.tolist()

    def SP_from_C_with_Nan(conductivity: str, temperature: str, pressure: str):
        try:
            value = gsw.SP_from_C(
                float(conductivity) * 10, float(temperature), float(pressure))
            return numpy.around(value, 4)
        except:
            return None

    return calc_bp