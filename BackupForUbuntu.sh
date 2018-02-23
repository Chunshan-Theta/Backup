#backup and sftp to another pc.

#cd /home  #base dir for put file

ID=20$(date +"%y_%m_%dv%I_%M_%S")

# back up Mysql
mysqldump -A > /home/administrator/BackupCommand/${ID}all_databases.sql -u root -pytwu57874 -h localhost
# restore Mysql
#mysql <all_databases.sql -u root -pWulab35415


# backup Web File
# '--exclude' could skip dir you don't want to back up
echo "Wulab35415" | sudo -S tar cvpzf /home/administrator/BackupCommand/${ID}backup.tgz /var/www/


HOST=140.115.126.216
USER=gavin	
PASSWD=gavin
TargetDir=/home/BackupOfWuLAB/126_18 #Target dir for put file
echo $ID

lftp<<END_SCRIPT

open sftp://$HOST
set sftp:auto-confirm yes
user $USER $PASSWD
cd $TargetDir
put /home/administrator/BackupCommand/${ID}all_databases.sql
put /home/administrator/BackupCommand/${ID}backup.tgz

END_SCRIPT
#end

exit 0
