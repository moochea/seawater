import logging
from datetime import datetime
from pathlib import Path


class CommonLogging:
    def __init__(self, log_config):
        log_level = getattr(logging, log_config.log_level.upper(), logging.DEBUG)
        CommonLogging.set_up_logging(
            folder=log_config.folder,
            file_name=log_config.file_name,
            append_date=log_config.append_date,
            date_format=log_config.date_format,
            log_format=log_config.log_format,
            log_level=log_level)

    @staticmethod
    def get_log_file_path(folder="./logs", file_name='log', append_date=True, date_format="%Y-%m-%d_%H-%M-%S"):
        date_string = datetime.now().strftime(date_format)
        file_name_format = f"{file_name}_{date_string}.log" if append_date else f"{file_name}.log"
        folder_path = Path.expanduser(Path(folder))
        file_path = Path.absolute(Path.joinpath(folder_path, file_name_format))
        return file_path

    @staticmethod
    def set_up_logging(folder, file_name, append_date, date_format, log_level, log_format):
        output_file=CommonLogging.get_log_file_path(
            folder=folder,
            file_name=file_name,
            append_date=append_date,
            date_format=date_format)
        # print(f"setting up logging with log level {log_level}")
        logging.basicConfig(filename=output_file, level=log_level, format=log_format)
