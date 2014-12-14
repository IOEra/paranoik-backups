#pylint: skip-file
import unittest

from paranoik.backup.backupable import Backupable


class BackupableTests(unittest.TestCase):
    def test_backupable_raises_type_error(self):
        self.assertRaises(TypeError, lambda: Backupable("Some resource"))


if __name__ == '__main__':
    unittest.main()