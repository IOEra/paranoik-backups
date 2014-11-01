"""
Contains Tar Compressor.
"""

import os
import tarfile


class TarCompressor:
    """
    Compressor that allows to easily add files to an archive.
    """

    def __init__(self, file_path):
        """
        Constructor of the Tar compressor.
        :param file_path: Location of the compressed archive.
        :return:
        """
        self._file_path = file_path
        self._file = tarfile.open(self._file_path, "w:gz")

    def add(self, directory_path):
        """
        Add directory to the archive.
        :param directory_path: Path to the directory
        :return:
        """
        archive_name = os.path.basename(directory_path)
        self._file.add(directory_path, arcname=archive_name)

    def close(self):
        """
        Closes the archive after everything has been added.
        :return:
        """
        self._file.close()
