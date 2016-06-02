from abc import ABCMeta
from concurrent import futures

from tornado.web import RequestHandler


class AsyncRequestHandler(RequestHandler, metaclass=ABCMeta):

    def _async_func_exec(self, func, *args, **kwargs):
        e = futures.ThreadPoolExecutor(max_workers=3)
        e.submit(func, args, kwargs)
