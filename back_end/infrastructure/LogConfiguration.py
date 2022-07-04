import json


class LogConfiguration:
    def __init__(self, json_file):
        log_config = json.load(json_file)
        self.folder = log_config['folder']
        self.file_name = log_config['file_name']
        self.append_date = log_config['append_date']
        self.date_format = log_config['date_format']
        self.log_format = log_config['log_format']
        self.log_level = log_config['log_level']