Paranoik
========

Paranoik is a Python Framework, intended to easify automation of backups on servers and developers' machines. Most of the currently available backup solutions are too hard to configure, have a big learning curve, and are not written in Python. :) Since now I have tried a bunch of backup tools, but no one fully satisfied my needs.

Overview
--------

Paranoik provides a mechanism to backup different things on a server, like:

* Directories
* MySQL Databases
* PostgreSQL Databases
* etc.

Separate components that define backup logic are called "backup providers". It is pretty easy to create new backup providers. It is nothing more than a class that inherits from `Backupable` (something that can be backuped).

Backup Providers
----------------

* Directory - allows to copy directories to another backup location.

```python
    directory = Directory("Some Directory Backup Resource")
    directory.path = "/path/to/directory"
    directory.destination = "/backup/location"
    directory.backup()
```

* MySQL - executes `mysqldump` and writes the output to a file.

```python
    database = MySQL("Some Database")
    database.database = "database_name"
    database.username = "user"
    database.password = "Passw0rd!"
    database.destination = "/path/to/dump.sql"
    database.backup()
```

Storage
-------

The purpose of storage providers is to provide interface to different data stores.

*S3 Storage*
```python
    storage = S3("your_access_key", "your_secret_key")
    storage.bucket = "bucket_name"
    storage.add_file(tar_file_path)
```

*FTP Storage*
```python
    ftp = FTP("ftp.example.com", "username", "password")
    ftp.add_file("/path/to/file.tar.gz")
    ftp.close()
```

Suites
------

Backup suites allow you to group multiple backupable objects in a single backup scenario.
Lets assume that we would like to group the directory and database backups.

```python
    suite = BackupSuite("Issue Tracker Backup")
    suite.add_backupable(directory)
    suite.add_backupable(database)
    suite.run()
```

When the `run` method is invoked, the suite will iteratively call the `backup` methods
of each backupable object and iteratively do the cleanup.

Compatibility
=============

Paranoik Backups is compatible with the Python >= 2.6 and Python >= 3.0
