import httplib, urllib, re, sys, json, socket, struct

# python shodan.py 0
#                  ^ this is the page number

shodan = {
	'apikey': '<your shodan API key>',
	'query': r'"root%40"+"android"+port%3A23',
}

conn = httplib.HTTPSConnection('api.shodan.io')
req = conn.request('GET', '/shodan/host/search?key='+shodan['apikey']+'&query='+shodan['query']+'&page='+str(sys.argv[1:][0]))
res = conn.getresponse()
body = res.read()

conn.close()

r = json.loads(body)
for i in r['matches']:
	ip = socket.inet_ntoa(struct.pack('!L', i['ip']))
	print str(sys.argv[1:][0])+','+ip+','+i['isp']+','+i['data'][3:]
