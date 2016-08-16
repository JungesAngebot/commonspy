""" Module for communication between clients and the mongo db middleware. """


def exec_http_get(base_url, endpoint, content_id=None, page=0, size=10):
    endpoint_url = '%s/%s' % (base_url, endpoint)
    if content_id is not None:
        endpoint_url = '%s/%s' % (endpoint_url, content_id)


