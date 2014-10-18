import os
import datetime

from paranoik.backup.providers.mysql import MySQL
from paranoik.backup.providers.directory import Directory
from paranoik.compress.tar import Tar
from paranoik.storage.s3 import S3


backup_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
BACKUP_DIR = os.path.join("/root", "backup",
                          backup_time)
os.mkdir(BACKUP_DIR)

# Backup MySQL
database_file = os.path.join(BACKUP_DIR, "mysql_database.sql")
database = MySQL("Redmine database")
database.database = "redmine"
database.username = "redmine"
database.password = ""
database.destination = database_file
database.backup()

# Backup directories
srv_backup = os.path.join(BACKUP_DIR, "redmine")
srv_redmine = Directory("Redmine source")
srv_redmine.path = "/srv/redmine"
srv_redmine.destination = srv_backup
srv_redmine.backup()

# Compress the whole backup
tar_file_name = "{0}.tar.gz".format(backup_time)
tar_file_path = os.path.join("/root", "backup", tar_file_name)

tar = Tar(tar_file_path)
tar.add(BACKUP_DIR)
tar.close()

# Uploaod to S3
syncer = S3("your_access_key", "your_secret_key")
syncer.bucket = "bucket_name"
syncer.add_file(tar_file_path)
