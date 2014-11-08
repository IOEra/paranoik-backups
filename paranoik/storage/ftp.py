"""
Contains FTP Storage Provider.
"""

import os
import ftplib


class FTP:
    """
    Provide FTP Storage Interface.
    """

    def __init__(self, host, username, password):
        """
        Initializes FTP Connection.
        :param host: FTP Host
        :param username: FTP Username
        :param password: FTP Password
        :return:
        """
        self._host = host
        self._username = username
        self._password = password
        self._session = ftplib.FTP(self._host, self._username, self._password)

    def add_file(self, file_path):
        """
        Uploads file to FTP Server
        :param file_path: File to be uploaded
        :return:
        """
        with open(file_path, 'rb') as local_file:
            file_name = os.path.basename(local_file.name)
            self._session.storbinary('STOR {0}'.format(file_name), local_file)

    def close(self):
        """
        Closes the FTP Session.
        """
        self._session.quit()
