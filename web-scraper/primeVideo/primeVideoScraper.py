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
        filmInfoNode = div.find_all("span", {"class": "dv-grid-beard-info"})[0]
        print(filmInfoNode.contents.__len__())
        if (filmInfoNode.contents.__len__() > 6):
            nameNode = div.find("a")
            imdbNode = filmInfoNode.contents[1]
            filmYearNode = filmInfoNode.contents[3]
            imdbScore = str(imdbNode.text).splitlines()[1].strip()
            filmItem = {"id": index, "name": nameNode.text, "imdbScore": imdbScore, "year": filmYearNode.string, "link": nameNode["href"]}
            filmItemList.append(filmItem)
            index += 1
        # print("################################################################################ film data ends")
    print(filmItemList)
    return filmItemList

# print(open(os.path.join(os.getcwd(), exampleUrl), "r", encoding='utf-8'))
primeVideoSoup = initSoup(open(os.path.join(os.getcwd(), exampleUrl), "r", encoding='utf-8'))
divList =  primeVideoSoup.find_all("div", {"class":"mustache"}, limit=20)
print("################################################################################")
createCsvFile(extractFilmName(divList))
