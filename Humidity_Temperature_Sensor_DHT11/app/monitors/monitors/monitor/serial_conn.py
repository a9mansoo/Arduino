import time
from threading import Thread
from serial import Serial, SerialException
from queue import Queue



class SerialConnection(Thread):
    int_max_buffer = 1024
    msg_size = 1024


    def __init__(self, serial_dev, baud_rate=9600, timeout=2):
        super().__init__()
        self.daemon = True
        self.msg_queue = Queue()
        self.serial_dev = serial_dev
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.conn = None
        self.isConnected = False
        self.start()

    def connect(self):
        if self.conn is not None:
            return False
        try:
            self.conn = Serial(self.serial_dev, self.baud_rate, timeout=self.timeout)
            self.isConnected = True
        except (ValueError, SerialException):
            self.conn = None
            return False

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()
            self.isConnected = False

    def run(self):
        buffer = ""
        while True:
            if self.conn is None:
                time.sleep(2)
                continue
            try:
                read_data = self.conn.read(self.msg_size).decode().strip()
                print(f"Serial Output Read: {read_data}")
                buffer += read_data
                if buffer.endswith("}") and buffer.startswith("{"):
                    data = buffer
                    self.msg_queue.put(data)
                    buffer = ""
                if len(buffer) > self.int_max_buffer:
                    buffer = ""
            except Exception as e:
                pass
            time.sleep(10)
