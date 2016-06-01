import datetime
import json
import logging
import socket
import uuid
from abc import ABCMeta
from threading import current_thread

from pythonjsonlogger import jsonlogger

logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)


log_handler = logging.StreamHandler(open('api.log.json', 'w+', encoding='utf-8'))
formatter = jsonlogger.JsonFormatter()
log_handler.setFormatter(formatter)
log_handler.setLevel(logging.DEBUG)
logger.addHandler(log_handler)

__REQUEST_ID__ = None


class RequestHandler:

    __metaclass__ = ABCMeta

    def _prepare_request(self):
        global __REQUEST_ID__
        __REQUEST_ID__ = str(uuid.uuid4())


class Message:

    level = {
        '10': 'Debug',
        '20': 'Info',
        '30': 'Warining',
        '40': 'Error'
    }

    def __init__(self, message):
        self.timestamp = str(datetime.datetime.now())
        self.message = message
        self.level = self._logging_level()
        self.hostname = socket.getfqdn()
        self.thread_name = current_thread().getName()
        self.request_id = __REQUEST_ID__

    def _logging_level(self):
        return Message.level[str(logger.level)]

    def __str__(self):
        return json.dumps(self.__dict__)
