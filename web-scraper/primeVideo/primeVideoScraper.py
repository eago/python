import os
import sys
import codecs
from urllib3 import request
import requests
import time
import datetime
from bs4 import BeautifulSoup

"""
This script aims to parser Amazon France prime video web page (https://www.primevideo.com/) to get the films with an IMDb notes.
Then it will write the results in an csv file for personal usage.
The script uses exclusively the BeautifulSoup library (https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/).
This file is under MIT License @Copyright, you can copy it, change it use it with all rights if it's allowed by law.
"""

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
            csvFile.write("id|name|imdbScore|year|category|link\n")
            for filmItem in filmItemList:
                line = str(filmItem.get("id")) + "|" + filmItem.get("name") + "|" + str(filmItem.get("imdbScore")) + "|" + filmItem.get("year") + "|"+ filmItem.get("category") + "|" + filmItem.get("link")
                csvFile.write(line + "\n")
        print("csv file is created")
    except AssertionError as error:
        print(error)
        print("can not create csv file")

def sortFilmListByImdbScore(filmItemList):
    filmItemList.sort(key = lambda film: film.get("imdbScore"), reverse = True)

def initSoup(file):
    return BeautifulSoup(file, "lxml")

def extractFilmName(divTagList, category):
    filmItemList = []
    filmItemList.sort(key=divTagList)
    index = 1
    IMDB_NOTE_POSTION = 0
    FILM_YEAR_POSITION = 1
    for div in divTagList:
        filmInfoNode = div.find_all("span", {"class": "dv-grid-beard-info"})[IMDB_NOTE_POSTION]
        if (filmInfoNode.contents.__len__() > 2):
            nameNode = div.find("a")
            imdbNode = filmInfoNode.contents[IMDB_NOTE_POSTION]
            filmYearNode = filmInfoNode.contents[FILM_YEAR_POSITION]
            imdbScore = str(imdbNode.text).split(' ')[1].strip()
            imdbScore = str.replace(imdbScore, ",", ".")
            filmItem = {"id": index, "name": nameNode.text, "imdbScore": float(imdbScore), "year": filmYearNode.string, "category": category, "link": nameNode["href"]}
            filmItemList.append(filmItem)
            index += 1
        # print("################################################################################ film data ends")
    sortFilmListByImdbScore(filmItemList)
    # print(filmItemList)
    return filmItemList

# UTF8Writer = codecs.getwriter("utf8")
# sys.stdout = UTF8Writer(sys.stdout)
# print(open(os.path.join(os.getcwd(), exampleUrl), "r", encoding='utf-8'))
primeVideoSoup = initSoup(open(os.path.join(os.getcwd(), url), "r", encoding='utf-8'))
divList =  primeVideoSoup.find_all("div", {"class":"mustache"}, limit=1000)
print("################################################################################")
# extractFilmName(divList, "Drame")
createCsvFile(extractFilmName(divList, "Drame"))
