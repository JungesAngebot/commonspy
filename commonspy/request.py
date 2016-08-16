""" Module for communication between clients and the mongo db middleware. """
import requests

error_http_codes = (400, 404, 500)


def exec_http_get(base_url, endpoint, content_id=None, page=0, size=10, auth=None):
    """ Executes a http get request to the mongo middleware.

    Based on the content id the url will be build and used for the actual http get request.
    If the content id is None, a collection is requested so, it's required to access the
    _embedded property of the response. Otherwise the content will be o the root
    level of the json.

    Depending on the auth parameter, the request will use authentication or not. By
    default no authentication will be used. To use e.g. Http Basic Auth:

    exec_http_get('http://localhost:8080/read', 'stories', auth=HTTPBasicAuth('username', 'password'))

    The requesting works with paging. So by default the function will always request the first page
    with 10 documents. This behaviour can be modified by setting the page and size parameters on
    function call.

    :param: base_url: is the root url of the service without dynamic parts or direct endpoints
    :param: endpoint: specifies the endpoint to access (e.g. stories, assets etc.)
    :param: content_id: if specified it will be appended to the request url to retrieve a single resource
    :param: page: specifies which page to access. Default is 0 so the first page
    :param: size: specifies how many documents should be returned. Default is 10
    :param: auth: specifies authentication details. If None no authentication will be used.
    """
    request_url = _build_request_url(base_url, content_id, endpoint, page, size)
    response = requests.get(request_url, auth=auth) if auth is not None else requests.get(request_url)
    if response.status_code in error_http_codes:
        pass
    return response.json()['_embedded'][endpoint] if content_id is None else response.json()


def _build_request_url(base_url, content_id, endpoint, page, size):
    endpoint_url = '%s/%s' % (base_url, endpoint)
    if content_id is not None:
        endpoint_url = '%s/%s' % (endpoint_url, content_id)
    return '%s?page=%s&size=%s' % (endpoint_url, page, size)
