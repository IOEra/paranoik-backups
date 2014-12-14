"""
Contains the interface used by backup providers.
"""

from abc import ABCMeta, abstractmethod
from six import add_metaclass


@add_metaclass(ABCMeta)
class Backupable(object):
    """
    Interface for all items that can be backed up.
    """

    def __init__(self, resource_name):
        """
        When constructed each backupable item needs to provide name of the
        resource, which is being backed up. The resource name could be used
        later for pretty printing the name.
        :param resource_name:
        :return:
        """
        self._resource_name = resource_name
        self._destination = None

    @property
    def destination(self):
        """
        Destination property is the location where the data dump is going to
        be stored after the backup method is invoked. In most cases this is
        the output location of the dump.
        :return:
        """
        if self._destination is None:
            raise ValueError("Backup destination for {0} is not set.".format(
                self._resource_name))
        return self._destination

    @destination.setter
    def destination(self, value):
        """
        Setter method of the destination property.
        :param value:
        :return:
        """
        self._destination = value

    @abstractmethod
    def backup(self):
        """
        Procedure that needs to be overwritten by backup providers. Defines
        the way specific backup operation is performed.
        :return:
        """
        pass

    @abstractmethod
    def cleanup(self):
        """
        Removes unneeded artifacts that have been created during backup.
        :return:
        """
        pass
