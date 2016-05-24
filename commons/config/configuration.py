import configparser
import os


class ConfigUtils:
    def __init__(self, configfile):
        if not os.path.isfile(configfile):
            raise Exception('The file {} does not exist!'.format(configfile))
        self.parser = configparser.ConfigParser()
        self.parser.read(configfile)

    def get_property(self, key):
        pass
