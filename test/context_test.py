import unittest

from commonspy.context import ApplicationContext


class TestClass:
    pass


class Configuration:
    def test_class(self):
        """
        :name test_class
        :return:
        """
        return TestClass()


class ApplicationContextTest(unittest.TestCase):
    def test_get_instance(self):
        context = ApplicationContext()
        context.configuration = Configuration()
        result = context.get_instance('test_class')

        self.assertTrue(isinstance(result, TestClass))

    def test_get_cached_instance(self):
        context = ApplicationContext()
        context.configuration = Configuration()
        result_one = context.get_instance('test_class')
        result_two = context.get_instance('test_class')

        self.assertEquals(result_one, result_two)
