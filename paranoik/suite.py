"""
Suites allow grouping of multiple backup providers.
"""


class BackupSuite:
    """
    Handles grouping of multiple backup providers.
    """
    def __init__(self, suite_name):
        """
        :param suite_name: Name of the suite
        :return:
        """
        self._suite_name = suite_name
        self._backupables = []

    def add_backupable(self, backupable):
        """
        Adds backupable object to the backup group.
        :param backupable: Backupable
        :return:
        """
        self._backupables.append(backupable)

    def _backup_backupables(self):
        """
        Performs backup on all backupable objects.
        :return:
        """
        for backupable in self._backupables:
            backupable.backup()

    def _cleanup_backupables(self):
        """
        Performs cleanup on all backupable objects.
        :return:
        """
        for backupable in self._backupables:
            backupable.cleanup()

    def run(self):
        """
        Runs the backup suite and performs backup on all backupable objects
        that have been provided. After the successful execution of the whole
        group, cleanup is performed.
        :return:
        """
        self._backup_backupables()
        self._cleanup_backupables()
