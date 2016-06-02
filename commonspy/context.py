import inspect

from commonspy.logging import logger, Message


class ApplicationContext:
    def __init__(self):
        self.configuration = None
        self.inst_cache = dict()

    def get_instance(self, qualifier):
        if qualifier in self.inst_cache: return self.inst_cache[qualifier]
        result = inspect.getmembers(self.configuration, predicate=inspect.ismethod)
        for method in result:
            logger.debug(Message(method).__dict__)
            func = getattr(self.configuration, method[0])
            if qualifier in func.__doc__:
                instance = func()
                self.inst_cache[qualifier] = instance
                return instance
        return None

    def set_configuration(self, configuration):
        self.configuration = configuration()
