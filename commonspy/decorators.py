import functools

from flask import jsonify


def json(function):
    @functools.wraps(function)
    def wrapped(*args, **kwargs):
        rv = function(*args, **kwargs)
        return jsonify(rv)
    return wrapped
