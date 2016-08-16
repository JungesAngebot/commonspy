import urllib.request
import uuid
from abc import ABCMeta

from commonspy.decorators import deprecated
from flask.views import MethodView

"""
Module contains some commons http helper methods.
"""


def download_file(url, desitination): urllib.request.urlretrieve(url, desitination)


def request_uuid(): return str(uuid.uuid4())


__REQUEST_ID__ = None


@deprecated
class RequestHandler(MethodView):
    """
    This is a bsic request handler that sets a uuid for the current request. This uuid is used to
    trace the request calles in a microservice environment. This request handler should only be used
    in combination with the flask microframework.
    """
    __metaclass__ = ABCMeta

    def _prepare_request(self):
        """
        Prepares the request.
        :return:
        """
        global __REQUEST_ID__
        __REQUEST_ID__ = str(uuid.uuid4())
        from commonspy.logging import logger
        from commonspy.logging import Message
        logger.info(Message('Executing get request ...').__dict__)
        self._sortable()

    def _sortable(self):
        from flask import request
        self.sort_key = request.args.get('sort_key') if 'sort_key' in request.args else 'id'
        self.sort_order = request.args.get('sort_order') if 'sort_order' in request.args else 'desc'

    def get(self, *args):
        self._prepare_request()

    def post(self, *args):
        self._prepare_request()

    def put(self, *args):
        self._prepare_request()

    def delete(self, *args):
        self._prepare_request()
