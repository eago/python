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

# exampleUrl = "web-scraper\\primeVideo\\html\\example.html"
url_drame = "html\\Prime Video_ Parcourir_drame.html"
url_comedy = "html\\Prime Video_ Parcourir_comedy.html"
url_popular = "html\\Prime Video_ Parcourir_popular.html"
url_recent = "html\\Prime Video_ Parcourir_recent.html"
exampleUrl = "html\\example.html"

class Category:
    DRAMA = "drama"
    COMEDY = "comedy"
    POPULAR = "popular"
    RECENT = "recent"

def initSoup(file):
    return BeautifulSoup(file, "lxml")

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

def appendFilmListWithCategory(originList: [], newList: [], category: str):
    # I know this is far from efficient :(, but we will talk about it later
    for film in newList:
        existedFilm = next((f for f in originList if f.get("name") == film.get("name") and f.get("year") == film.get("year")), None)
        if (existedFilm is not None):
            existedFilm["category"] = existedFilm.get("category") + "," + category
        else:
            originList.append(film)
    return originList

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

def getFilmListByCategory(url, category):
    primeVideoSoup = initSoup(open(os.path.join(os.getcwd(), url), "r", encoding='utf-8'))
    divList =  primeVideoSoup.find_all("div", {"class":"mustache"}, limit=1000000)
    return extractFilmName(divList, category)

# UTF8Writer = codecs.getwriter("utf8")
# sys.stdout = UTF8Writer(sys.stdout)
print("################################################################################")
dramaFilmList = getFilmListByCategory(url_drame, Category.DRAMA)
comedyFilmList = getFilmListByCategory(url_comedy, Category.COMEDY)
popularFilmList = getFilmListByCategory(url_popular, Category.POPULAR)
recentFilmList = getFilmListByCategory(url_recent, Category.RECENT)
completFilmList = appendFilmListWithCategory(dramaFilmList, comedyFilmList, Category.COMEDY)
completFilmList = appendFilmListWithCategory(completFilmList, popularFilmList, Category.POPULAR)
completFilmList = appendFilmListWithCategory(completFilmList, recentFilmList, Category.RECENT)
createCsvFile(completFilmList)
