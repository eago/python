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

downloadUrlStringList = ['http://goalkicker.com/DotNETFrameworkBook/DotNETFrameworkNotesForProfessionals.pdf', 'http://goalkicker.com/AlgorithmsBook/AlgorithmsNotesForProfessionals.pdf', 'http://goalkicker.com/AndroidBook/AndroidNotesForProfessionals.pdf', 'http://goalkicker.com/Angular2Book/Angular2NotesForProfessionals.pdf', 'http://goalkicker.com/AngularJSBook/AngularJSNotesForProfessionals.pdf', 'http://goalkicker.com/BashBook/BashNotesForProfessionals.pdf', 'http://goalkicker.com/CBook/CNotesForProfessionals.pdf', 'http://goalkicker.com/CPlusPlusBook/CPlusPlusNotesForProfessionals.pdf', 'http://goalkicker.com/CSharpBook/CSharpNotesForProfessionals.pdf', 'http://goalkicker.com/CSSBook/CSSNotesForProfessionals.pdf', 'http://goalkicker.com/EntityFrameworkBook/EntityFrameworkNotesForProfessionals.pdf', 'http://goalkicker.com/ExcelVBABook/ExcelVBANotesForProfessionals.pdf', 'http://goalkicker.com/GitBook/GitNotesForProfessionals.pdf', 'http://goalkicker.com/HaskellBook/HaskellNotesForProfessionals.pdf', 'http://goalkicker.com/HTML5Book/HTML5NotesForProfessionals.pdf', 'http://goalkicker.com/HTML5CanvasBook/HTML5CanvasNotesForProfessionals.pdf', 'http://goalkicker.com/iOSBook/iOSNotesForProfessionals.pdf', 'http://goalkicker.com/JavaBook/JavaNotesForProfessionals.pdf', 'http://goalkicker.com/JavaScriptBook/JavaScriptNotesForProfessionals.pdf', 'http://goalkicker.com/jQueryBook/jQueryNotesForProfessionals.pdf', 'http://goalkicker.com/LaTeXBook/LaTeXNotesForProfessionals.pdf', 'http://goalkicker.com/LinuxBook/LinuxNotesForProfessionals.pdf', 'http://goalkicker.com/MATLABBook/MATLABNotesForProfessionals.pdf', 'http://goalkicker.com/MicrosoftSQLServerBook/MicrosoftSQLServerNotesForProfessionals.pdf', 'http://goalkicker.com/MongoDBBook/MongoDBNotesForProfessionals.pdf', 'http://goalkicker.com/MySQLBook/MySQLNotesForProfessionals.pdf', 'http://goalkicker.com/NodeJSBook/NodeJSNotesForProfessionals.pdf', 'http://goalkicker.com/ObjectiveCBook/ObjectiveCNotesForProfessionals.pdf', 'http://goalkicker.com/OracleDatabaseBook/OracleDatabaseNotesForProfessionals.pdf', 'http://goalkicker.com/PerlBook/PerlNotesForProfessionals.pdf', 'http://goalkicker.com/PHPBook/PHPNotesForProfessionals.pdf', 'http://goalkicker.com/PostgreSQLBook/PostgreSQLNotesForProfessionals.pdf', 'http://goalkicker.com/PowerShellBook/PowerShellNotesForProfessionals.pdf', 'http://goalkicker.com/PythonBook/PythonNotesForProfessionals.pdf', 'http://goalkicker.com/RBook/RNotesForProfessionals.pdf', 'http://goalkicker.com/RubyOnRailsBook/RubyOnRailsNotesForProfessionals.pdf', 'http://goalkicker.com/RubyBook/RubyNotesForProfessionals.pdf', 'http://goalkicker.com/SQLBook/SQLNotesForProfessionals.pdf', 'http://goalkicker.com/SwiftBook/SwiftNotesForProfessionals.pdf', 'http://goalkicker.com/TypeScriptBook2/TypeScriptNotesForProfessionals.pdf', 'http://goalkicker.com/VBABook/VBANotesForProfessionals.pdf', 'http://goalkicker.com/VisualBasic_NETBook/VisualBasic_NETNotesForProfessionals.pdf']
downloadUrlStringListTest = ['http://goalkicker.com/DotNETFrameworkBook/DotNETFrameworkNotesForProfessionals.pdf']
def getSoup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content.decode('utf-8','ignore'), 'lxml')
    return soup

def crawl(url, element, attribut):
    # headers = {
    #     'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    # }
    # req = request.Request(url , headers)
    # content = request.urlopen(req).read()
    # content = bs4.BeautifulSoup(content, 'lxml')
    # return content
    soup = getSoup(url)
    html = soup.prettify().encode('UTF-8')
    # print(soup.button)
    books = soup.select(element)
    # print(books)
    bookNames = []

    for book in books:
        bookNames.append(indexUrl + book.get(attribut) + '/')

    print(bookNames)
    # print (soup.find('div', id='navbutton_account')['title']).encode('utf-8')
    return bookNames

def getDownLoadUrlList(bookNames, attribut):
    downloadUrls = []
    reg = r'\'(.+)\''
    regex = re.compile(reg)
    for bookUrl in bookNames:
       downloadUrls.append(bookUrl + re.findall(regex, getSoup(bookUrl).button.get(attribut))[0])
    print(downloadUrls)
    return downloadUrls

def getFile(url):
    fileName = url.split('/')[-1]
    response = requests.get(url)
    response.raise_for_status()
    file = open(fileName, 'wb')
    file.write(response.content)
    file.close
    print("Sucessful to download" + " " + fileName)

    # blockSize = 8192
    # while True:
    #     buffer = response.content.read(blockSize)
    #     if not buffer:
    #         break
    #     file.write(buffer)


################ Tests while ############################
# getDownLoadUrlList(crawl(indexUrl, 'div .bookContainer > a', 'href'))
# crawl(indexUrl, 'div .bookContainer > a', 'href')
# crawl('http://goalkicker.com/VBABook/', 'button', 'class')

print(getSoup('http://goalkicker.com/VBABook/').button.get('onclick'))
# reg = r'\'(.+)\''
# regex = re.compile(reg)
# print(re.findall(regex, getSoup('http://goalkicker.com/VBABook/').button.get('onclick')))



# getDownLoadUrlList(crawl(indexUrl, 'div .bookContainer > a', 'href'), 'onclick')

def download():
    os.mkdir('pdfDownload')
    os.chdir(os.path.join(os.getcwd(), 'pdfDownload'))
    for url in downloadUrlStringList:
        getFile(url)

# download()