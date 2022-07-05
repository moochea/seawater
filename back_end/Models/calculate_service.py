
from http import HTTPStatus
import http.client
from flask import jsonify, json


class CalculateService:
    def __init__(self, logger):
        self.logger = logger
        self.base_url ="localhost"
        self.port = 9998
        
    def check_present(self):
        self.logger.info("Check service presence")
        response = jsonify("failed")
        response.status_code = HTTPStatus.BAD_REQUEST
        try:
            connection = http.client.HTTPConnection(self.base_url, port=self.port, timeout=10)
            connection.request("GET", "/")
            response = connection.getresponse()
            connection.close()
            self.logger.info(f"service status: {response.status}")
            return response.status == HTTPStatus.OK
        except:
            self.logger.error("unable to connect")
            return False

    def calculate_psal(self, dictionary_list):
        response = jsonify("failed")
        response.status_code = HTTPStatus.BAD_REQUEST
        try:
            connection = http.client.HTTPConnection(self.base_url, port=self.port, timeout=30)
            entries = json.dumps(dictionary_list)
            connection.request("POST", "/api/calculations/practical_salinity", entries)
            response = connection.getresponse()
            connection.close()
            self.logger.info("service response: " + response.reason)
            data = json.loads(response.read()) # need to decode as a list
            self.logger.info(f"calcuate psal result length: {len(data)}")
            return data
        except:
            self.logger.error("unable to connect")
            return False


if __name__ == "__main__":


    base_url = "localhost"
    connection = http.client.HTTPConnection(base_url, port=9998)
    connection.request("GET", "/")
    response = connection.getresponse()
    print(response.read().decode())
    connection.close()
    print("finish!")
