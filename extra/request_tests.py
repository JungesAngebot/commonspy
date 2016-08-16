from pprint import pprint

from requests.auth import HTTPBasicAuth

from commonspy.request import exec_http_get

json = exec_http_get('http://localhost:8080/read', 'stories', auth=HTTPBasicAuth('juan', 'juanHackt'))

pprint(json)
