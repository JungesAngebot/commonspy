from pprint import pprint

from requests.auth import HTTPBasicAuth

from commonspy.request import request_content

json = request_content('http://localhost:8080/read', 'stories', auth=HTTPBasicAuth('juan', 'juanHackt'))

pprint(json)
