"""
Contains Amazon S3 Storage Provider.
"""

import os

from boto.s3.connection import S3Connection
from boto.s3.key import Key


class S3:
    """
    Provides storage interface to Amazon S3.
    """

    def __init__(self, access_key, secret_key):
        """
        Constructs the Amazon S3 storage interface.
        :param access_key: Access key to Amazon S3
        :param secret_key: Secret key to Amazon S3
        :return:
        """
        self._bucket_name = None
        self._access_key = access_key
        self._secret_key = secret_key
        self._connection = self._connect()

    def _connect(self):
        """
        Initializes S3 Connection objects and returns it.
        :return: S3Connection
        """
        return S3Connection(aws_access_key_id=self._access_key,
                            aws_secret_access_key=self._secret_key)

    def _get_bucket(self):
        """
        Returns bucket from connection.
        :return: S3Bucket
        """
        return self._connection.get_bucket(self.bucket)

    @property
    def bucket(self):
        """
        Property used to store bucket name.
        :return: bucket_name
        """
        if self._bucket_name is None:
            raise ValueError("Bucket is not defined.")
        return self._bucket_name

    @bucket.setter
    def bucket(self, bucket_name):
        """
        Setter for the bucket name.
        :param bucket_name:
        :return:
        """
        self._bucket_name = bucket_name

    def add_file(self, file_path):
        """
        Provided path is uploaded to the Amazon S3 bucket.
        :param file_path:
        :return:
        """
        bucket = self._get_bucket()
        file_name = os.path.basename(file_path)
        key = Key(bucket)
        key.key = file_name
        key.set_contents_from_filename(file_path)
