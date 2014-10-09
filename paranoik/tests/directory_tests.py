import os
import unittest
import shutil

from paranoik.backup.providers.directory import Directory, DirectoryError
from paranoik.backup.backupable import Backupable


class DirectoryTests(unittest.TestCase):
    def test_directory_is_backupable(self):
        directory = Directory("Some important directory")
        self.assertIsInstance(directory, Backupable)

    def test_perform_backup(self):
        os.mkdir("/tmp/dummy_test_backup_dir")
        directory = Directory("Directory with images")
        directory.path = "/tmp/dummy_test_backup_dir"
        directory.destination = "/tmp/dummy_test_backup_dir_backup"
        directory.backup()
        self.assertTrue(os.path.exists("/tmp/dummy_test_backup_dir_backup"))
        os.rmdir("/tmp/dummy_test_backup_dir")
        os.rmdir("/tmp/dummy_test_backup_dir_backup")
        self.assertFalse(os.path.exists("/tmp/dummy_test_backup_dir_backup"))

    def test_backup_without_path_set(self):
        directory = Directory("Some random directory")
        self.assertRaises(DirectoryError, lambda: directory.backup())

    def test_backup_without_destination(self):
        directory = Directory("Directory with images")
        directory.path = "/tmp"
        self.assertRaises(ValueError, lambda: directory.backup())

if __name__ == '__main__':
    unittest.main()