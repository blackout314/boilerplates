#!/bin/sh
GREEN='\033[0;32m'
RED='\033[0;31m'
RESET='\033[0m'


echo -e "${GREEN}INSTALL${RESET} vim screen mc ntfs-3g"

apt-get install vim screen mc -y
apt-get install ntfs-3g -y

echo -e "${GREEN}CREATE${RESET} /media/NAS01"

mkdir /media/NAS01
# useradd syncthing -m -G users
# passwd syncthing

echo -e "${GREEN}INSTALL${RESET} samba"

apt-get install samba samba-common-bin -y
