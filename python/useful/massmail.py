#!/usr/bin/python
# -*- coding: utf-8 -*-

import socks  # necessite socksipy =>  apt-get install python-socksipy
import socket
import smtplib
#import gnupg #apt-get install python-gnupg or pip install gnupg
from email.mime.text import MIMEText

#####################################################################
##comment for not using Tor(be sure Tor running using socksport 9050)
##or adpat for your socks proxy

# init the socks socket
s = socks.socksocket()

#set default proxy settings for newly created socksocket objects,
#to force 3rd party modules smtplib to use the socks proxy
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket
###################################################################

sender = raw_input("Enter the smtp sender adress : ")
origine = raw_input("Enter the address the message should appear to come from: ")
password = raw_input ("enter the smtp password")

# Open the file and init the recipient list
fo = open("foo.txt", "rw+")
recipient = []

#add each adress to recipient list
for i in fo.readlines():
      recipient.append(i.split('\n')[0])

      print recipient
# Close open file
      fo.close()

#mail construction
message = "mettre ici le corp du message à envoyer (codage ascii-us)"
message = MIMEText(message)
message['Subject'] = 'Test'
message['From'] = origine
message['To'] = ", ".join(recipient)
# Send the message via the austici SMTP server.
s = smtplib.SMTP('smtp.autistici.org', 587)
s.starttls()
s.login(sender, password)
s.sendmail(origine, recipient, message.as_string())
s.quit()

