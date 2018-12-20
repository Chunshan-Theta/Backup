#backup and sftp to another pc.



BASE=/home/*****/Desktop/backup/Backupfolder
#cd /home  #base dir for put file
ID=20$(date +"%y_%m_%dv%I_%M_%S")


#init folder
echo "passwords" | sudo rm -rf ${BASE}
mkdir ${BASE}
# back up Mysql
mysqldump -A > ${BASE}/${ID}all_databases.sql -u root -proot -h localhost
# restore Mysql
#mysql <all_databases.sql -u root -pWulab35415


# backup Web File
# '--exclude' could skip dir you don't want to back up
#echo "Wulab35415" | sudo -S tar cvpzf /home/administrator/BackupCommand/${ID}backup.tgz /var/www/


HOST=***.***.***.***
USER=*****	
PASSWD=*****	
TargetDir=/home/BackupOfWuLAB/126_20 #Target dir for put file
echo $ID

lftp<<END_SCRIPT
open sftp://$HOST
set sftp:auto-confirm yes
user $USER $PASSWD
cd $TargetDir
put ${BASE}/${ID}all_databases.sql
END_SCRIPT
#end

exit 0
