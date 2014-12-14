"""
This module works as a wrapper around ConfigParser, making it easier for the
developer to read options from different configuration files.
"""

import os
from configparser import ConfigParser
from paranoik.utils.singleton import Singleton

CONFIG_FILES = (
    '/etc/paranoik.conf',
    os.path.expanduser('~/.paranoik.conf')
)


@Singleton
class ConfigReader:
    """
    Singleton class for reading configuration Paranoik files.
    """
    def __init__(self):
        self._config = ConfigParser()
        self._config.read(CONFIG_FILES)

    def read(self, section, option):
        """
        Retrieves information from the
        :param section: section from which to read
        :param option: option to read
        :return: value of the setting
        """
        return self._config.get(section, option)