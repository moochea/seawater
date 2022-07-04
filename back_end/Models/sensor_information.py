class SensorInformation:
    def __init__(self, sensor_info_dict):
        self.firmware_version = sensor_info_dict['Firmware_Version']
        self.type = sensor_info_dict['Sensor_Type']
        self.slot = sensor_info_dict['Slot']
        self.id = sensor_info_dict['SensorId']
