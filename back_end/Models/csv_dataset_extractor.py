import os
from datetime import datetime

import pandas
from Models.sensor_information import SensorInformation


class CsvDataSetExtractor:
    """
    Very specific to the EMSO csv file structure
    """
    def __init__(self, data_path):

        # data_path = "./data/58220.csv"
        if not os.path.exists(data_path):
            print(f"File {data_path} not found")
            raise FileNotFoundError()
        self.data_path = data_path

    def extract_sensor_info(self):
        # extract sensor information from first line from file
        with open(self.data_path) as csvfile:
            sensor_data = csvfile.readline().strip('\n').strip(';').split(';')
        return SensorInformation(dict([ data.split('=') for data in sensor_data ]))

    def load_data(self):
        df = pandas.read_csv(filepath_or_buffer=self.data_path, delimiter=';', skiprows=1)

        # Rename column headers
        df.columns=["date", "time", "temperature", "conductivity", "pressure", "salinity", "sound_speed", "unnamed"]

        # Remove unnecessary columns / NA columns
        df.pop("unnamed")

        # Extract units
        units = df.iloc[0]

        # Remove units from dataframe
        df.drop(df.index[0], inplace=True)

        timestamp_string = df.apply(lambda row: f"{row['date']} {row['time']}", axis=1)
        # print(timestamp_string)
        df['timestamp'] = pandas.to_datetime(timestamp_string).astype(str)
        df.sort_values(by=["timestamp"], inplace=True)
        return df, units
