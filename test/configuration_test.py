import unittest

from commonspy.configuration import IniConfig, JsonConfig, JsonBasedConfiguration, ConfigurationKeyNotFoundException


class IniConfigTest(unittest.TestCase):
    def test_get_property_no_such_section(self):
        config = IniConfig('test.ini')
        with self.assertRaises(Exception):
            config.get_property('Some', 'none')

    def test_get_property_key_does_not_exist(self):
        config = IniConfig('test.ini')
        with self.assertRaises(Exception):
            config.get_property('TestSection', 'none')

    def test_config_file_does_not_exist(self):
        with self.assertRaises(Exception):
            IniConfig('doesnotexist.ini')

    def test_get_property_key_section_exists(self):
        config = IniConfig('test.ini')
        result = config.get_property('TestSection', 'testproperty')

        self.assertEquals(result, 'test')


class JsonConfigTest(unittest.TestCase):
    def test_config_file_does_not_exist(self):
        with self.assertRaises(Exception):
            JsonConfig('doesnotexist.json')

    def test_config_single_key_does_not_exist(self):
        config = JsonConfig('config.json')
        with self.assertRaises(Exception):
            config.get_property('none')

    def test_config_single_key_exists(self):
        config = JsonConfig('config.json')
        result = config.get_property('simple')

        self.assertEqual(result, 'value')

    def test_config_keychain_with_non_existing_key(self):
        config = JsonConfig('config.json')
        with self.assertRaises(Exception):
            config.get_property('chain.property.key')

    def test_config_keychain_with_existing_keys(self):
        config = JsonConfig('config.json')
        result = config.get_property('chain.some.key')

        self.assertEquals(result, 'value')


class JsonBasedConfigurationTest(unittest.TestCase):
    def test_config_file_does_not_exist(self):
        with self.assertRaises(TypeError):
            JsonBasedConfiguration.create_from_file('none.json')

    def test_config_single_key_does_not_exist(self):
        config = JsonBasedConfiguration.create_from_file("config.json")
        with self.assertRaises(ConfigurationKeyNotFoundException):
            config.property('none')

    def test_config_single_key_exist(self):
        config = JsonBasedConfiguration.create_from_file('config.json')

        result = config.property('simple')

        self.assertEquals(result, 'value')

    def test_config_keychain_with_non_existing_key(self):
        config = JsonBasedConfiguration.create_from_file('config.json')

        with self.assertRaises(ConfigurationKeyNotFoundException):
            config.property('chain.property.key')

    def test_config_kechain_with_existing_key(self):
        config = JsonBasedConfiguration.create_from_file('config.json')

        result = config.property('chain.some.key')

        self.assertEquals(result, 'value')
