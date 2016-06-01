import inspect

from commonspy.logging import logger, Message


class ApplicationContext:
    def __init__(self):
        self.configuration = None

    def get_instance(self, qualifier):
        result = inspect.getmembers(self.configuration, predicate=inspect.ismethod)
        for method in result:
            logger.debug(Message(method).__dict__)
            func = getattr(self.configuration, method[0])
            if qualifier in func.__doc__:
                return func()
        return None

    def set_configuration(self, configuration):
        self.configuration = configuration()
