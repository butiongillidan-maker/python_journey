raw_sensor_data = {
    "sensor_1": 24.5,
    "sensor_2": -999.0,
    "sensor_3": 18.2,
    "sensor_4": 0.0,
    "sensor_5": 31.0,
    "sensor_6": -999.0
}

cleaned_data = {sensor:data for sensor, data in raw_sensor_data.items() if data > 0.0}

print(cleaned_data)


