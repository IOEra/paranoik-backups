"""
Contains MySQL Backup Provider.
"""


import os

from paranoik.backup.backupable import Backupable
from paranoik.utils.command_executor import CommandExecutor


class MySQL(Backupable):
    """
    MySQL Backup Provider. Performs backup on a MySQL database.
    """

    _database = None
    _host = None
    _username = None
    _password = None

    @property
    def database(self):
        """
        Getter of the database name.
        :return:
        """
        if self._database is None:
            raise ValueError("Database is not set.")
        return self._database

    @database.setter
    def database(self, value):
        """
        Setter of the database name.
        :param value:
        :return:
        """
        self._database = value

    @property
    def host(self):
        """
        Getter of the host name.
        :return:
        """
        if self._host is None:
            return "localhost"
        return self._host

    @database.setter
    def host(self, value):
        """
        Setter of the host name.
        :param value:
        :return:
        """
        self._host = value


    @property
    def username(self):
        """
        Getter of the username.
        :return:
        """
        if self._username is None:
            raise ValueError("Username is not set.")
        return self._username

    @username.setter
    def username(self, username):
        """
        Setter of the username
        :param username:
        :return:
        """
        self._username = username

    @property
    def password(self):
        """
        Getter of the password.
        :return:
        """
        if self._password is None:
            raise ValueError("Password is not set.")
        return self._password

    @password.setter
    def password(self, value):
        """
        Setter of the password.
        :param value:
        :return:
        """
        self._password = value

    def backup(self):
        """
        Executes mysqldump and performs backup. The backup is stored in the
        destination file.
        :return:
        """
        with open(self.destination, 'w') as dump_file:
            command = [
                "mysqldump", "-u", self.username, "-p" + self.password,
                "-h", self.host, self.database
            ]
            executor = CommandExecutor(command, stdout=dump_file)
            executor.execute()

    def cleanup(self):
        """
        Removes the destination file.
        :return:
        """
        os.remove(self.destination)
