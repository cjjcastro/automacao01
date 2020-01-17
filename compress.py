import tarfile
import os

with tarfile.open('/opt/bacnobackup/backup.sql.tar.gz', "w:gz") as tar:
        tar.add('/opt/bancodump/backup.sql', arcname=os.path.basename('/opt/bancodump/backup.sql'))
