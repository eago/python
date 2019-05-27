import os
import sys
from urllib3 import request
import requests
import time
import datetime

url = "html/Prime Video_ Parcourir.html"

def createCsvFile():
    os.chdir(os.path.join(os.getcwd(), 'csv'))
    try:
        open('video' + str(datetime.datetime.now().timestamp()) + '.csv', 'wb')
        print("csv file is created")
    except AssertionError as error:
        print(error)
        print("can not create csv file")


#createCsvFile()
