import configparser
import json
import os

from commonspy.decorators import deprecated

"""
This module provides classes for accessing different configuration formats / files.
"""


@deprecated
class IniConfig:
    """
    This commonspy class helps you to get properties out of an ini file.
    Validation if part of this config class.
    """
    def __init__(self, configfile):
        """
        Create an instance of the config class with a config file. The constructor will
        validate if the specified file exists. If not it will raise an exception.
        Otherwise the configuration file (ini) will be parsed for later access.

        :param configfile: ini file to parse
        """
        if not os.path.isfile(configfile):
            raise Exception('The file {} does not exist!'.format(configfile))
        self.parser = configparser.ConfigParser()
        self.parser.read(configfile)

    def get_property(self, section, key):
        """
        Checks if the specified section exists in the configuration file and checks also if the specified
        key exists in the configuration. If one of the two conditions is not met the method will
        raise an exception. Otherwise the value of the property will be returned.

        :param section: config section in the ini file
        :param key: key in the specified config section
        :return: value of the config key
        """
        if section not in self.parser:
            raise Exception('Section {} does not exist in config file!'.format(section))
        if key not in self.parser[section]:
            raise Exception('Key {} is not in section {}!'.format(key, section))
        return self.parser[section][key]


@deprecated
class JsonConfig:
    """
    This class handles json based configuration. It parses a given json file for
    accessing different values in it.
    """
    def __init__(self, configfile):
        """
        The constructor of the json config will validate if the specified file exists. If not it
        will raise an exception. Otherwise the configuration will be read and parsed for
        later processing / value retrieval.

        :param configfile: json file to load
        """
        if not os.path.isfile(configfile):
            raise Exception('The file {} does not exist!'.format(configfile))
        with open(configfile) as file:
            self.json = json.load(file)

    def get_property(self, key):
        """
        This method provides you access to the configuration file. You can access a value by specifying the
        correct json key. You can also chain the keys:
        {
          "simple": "value",
          "chain": {
            "some": {
              "key": "value"
            }
          }
        }
        If you want to access the inner "key": "value" property just provide a key like: chain.some.key.
        :param key: key or key chain to access values
        :return: value of the specified key or key chain
        """
        keys = key.split('.')
        json_tmp = self.json
        for inner_key in keys:
            if inner_key in json_tmp:
                json_tmp = json_tmp[inner_key]
            else:
                raise Exception('Key {} does not exist!'.format(inner_key))
        return json_tmp



