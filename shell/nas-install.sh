#!/bin/sh

apt-get install vim screen mc -y
apt-get install ntfs-3g -y
mkdir /media/NAS01
# useradd syncthing -m -G users
# passwd syncthing

apt-get install samba samba-common-bin -y
