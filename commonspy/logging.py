import datetime
import json
import logging
import socket
from threading import current_thread
from commonspy.http import __REQUEST_ID__
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


def log_info(message):
    logger.info(Message(message).__dict__)


def log_warning(message):
    logger.warn(Message(message).__dict__)


def log_error(message):
    logger.error(Message(message).__dict__)


def log_debug(message):
    logger.debug(Message(message).__dict__)


def change_log_location(new_location):
    global log_handler
    global logger
    log_handler = logging.StreamHandler(open(new_location, 'w+', encoding='utf-8'))
    formatter = jsonlogger.JsonFormatter()
    log_handler.setFormatter(formatter)
    log_handler.setLevel(logging.DEBUG)
    logger.addHandler(log_handler)


def build_message_from_exception_chain(e: Exception):
    """ Concats the messages of the exception chain into a single string

    Uses the pipe symbol ('|') for separating the messages.

    :param e: the exception to generate the message from
    :return: the concatenated message from the exception chain
    """
    exception = e
    message = str(exception)
    while (exception.__cause__):
        exception = exception.__cause__
        message = message + " | " + str(exception)
    return message