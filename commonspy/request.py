""" Module for communication between clients and the mongo db middleware. """
import requests
from commonspy.logging import log_error

error_http_codes = (400, 404, 500)


def exec_http_get(base_url, endpoint, content_id=None, page=0, size=10):
    """ Executes a http get request to the mongo middleware.

    """
    request_url = _build_request_url(base_url, content_id, endpoint, page, size)
    response = requests.get(request_url)
    if response.status_code in error_http_codes:
        log_error('Http request failed with status code %s.' % response.status_code)

    return response.json()['_embedded'][endpoint] if content_id is None else response.json()


def _build_request_url(base_url, content_id, endpoint, page, size):
    endpoint_url = '%s/%s' % (base_url, endpoint)
    if content_id is not None:
        endpoint_url = '%s/%s' % (endpoint_url, content_id)
    return '%s?page=%s&size=%s' % (endpoint_url, page, size)
