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
        self.callback = None
        self.start()

    def start_conn(self):
        bol_connected = self.obj_conn.connect()
        if not bol_connected:
            return False
        return True
    
    def register_log_callback(self, fnc_callable):
        if self.callback is None:
            self.callback = fnc_callable

    def run(self):
        while True:
            if self.obj_conn.isConnected and not self.obj_conn.msg_queue.empty():
                try:
                    obj_data = self.obj_conn.msg_queue.get()
                    if self.callback is not None:
                        self.callback(obj_data)
                except Exception as e:
                    pass
            time.sleep(0.1)
