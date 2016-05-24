import unittest

from commons.config.configuration import Config


class ConfigUtilsTest(unittest.TestCase):
    def test_get_property_no_such_section(self):
        config = Config('test.ini')
        with self.assertRaises(Exception):
            config.get_property('Some', 'none')

    def test_get_property_key_does_not_exist(self):
        config = Config('test.ini')
        with self.assertRaises(Exception):
            config.get_property('TestSection', 'none')

    def test_config_file_does_not_exist(self):
        with self.assertRaises(Exception):
            Config('doesnotexist.ini')

    def test_get_property_key_section_exists(self):
        config = Config('test.ini')
        result = config.get_property('TestSection', 'testproperty')

        self.assertEquals(result, 'test')
