import os

from paranoik.backup.backupable import Backupable
from paranoik.utils.command_executor import CommandExecutor


class MySQL(Backupable):
    _database = None
    _username = None
    _password = None

    @property
    def database(self):
        if self._database is None:
            raise ValueError("Database is not set.")
        return self._database

    @database.setter
    def database(self, value):
        self._database = value

    @property
    def username(self):
        if self._username is None:
            raise ValueError("Username is not set.")
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        if self._password is None:
            raise ValueError("Password is not set.")
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    def backup(self):
        with open(self.destination, 'w') as dump_file:
            command = ["mysqldump", "-u", self.username, "-p" + self.password,
                       self.database]
            CommandExecutor.execute(command, stdout=dump_file)

    def cleanup(self):
        os.remove(self.destination)