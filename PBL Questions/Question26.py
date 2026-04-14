class SensorFailureError(Exception):
    pass

try:
    raise SensorFailureError()
except SensorFailureError:
    print("Maintenance mode")
