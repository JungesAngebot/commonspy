import configparser
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
