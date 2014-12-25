from abc import ABCMeta, abstractmethod
from six import add_metaclass

from paranoik.config.config_reader import ConfigReader


@add_metaclass(ABCMeta)
class NotificationBase(object):
    def __init__(self, title, message):
        self._config = ConfigReader.get_instance()
        self._title = title
        self._message = message

    @abstractmethod
    def send(self):
        pass