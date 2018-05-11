#!/bin/sh

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

/etc/init.d/samba restart

#smbpasswd -a syncthing
