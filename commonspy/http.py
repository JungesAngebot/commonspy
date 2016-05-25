import urllib.request

"""
Module contains some commons http helper methods.
"""


def download_file(url, desitination): urllib.request.urlretrieve(url, desitination)
