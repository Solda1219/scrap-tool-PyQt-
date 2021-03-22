import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import openpyxl
from bs4 import BeautifulSoup
import pandas as pd
import time
import json
import os
import sys
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
        return 0

def findClickY(driver):
    element = driver.find_element_by_xpath("//a[@class='next']")
    if element:
        return element
    else:
        return False

domurl= "https://www.yellowpages.com"
url= "https://www.yellowpages.com/los-angeles-ca/restaurants?page=2"

response= requests.get(url)
time.sleep(0.5)
soup = BeautifulSoup(response.text, 'html.parser')
itemNodes= soup.find_all('div', attrs= {'class': 'v-card'})
businessName= itemNodes[0].find('h2').text
streetAddress= itemNodes[0].find('div', attrs= {'class': 'street-address'}).text
locality= itemNodes[0].find('div', attrs= {'class': 'locality'}).text
address= streetAddress+ ' '+locality
phoneNumber= itemNodes[0].find('div', attrs= {'class': 'phones phone primary'}).text
website= itemNodes[0].find('a', attrs= {'class': 'track-visit-website'}).attrs['href']
email= ''
new = {'Business Name': businessName, 'Address': address, 'Phone Number': phoneNumber, 'Website': website, 'Email': email}
print(new)

