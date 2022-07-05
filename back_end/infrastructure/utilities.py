import json
import os
from datetime import datetime

import pandas

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

    @staticmethod
    def dict_list_to_dataframe(dict_list):
        dict_of_lists = {}
        for item in dict_list:
            for key in item.keys():
                if key not in dict_of_lists.keys():
                    dict_of_lists[key] = []
                dict_of_lists[key].append(item[key])
        return pandas.DataFrame(dict_of_lists)



