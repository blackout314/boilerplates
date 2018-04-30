#!/bin/bash

domain=$1

apt-get install nginx -y

cat > /etc/nginx/conf.d/syncthing.conf <<EOL
server {
  listen 80;
  server_name ${domain};

  root /usr/share/nginx/syncthing;
  access_log /var/log/nginx/${domain}.log;
  error_log /var/log/nginx/${domain}.error.log;
  location / {
    proxy_pass http://127.0.0.1:8384;
    proxy_set_header X-Real-IP \$remote_addr;
    proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto \$scheme;
  }
}
EOL

mkdir /usr/share/nginx/syncthing
nginx -t
systemctl reload nginx
