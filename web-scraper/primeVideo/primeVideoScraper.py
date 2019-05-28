import os
import sys
from urllib3 import request
import requests
import time
import datetime
from bs4 import BeautifulSoup

url = "html\\Prime Video_ Parcourir.html"
exampleUrl = "html\\example.html"

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

def createCsvFile():
    os.chdir(os.path.join(os.getcwd(), 'csv'))
    try:
        open('video' + str(datetime.datetime.now().timestamp()) + '.csv', 'wb')
        print("csv file is created")
    except AssertionError as error:
        print(error)
        print("can not create csv file")
def initSoup(file):
    return BeautifulSoup(file, "lxml")

#createCsvFile()
soup = initSoup(html_doc)
print(open(os.path.join(os.getcwd(), exampleUrl), "r", encoding='utf-8'))
primeVideoSoup = initSoup(open(os.path.join(os.getcwd(), url), "r", encoding='utf-8'))
divList =  primeVideoSoup.find_all("span", limit=2)
print(divList)
print(repr(primeVideoSoup.title))
# print(soup.a['href'])
# for child in soup.head.descendants:
#     print(child)
