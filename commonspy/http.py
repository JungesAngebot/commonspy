import urllib.request
import uuid
from abc import ABCMeta, abstractmethod

from flask.views import MethodView

"""
Module contains some commons http helper methods.
"""


def download_file(url, desitination): urllib.request.urlretrieve(url, desitination)


def request_uuid(): return str(uuid.uuid4())


__REQUEST_ID__ = None


class RequestHandler(MethodView):
    """
    This is a bsic request handler that sets a uuid for the current request. This uuid is used to
    trace the request calles in a microservice environment.
    """
    __metaclass__ = ABCMeta

    def _prepare_request(self):
        """
        Prepares the request.
        :return:
        """
        global __REQUEST_ID__
        __REQUEST_ID__ = str(uuid.uuid4())

    def _sortable(self, request):
        if 'sort_key' in request.args:
            self.sort_key = request.args.get('sort_key')
        if 'sort_order' in request.args:
            self.sort_order = request.args.get('sort_order')

    @abstractmethod
    def get(self, *args):
        self._prepare_request()

    @abstractmethod
    def post(self, *args):
        self._prepare_request()

    @abstractmethod
    def put(self, *args):
        self._prepare_request()

    @abstractmethod
    def delete(self, *args):
        self._prepare_request()
