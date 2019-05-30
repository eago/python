import os
import sys
from urllib3 import request
import requests
import time
import datetime
from bs4 import BeautifulSoup

url = "web-scraper\\primeVideo\\html\\Prime Video_ Parcourir.html"
exampleUrl = "web-scraper\\primeVideo\\html\\example.html"

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

def extractFilmName(divTagList):
    for div in divTagList:
        nameNode = div.find("a")
        print(nameNode)
        # print(div.find_all("span", {"class": "dv-grid-beard-info"})[0])
        imdbNode = div.find_all("span", {"class": "dv-grid-beard-info"})[0].contents[1]
        print(imdbNode)
        imdbScore = str(imdbNode.text).splitlines()[1].strip()
        print("################################################################################ film data begins")
        filmItem = {"name": nameNode.text, "imdbScore": imdbScore, "link": nameNode["href"]}
        print(filmItem)
        print("################################################################################ film data ends")

#createCsvFile()
# soup = initSoup(html_doc)
# print(open(os.path.join(os.getcwd(), exampleUrl), "r", encoding='utf-8'))
primeVideoSoup = initSoup(open(os.path.join(os.getcwd(), exampleUrl), "r", encoding='utf-8'))
# divList =  primeVideoSoup.find_all("span", limit=2)
divList =  primeVideoSoup.find_all("div", {"class":"mustache"}, limit=1)
# print(divList)
print("################################################################################")
extractFilmName(divList)
