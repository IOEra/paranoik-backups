"""
Contains Directory Backup Provider.
"""

import shutil

from paranoik.backup.backupable import Backupable


class Directory(Backupable):
    """
    Backup provider to perform backups on directories.
    """

    _path = None

    @property
    def path(self):
        """
        Directory path getter.
        :return:
        """
        if self._path is None:
            raise DirectoryBackupError("Directory path is not set.")
        return self._path

    @path.setter
    def path(self, value):
        """
        Setter for the directory path.
        :param value:
        :return:
        """
        self._path = value

    def backup(self):
        """
        Performs backup operation and copies the directory to destination.
        :return:
        """
        shutil.copytree(self.path, self.destination)

    def cleanup(self):
        """
        Removes the destination folder.
        :return:
        """
        shutil.rmtree(self.destination)


class DirectoryBackupError(Exception):
    """
    Exception raised when something goes wrong during directory backup.
    """
    pass
