#pylint: skip-file

import unittest

from paranoik.suite import BackupSuite
from paranoik.backup.backupable import Backupable


class DummyBackupable(Backupable):

    def __init__(self, *args, **kwargs):
        Backupable.__init__(self, *args, **kwargs)
        self.backup_called = False
        self.cleanup_called = False

    def backup(self):
        self.backup_called = True

    def cleanup(self):
        self.cleanup_called = True


class SuiteTests(unittest.TestCase):
    def test_suite_grouping(self):
        first_backupable = DummyBackupable("First backupable")
        second_backupable = DummyBackupable("Second backupable")

        suite = BackupSuite("Backup of Issue Tracker")
        suite.add_backupable(first_backupable)
        suite.add_backupable(second_backupable)
        suite.run()

        self.assertTrue(first_backupable.backup_called)
        self.assertTrue(first_backupable.cleanup_called)
        self.assertTrue(second_backupable.backup_called)
        self.assertTrue(second_backupable.cleanup_called)

if __name__ == "__main__":
    unittest.main()