#!/bin/bash

## sudo apt-get install apt-transport-https

apt-get update
apt-get install curl -y
curl -s https://syncthing.net/release-key.txt | apt-key add -

echo "deb https://apt.syncthing.net/ syncthing stable" | tee /etc/apt/sources.list.d/syncthing.list
apt-get update
apt-get install syncthing -y

useradd -r syncthing -m -d /home/syncthing
usermod -a -G users syncthing
systemctl enable syncthing@syncthing.service
# systemctl start syncthing@syncthing.service
curl -I 127.0.0.1:8384
