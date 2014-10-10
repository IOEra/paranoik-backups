import shutil

from paranoik.backup.backupable import Backupable


class Directory(Backupable):
    _path = None

    @property
    def path(self):
        if self._path is None:
            raise DirectoryError("Directory path is not set.")
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    def backup(self):
        shutil.copytree(self.path, self.destination)


class DirectoryError(Exception):
    pass