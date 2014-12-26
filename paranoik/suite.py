"""
Suites allow grouping of multiple backup providers.
"""

from paranoik.notifiers.broadcaster import NotificationBroadcaster
from paranoik.config.config_reader import ConfigReader


class BackupSuite:
    """
    Handles grouping of multiple backup providers.
    """
    def __init__(self, suite_name):
        """
        :param suite_name: Name of the suite
        :return:
        """
        self._config = ConfigReader.get_instance()
        self._suite_name = suite_name
        self._backupables = []

    def add_backupable(self, backupable):
        """
        Adds backupable object to the backup group.
        :param backupable: Backupable
        :return:
        """
        self._backupables.append(backupable)

    def add_backupables(self, backupables):
        self._backupables += backupables

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

    def _notify(self, success=False, error=None):
        """
        :return:
        """
        if success:
            title = "Successful Paranoik Backup"
            message = "Your Paranoik Backup was successfully executed."
        else:
            import traceback
            error = traceback.format_exc()
            title = "Failed Paranoik Backup"
            message = "Your Paranoik Backup failed: {0}".format(error)
        broadcaster = NotificationBroadcaster()
        broadcaster.broadcast(title, message)

    def run(self):
        """
        Runs the backup suite and performs backup on all backupable objects
        that have been provided. After the successful execution of the whole
        group, cleanup is performed.
        :return:
        """
        notify = self._config.read("notifiers", "notify", data_type=bool)
        try:
            self._backup_backupables()
            self._cleanup_backupables()
            if notify:
                self._notify(success=True)
        except Exception:
            if notify:
                self._notify(success=False)
