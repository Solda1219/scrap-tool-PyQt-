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

signinUrl= "https://www.linkedin.com/uas/login"
intendedUrl= "https://www.linkedin.com/sales/search/people?companySize=C&doFetchHeroCard=false&geoIncluded=103644278&industryIncluded=9&logHistory=true&page=1&searchSessionId=516hVLSTRf%2BtnQWMOI1KOw%3D%3D&titleIncluded=Managing%2520Partner%3A154&titleTimeScope=CURRENT&page=2"
# &page=2

domurl= "https://www.linkedin.com"

# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

# this is page next part
linkedin_username= "sharmin_moon7@yahoo.com"
linkedin_password= "Masum@123"
driver= headDriver()
driver.get(signinUrl)
time.sleep(2)

username_input = driver.find_element_by_id('username')
username_input.send_keys(linkedin_username)

password_input = driver.find_element_by_id('password')
password_input.send_keys(linkedin_password)
password_input.submit()
driver.get(intendedUrl)
time.sleep(5)
for i in range(8):
    time.sleep(0.5)
    recentList = driver.find_elements_by_xpath("//section[@class='result-lockup']")
    if len(recentList) == 0 :
        break
    else :
        driver.execute_script("arguments[0].scrollIntoView();", recentList[len(recentList) - 1 ] )

soup= BeautifulSoup(driver.page_source, 'html.parser')

itemNodes= soup.find_all('section', attrs= {'class': 'result-lockup'})
# itemNodes= soup.find_all('li', attrs= {'class': 'pv5 ph2 search-results__result-item'})
nodeLinks= []
print(len(itemNodes))
print(itemNodes)
for itemNode in itemNodes:
    try:
        tmp= domurl+ itemNode.find('a', attrs= {'class': 'ember-view result-lockup__icon-link'}).attrs['href']
        nodeLink= tmp.split(',', 1)[0].replace('sales/people', 'in')
        nodeLinks.append(nodeLink)
    except:
        continue

print(nodeLinks)
driver.get(nodeLinks[0])
time.sleep(1)
profileUrl= driver.current_url
soup= BeautifulSoup(driver.page_source, 'html.parser')
name= soup.find('li', attrs= {'class': 'inline t-24 t-black t-normal break-words'}).text.strip()
jobtitle= soup.find('h2', attrs= {'class': 'mt1 t-18 t-black t-normal break-words'}).text.strip()
location= soup.find('li', attrs= {'class': 't-16 t-black t-normal inline-block'}).text.strip()
print(name)
print(jobtitle)
print(profileUrl)
print(location)



# url= "https://www.yellowpages.com/los-angeles-ca/restaurants?page=2"
# driver.get(url)
# time.sleep(5)


# # this is itemNode clicks in one page
# itemClicks= driver.find_elements_by_xpath("//div[@class='v-card']")
# itemClicks[0].click()
# time.sleep(3)
# soup = BeautifulSoup(driver.page_source, 'html.parser')

# # # this is detailed info
# detailInfo= soup.find('header', attrs= {'id': 'main-header'})
# title= detailInfo.find('h1').text
# phone= detailInfo.find('p', attrs= {'class': 'phone'}).text
# address= detailInfo.find('h2', attrs= {'class': 'address'}).text
# website= detailInfo.find('a', attrs= {'class': 'primary-btn website-link'}).attrs['href']
# print(title)
# print(phone)
# print(address)
# print(website)
# soup = BeautifulSoup(driver.page_source, 'html.parser')




