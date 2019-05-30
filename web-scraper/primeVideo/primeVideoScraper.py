import os
import sys
from urllib3 import request
import requests
import time
import datetime
from bs4 import BeautifulSoup

# url = "web-scraper\\primeVideo\\html\\Prime Video_ Parcourir.html"
# exampleUrl = "web-scraper\\primeVideo\\html\\example.html"
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

def createCsvFile(filmItemList):
    os.chdir(os.path.join(os.getcwd(), 'csv'))
    try:
        fileName = 'video' + str(datetime.datetime.now().timestamp()) + '.csv'
        open(fileName, 'wb')
        with open(fileName, 'a', encoding="utf8") as csvFile:
            # sortedFilmItemList = filmItemList.sort(key= id)
            for filmItem in filmItemList:
                line = str(filmItem.get("id")) + "|" + filmItem.get("name") + "|" + filmItem.get("imdbScore") + "|" + filmItem.get("year") + "|" + filmItem.get("link")
                csvFile.write(line + "\n")
        print("csv file is created")
    except AssertionError as error:
        print(error)
        print("can not create csv file")

def initSoup(file):
    return BeautifulSoup(file, "lxml")

def extractFilmName(divTagList):
    filmItemList = []
    filmItemList.sort(key=divTagList)
    index = 1
    for div in divTagList:
        # print(nameNode)
        # print(div.find_all("span", {"class": "dv-grid-beard-info"})[0])
        filmInfoNode = div.find_all("span", {"class": "dv-grid-beard-info"})[0]
        print(filmInfoNode.contents.__len__())
        if (filmInfoNode.contents.__len__() > 6):
            nameNode = div.find("a")
            imdbNode = filmInfoNode.contents[1]
            filmYearNode = filmInfoNode.contents[3]
            # print(filmInfoNode)
            # print(imdbNode)
            imdbScore = str(imdbNode.text).splitlines()[1].strip()
            # print("################################################################################ film data begins")
            filmItem = {"id": index, "name": nameNode.text, "imdbScore": imdbScore, "year": filmYearNode.string, "link": nameNode["href"]}
            filmItemList.append(filmItem)
            index += 1
        # print(filmItem)
        # print("################################################################################ film data ends")
    print(filmItemList)
    return filmItemList

#createCsvFile()
# soup = initSoup(html_doc)
# print(open(os.path.join(os.getcwd(), exampleUrl), "r", encoding='utf-8'))
primeVideoSoup = initSoup(open(os.path.join(os.getcwd(), exampleUrl), "r", encoding='utf-8'))
# divList =  primeVideoSoup.find_all("span", limit=2)
divList =  primeVideoSoup.find_all("div", {"class":"mustache"}, limit=20)
# print(divList)
print("################################################################################")
createCsvFile(extractFilmName(divList))
