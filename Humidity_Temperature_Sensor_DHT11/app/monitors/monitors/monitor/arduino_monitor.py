import time
from threading import Thread
from .serial_conn import SerialConnection


class ArduinoMonitor(Thread):
    retry_delay = 2


    def __init__(self):
        super().__init__(daemon=True)
        self.serial_dev = "/dev/arduino"
        self.baud_rate = 9600
        self.timeout = 2
        self.obj_conn = SerialConnection(self.serial_dev, self.baud_rate, self.timeout)
        self.LastResponse = ""
        self.start()

    def start_conn(self):
        bol_connected = self.obj_conn.connect()
        if not bol_connected:
            return False
        return True

    def run(self):
        while True:
            self.LastResponse = ""
            if self.obj_conn.isConnected and not self.obj_conn.msg_queue.empty():
                try:
                    obj_data = self.obj_conn.msg_queue.get()
                    self.LastResponse = obj_data
                except Exception as e:
                    self.LastResponse = ""
            time.sleep(0.1)
