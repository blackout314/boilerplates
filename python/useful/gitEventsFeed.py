import json
import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def getFeed(url):
  try:
    response = requests.get (url, allow_redirects=False, timeout=7, verify=False)
    data = json.loads(response.text)
    for element in data:
      print element['created_at'] + ", " + element['type'] + ", " + element['actor']['display_login'] + ", " + element['repo']['name']
  except Exception as e:
    print e

def main (argv):
  URL = 'https://api.github.com/users/' + argv[0] + '/received_events/public'
  getFeed(URL)

if __name__ == "__main__":
  main(sys.argv[1:])
