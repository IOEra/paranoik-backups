import shutil

from paranoik.backup.backupable import Backupable


class Directory(Backupable):
    _path = None

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    def backup(self):
        if self.path is None:
            raise DirectoryError("Directory path is not set.")
        shutil.copytree(self.path, self.destination)


class DirectoryError(Exception):
    pass