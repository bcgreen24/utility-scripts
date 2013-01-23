su -s /bin/bash o1.ftp
cd /data/disk/o1/static/campuscms/campuscms-1.01.20130103-dev/sites/ssha.ucmerced.edu/themes/cms-theme-inception
git pull > /home/o1.ftp/gitpull.txt
date >> /home/o1.ftp/gitpull.txt
exit
cd /data/disk/o1/static/campuscms/campuscms-1.01.20130103-dev/sites/ssha.ucmerced.edu
drush cc all >> /home/o1.ftp/gitpull.txt













