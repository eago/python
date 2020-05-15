#!python3
# searchpypi.py  Open several search results

import requests, sys, webbrowser, bs4, logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s  -  %(message)s')
logging.disable(logging.CRITICAL)
print('Searching...')
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))

webbrowser.open('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('.package-snippet')
logging.info(len(linkElems))

numOpen = min(5, len(linkElems))

for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening ', urlToOpen)
    webbrowser.open(urlToOpen)
