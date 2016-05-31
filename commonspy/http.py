import urllib.request
import uuid

"""
Module contains some commons http helper methods.
"""


def download_file(url, desitination): urllib.request.urlretrieve(url, desitination)


def request_uuid(): return str(uuid.uuid4())
