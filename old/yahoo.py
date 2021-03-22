from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import openpyxl
from bs4 import BeautifulSoup
import pandas as pd
import time
import datetime
import json
import os
import sys
import re
import _thread
import threading
import concurrent.futures
from functools import partial
from selenium.webdriver.support.ui import WebDriverWait


def headDriver():
    options = Options()
    options.headless = False
    options.add_argument("--window-size=1920,1200")
    try:
        driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
        agent = driver.execute_script("return navigator.userAgent")
        driver.close()
        options.add_argument("user-agent="+agent)
        driver= webdriver.Chrome(options= options, executable_path="chromedriver.exe")
        return driver
    except:
        print("You must use same chrome version with chrome driver!")
        error= "You must use same chrome version with chrome driver!"
        return 0

def findClickY(driver):
    element = driver.find_element_by_xpath("//a[@class='next']")
    if element:
        return element
    else:
        return False

query= """designer+"@gmail.com"+AND+"Us"+AND+"New York"+site:instagram.com """
url= "https://search.yahoo.com/search?q="+ query

# https://search.yahoo.com/search?q= designer "@gmail.com" AND Us AND "New York" site:instagram.com

driver= headDriver()

driver.get(url)

time.sleep(5)
try:
	driver.find_element_by_xpath("//button[@name='agree']").click()
	time.sleep(1)
except:
	pass

soup = BeautifulSoup(driver.page_source, 'html.parser')

# print(soup)

itemNodes= soup.find_all('div', attrs={'class':'dd algo algo-sr relsrch Sr'})

for itemNode in itemNodes:
    newPage= []
    source= itemNode.find('span', attrs= {'class': "fz-ms fw-m fc-12th wr-bw lh-17"}).text
    description= itemNode.find('p', attrs= {'class': 'fz-ms lh-1_43x'}).text
    title= itemNode.find('h3').text
    email= "ppp"
    url= itemNode.find('a').attrs['href']

    new = {'Source': source, 'Description': description, 'Title': title, 'Email': email, 'Url': url}
    newPage.append(new)
    # self.saveToCsv(filename, newPage, columns)
    print(newPage)

nextBtn= driver.find_element_by_xpath("//a[@class='next']")

nextBtn.click()
time.sleep(3)
try:
	nextBtn= driver.find_element_by_xpath("//a[@class='next']")
	print(nextBtn)
except:
	nextBtn= ''
if (nextBtn== ''):
	print('gooooood')


