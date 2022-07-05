from http import HTTPStatus

import gsw as gsw
import numpy
import pandas as pandas
from flask import Blueprint, request, jsonify, json


def construct():
    calc_bp = Blueprint("calc", __name__, url_prefix="/api/calc")

    @calc_bp.route('/practical_salinity', methods=('POST',))
    def calculate_psal():
        print("calculate_psal")
        data = json.loads(request.data)
        dataframe = convert_to_dataframe(data)
        psal = return_psalinity_list(dataframe)
        response = jsonify(psal)
        response.status = HTTPStatus.OK
        return response

    def convert_to_dataframe(data):
        conductivity="conductivity"
        pressure="pressure"
        temperature="temperature"
        conductivity_values=[]
        temperature_values=[]
        pressure_values=[]
        for item in data:
            conductivity_values.append(item[conductivity])
            pressure_values.append(item[pressure])
            temperature_values.append(item[temperature])
        return pandas.Dataframe({conductivity: conductivity_values, temperature: temperature_values, pressure: pressure_values })

    def return_psalinity_list(dataframe):
        dataframe["pSalinity"] = dataframe.apply(lambda row: SP_from_C_with_Nan(
            row.conductivity, row.temperature, row.pressure), axis=1)
        return dataframe

    def SP_from_C_with_Nan(conductivity: str, temperature: str, pressure: str):
        try:
            value = gsw.SP_from_C(
                float(conductivity) * 10, float(temperature), float(pressure))
            return numpy.around(value, 4)
        except:
            return None

    return calc_bp