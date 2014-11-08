#pylint: skip-file
import unittest
import mock

from paranoik.utils.compatibility import BUILTIN
from paranoik.backup.providers.mysql import MySQL
from paranoik.backup.backupable import Backupable


class MySQLTests(unittest.TestCase):
    def test_database_is_backupable(self):
        database = MySQL("Some database")
        self.assertTrue(isinstance(database, Backupable))

    def test_required_fields_not_set(self):
        database = MySQL("Some database")
        required_fields = ("database", "username", "password")
        for field in required_fields:
            self.assertRaises(ValueError, lambda: getattr(database, field))

    def test_required_fields_set(self):
        database = MySQL("Some database")
        database.database = "test_database"
        self.assertEquals(database.database, "test_database")

        database.username = "test_username"
        self.assertEquals(database.username, "test_username")

        database.password = "test_password"
        self.assertEquals(database.password, "test_password")

    @mock.patch("paranoik.utils.command_executor.CommandExecutor")
    @mock.patch("{0}.open".format(BUILTIN))
    @mock.patch("os.remove")
    def test_mysql_backup(self, remove, open, command_executor):
        database = MySQL("Some database")
        database.database = "test_database"
        database.username = "test_username"
        database.password = "test_password"
        database.destination = "/file/path.sql"

        self.assertFalse(open.called)
        database.backup()
        self.assertTrue(open.called)

        self.assertFalse(remove.called)
        database.cleanup()
        self.assertTrue(remove.called)
