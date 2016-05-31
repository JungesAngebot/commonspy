import datetime
import json
import socket
from threading import current_thread


class Message:

    level = {
        '10': 'Debug',
        '20': 'Info',
        '30': 'Warining',
        '40': 'Error'
    }

    def __init__(self, message, level):
        self.timestamp = str(datetime.datetime.now())
        self.message = message
        self.level = level
        self.hostname = socket.getfqdn()
        self.thread_name = current_thread().getName()

    def __str__(self):
        return json.dumps(self.__dict__)
