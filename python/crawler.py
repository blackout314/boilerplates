#d!/usr/bin/env python

# pip install urlparse2

import requests
from lxml import html,etree
import urlparse2
import collections
import sys
from urllib.parse import urljoin

# Disable SSL warnings
try:
    import requests.packages.urllib3
    requests.packages.urllib3.disable_warnings()
except:
    pass

START = sys.argv[1]

urlq = collections.deque()  
urlq.append(START)  
found = set()  
found.add(START)

while len(urlq):  
  url = urlq.popleft()

  response = requests.get(url)
  body = html.fromstring(response.content)


  # Prints the page title
  print ( body.xpath('//title/text()') )
  result = etree.tostring(body, pretty_print=True, method="html")
  # print ( result )

  # Find all links, but make sure we stay on the same site.
  links = {urljoin(response.url, url) for url in body.xpath('//a/@href') if urljoin(response.url, url).startswith(START)}

  # Set difference to find new URLs
  for link in (links - found):
    found.add(link)
    urlq.append(link)

print ( found )
