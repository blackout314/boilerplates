import requests

r = requests.get(
  "https://blackout.altervista.org",
  proxies={"http": "http://127.0.0.1:9150"}
)
print(r.text)
