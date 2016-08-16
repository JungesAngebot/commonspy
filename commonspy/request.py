""" Module for communication between clients and the mongo db middleware. """
import requests


def exec_http_get(base_url, endpoint, content_id=None, page=0, size=10):
    request_url = _build_request_url(base_url, content_id, endpoint, page, size)
    response = requests.get(request_url)


def _build_request_url(base_url, content_id, endpoint, page, size):
    endpoint_url = '%s/%s' % (base_url, endpoint)
    if content_id is not None:
        endpoint_url = '%s/%s' % (endpoint_url, content_id)
    return '%s?page=%s&size=%s' % (endpoint_url, page, size)

