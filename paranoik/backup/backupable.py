class Backupable:
    def __init__(self, resource_name):
        self._resource_name = resource_name
        self._destination = None

    @property
    def destination(self):
        if self._destination is None:
            raise ValueError("Backup destination for {0} is not set.".format(
                self._resource_name
            ))
        return self._destination

    @destination.setter
    def destination(self, value):
        self._destination = value

    def backup(self):
        raise NotImplementedError("Backup method needs to be overwritten.")