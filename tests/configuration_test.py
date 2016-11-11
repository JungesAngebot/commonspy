import os
import unittest

from commonspy.configuration import IniConfig, JsonConfig, JsonBasedConfiguration, ConfigurationKeyNotFoundException, YamlConfiguration
from tests import TEST_ROOT


class IniConfigTest(unittest.TestCase):
    def test_get_property_no_such_section(self):
        config = IniConfig('%s/test.ini' % TEST_ROOT)
        with self.assertRaises(Exception):
            config.get_property('Some', 'none')

    def test_get_property_key_does_not_exist(self):
        config = IniConfig('%s/test.ini' % TEST_ROOT)
        with self.assertRaises(Exception):
            config.get_property('TestSection', 'none')

    def test_config_file_does_not_exist(self):
        with self.assertRaises(Exception):
            IniConfig('doesnotexist.ini')

    def test_get_property_key_section_exists(self):
        config = IniConfig('%s/test.ini' % TEST_ROOT)
        result = config.get_property('TestSection', 'testproperty')

        self.assertEquals(result, 'test')


class JsonConfigTest(unittest.TestCase):
    def test_config_file_does_not_exist(self):
        with self.assertRaises(Exception):
            JsonConfig('doesnotexist.json')

    def test_config_single_key_does_not_exist(self):
        config = JsonConfig('%s/config.json' % TEST_ROOT)
        with self.assertRaises(Exception):
            config.get_property('none')

    def test_config_single_key_exists(self):
        config = JsonConfig('%s/config.json' % TEST_ROOT)
        result = config.get_property('simple')

        self.assertEqual(result, 'value')

    def test_config_keychain_with_non_existing_key(self):
        config = JsonConfig('%s/config.json' % TEST_ROOT)
        with self.assertRaises(Exception):
            config.get_property('chain.property.key')

    def test_config_keychain_with_existing_keys(self):
        config = JsonConfig('%s/config.json' % TEST_ROOT)
        result = config.get_property('chain.some.key')

        self.assertEquals(result, 'value')


class JsonBasedConfigurationTest(unittest.TestCase):
    def test_config_file_does_not_exist(self):
        with self.assertRaises(TypeError):
            JsonBasedConfiguration.create_from_file('none.json')

    def test_config_single_key_does_not_exist(self):
        config = JsonBasedConfiguration.create_from_file('%s/config.json' % TEST_ROOT)
        with self.assertRaises(ConfigurationKeyNotFoundException):
            config.property('none')

    def test_config_single_key_exist(self):
        config = JsonBasedConfiguration.create_from_file('%s/config.json' % TEST_ROOT)

        result = config.property('simple')

        self.assertEquals(result, 'value')

    def test_config_keychain_with_non_existing_key(self):
        config = JsonBasedConfiguration.create_from_file('%s/config.json' % TEST_ROOT)

        with self.assertRaises(ConfigurationKeyNotFoundException):
            config.property('chain.property.key')

    def test_config_kechain_with_existing_key(self):
        config = JsonBasedConfiguration.create_from_file('%s/config.json' % TEST_ROOT)

        result = config.property('chain.some.key')

        self.assertEquals(result, 'value')


class YamlConfigurationTest(unittest.TestCase):
    def test_top_level_property(self):
        config = YamlConfiguration.create_from_file('%s/config.yml' % TEST_ROOT)

        result = config.property('top_level')

        self.assertEqual(result, 'value')

    def test_second_level_property(self):
        config = YamlConfiguration.create_from_file('%s/config.yml' % TEST_ROOT)

        result = config.property('nested.property')

        self.assertEqual(result, 'value')

    def test_property_does_not_exist(self):
        config = YamlConfiguration.create_from_file('%s/config.yml' % TEST_ROOT)

        result = config.property('not.nothing')

        self.assertEquals(result, None)

    def test_overwrite_property_in_env(self):
        os.environ['test'] = 'value'

        config = YamlConfiguration.create_from_file('%s/config.yml' % TEST_ROOT)

        result = config.property('test')

        self.assertEquals(result, 'value')
