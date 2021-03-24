from Constant import PARAM_MAX_DELTAS, STATUS_CODES


def is_there_a_spike(sensor_reading, next_sensor_reading, max_delta):
    if next_sensor_reading - sensor_reading > max_delta:
        return True
    return False


def detect_spike_in_sensor_stream(param_name, sensor_stream):
    max_delta = PARAM_MAX_DELTAS[param_name]
    for index, sensor_reading in enumerate(sensor_stream[:-1]):
        next_sensor_reading = sensor_stream[index + 1]
        if is_there_a_spike(sensor_reading, next_sensor_reading, max_delta):
            return STATUS_CODES["500"]
    return STATUS_CODES["200"]


def validate_sensor_stream(param_name, sensor_stream):
    if sensor_stream is None:
        return STATUS_CODES["400"]
    if param_name not in PARAM_MAX_DELTAS:
        return STATUS_CODES["404"]
    return detect_spike_in_sensor_stream(param_name, sensor_stream)
