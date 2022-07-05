
from http import HTTPStatus
import http.client

from flask import jsonify


class CalculateService:
    def __init__(self, logger):
        self.logger= logger
        self.base_url="http://localhost:9998"
        
    def check_present(self):
        self.logger.info("calculate salinity through service")
        response = jsonify("failed")
        response.status_code = HTTPStatus.BAD_REQUEST
        try:
            connection =  http.client.HTTPSConnection(self.base_url)
            connection.request("GET", "/")
            response = connection.getresponse()
            self.logger.info("service response: " + response.reason)
            return response.status_code == HTTPStatus.OK
        except:
            self.logger.error("unable to connect")
            return False



