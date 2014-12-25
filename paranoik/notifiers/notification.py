from abc import ABCMeta, abstractmethod
from six import add_metaclass

from paranoik.config.config_reader import ConfigReader


@add_metaclass(ABCMeta)
class NotificationBase(object):
    def __init__(self):
        self._config = ConfigReader.get_instance()

    @abstractmethod
    def send(self):
        pass