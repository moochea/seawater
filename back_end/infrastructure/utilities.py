import json
import os
from datetime import datetime

from infrastructure.LogConfiguration import LogConfiguration


class Utilities:
    @staticmethod
    def read_configuration():
        file_path = "./log_config.json"
        full_path = os.path.expanduser(file_path)
        if os.path.exists(full_path):
            file = open(full_path, 'r')
            config = LogConfiguration(file)
            return config
        else:
            print(f"Configuration file {full_path} could not be loaded")

    @staticmethod
    def json_to_dictionary(json_string: str):
        return json.loads(json_string)

    @staticmethod
    def datetime_to_string(datetime_object: datetime):
        return datetime_object.astimezone().strftime("%m/%d/%Y, %H:%M:%S")