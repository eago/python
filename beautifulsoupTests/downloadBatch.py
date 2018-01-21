import os
import re
import bs4
import sys
from urllib import request
import requests
from bs4 import BeautifulSoup

indexUrl = "http://goalkicker.com/"
path = './docPack/'
totalResults = {}
oriResults = {}

def crawl(url):
    # headers = {
    #     'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    # }
    # req = request.Request(url , headers)
    # content = request.urlopen(req).read()
    # content = bs4.BeautifulSoup(content, 'lxml')
    # return content
    page = requests.get(url)
    soup = BeautifulSoup(page.content.decode('utf-8','ignore'), 'lxml')
    html = soup.prettify().encode('UTF-8')
    books = soup.select("div .bookContainer > a ")

    bookNames = []

    for book in books:
        bookNames.append(book.get('href'))

    print(bookNames)
    # print (soup.find('div', id='navbutton_account')['title']).encode('utf-8')
    return html

# def getUrlList(html):
#     html

crawl(indexUrl)