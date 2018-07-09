#!/bin/sh
GREEN='\033[0;32m'
RED='\033[0;31m'
RESET='\033[0m'


echo -e "${GREEN}INSTALL${RESET} fstab"

GID=`id -g syncthing`
UID=`id -u syncthing`
echo "/etc/fstab"
echo "/dev/sda1 /media/NAS01 auto nofail,uid=$UID,gid=$GID,noatime 0 0"

echo "[NAS]
comment = MNAS
path = /media/NAS01
valid users = @users
force group = users
create mask = 0660
directory mask = 0771
read only = no" > /etc/samba/smb.conf

echo -e "${GREEN}RESTART${RESET} smb"

/etc/init.d/samba restart

#smbpasswd -a syncthing
