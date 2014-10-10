import os
import tarfile


class Tar:
    def __init__(self, file_path):
        self._file_path = file_path
        self._file = tarfile.open(self._file_path, "w:gz")

    def add(self, directory_path):
        archive_name = os.path.basename(directory_path)
        self._file.add(directory_path, arcname=archive_name)

    def close(self):
        self._file.close()