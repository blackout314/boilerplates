#!/bin/sh

curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh

groupadd docker
gpasswd -a pi docker
