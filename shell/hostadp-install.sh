#!/bin/bash

apt-get install hostapd dnsmasq
systemctl disable hostapd
systemctl disable dnsmasq

cat >> /etc/network/interfaces <<EOL

auto uap0
iface uap0 inet static
  address 192.168.50.1
  netmask 255.255.255.0
  network 192.168.50.0
  broadcast 192.168.50.255
  gateway 192.168.50.1
EOL

cat > /etc/default/hostapd <<EOL

  interface=uap0
  # driver=
  ssid=awesomewifi
  country_code=GB
  hw_mode=g
  channel=10
  macaddr_acl=0
  auth_algs=1
  ignore_broadcast_ssid=0
  wpa=2
  wpa_passphrase=myawesomepassword
  wpa_key_mgmt=WPA-PSK
  wpa_pairwise=CCMP
  wpa_group_rekey=86400
  ieee80211n=1
  wme_enabled=1
EOL

cat > /etc/hostapd/hostapd.conf <<EOL
  DAEMON_CONF="/etc/hostapd/hostapd.conf"
EOL

cat > /etc/dnsmasq.confg <<EOL

  interface=uap0
  no-dhcp-interface=lo,wlan0
  bind-interfaces
  server=8.8.8.8
  domain-needed
  bogus-priv
  dhcp-range=192.168.50.50,192.168.50.150,12h
EOL


cat > /usr/local/bin/hostapdstart <<EOL

#!/bin/bash
  /sbin/iw dev wlan0 interface add uap0 type __ap
  systemctl start dnsmasq
  sysctl net.ipv4.ip_forward=1
  iptables -t nat -A POSTROUTING -s 192.168.50.0/24 ! -d 192.168.50.0/24 -j MASQUERADE
  ifup uap0  
  systemctl start hostapd
EOL
