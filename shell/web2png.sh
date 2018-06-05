#!/bin/sh

  apt-get install libfontconfig1 libxrender1 -y
  apt-get install libxext6 -y
  wget https://github.com/h4cc/wkhtmltoimage-amd64/raw/master/bin/wkhtmltoimage-amd64
  chmod +x wkhtmltoimage-amd64
  git clone https://github.com/PHPGangsta/WebsiteToImage
