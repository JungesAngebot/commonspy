import functools
import warnings

from commonspy.logging import log_debug
from flask import jsonify


def traced_call(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        log_debug('Call %s ... with args %s and kwargs %s.' % (func.__name__, args, kwargs))
        return func(*args, **kwargs)
    return wrapped


def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emmitted
    when the function is used."""

    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warnings.simplefilter('always', DeprecationWarning)
        warnings.warn("Call to deprecated function {}.".format(func.__name__), category=DeprecationWarning, stacklevel=2)
        warnings.simplefilter('default', DeprecationWarning)
        return func(*args, **kwargs)

    return new_func


def json(function):
    @functools.wraps(function)
    def wrapped(*args, **kwargs):
        rv = function(*args, **kwargs)
        return jsonify(rv)
    return wrapped
