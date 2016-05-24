import configparser
import json
import os


class IniConfig:
    def __init__(self, configfile):
        if not os.path.isfile(configfile):
            raise Exception('The file {} does not exist!'.format(configfile))
        self.parser = configparser.ConfigParser()
        self.parser.read(configfile)

    def get_property(self, section, key):
        if section not in self.parser:
            raise Exception('Section {} does not exist in config file!'.format(section))
        if key not in self.parser[section]:
            raise Exception('Key {} is not in section {}!'.format(key, section))
        return self.parser[section][key]


class JsonConfig:
    def __init__(self, configfile):
        if not os.path.isfile(configfile):
            raise Exception('The file {} does not exist!'.format(configfile))
        with open(configfile) as file:
            self.json = json.load(file)

    def get_property(self, key):
        keys = key.split('.')
        json_tmp = self.json
        for inner_key in keys:
            if inner_key in json_tmp:
                json_tmp = json_tmp[inner_key]
            else:
                raise Exception('Key {} does not exist!'.format(inner_key))
        return json_tmp
