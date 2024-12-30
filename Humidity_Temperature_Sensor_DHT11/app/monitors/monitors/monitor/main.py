import logging
import time
from .arduino_monitor import ArduinoMonitor

arduino = ArduinoMonitor()
str_filename = "/sensor/sensor_data.log"

rootLogger = logging.getLogger(__name__)
rootLogger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(str_filename, mode="w")
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
file_handler.setFormatter(formatter)
rootLogger.addHandler(file_handler)

def retry_connection(int_attempts=10):
    global arduino
    bol_connected = False
    if arduino.obj_conn.isConnected:
        return True
    for _ in range(int_attempts):
        if not bol_connected:
            time.sleep(5)
        else:
            bol_connected = True
            break
        bol_connected = arduino.start_conn()
    return bol_connected


def log_data(obj_log):
    print(f"Logging Data: {obj_log}")
    rootLogger.info(obj_log)
    file_handler.flush()


def main():
    arduino.register_log_callback(log_data)
    arduino.start_conn()
    while True:
        if not retry_connection():
            time.sleep(30)
        time.sleep(1)