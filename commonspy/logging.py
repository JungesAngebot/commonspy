import datetime
import json
import logging
import socket
from threading import current_thread

from pythonjsonlogger import jsonlogger

logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)


log_handler = logging.StreamHandler(open('api.log.json', 'w+', encoding='utf-8'))
formatter = jsonlogger.JsonFormatter()
log_handler.setFormatter(formatter)
log_handler.setLevel(logging.DEBUG)
logger.addHandler(log_handler)


class Message:

    level = {
        '10': 'Debug',
        '20': 'Info',
        '30': 'Warining',
        '40': 'Error'
    }

    def __init__(self, message, *args, **kwargs):
        self.timestamp = str(datetime.datetime.now())
        self.message = message
        self.level = self._logging_level()
        self.hostname = socket.getfqdn()
        self.thread_name = current_thread().getName()
        self.request_id = kwargs.pop('request_id', None)

    def _logging_level(self):
        return Message.level[str(logger.level)]

    def __str__(self):
        return json.dumps(self.__dict__)
