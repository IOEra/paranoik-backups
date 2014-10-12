import unittest

from paranoik.backup.backupable import Backupable


class BackupableTests(unittest.TestCase):
    def test_backup_method_raises_not_implemented(self):
        backupable = Backupable("Some resource")
        self.assertRaises(NotImplementedError, lambda: backupable.backup())

if __name__ == '__main__':
    unittest.main()