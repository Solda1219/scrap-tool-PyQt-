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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException



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



query= """designer+"@gmail.com"+AND+"New York"+site:instagram.com """
url= "https://www.bing.com/search?q="+ query


driver= headDriver()

driver.get(url)

time.sleep(5)
try:
    driver.find_element_by_id("bnp_hfly_cta2").click()
    time.sleep(1)
except:
    pass

soup = BeautifulSoup(driver.page_source, 'html.parser')

itemNodes= soup.find_all('li', attrs={'class':'b_algo'})

for itemNode in itemNodes:
    newPage= []
    source= itemNode.find('cite').text
    description= itemNode.find('p').text
    title= itemNode.find('h2').text
    email= "ppp"
    url= itemNode.find('a').attrs['href']

    new = {'Source': source, 'Description': description, 'Title': title, 'Email': email, 'Url': url}
    newPage.append(new)
    # self.saveToCsv(filename, newPage, columns)
    print(newPage)

# nextBtn= driver.find_element_by_xpath("//div[@class='sw_next']")
# print(nextBtn)
pageBtns= driver.find_elements_by_xpath("//a[@class= 'b_widePag sb_bp']")
for pageBtn in pageBtns:
	print(pageBtn.text)
pageBtns[3].click()

# nextBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sw_next']")))
# pageBtns[3].click()


# time.sleep(3)
# soup = BeautifulSoup(driver.page_source, 'html.parser')

# itemNodes= soup.find_all('li', attrs={'class':'b_algo'})

# for itemNode in itemNodes:
#     newPage= []
#     source= itemNode.find('cite').text
#     description= itemNode.find('p').text
#     title= itemNode.find('h2').text
#     email= "ppp"
#     url= itemNode.find('a').attrs['href']

#     new = {'Source': source, 'Description': description, 'Title': title, 'Email': email, 'Url': url}
#     newPage.append(new)
#     # self.saveToCsv(filename, newPage, columns)
#     print(newPage)


# def findClickBing(driver):
#     element = driver.find_element_by_xpath("//a[@class='sb_pagN sb_pagN_bp b_widePag sb_bp']")
#     if element:
#         return element
#     else:
#         return False