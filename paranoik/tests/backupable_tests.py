#pylint: skip-file
import unittest

from paranoik.backup.backupable import Backupable


class BackupableTests(unittest.TestCase):
    def test_backup_method_raises_not_implemented(self):
        backupable = Backupable("Some resource")
        self.assertRaises(NotImplementedError, lambda: backupable.backup())

    def test_cleanup_method_raises_not_implemented_error(self):
        backupable = Backupable("Some resource")
        self.assertRaises(NotImplementedError, lambda: backupable.cleanup())

if __name__ == '__main__':
    unittest.main()