"""
This module works as a wrapper around ConfigParser, making it easier for the
developer to read options from different configuration files.
"""

import os
from configparser import ConfigParser
from paranoik.utils.singleton import Singleton
from paranoik import PARANOIK_MODULE_DIR

CONFIG_FILES = (
    os.path.join(PARANOIK_MODULE_DIR, "paranoik.conf"),
    '/etc/paranoik.conf',
    os.path.expanduser('~/.paranoik.conf'),
)


@Singleton
class ConfigReader:
    """
    Singleton class for reading configuration Paranoik files. Configuration
    is read from the multiple configuration files.
    """
    def __init__(self):
        self._config = ConfigParser()
        self._config.read(CONFIG_FILES)

    def read(self, section, option, data_type=None):
        """
        Retrieves information from the
        :param section: section from which to read
        :param option: option to read
        :return: value of the setting
        """
        getters = {
            None: self._config.get,
            bool: self._config.getboolean
        }
        return getters[data_type](section, option)
