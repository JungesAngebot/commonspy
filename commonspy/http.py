import urllib.request


def download_file(url, desitination):
    urllib.request.urlretrieve(url, desitination)
