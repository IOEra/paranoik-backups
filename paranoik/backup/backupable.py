"""
Contains the interface used by backup providers.
"""


class Backupable:
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
                self._resource_name
            ))
        return self._destination

    @destination.setter
    def destination(self, value):
        """
        Setter method of the destination property.
        :param value:
        :return:
        """
        self._destination = value

    def backup(self):
        """
        Procedure that needs to be overwritten by backup providers. Defines
        the way specific backup operation is performed.
        :return:
        """
        raise NotImplementedError("Backup method needs to be overwritten.")

    def cleanup(self):
        """
        Removes unneeded artifacts that have been created during backup.
        :return:
        """
        raise NotImplementedError("Cleanup method needs to be overwritten.")