import requests
import json
from bs4 import BeautifulSoup

API_HOSTNAME = 'https://replace.me.with.proxycurl.hostname.com/some_endpoint'
payload = {
    'id': 'bill-gates-crawl-id',
    'url': 'https://www.linkedin.com/in/williamhgates/',
    'type': 'browser',
    'headers': {'LANG', 'en'},
}
r = requests.post(API_HOSTNAME, auth=HTTPBasicAuth('USER', 'PASSWD'), data=json.dumps(payload))

response_dic = r.json()
soup = BeautifulSoup(response_dic['data'])
h1 = soup.find_all("h1", class_="pv-top-card-section__name")[0]
print(h1.text)

# What does this script do:
# 1. Delegate your IP address with other residential IP address to avoid Linkedin bans your IP
# 2. Simulate many logged in Linkedin accounts
# 3. Use an advanced wed scrawler that behaves like a browser that allows to render Javascript
