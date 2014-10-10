import unittest

from paranoik.backup.providers.mysql import MySQL
from paranoik.backup.backupable import Backupable


class DirectoryTests(unittest.TestCase):
    def test_database_is_backupable(self):
        database = MySQL("Some database")
        self.assertIsInstance(database, Backupable)