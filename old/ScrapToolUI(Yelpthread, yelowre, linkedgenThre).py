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
# import datetime
import json
import os
import sys
import re
import _thread
import threading
import concurrent.futures
from functools import partial
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import socket
import uuid
import webbrowser
import psutil
# import subprocess
# import win32ui
modifyNum= 5

def modifyUrls( urls):
    modifiedUrls= []
    if len(urls)<= modifyNum:
        modifiedUrls.append(urls)
        return modifiedUrls
    else:
        modifiedUrlsLen= int(len(urls)/modifyNum)
        for i in range(modifiedUrlsLen):
            new= []
            for ii in range(modifyNum):
                new.append(urls[ii+i*modifyNum])
            modifiedUrls.append(new)
        rest= []
        for iii in range(len(urls)- (i+1)*modifyNum):
            rest.append(urls[iii+(i+1)*modifyNum])
        modifiedUrls.append(rest)
    return modifiedUrls
# The tab part of UI
class tabdemo(QTabWidget):
    def __init__(self, parent = None):
        super(tabdemo, self).__init__(parent)
        # self.setStyleSheet('border: 0.5px solid #666666')
        self.setStyleSheet("QTabWidget::pane { border-left: 7px solid #3a3a3a; border-right: 7px solid #3a3a3a; border-bottom: 7px solid #3a3a3a} QTabWidget::tab-bar:top {background-color: #3a3a3a; top: 1px; } QTabBar::tab {background-color: #3a3a3a; width: 106.53px; height: 40px; color: white; font-weight:bold; font-size: 9px; border-top: 0.5px solid #666666; } QTabBar::tab:selected {background: #282828;}" "QLabel{color: #dbdbdb; margin-top: 15px; margin-bottom: 5px}" "QLineEdit{color: #dbdbdb; selection-background-color:#3a3a3a; height: 30px; border: 0.5px solid #666666;}" "QComboBox{color:#dbdbdb; border: 0.5px solid #666666; height: 30px} ")
        self.dashboard = QWidget()
        self.dashboard.setStyleSheet("background-color:#282828; ")
        self.webemail = QWidget()
        self.webemail.setStyleSheet("background-color:#282828; ")
        self.socialmail = QWidget()
        self.socialmail.setStyleSheet("background-color:#282828; ")
        self.googlemap = QWidget()
        self.googlemap.setStyleSheet("background-color:#282828; ")
        self.yellowpage = QWidget()
        self.yellowpage.setStyleSheet("background-color:#282828; ")
        self.yelppage = QWidget()
        self.yelppage.setStyleSheet("background-color:#282828; ")
        self.linkedinnav = QWidget()
        self.linkedinnav.setStyleSheet("background-color:#282828; ")
        self.linkedingeneral= QWidget()
        self.linkedingeneral.setStyleSheet("background-color:#282828; ")
      
        self.tabdash= self.addTab(self.dashboard,"Tab 1")
        self.tabWeb= self.addTab(self.webemail,"Tab 2")
        self.tabSocial= self.addTab(self.socialmail,"Tab 3")
        self.tabGMap= self.addTab(self.googlemap, "Tab 4")
        self.tabYellow= self.addTab(self.yellowpage, "Tab 5")
        self.tabYelp= self.addTab(self.yelppage, "Tab 6")
        self.tabLinkedin= self.addTab(self.linkedingeneral, "Tab 7")
        self.tabSalesNav= self.addTab(self.linkedinnav, "Tab 8")
        
        self.dashboardUI()
        self.webemailUI()
        self.socialmailUI()
        self.googlemapUI()
        self.yellowpageUI()
        self.yelppageUI()
        self.linkedinnavUI()
        self.linkedingeneralUI()
        self.setWindowTitle("Scrping tool")
      
    def dashboardUI(self):
        # layout = QVBoxLayout()
        # layout.addStretch(0)
        # layout.setContentsMargins(-1, -1, -1, 0)
        # title= "<strong>Power Scrap</strong>"
        # text= "This is powerful scraping tool which scrap from useful data!\n\n This provides Website email scrap, Social mail scrap, Google map scrap, Yellow and Yelp page,\n Linkedin General search, Linkedin Sales Nav.\n\n\
        # 1, Website email scrap\n You type any website's url then it will scrap emails from there.\n\n 2, Social mail scrap\n You can have to input keyword and you can choose Search engines which you want.\n Also if any search engine block your ip then you can easily change engine and scrap again from that engine.\n\n 3, Google Map scrap\n Here you can scrap from google map search result.\n But here onething you have to remember, this part provides only google map scrap.\n So if you type url that differant type, then it will show an error message\n You can simply take a look about valid type as you type 'restaurants in new york' in google.\n\n 4, Yellow, Yelp page scrap.\n You have to input yellow, yelp page search result url.\n Then this tool grap infos for you.\n\n 5, Linkedin General search\n You have to input linkedin search url. Then this tool grab infos from there.\n\n 6, Linkedin Sales Nav\n You have to input linkedin sales nav search url.\n Then this tool grab people's info.\n\n\n Note!\n This provides powerful scrap. But onething you have to remember, You need to insert valid type url in each tool.\n Then you will get wonderful result.\n\n\n Thanks so much!"
        # titleLabel= QLabel(title)
        # titleLabel.setAlignment(Qt.AlignCenter)
        # titleLabel.setStyleSheet('color: rgb(254, 121, 190); font-size: 40px; font-family: NSimSun;')
        # label= QLabel(text)
        # label.setAlignment(Qt.AlignCenter)
        # label.setStyleSheet('color: rgb(98, 114, 164); font-size:14px')
        # layout.addWidget(titleLabel)
        # layout.addStretch(0)
        # layout.addWidget(label)
        # layout.addStretch(2)
        layout= QFormLayout()
        label1= QLabel('About the Power Scrap')
        label1.setStyleSheet('color: #fd6331; font-size: 16px; margin-bottom: 5px')
        layout.addRow('', QLabel(''))
        layout.addRow('',label1)
        label12= QLabel('This is powerful scraping tool which scrap from useful data. This provides Website email scrap, Social mail scrap, Google map')
        label12.setStyleSheet('color: white; font-size: 12px; margin-top: 0px; margin-bottom:2px')
        layout.addRow('', label12)
        label13= QLabel('scrap, Yellow and Yelp page, Linkedin General Search, Linkedin Sales Nav.')
        label13.setStyleSheet('color: white; font-size: 12px; margin-top: 0px; margin-bottom:2px')
        layout.addRow('', label13)
        label2= QLabel('Guidelines')
        label2.setStyleSheet('color: #fd6331; font-size: 16px; margin-bottom: 5px')
        layout.addRow('', label2)
        label21= QLabel("1.Website email scrap: You can type any website's url then it will scrap emails from there.")
        label21.setStyleSheet('color: white; font-size: 12px; margin-top: 0px; margin-bottom:7px')
        layout.addRow('', label21)
        label22= QLabel("2.Social mail scrap: You can have to input keyword and you can choose Search engines which you want. Also if any search engine block your IP")
        label22.setStyleSheet('color: white; font-size: 12px; margin-top: 0px; margin-bottom:2px')
        layout.addRow('', label22)
        label23= QLabel("then you can easily change engine and scrap again using that engine.")
        label23.setStyleSheet('color: white; font-size: 12px; margin-top: 0px; margin-bottom:7px')
        layout.addRow('', label23)
        label24= QLabel("3.Google Map scrap: Here you can scrap from google map search result. But here one thing you have to remember, this part provides only")
        label24.setStyleSheet('color: white; font-size: 12px; margin-top: 0px; margin-bottom:2px')
        layout.addRow('', label24)
        label25= QLabel("google map scrap. So if you type URL that different type, then it will show an error message.")
        label25.setStyleSheet('color: white; font-size: 12px; margin-top: 0px; margin-bottom:2px')
        layout.addRow('', label25)
        label26= QLabel("You can simply take a look about valid type as you type 'restaurants in new york' in google.")
        label26.setStyleSheet('color: white; font-size: 12px; margin-top: 0px; margin-bottom:7px')
        layout.addRow('', label26)
        label27= QLabel("4.Yellow, Yelp page scrap: You have to input yellow, yelp page search result URL. Then this tool scrap info's for you.")
        label27.setStyleSheet('color: white; font-size: 12px; margin-top: 0px; margin-bottom:7px')
        layout.addRow('', label27)
        label28= QLabel("5.Linkedin General Search: You have to input Linkedin search URL. Then this tool grap info's from there.")
        label28.setStyleSheet('color: white; font-size: 12px; margin-top: 0px; margin-bottom:7px')
        layout.addRow('', label28)
        label29= QLabel("Linkedin Sales Nav: You have to input Linkedin sales nav search URL. Then this tool grab people's info.")
        label29.setStyleSheet('color: white; font-size: 12px; margin-top: 0px; margin-bottom:7px')
        layout.addRow('', label29)
        label3= QLabel("For more info and support please ")
        label3.setStyleSheet('color: white; font-size: 12px; margin-top: 0px; margin-bottom:7px')
        contactlay= QFormLayout()
        contactBtn= QPushButton('contact support')
        contactBtn.setFixedWidth(80)
        contactBtn.setStyleSheet('background-color: #282828; color: #fd6331; border: 0px')
        contactlay.addRow(label3, contactBtn)
        layout.addRow('', contactlay)
        label4= QLabel("Dependency")
        label4.setStyleSheet('color: #fd6331; font-size: 16px; margin-bottom: 5px')
        layout.addRow('', label4)
        label41= QLabel("To run this application, you must need to use chrome driver with same chrome browser version. Download links are given below.")
        label41.setStyleSheet('color: white; font-size: 12px; margin-top: 0px; margin-bottom:2px')
        layout.addRow('', label41)
        downBrowser= QPushButton('Download chrome browser')
        downBrowser.setFixedWidth(130)
        downBrowser.setStyleSheet('background-color: #282828; color: #fd6331; border: 0px')
        layout.addRow('', downBrowser)
        downDriver= QPushButton('Download chrome driver')
        downDriver.setFixedWidth(120)
        downDriver.setStyleSheet('background-color: #282828; color: #fd6331; border: 0px')

        layout.addRow('', downDriver)
        comLabel= QLabel("copyright @ powerscrapper.io all rights reserved")
        comLabel.setStyleSheet('color: white; font-size: 12px; margin-top: 140px; margin-left: 265px; margin-bottom:2px')
        layout.addRow('', comLabel)
        downDriver.clicked.connect(self.downloadDriver)
        downBrowser.clicked.connect(self.downloadBrowser)
        self.setTabText(0,"DASHBOARD")
        self.dashboard.setLayout(layout)


    def downloadDriver(self):
        webbrowser.open('https://chromedriver.chromium.org/downloads', new=2)

    def downloadBrowser(self):
        webbrowser.open('https://www.google.com/chrome/', new= 3)
      
    def webemailUI(self):
        description = "Please enter any website's url where you want to scrap email from."
        label= QLabel(self.webemail)
        label.setText(description)
        # label.setStyleSheet('margin-left: 210px; margin-top: 90px; color: rgb(254, 121, 190)')
        layout= QFormLayout()
        layout.addRow('', label)

        # labelForEdit.setStyleSheet('margin-left: 210px; margin-top: 100px')
        Edit= QLineEdit()
        Edit.setStyleSheet('margin-bottom: 15px')
        layout.addRow('',Edit)
        startForWebEmail= QPushButton(self.webemail)
        startForWebEmail.setText('Start')
        startForWebEmail.setFixedWidth(100)
        startForWebEmail.setFixedHeight(30)
        startForWebEmail.setStyleSheet('background-color: #526ee7; color: #dbdbdb; border-radius: 3px')
        # trigger webemail scrap
        startForWebEmail.clicked.connect(partial(self.webemailScrapTrigger, Edit))

        # startForWebEmail.setStyleSheet('margin-left: 290px; margin-top: 120px')
        layout.addRow('', startForWebEmail)
        self.webemail.setLayout(layout)


        self.setTabText(1,"WEB EMAIL")

    def socialmailUI(self):
        layout = QFormLayout()
        labelForKey= QLabel('Keyword/Category/Job title')
        # labelForKey.setStyleSheet('margin-top: 10px')
        layout.addRow('', labelForKey) 
        EditForKey= QLineEdit()
        # EditForKey.setStyleSheet('margin-bottom: 5px')
        layout.addRow('', EditForKey)
        labelForLocation= QLabel('Location(Optional)')
        layout.addRow('', labelForLocation)
        EditForLocation= QLineEdit()
        # EditForLocation.setStyleSheet('margin-bottom: 5px')
        layout.addRow('', EditForLocation)
        labelForSelctSocial= QLabel('Select Social Network')
        layout.addRow('', labelForSelctSocial)
        selectSocial= QComboBox()
        selectSocial.addItem('Instagram.com')
        selectSocial.addItem('Facebook.com')
        selectSocial.addItem('Linkedin.com')
        selectSocial.addItem('Twitter.com')
        # selectSocial.setStyleSheet('margin-bottom: 5px')
        layout.addRow('', selectSocial)
        labelForCountry= QLabel('Country')
        layout.addRow('', labelForCountry)
        EditForCountry= QLineEdit()
        # EditForCountry.setStyleSheet('margin-bottom: 5px')
        layout.addRow('', EditForCountry)
        labelForEngine= QLabel('Select search engine')
        layout.addRow('', labelForEngine )
        selectEngine= QComboBox()
        selectEngine.addItem('Google')
        selectEngine.addItem('Yahoo')
        selectEngine.addItem('Bing')
        # selectEngine.setStyleSheet('margin-bottom: 5px')
        layout.addRow('', selectEngine)
        labelForEmailType= QLabel('Email type for search')
        layout.addRow('', labelForEmailType)
        selectForEmailType= QComboBox()
        selectForEmailType.addItem('@gmail.com, @yahoo.com, @outlook.com, @zoho.com, @hotmail.com')
        selectForEmailType.addItem('@gmail.com')
        selectForEmailType.addItem('@yahoo.com')
        selectForEmailType.addItem('@outlook.com')
        selectForEmailType.addItem('@zoho.com')
        selectForEmailType.setStyleSheet('margin-bottom: 5px')
        layout.addRow('', selectForEmailType)
        labelForPageNum= QLabel('Please type Page count(optional)')
        layout.addRow('', labelForPageNum )
        EditForPageNum= QLineEdit()
        # EditForPageNum.setStyleSheet('margin-bottom: 5px')
        layout.addRow('', EditForPageNum)

        labelForPath= QLabel('Please choose file path to save(optional)')
        # labelForPath.setStyleSheet('margin-top: 5px; margin-bottom: 5px')
        layout.addRow('', labelForPath)

        # This is save path part
        savePathForm= QFormLayout()
        # EditForFileName= QLineEdit('scrap')
        # EditForFileName.setStyleSheet('margin-bottom:5px')
        # savePathForm.addRow(QLabel('File Name'), EditForFileName)

        nowPath= os.path.dirname(os.path.abspath(__file__))
        print(nowPath)

        savePathBtn= QPushButton('Driver Location')
        savePathBtn.setFixedWidth(100)
        savePathBtn.setFixedHeight(30)
        savePathBtn.setStyleSheet('background-color: #526ee7; color: #dbdbdb; border-radius: 3px')
        savePath= QLineEdit()
        savePath.setText(nowPath+'/save.csv')
        savePath.setStyleSheet('margin-bottom:15px')
        savePathBtn.clicked.connect(partial(self.filePathSelect, savePath))
        savePathForm.addRow(savePathBtn, savePath)
        # hbox = QHBoxLayout()

        # rCsv = QRadioButton("CSV")
        # rCsv.setChecked(True)
        # rXls = QRadioButton("XLS")
        # hbox.addWidget(rCsv)
        # hbox.addWidget(rXls)
        # hbox.addStretch()
        # labelForType= QLabel('Export File Type')
        # labelForType.setStyleSheet('margin-bottom:15px')
        # savePathForm.addRow(labelForType, hbox)
        

        layout.addRow('', savePathForm)
        startForSocial= QPushButton(self.webemail)
        startForSocial.setText('Start')
        startForSocial.setFixedWidth(100)
        startForSocial.setFixedHeight(30)
        startForSocial.setStyleSheet('background-color: #526ee7; color: #dbdbdb; border-radius: 3px')
        layout.addRow(QLabel(''), startForSocial)
        self.setTabText(2,"SOCIAL MAIL")
        self.socialmail.setLayout(layout)

        startForSocial.clicked.connect(partial(self.socialBoolScrapTrigger, EditForKey, EditForLocation, selectSocial, EditForCountry, selectEngine, selectForEmailType, EditForPageNum, savePath))

    def filePathSelect(self, savePath):
        dlg= QFileDialog()
        filePath= dlg.getSaveFileName(self, "save file", "save.csv", "csv file(*.csv);;xls file(*.xls)")
        print(filePath)
        savePath.setText(filePath[0])
        
    

    def googlemapUI(self):
        layout= QFormLayout()
        labelForDesc= QLabel("Please enter any googlemap's url where you want to scrap from.")
        # labelForDesc.setStyleSheet('margin-top: 10px')
        layout.addRow('', labelForDesc)
        eidtForGoogleMap= QLineEdit()
        # eidtForGoogleMap.setStyleSheet('margin-bottom:10px')
        layout.addRow('', eidtForGoogleMap)

        labelForPageNum= QLabel('Please type Page count(optional)')
        layout.addRow('', labelForPageNum )
        EditForPageNum= QLineEdit()
        # EditForPageNum.setStyleSheet('margin-bottom: 10px')
        layout.addRow('', EditForPageNum)

        # This is save path part
        labelForPath= QLabel('Please choose file path to save(optional)')
        # labelForPath.setStyleSheet(' margin-bottom: 10px')
        layout.addRow('', labelForPath)

        
        savePathForm= QFormLayout()

        nowPath= os.path.dirname(os.path.abspath(__file__))
        print(nowPath)

        savePathBtn= QPushButton('Driver Location')
        savePathBtn.setFixedWidth(100)
        savePathBtn.setFixedHeight(30)
        savePathBtn.setStyleSheet('background-color: #526ee7; color: #dbdbdb; border-radius: 3px')
        savePath= QLineEdit()
        savePath.setText(nowPath+'/save.csv')
        savePath.setStyleSheet('margin-bottom:15px')
        savePathBtn.clicked.connect(partial(self.filePathSelect, savePath))
        savePathForm.addRow(savePathBtn, savePath)
        
        layout.addRow('', savePathForm)
        startForGoogleMap= QPushButton(self.webemail)
        startForGoogleMap.setText('Start')
        startForGoogleMap.setFixedWidth(100)
        startForGoogleMap.setFixedHeight(30)
        startForGoogleMap.setStyleSheet('background-color: #526ee7; color: #dbdbdb; border-radius: 3px')
        layout.addRow(QLabel(''), startForGoogleMap)
        self.setTabText(3,"GOOGLE MAP")
        self.googlemap.setLayout(layout)
		
        startForGoogleMap.clicked.connect(partial(self.googlemapScrapTrigger, eidtForGoogleMap, EditForPageNum, savePath))

        

    def yellowpageUI(self):
        layout= QFormLayout()
        labelForDesc= QLabel("Please enter any yellow page's url where you want to scrap from.")
        # labelForDesc.setStyleSheet('margin-top: 10px')
        layout.addRow('', labelForDesc)
        eidtForYellowPage= QLineEdit()
        # eidtForYellowPage.setStyleSheet('margin-bottom:10px')
        layout.addRow('', eidtForYellowPage)

        labelForPageNum= QLabel('Please type Page count(optional)')
        layout.addRow('', labelForPageNum )
        EditForPageNum= QLineEdit()
        # EditForPageNum.setStyleSheet('margin-bottom: 10px')
        layout.addRow('', EditForPageNum)

        # This is save path part
        labelForPath= QLabel('Please choose file path to save(optional)')
        # labelForPath.setStyleSheet(' margin-bottom: 10px')
        layout.addRow('', labelForPath)

        
        savePathForm= QFormLayout()

        nowPath= os.path.dirname(os.path.abspath(__file__))

        savePathBtn= QPushButton('Driver Location')
        savePathBtn.setFixedWidth(100)
        savePathBtn.setFixedHeight(30)
        savePathBtn.setStyleSheet('background-color: #526ee7; color: #dbdbdb; border-radius: 3px')
        savePath= QLineEdit()
        savePath.setText(nowPath+'/save.csv')
        savePath.setStyleSheet('margin-bottom:15px')
        savePathBtn.clicked.connect(partial(self.filePathSelect, savePath))
        savePathForm.addRow(savePathBtn, savePath)
        
        layout.addRow('', savePathForm)
        startForYellowPage= QPushButton(self.webemail)
        startForYellowPage.setText('Start')
        startForYellowPage.setFixedWidth(100)
        startForYellowPage.setFixedHeight(30)
        startForYellowPage.setStyleSheet('background-color: #526ee7; color: #dbdbdb; border-radius: 3px')
        layout.addRow(QLabel(''), startForYellowPage)
        self.setTabText(4,"YELLOW PAGE")
        self.yellowpage.setLayout(layout)

        startForYellowPage.clicked.connect(partial(self.yellowpageScrapTrigger, eidtForYellowPage, EditForPageNum, savePath))



    def yelppageUI(self):
        layout= QFormLayout()
        labelForDesc= QLabel("Please enter any yelp page's url where you want to scrap from.")
        # labelForDesc.setStyleSheet('margin-top: 10px')
        layout.addRow('', labelForDesc)
        eidtForYelpPage= QLineEdit()
        # eidtForYelpPage.setStyleSheet('margin-bottom:10px')
        layout.addRow('', eidtForYelpPage)

        labelForPageNum= QLabel('Please type Page count(optional)')
        layout.addRow('', labelForPageNum )
        EditForPageNum= QLineEdit()
        # EditForPageNum.setStyleSheet('margin-bottom: 10px')
        layout.addRow('', EditForPageNum)

        # This is save path part
        labelForPath= QLabel('Please choose file path to save(optional)')
        # labelForPath.setStyleSheet(' margin-bottom: 10px')
        layout.addRow('', labelForPath)

        
        savePathForm= QFormLayout()

        nowPath= os.path.dirname(os.path.abspath(__file__))

        savePathBtn= QPushButton('Driver Location')
        savePathBtn.setFixedWidth(100)
        savePathBtn.setFixedHeight(30)
        savePathBtn.setStyleSheet('background-color: #526ee7; color: #dbdbdb; border-radius: 3px')
        savePath= QLineEdit()
        savePath.setText(nowPath+'/save.csv')
        savePath.setStyleSheet('margin-bottom:15px')
        savePathBtn.clicked.connect(partial(self.filePathSelect, savePath))
        savePathForm.addRow(savePathBtn, savePath)
        
        layout.addRow('', savePathForm)
        startForYelpPage= QPushButton(self.webemail)
        startForYelpPage.setText('Start')
        startForYelpPage.setFixedWidth(100)
        startForYelpPage.setFixedHeight(30)
        startForYelpPage.setStyleSheet('background-color: #526ee7; color: #dbdbdb; border-radius: 3px')
        layout.addRow(QLabel(''), startForYelpPage)
        self.setTabText(5,"YELP PAGE")
        self.yelppage.setLayout(layout)

        startForYelpPage.clicked.connect(partial(self.yelppageScrapTrigger, eidtForYelpPage, EditForPageNum, savePath))


    def linkedinnavUI(self):
        layout = QFormLayout()

        labelForUsername= QLabel('Linkedin Username')
        # labelForUsername.setStyleSheet('margin-top:30px; margin-bottom: 5px')
        layout.addRow('', labelForUsername)
        username= QLineEdit()
        # username.setStyleSheet(" margin-bottom: 15px")
        layout.addRow('', username)
        labelForPass= QLabel('Linkedin Password')
        # labelForPass.setStyleSheet('margin-bottom: 5px')
        layout.addRow('', labelForPass)
        password= QLineEdit()
        # password.setStyleSheet("margin-bottom: 15px")
        layout.addRow('', password)
        labelForIntendedUrl= QLabel('Intended Url')
        # labelForIntendedUrl.setStyleSheet('margin-bottom: 5px')
        layout.addRow('', labelForIntendedUrl)
        intendedUrl= QLineEdit()
        # intendedUrl.setStyleSheet("margin-bottom: 15px")
        layout.addRow('', intendedUrl)
        labelForPageNum= QLabel('Please type Page count(optional)')
        # labelForPageNum.setStyleSheet('margin-bottom: 5px')
        layout.addRow('', labelForPageNum )
        EditForPageNum= QLineEdit()
        # EditForPageNum.setStyleSheet('margin-bottom: 15px')
        layout.addRow('', EditForPageNum)

        # This is save path part
        labelForPath= QLabel('Please choose file path to save(optional)')
        # labelForPath.setStyleSheet(' margin-bottom: 5px')
        layout.addRow('', labelForPath)

        
        savePathForm= QFormLayout()

        nowPath= os.path.dirname(os.path.abspath(__file__))

        savePathBtn= QPushButton('Driver Location')
        savePathBtn.setFixedWidth(100)
        savePathBtn.setFixedHeight(30)
        savePathBtn.setStyleSheet('background-color: #526ee7; color: #dbdbdb; border-radius: 3px')
        savePath= QLineEdit()
        savePath.setText(nowPath+'/save.csv')
        savePath.setStyleSheet('margin-bottom:15px')
        savePathBtn.clicked.connect(partial(self.filePathSelect, savePath))
        savePathForm.addRow(savePathBtn, savePath)
        
        layout.addRow('', savePathForm)
        

        startForLinkedinNav= QPushButton('Start')
        startForLinkedinNav.setFixedWidth(100)
        startForLinkedinNav.setFixedHeight(30)
        startForLinkedinNav.setStyleSheet('background-color: #526ee7; color: #dbdbdb; border-radius: 3px')
        layout.addRow(QLabel(), startForLinkedinNav)

        self.setTabText(7,"SALES NAV")
        self.linkedinnav.setLayout(layout)
        startForLinkedinNav.clicked.connect(partial(self.linkedinNavScrapTrigger, username, password, intendedUrl, EditForPageNum, savePath))



    def linkedingeneralUI(self):
        layout = QFormLayout()

        labelForUsername= QLabel('Linkedin Username')
        # labelForUsername.setStyleSheet('margin-top:30px; margin-bottom: 5px')
        layout.addRow('', labelForUsername)
        username= QLineEdit()
        # username.setStyleSheet(" margin-bottom: 15px")
        layout.addRow('', username)
        labelForPass= QLabel('Linkedin Password')
        # labelForPass.setStyleSheet('margin-bottom: 5px')
        layout.addRow('', labelForPass)
        password= QLineEdit()
        # password.setStyleSheet("margin-bottom: 15px")
        layout.addRow('', password)
        labelForIntendedUrl= QLabel('Intended Url')
        # labelForIntendedUrl.setStyleSheet('margin-bottom: 5px')
        layout.addRow('', labelForIntendedUrl)
        intendedUrl= QLineEdit()
        # intendedUrl.setStyleSheet("margin-bottom: 15px")
        layout.addRow('', intendedUrl)
        labelForPageNum= QLabel('Please type Page count(optional)')
        # labelForPageNum.setStyleSheet('margin-bottom: 5px')
        layout.addRow('', labelForPageNum )
        EditForPageNum= QLineEdit()
        # EditForPageNum.setStyleSheet('margin-bottom: 15px')
        layout.addRow('', EditForPageNum)

        # This is save path part
        labelForPath= QLabel('Please choose file path to save(optional)')
        # labelForPath.setStyleSheet(' margin-bottom: 5px')
        layout.addRow('', labelForPath)

        
        savePathForm= QFormLayout()

        nowPath= os.path.dirname(os.path.abspath(__file__))

        savePathBtn= QPushButton('Driver Location')
        savePathBtn.setFixedWidth(100)
        savePathBtn.setFixedHeight(30)
        savePathBtn.setStyleSheet('background-color: #526ee7; color: #dbdbdb; border-radius: 3px')
        savePath= QLineEdit()
        savePath.setText(nowPath+'/save.csv')
        savePath.setStyleSheet('margin-bottom:15px')
        savePathBtn.clicked.connect(partial(self.filePathSelect, savePath))
        savePathForm.addRow(savePathBtn, savePath)
        
        layout.addRow('', savePathForm)
        

        startForLinkedinGeneral= QPushButton('Start')
        startForLinkedinGeneral.setFixedWidth(100)
        startForLinkedinGeneral.setFixedHeight(30)
        startForLinkedinGeneral.setStyleSheet('background-color: #526ee7; color: #dbdbdb; border-radius: 3px')
        layout.addRow(QLabel(), startForLinkedinGeneral)

        self.setTabText(6,"LINKEDIN")
        self.linkedingeneral.setLayout(layout)
        startForLinkedinGeneral.clicked.connect(partial(self.linkedinGeneralScrapTrigger, username, password, intendedUrl, EditForPageNum, savePath))


    def webemailScrapTrigger(self, urlEdit):
        scrap= WebEmailScrape()
        # this is validation part for website email scrap
        if('http' in urlEdit.text() and len(urlEdit.text())> 8):
            # _thread.start_new_thread(scrap.webEmailScrape, (urlEdit.text(),))
            scrap.start(urlEdit.text())
        else:
            self.showdialog('Error', 'Url Error', 'Please type valid url!')

    def socialBoolScrapTrigger(self, EditForKey, EditForLocation, selectSocial, EditForCountry, selectEngine, selectForEmailType, EditForPageNum, savePath):
        defaultPageNum= 30

        scrap= SocialBooleanScrap()
        # this is validation part for social boolean scrap
        if(EditForKey.text()== ''):
            self.showdialog('Validation', 'Keyword Missed', 'Please type Keyword!')
            return 0
        elif(len(savePath.text())<5):
            self.showdialog('Validation', 'File Path Error', 'Please type correct path!')
            return 0
        elif(len(savePath.text())>4 and (savePath.text()[-4:]!= '.csv' and savePath.text()[-4:]!= '.xls')):
            self.showdialog('Validation', 'File extension Error', "Please use '.csv' or '.xls' extension")
            return 0
        elif(EditForPageNum.text()!= ''):
            if EditForPageNum.text().isdigit()!= True:
                self.showdialog('Validation', 'Page Count Error', 'Please type integer!')
                return 0
            elif (EditForPageNum.text().isdigit()== True) and (int(EditForPageNum.text())> 50):
                self.showdialog('Validation', 'Page Limit Error', 'Please insert number lower than 50!')
                return 0
            elif (EditForPageNum.text().isdigit()== True) and (int(EditForPageNum.text())== 0):
                self.showdialog('Validation', 'Page Limit Error', 'Please insert number greater than 1!')
                return 0
            else:
                scrap.start(EditForKey.text(), EditForLocation.text(), selectSocial.currentText(), EditForCountry.text(), selectEngine.currentText(), selectForEmailType.currentText(), int(EditForPageNum.text()), savePath.text())
        else:
            scrap.start(EditForKey.text(), EditForLocation.text(), selectSocial.currentText(), EditForCountry.text(), selectEngine.currentText(), selectForEmailType.currentText(), defaultPageNum, savePath.text())

    def googlemapScrapTrigger(self, urlEdit, EditForPageNum, savePath):
        scrap= GoogleMapScrap()
        defaultPageNum= 30

        # this is validation part for website email scrap
        if(urlEdit.text()== ''):
            self.showdialog('Validation', 'Url Missed', 'Please type Url!')
            return 0
        elif('http' not in urlEdit.text() or len(urlEdit.text())<9 ):
            self.showdialog('Validation', 'Url Error', 'Please type valid url!')
            return 0
        elif(len(savePath.text())<5):
            self.showdialog('Validation', 'File Path Error', 'Please type correct path!')
            return 0
        elif(len(savePath.text())>4 and (savePath.text()[-4:]!= '.csv' and savePath.text()[-4:]!= '.xls')):
            self.showdialog('Validation', 'File extension Error', "Please use '.csv' or '.xls' extension")
            return 0
        elif(EditForPageNum.text()!= ''):
            if EditForPageNum.text().isdigit()!= True:
                self.showdialog('Validation', 'Page Count Error', 'Please type integer!')
                return 0
            elif (EditForPageNum.text().isdigit()== True) and (int(EditForPageNum.text())> 50):
                self.showdialog('Validation', 'Page Limit Error', 'Please insert number lower than 50!')
                return 0
            elif (EditForPageNum.text().isdigit()== True) and (int(EditForPageNum.text())== 0):
                self.showdialog('Validation', 'Page Limit Error', 'Please insert number greater than 1!')
                return 0
            else:
                scrap.start(urlEdit.text(), int(EditForPageNum.text()), savePath.text())

        else:
            scrap.start(urlEdit.text(), defaultPageNum, savePath.text())


    def yelppageScrapTrigger(self, urlEdit, EditForPageNum, savePath):
        scrap= YelpPageScrap()
        defaultPageNum= 30

        # this is validation part for website email scrap
        if(urlEdit.text()== ''):
            self.showdialog('Validation', 'Url Missed', 'Please type Url!')
            return 0
        elif('http' not in urlEdit.text() or len(urlEdit.text())<9 ):
            self.showdialog('Validation', 'Url Error', 'Please type valid url!')
            return 0
        elif(len(savePath.text())<5):
            self.showdialog('Validation', 'File Path Error', 'Please type correct path!')
            return 0
        elif(len(savePath.text())>4 and (savePath.text()[-4:]!= '.csv' and savePath.text()[-4:]!= '.xls')):
            self.showdialog('Validation', 'File extension Error', "Please use '.csv' or '.xls' extension")
            return 0
        elif(EditForPageNum.text()!= ''):
            if EditForPageNum.text().isdigit()!= True:
                self.showdialog('Validation', 'Page Count Error', 'Please type integer!')
                return 0
            elif (EditForPageNum.text().isdigit()== True) and (int(EditForPageNum.text())> 50):
                self.showdialog('Validation', 'Page Limit Error', 'Please insert number lower than 50!')
                return 0
            elif (EditForPageNum.text().isdigit()== True) and (int(EditForPageNum.text())== 0):
                self.showdialog('Validation', 'Page Limit Error', 'Please insert number greater than 1!')
                return 0
            else:
                scrap.start(urlEdit.text(), int(EditForPageNum.text()), savePath.text())

        else:
            scrap.start(urlEdit.text(), defaultPageNum, savePath.text())


    def yellowpageScrapTrigger(self, urlEdit, EditForPageNum, savePath):
        scrap= YellowPageScrap()
        defaultPageNum= 30

        # this is validation part for website email scrap
        if(urlEdit.text()== ''):
            self.showdialog('Validation', 'Url Missed', 'Please type Url!')
            return 0
        elif('http' not in urlEdit.text() or len(urlEdit.text())<9 ):
            self.showdialog('Validation', 'Url Error', 'Please type valid url!')
            return 0
        elif(len(savePath.text())<5):
            self.showdialog('Validation', 'File Path Error', 'Please type correct path!')
            return 0
        elif(len(savePath.text())>4 and (savePath.text()[-4:]!= '.csv' and savePath.text()[-4:]!= '.xls')):
            self.showdialog('Validation', 'File extension Error', "Please use '.csv' or '.xls' extension")
            return 0
        elif(EditForPageNum.text()!= ''):
            if EditForPageNum.text().isdigit()!= True:
                self.showdialog('Validation', 'Page Count Error', 'Please type integer!')
                return 0
            elif (EditForPageNum.text().isdigit()== True) and (int(EditForPageNum.text())> 50):
                self.showdialog('Validation', 'Page Limit Error', 'Please insert number lower than 50!')
                return 0
            elif (EditForPageNum.text().isdigit()== True) and (int(EditForPageNum.text())== 0):
                self.showdialog('Validation', 'Page Limit Error', 'Please insert number greater than 1!')
                return 0
            else:
                scrap.start(urlEdit.text(), int(EditForPageNum.text()), savePath.text())

        else:
            scrap.start(urlEdit.text(), defaultPageNum, savePath.text())

    def linkedinGeneralScrapTrigger(self, username, password, intendedUrl, EditForPageNum, savePath):
        scrap= LinkedinGeneralScrap()
        defaultPageNum= 30
        if(username.text()== ''):
            self.showdialog('Validation', 'User name Missed', 'Please type user name!')
            return 0
        elif(password.text()== ''):
            self.showdialog('Validation', 'Password Missed', 'Please type password!')
        elif('http' not in intendedUrl.text() or len(intendedUrl.text())<9 ):
            self.showdialog('Validation', 'Url Error', 'Please type valid url!')
            return 0
        elif(len(savePath.text())<5):
            self.showdialog('Validation', 'File Path Error', 'Please type correct path!')
            return 0
        elif(len(savePath.text())>4 and (savePath.text()[-4:]!= '.csv' and savePath.text()[-4:]!= '.xls')):
            self.showdialog('Validation', 'File extension Error', "Please use '.csv' or '.xls' extension")
            return 0
        elif(EditForPageNum.text()!= ''):
            if EditForPageNum.text().isdigit()!= True:
                self.showdialog('Validation', 'Page Count Error', 'Please type integer!')
                return 0
            elif (EditForPageNum.text().isdigit()== True) and (int(EditForPageNum.text())> 50):
                self.showdialog('Validation', 'Page Limit Error', 'Please insert number lower than 50!')
                return 0
            elif (EditForPageNum.text().isdigit()== True) and (int(EditForPageNum.text())== 0):
                self.showdialog('Validation', 'Page Limit Error', 'Please insert number greater than 1!')
                return 0
            else:
                scrap.start(username.text(), password.text(), intendedUrl.text(), int(EditForPageNum.text()), savePath.text())

        else:
            scrap.start(username.text(), password.text(), intendedUrl.text(), defaultPageNum, savePath.text())

    def linkedinNavScrapTrigger(self, username, password, intendedUrl, EditForPageNum, savePath):
        scrap= LinkedinNavScrap()
        defaultPageNum= 30
        if(username.text()== ''):
            self.showdialog('Validation', 'User name Missed', 'Please type user name!')
            return 0
        elif(password.text()== ''):
            self.showdialog('Validation', 'Password Missed', 'Please type password!')
        elif('http' not in intendedUrl.text() or len(intendedUrl.text())<9 ):
            self.showdialog('Validation', 'Url Error', 'Please type valid url!')
            return 0
        elif(len(savePath.text())<5):
            self.showdialog('Validation', 'File Path Error', 'Please type correct path!')
            return 0
        elif(len(savePath.text())>4 and (savePath.text()[-4:]!= '.csv' and savePath.text()[-4:]!= '.xls')):
            self.showdialog('Validation', 'File extension Error', "Please use '.csv' or '.xls' extension")
            return 0
        elif(EditForPageNum.text()!= ''):
            if EditForPageNum.text().isdigit()!= True:
                self.showdialog('Validation', 'Page Count Error', 'Please type integer!')
                return 0
            elif (EditForPageNum.text().isdigit()== True) and (int(EditForPageNum.text())> 50):
                self.showdialog('Validation', 'Page Limit Error', 'Please insert number lower than 50!')
                return 0
            elif (EditForPageNum.text().isdigit()== True) and (int(EditForPageNum.text())== 0):
                self.showdialog('Validation', 'Page Limit Error', 'Please insert number greater than 1!')
                return 0
            else:
                scrap.start(username.text(), password.text(), intendedUrl.text(), int(EditForPageNum.text()), savePath.text())

        else:
            scrap.start(username.text(), password.text(), intendedUrl.text(), defaultPageNum, savePath.text())


    def showdialog(self, wintitle, title, desc, icon= 'warn'):
        msg = QMessageBox()
        msg.setStyleSheet("background-color:#303030; color:#dddddd")
        if icon== 'warn':
            msg.setIcon(QMessageBox.Warning)
        elif icon== 'info':
            msg.setIcon(QMessageBox.Information)
        elif icon== 'critical':
            msg.setIcon(QMessageBox.Critical)
        elif icon== 'que':
            msg.setIcon(QMessageBox.Question)
        msg.setText(title)
        msg.setInformativeText(desc)
        msg.setWindowTitle(wintitle)
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # msg.buttonClicked.connect(msgbtn)
        msg.exec_()
      

class totalpage(QWidget):
    def __init__(self, parent = None):
        super(totalpage, self).__init__(parent)
        self.title= 'Power Scrap'
        self.setWindowTitle(self.title)
        self.userEmail= ''
        self.tmpPath = self.resource_path('data')
        self.loginStatus= False
        self.setStyleSheet("background-color: #282828;")
        splitter1 = QSplitter()
        splitter1.setOrientation(Qt.Vertical)
        header= QFrame(splitter1)
        header.setFixedHeight(50)
        header.setStyleSheet("background-color: #3A3A3A;")
        header.setFrameShape(QFrame.StyledPanel)
        layoutForHead= QHBoxLayout(self)
        layoutForHead.addStretch(0)
        btnSuper= QPushButton('UPGRADE')
        btnSuper.setFixedWidth(100)
        btnSuper.setFixedHeight(32)
        btnSuper.setStyleSheet('background-color: #fd6331; color: #dbdbdb; border-radius: 3px; font-weight: bold;')
        layoutForHead.addWidget(btnSuper)
        self.btnLogin= QPushButton('LOGIN')
        self.btnLogin.setFixedWidth(100)
        self.btnLogin.setFixedHeight(32)
        self.btnLogin.setStyleSheet('background-color: #303030; color: #dbdbdb; border-radius: 3px; border: 0.5px solid #666666; font-weight: bold')
        if self.loginStatus== True:
            self.btnLogin.setText('LOGOUT')
        self.btnLogin.clicked.connect(self.loginUI)
        layoutForHead.addWidget(self.btnLogin)
        header.setLayout(layoutForHead)

        body = QFrame(splitter1)
        body.setFrameShape(QFrame.StyledPanel)
        layoutForBody= QHBoxLayout(self)
        self.tab= tabdemo()
        # self.tab.setTabIcon(self.tab.tabdash, QIcon("lock2.png"))
        # self.tab.setIconSize(QSize(15, 15)) 
        # self.tab.setTabIcon(self.tab.tabdash, QIcon(""))

        # self.setdisableAllTab(False)



        layoutForBody.addWidget(self.tab)
        body.setLayout(layoutForBody)
        hbox= QHBoxLayout(self)
        hbox.addWidget(splitter1)
        self.setFixedWidth(898)
        # self.setMinimumSize(800, 700)
        # self.setFixedHeight(550)
        self.show()
        # self.showdownload('Note', 'Do you have chrome driver with same chrome version?', 'You have to use same driver version with chrome browser to use this tool. Press "No" to download', 'info')

    # def showdownload(self, wintitle, title, desc, icon= 'warn'):
    #     msg = QMessageBox()
    #     msg.setStyleSheet("background-color:#303030; color:#dddddd")
    #     if icon== 'warn':
    #         msg.setIcon(QMessageBox.Warning)
    #     elif icon== 'info':
    #         msg.setIcon(QMessageBox.Information)
    #     elif icon== 'critical':
    #         msg.setIcon(QMessageBox.Critical)
    #     elif icon== 'que':
    #         msg.setIcon(QMessageBox.Question)
    #     msg.setText(title)
    #     msg.setInformativeText(desc)
    #     msg.setWindowTitle(wintitle)
    #     # msg.setDetailedText("The details are as follows:")
    #     msg.setStandardButtons(QMessageBox.Yes)
    #     msg.addButton(QMessageBox.No)
    #     # msg.buttonClicked.connect(msgbtn)
    #     if(msg.exec_()==QMessageBox.No):
    #         webbrowser.open('https://chromedriver.chromium.org/downloads', new=2)


    def closeEvent(self, event):
        msg = QMessageBox()
        msg.setStyleSheet("background-color:#303030; color:#dddddd")
        msg.setText('Are you sure to close the window?')
        msg.setWindowTitle('Window Close')
        msg.setIcon(QMessageBox.Question)
        msg.setInformativeText('It will automatically logged out.')
        msg.setStandardButtons(QMessageBox.Yes)
        msg.addButton(QMessageBox.No)
        # msg.buttonClicked.connect(msgbtn)
        if(msg.exec_()==QMessageBox.Yes):
            if(self.userEmail!= ''):
                self.logout()
            event.accept()
        else:
            event.ignore()
        # self.showCloseDlg('Window Close', 'Are you sure to close the window?', 'It will automatically logged out.', 'que')

        # msg= QMessageBox()
        # msg.setStyleSheet('color: white;')
        # reply = msg.question(self, 'Window Close', 'Are you sure you want to close the window?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    
        # if reply == QMessageBox.Yes:
        #     # when cloe, will be loged out
        #     if(self.userEmail!= ''):
        #         self.logout()
        #     event.accept()
        #     print('Window closed')
        # else:
        #     event.ignore()
    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def setdisableAllTab(self, status):
        self.tab.setIconSize(QSize(25, 25))
        # self.tab.setTabIcon(self.tab.tabWeb, QIcon(self.tmpPath+"\\lock2.ico"))
        self.tab.setTabIcon(self.tab.tabSocial, QIcon(self.tmpPath+"\\lock2.ico"))
        self.tab.setTabIcon(self.tab.tabGMap, QIcon(self.tmpPath+"\\lock2.ico"))
        self.tab.setTabIcon(self.tab.tabYelp, QIcon(self.tmpPath+"\\lock2.ico"))
        self.tab.setTabIcon(self.tab.tabYellow, QIcon(self.tmpPath+"\\lock2.ico"))
        self.tab.setTabIcon(self.tab.tabLinkedin, QIcon(self.tmpPath+"\\lock2.ico"))
        self.tab.setTabIcon(self.tab.tabSalesNav, QIcon(self.tmpPath+"\\lock2.ico"))
        for i in range(6):
            self.tab.setTabEnabled(i+2, status)

    def setLoginTab(self, package):
        if package['website_email']== 1:
            self.tab.setTabEnabled(1, True)
            self.tab.setTabIcon(self.tab.tabWeb, QIcon(""))
        if package['google_map']== 1:
            self.tab.setTabEnabled(3, True)
            self.tab.setTabIcon(self.tab.tabGMap, QIcon(""))
        if package['social_email']== 1:
            self.tab.setTabEnabled(2, True)
            self.tab.setTabIcon(self.tab.tabSocial, QIcon(""))
        if package['yelp_page']== 1:
            self.tab.setTabEnabled(5, True)
            self.tab.setTabIcon(self.tab.tabYelp, QIcon(""))
        if package['yellow_page']== 1:
            self.tab.setTabEnabled(4, True)
            self.tab.setTabIcon(self.tab.tabYellow, QIcon(""))
        if package['linkedin_gen_search']== 1:
            self.tab.setTabEnabled(6, True)
            self.tab.setTabIcon(self.tab.tabLinkedin, QIcon(""))
        if package['linkedin_sales_nav']== 1:
            self.tab.setTabEnabled(7, True)
            self.tab.setTabIcon(self.tab.tabSalesNav, QIcon(""))

    # def setSuperTab(self, status):
    #     for i in range(5):
    #         self.tab.setTabEnabled(i+3, status)

    def loginUI(self):
        if self.btnLogin.text()== 'LOGIN':
            self.loginDg = QDialog()
            self.loginDg.setStyleSheet("background-color: #282828")
            # self.loginDg.setMinimumSize(300, 200)
            # self.loginDg.resize(300, 200)
            layout= QFormLayout()
            email= QLineEdit()
            email.setStyleSheet("color: #dbdbdb; selection-background-color:#3a3a3a; height: 25px; width: 200px; border: 0.5px solid #666666;")
            labelForEmail= QLabel('Email')
            labelForEmail.setStyleSheet('color: #dbdbdb')
            layout.addRow(labelForEmail, email)

            password= QLineEdit()
            password.setStyleSheet("color: #dbdbdb; selection-background-color:#3a3a3a; height: 25px; width: 200px; border: 0.5px solid #666666;")
            password.setEchoMode(QLineEdit.Password)
            labelForPass= QLabel('Password')
            labelForPass.setStyleSheet('color: #dbdbdb')
            layout.addRow(labelForPass, password)
            btnLogin= QPushButton("LOGIN")
            btnLogin.setStyleSheet("color: #dbdbdb; background-color:#fd6331")
            btnLogin.clicked.connect(partial(self.login, email, password))
            # btnLogin.setStyleSheet('margin-bottom: 5px')
            layout.addRow(QLabel(), btnLogin)
            btnRegister= QPushButton('REGISTER')
            btnRegister.setStyleSheet("color: #dbdbdb; background-color: #3a3a3a")

            # this is register part
            # btnRegister.clicked.connect(self.registerUI)
            labelForRegister= QLabel("Didn't register?")
            labelForRegister.setStyleSheet('color: #dbdbdb')

            # labelForRegister.setStyleSheet('margin-top: 10px')
            # btnRegister.setStyleSheet('margin-top: 10px')
            layout.addRow(labelForRegister, btnRegister)
            self.loginDg.setLayout(layout)
            self.loginDg.setWindowTitle("Login")
            self.loginDg.setWindowModality(Qt.ApplicationModal)

            self.loginDg.exec_()
        elif self.btnLogin.text()== 'LOGOUT':
            self.logout()

    def login(self, email, password):
        loginUrl= 'https://scrap.rapasshop.com/login'
        if(email.text()== '' or password.text()== ''):
            self.showdialog('Validation', 'Validation Error', 'You must fill out all fields!')
        else:
            self.userEmail= email.text()
            ip= self.getIp()
            uuidOfCom= self.getUUID()
            PARAMS= {
                'email': email.text(),
                'password': password.text(),
                'ip': str(ip),
                'uuidCom': str(uuidOfCom)
                }
            print(PARAMS)
            try:
                r= requests.get(url= loginUrl, params= PARAMS)
                print(r)
                package= r.json()
                self.setLoginTab(package)
                self.loginStatus= True
                # _thread.start_new_thread( self.alertWhileLogedin, () )
                self.btnLogin.setText('LOGOUT')
                self.showLoginSuccessdialog()
            except:
                try:
                    if(r.text== "already logedin"):
                        self.showdialog('Error', 'Logedin Status', 'You are already loged in using another. Please logout for that tool and try again!')
                    elif(r.text== "invalid user"):
                        self.showdialog('Error', 'Invalid user', 'You are not registered!', 'critical')
                    else:
                        self.showdialog('Error', 'Something went wrong from server!', 'critical')
                except:
                    self.showdialog('Error', 'Server side', 'There is no respond from server. Please Retry after server run.')

    def alertWhileLogedin(self):
        alertUrl= 'https://scrap.rapasshop.com/alertLoginStatus'
        PARAMS= {
            'email': self.userEmail
            }
        while True:
            requests.get(url= alertUrl, params= PARAMS)
            time.sleep(30)

    def getIp(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip= s.getsockname()[0]
        s.close()
        return ip

    def getUUID(self):
        s= uuid.UUID(int=uuid.getnode())
        return s

    def showLoginSuccessdialog(self):
        msg = QMessageBox()
        msg.setStyleSheet("background-color:#303030; color:#dddddd")
        msg.setIcon(QMessageBox.Information)
        msg.setText('Success')
        msg.setInformativeText('Successfully loged in!')
        msg.setWindowTitle('Login Success')
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.closeLoginDlg)
        msg.exec_()

    def closeLoginDlg(self):
        self.loginDg.close()
    
    def logout(self):
        logoutUrl= 'http://scrap.rapasshop.com/logout'
        r= requests.get(url= logoutUrl, params= {'email': self.userEmail})
        if(r.text== "logout success"):
            self.setdisableAllTab(False)
            self.showdialog('Success', 'Logout Success', 'Successfully loged out!', 'info')
            self.loginStatus= False
            self.btnLogin.setText('LOGIN')
        # else:
        #     self.showdialog('Error', 'Something went wrong from server!', 'critical')

        
    def registerUI(self):
        registerDg= QDialog()
        layout= QFormLayout()
        firstname= QLineEdit()
        layout.addRow(QLabel('First Name'), firstname)
        lastname= QLineEdit()
        layout.addRow(QLabel('Last Name'), lastname)
        email= QLineEdit()
        layout.addRow(QLabel('Email'), email)
        password= QLineEdit()
        layout.addRow(QLabel('Password'), password)
        repassword= QLineEdit()
        layout.addRow(QLabel('Retype Password'), repassword)
        btnRegister= QPushButton("Register")
        layout.addRow(QLabel(), btnRegister)
        btnRegister.clicked.connect(partial(self.register,firstname, lastname, email, password, repassword ))
        registerDg.setLayout(layout)
        registerDg.setWindowTitle("Register")
        registerDg.setWindowModality(Qt.ApplicationModal)
        registerDg.exec_()

    def register(self, firstname, lastname, email, password, repassword):
        registerUrl= "http://127.0.0.1:8000/register"
        if(firstname.text()== '' or lastname.text()=='' or email.text()== '' or password.text()== '' or repassword.text()== ''):
            self.showdialog('Validation', 'Validation Error', 'You must fill out all fields!')
        elif(password.text()!= repassword.text()):
            self.showdialog('Validation', 'Validation Error', 'You must input same passwords to confirm!')
        else:
            PARAMS= {'firstname': firstname.text(),
                'lastname': lastname.text(),
                'email': email.text(),
                'password': password.text()
                }
            print(PARAMS)
            r= requests.get(url= registerUrl, params= PARAMS)
            if(r.text== "Email in use!"):
                self.showdialog('Validation', 'Email error', 'Your email is in use!')
            elif(r.text== "Register success!"):
                self.showdialog('Success', 'Register success', 'Successfully registered!', 'info')
            else:
                self.showdialog('Error', 'Something went wrong from server!', 'critical')

    def showdialog(self, wintitle, title, desc, icon= 'warn'):
        msg = QMessageBox()
        msg.setStyleSheet("background-color:#303030; color:#dddddd")
        if icon== 'warn':
            msg.setIcon(QMessageBox.Warning)
        elif icon== 'info':
            msg.setIcon(QMessageBox.Information)
        elif icon== 'critical':
            msg.setIcon(QMessageBox.Critical)
        elif icon== 'que':
            msg.setIcon(QMessageBox.Question)
        msg.setText(title)
        msg.setInformativeText(desc)
        msg.setWindowTitle(wintitle)
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # msg.buttonClicked.connect(msgbtn)
        msg.exec_()

# From this, scrap part.

# email search from certain site
class WebEmailScrape():
    def __init__(self):
        super().__init__()
        self.loginTime= 5
        self.timeout= 1
        self.scrapFinished= False
        self.error= ''
    def headlessDriver(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument(f"--window-size=1920, 900")
        options.add_argument("--hide-scrollbars")
        try:
            driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
            agent = driver.execute_script("return navigator.userAgent")
            driver.close()
            options.add_argument("user-agent="+agent)
            driver= webdriver.Chrome(options= options, executable_path="chromedriver.exe")
            
            return driver
        except:
            print("You must use same chrome version with chrome driver!")
            self.error= "You must use same chrome version with chrome driver!"
            return 0
            
    def headDriver(self):
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
            self.error= "You must use same chrome version with chrome driver!"
            return 0

    def start(self, url):
        # to get dom
        url= url.strip()
        urltmp= url[8:]
        urltmp= urltmp.split('/')[0]
        self.domurl= url[:8]+ urltmp
        print(self.domurl)
        if(url[-1]== '/'):
            self.domurl= url[:-1]
        self.webemails= []
        self.totalUrls= [self.domurl]
        _thread.start_new_thread( self.webEmailScrapLogin, (url, ) )

        
        # with concurrent.futures.ThreadPoolExecutor() as executor:
        #     future = executor.submit(self.webEmailScrapLogin, url)
        #     return_value = future.result()
        #     if return_value== 0:
        #         self.showdialog('Error', 'Chrome Driver', "Couldn't get driver, maybe chrome driver version problem!", 'critical')
        #     elif return_value==1:
        #         self.showdialog('Error', 'Invalid Url', "Couldn't access url, maybe invalid url or can't access!")
        self.dlg= QDialog()
        self.dlg.setStyleSheet("background-color:#303030; color:#dddddd")
        self.successAlert(self.dlg)
        vbox= QVBoxLayout()
        self.emailField= QTextEdit()
        self.stopBtn= QPushButton("Stop")
        self.finishBtn= QPushButton("Finish")
        self.finishBtn.clicked.connect(self.emailDlgClose)
        self.stopBtn.clicked.connect(self.driverStop)
        hbox= QHBoxLayout()
        hbox.addWidget(self.stopBtn)
        hbox.addWidget(self.finishBtn)
        self.emailField.resize(300, 300)
        self.emailField.append('Now Scrap Starting...')
        vbox.addWidget(self.emailField)
        vbox.addLayout(hbox)
        self.dlg.setLayout(vbox)
        self.dlg.setWindowTitle("Website Email Scrap")
        self.dlg.setWindowModality(Qt.ApplicationModal)
        self.dlg.exec_()
        

        # webemails= []
        # webemails.push(url)

    def successAlert(self, dlg):
        if self.scrapFinished:
            msgFinsh = QMessageBox(dlg)
            msgFinsh.setStyleSheet("background-color:#303030; color:#dddddd")
            msgFinsh.setText('Success')
            msgFinsh.setInformativeText('Scrap success')
            msgFinsh.setWindowTitle('Scrap success')
            # msgFinsh.setDetailedText("The details are as follows:")
            msgFinsh.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            # msgFinsh.buttonClicked.connect(self.emailDlgClose)
            msgFinsh.exec_()
        else:
            threading.Timer(2.0, self.successAlert, [dlg]).start()
            

    def webEmailScrapLogin(self, url):
        self.driver= self.headlessDriver()
        urlValid= False
        if(self.driver== 0):
            print("Couldn't get driver, reason maybe chrome driver!")
            self.emailField.append("So you stoped? If not, Couldn't get driver, reason maybe chrome driver!")
            # self.emailField.append('Please retry!')
            # self.showdialog('Error', 'Driver Error', "Couldn't get driver, reason maybe chrome driver!", 'critical')
            return 0
        try:
            self.driver.get(url)
            time.sleep(self.loginTime)
            urlValid= True
        except:
            print("An exception occurred, maybe url is invalid or can't access!")
            self.emailField.append("So you stoped? If not, An exception occurred, maybe url is invalid or can't access!")
            # self.emailField.append('Please retry!')
            # self.showdialog('Error', 'Url Error', "An exception occurred, maybe url is invalid or can't access!", 'critical')
            return 1
        if urlValid== True:
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            self.emailFinder(soup)
            # urls= self.urlFinder(soup)
            urls= self.contactAbtUrlFinder(soup)
            for url1 in urls:
                # self.webEmailScrapRecursion(self.driver, url1)
                self.webEmailScrapNavbar(self.driver, url1)
            # self.emailField.append('Ended!')
            self.scrapFinished= True
            self.driver.close()


            
            

    def webEmailScrapRecursion(self, driver, url):
        urlValid= False
        if len(self.totalUrls)> 100 or len(self.webemails)> 100:
            return 0
        try:
            driver.get(url)
            time.sleep(self.timeout)
            urlValid= True
        except:
            # print('An exception occurred')
            # self.emailField.append("An exception occurred, maybe url is invalid or can't access!")
            # self.emailField.append('Please retry!')
            # self.showdialog('Error', 'Url Error', "An exception occurred, maybe url is invalid or can't access!", 'critical')
            return 0
        if urlValid== True:
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            self.emailFinder(soup)
            urls= self.urlFinder(soup)
            for url1 in urls:
                self.webEmailScrapRecursion(driver, url1)

    def webEmailScrapNavbar(self, driver, url):
        urlValid= False
        try:
            driver.get(url)
            time.sleep(self.timeout)
            urlValid= True
        except:
            return 0
        if urlValid== True:
            soup= BeautifulSoup(driver.page_source, 'html.parser')
            self.emailFinder(soup)

    def driverStop(self):
        try:
            time.sleep(self.timeout)
            self.driver.close()
        except:
            pass
        self.emailField.append('Stop running')

    def emailFinder(self, soup):
        EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

        if soup != None:
            for re_match in re.finditer(EMAIL_REGEX, soup.text):
                email = re_match.group()
                if email not in self.webemails:
                    self.webemails.append(email)
                    self.emailField.append(email)
                print(self.webemails)

    def urlFinder(self, soup):
        urls= []
        alinks= soup.find_all('a')
        for alink in alinks:

            try:
                alink= alink.attrs['href']
                alink= alink.strip()
            except:
                continue
            if len(alink)>0 and alink[-1]== '/':
                alink= alink[:-1]
            if len(alink)> 0:
                
                if ('http' in alink) and (alink not in self.totalUrls):
                    if self.domurl in alink:
                        self.totalUrls.append(alink)
                        urls.append(alink)
                elif(alink== "#"):
                    pass
                elif('http' not in alink):
                    if alink[0]== '/':
                        if (self.domurl+ alink) not in self.totalUrls:
                            self.totalUrls.append(self.domurl+ alink)
                            urls.append(self.domurl+ alink)
                    else:
                        if (self.domurl+ '/'+ alink) not in self.totalUrls:
                            self.totalUrls.append(self.domurl+ '/'+ alink)
                            urls.append(self.domurl+'/'+ alink)
        print(self.totalUrls)
        return urls

    def contactAbtUrlFinder(self, soup):
        urls= []
        alinks= soup.find_all('a')
        for alink in alinks:

            try:
                alink= alink.attrs['href']
                alink= alink.strip()
            except:
                continue
            if len(alink)>0 and alink[-1]== '/':
                alink= alink[:-1]
            if len(alink)> 0:
                
                if ('http' in alink):
                    if self.domurl in alink:
                        if ('contact' in alink.lower()) or ('about'in alink.lower()):
                            urls.append(alink)
                elif(alink== "#"):
                    pass
                elif('http' not in alink):
                    if alink[0]== '/':
                        if ('contact' in (self.domurl+ alink).lower()) or ('about' in (self.domurl+ alink).lower() ):
                            urls.append(self.domurl+ alink)
                    else:
                        if ('contact' in (self.domurl+ '/'+ alink).lower()) or ('about' in (self.domurl+ '/'+ alink).lower()):
                            urls.append(self.domurl+'/'+ alink)
        return urls

    def showdialog(self, wintitle, title, desc, icon= 'warn'):
        msg = QMessageBox()
        msg.setStyleSheet("background-color:#303030; color:#dddddd")
        if icon== 'warn':
            msg.setIcon(QMessageBox.Warning)
        elif icon== 'info':
            msg.setIcon(QMessageBox.Information)
        elif icon== 'critical':
            msg.setIcon(QMessageBox.Critical)
        elif icon== 'que':
            msg.setIcon(QMessageBox.Question)
        msg.setText(title)
        msg.setInformativeText(desc)
        msg.setWindowTitle(wintitle)
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.emailDlgClose)
        msg.exec_()

    def emailDlgClose(self):
        try:
            self.driver.close()
        except:
            pass
        self.dlg.close()


class SocialBooleanScrap():
    def __init__(self):
        super().__init__()
        
        self.dlg= QDialog()
        self.progressBar= QProgressBar(self.dlg)
        self.loginTime= 5
        self.timeout= 1
        self.scrapFinished= False
        self.progress= 1
        self.error= ''

    def showdialog(self, wintitle, title, desc, icon= 'warn'):
        msg = QMessageBox()
        msg.setStyleSheet("background-color:#303030; color:#dddddd")
        if icon== 'warn':
            msg.setIcon(QMessageBox.Warning)
        elif icon== 'info':
            msg.setIcon(QMessageBox.Information)
        elif icon== 'critical':
            msg.setIcon(QMessageBox.Critical)
        elif icon== 'que':
            msg.setIcon(QMessageBox.Question)
        msg.setText(title)
        msg.setInformativeText(desc)
        msg.setWindowTitle(wintitle)
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.emailDlgClose)
        msg.exec_()

    def headlessDriver(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument(f"--window-size=1920, 900")
        options.add_argument("--hide-scrollbars")
        try:
            driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
            agent = driver.execute_script("return navigator.userAgent")
            driver.close()
            options.add_argument("user-agent="+agent)
            driver= webdriver.Chrome(options= options, executable_path="chromedriver.exe")
            
            return driver
        except:
            print("You must use same chrome version with chrome driver!")
            self.error= "You must use same chrome version with chrome driver!"
            return 0
            
    def headDriver(self):
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
            self.error= "You must use same chrome version with chrome driver!"
            return 0

    def setProgress(self):
        if self.scrapFinished:
            if(self.error== ''):
                # _thread.start_new_thread( self.progressBar.setValue, (100, ) )
                # self.progressBar.setValue(100)
                self.progressBar.setValue(100)
                self.desc.setText('Success!')
                self.desc.setStyleSheet('font: 20px; color: green')
                # self.dlg.close()
                # self.showdialog("s", "ss", "ss")
                return 0
            else:
                # COMPLETED_STYLE = """
                #     QProgressBar{
                #         border: 2px solid grey;
                #         border-radius: 5px;
                #         text-align: center
                #     }

                #     QProgressBar::chunk {
                #         background-color: red;
                #         width: 10px;
                #         margin: 1px;
                #     }
                #     """
                # self.progressBar.setStyleSheet('background-color: red')
                self.desc.setText(self.error)
                self.desc.setStyleSheet('color: red')
                # self.progressBar.setStyleSheet(COMPLETED_STYLE)
                return 0
        else:

            self.progressBar.setValue(self.progress)
            threading.Timer(2.0, self.setProgress).start()

    def startProgressDialog(self):
        

        self.dlg.setStyleSheet("background-color:#303030; color:#dddddd")
        self.dlg.setWindowTitle('Scrap percent')
        self.desc= QLabel("Now inserting into file, Don't open file before finish!")
        vbox= QVBoxLayout()
        vbox.addWidget(self.desc)
        
        self.progressBar.setMaximum(101)
        vbox.addWidget(self.progressBar)
        self.setProgress()
        hbox= QHBoxLayout()
        stopBtn= QPushButton('Stop')
        stopBtn.clicked.connect(self.dlgClose)
        finishBtn= QPushButton('Finish')
        finishBtn.clicked.connect(self.dlgClose)
        hbox.addWidget(stopBtn)
        hbox.addWidget(finishBtn)
        vbox.addLayout(hbox)
        self.dlg.setLayout(vbox)
        self.dlg.setWindowModality(Qt.ApplicationModal)
        
        self.dlg.exec_()
        
        

    def dlgClose(self):
        self.dlg.close()

    def writeCsvheader(self, filename, columns):
        try:
            os.remove(filename)
        except:
            pass
        df= pd.DataFrame(columns= columns)
        # filename= str(datetime.datetime.now()).replace(':', '-')+'.csv'
        df.to_csv(filename, mode= 'x', index= False, encoding='utf-8-sig')
        # return filename

    def saveToCsv(self, filename, newPage, columns):
        df = pd.DataFrame(newPage, columns = columns)
        print("Now items writed in csv file!")
        df.to_csv(filename, mode='a', header=False, index=False, encoding='utf-8-sig')

    def emailFinder(self, texts):
        EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

        if texts != None:
            for re_match in re.finditer(EMAIL_REGEX, texts):
                email = re_match.group()
                return email
        return 0


    def googleOnepageScrap(self, soup, filename, columns):
        try:
            itemNodes= soup.find_all('div', attrs={'class':'g'})
            for itemNode in itemNodes:
                try:
                    newPage= []
                    source= itemNode.find('cite').text
                    description= itemNode.find('span', attrs= {'class': 'aCOpRe'}).text
                    title= itemNode.find('h3').text
                    try:
                        title= title.split(')')[0]+")"
                    except:
                        pass
                    email= self.emailFinder(description)
                    url= itemNode.find('a').attrs['href']

                    new = {'Source': source, 'Description': description, 'Title': title, 'Email': email, 'Url': url}
                    newPage.append(new)
                    self.saveToCsv(filename, newPage, columns)
                except:
                    continue
        except:
            pass


    def yahooOnepageScrap(self, soup, filename, columns):
        try:
            itemNodes= soup.find_all('div', attrs={'class':'dd algo algo-sr relsrch Sr'})

            for itemNode in itemNodes:
                try:
                    newPage= []
                    source= itemNode.find('span', attrs= {'class': "fz-ms fw-m fc-12th wr-bw lh-17"}).text
                    description= itemNode.find('p', attrs= {'class': 'fz-ms lh-1_43x'}).text
                    title= itemNode.find('h3').text
                    try:
                        title= title.split(')')[0]+")"
                    except:
                        pass
                    email= self.emailFinder(description)
                    url= itemNode.find('a').attrs['href']

                    new = {'Source': source, 'Description': description, 'Title': title, 'Email': email, 'Url': url}
                    newPage.append(new)
                    # self.saveToCsv(filename, newPage, columns)
                    self.saveToCsv(filename, newPage, columns)
                except:
                    continue
        except:
            pass

    def bingOnepageScrap(self, soup, filename, columns):
        try:
            itemNodes= soup.find_all('li', attrs={'class':'b_algo'})

            for itemNode in itemNodes:
                try:
                    newPage= []
                    source= itemNode.find('cite').text
                    description= itemNode.find('p').text
                    title= itemNode.find('h2').text
                    try:
                        title= title.split(')')[0]+")"
                    except:
                        pass
                    email= self.emailFinder(description)
                    url= itemNode.find('a').attrs['href']

                    new = {'Source': source, 'Description': description, 'Title': title, 'Email': email, 'Url': url}
                    newPage.append(new)
                    # self.saveToCsv(filename, newPage, columns)
                    self.saveToCsv(filename, newPage, columns)
                except:
                    continue
        except:
            pass

    def start(self, EditForKey, EditForLocation, selectSocial, EditForCountry, selectEngine, selectForEmailType, EditForPageNum, filename):
        if(len(selectForEmailType)>20 ):
            query= f"""{EditForKey}+(+"@gmail.com"+OR+"@yahoo.com"+OR+"@outlook.com"+OR+"@zoho.com"+OR+"@hotmail.com"+)+AND+"{EditForCountry}"+AND+"{EditForLocation}"+site:{selectSocial} """
        else:
            query= f"""{EditForKey}+(+"{selectForEmailType}"+)+AND+"{EditForCountry}"+AND+"{EditForLocation}"+site:{selectSocial} """

        if selectEngine== 'Google':
            _thread.start_new_thread( self.googleBooleanScrap, (query, EditForPageNum, filename,) )
        elif selectEngine== 'Yahoo':
            _thread.start_new_thread( self.yahooBooleanScrap, (query, EditForPageNum, filename, ) )
        elif selectEngine== 'Bing':
            _thread.start_new_thread( self.bingBooleanScrap, (query, EditForPageNum, filename, ) )

        # progress Dialog appear
        self.startProgressDialog()

    def googleBooleanScrap(self, query, pageNum, filename):
        # write csv header
        columns=['Source', 'Description', 'Title', 'Email', 'Url']
        try:
            self.writeCsvheader(filename, columns)
        except:
            self.error= "File path incorrect or File already exist! Please choose other name or delete orign file!"
            self.scrapFinished= True
            return 0

        nextBtnClass= "SJajHc NVbCr"

        url = 'https://google.com/search?q=' + query
        try:
            driver= self.headlessDriver()
            driver.get(url)
        except:
            self.scrapFinished= True
            return 0
        time.sleep(self.loginTime)
        for i in range(pageNum):
            
            if i== 0:
                soup = BeautifulSoup(driver.page_source, 'html.parser')

                itemNodes= soup.find_all('div', attrs={'class':'g'})
                pageBtns= driver.find_elements_by_xpath("//span[@class='SJajHc NVbCr']/ancestor::td[position()=1]")
                self.googleOnepageScrap(soup, filename, columns)
                self.progress= int(100/pageNum)
                if len(itemNodes)> 0 and pageBtns== []:
                    break
                if itemNodes== []:
                    self.error= "There is no match or maybe you are blocked! Please try again later!\n Or You can use VPN! :)"
                    break
            else:
                pageBtns= driver.find_elements_by_xpath("//span[@class='SJajHc NVbCr']/ancestor::td[position()=1]")
                if pageBtns== []:
                    break
                for nextBtn in pageBtns:
                    if nextBtn.text.strip()== str(i+1):
                        try:
                            try:
                                nextBtn.click()
                            except:
                                time.sleep(self.timeout)
                                nextBtn.click()
                            time.sleep(self.timeout)
                            soup = BeautifulSoup(driver.page_source, 'html.parser')
                            self.googleOnepageScrap(soup, filename, columns)
                            self.progress= int((100/pageNum)*(i+1))
                            break
                        except:
                            break
        self.scrapFinished= True
        
        driver.close()
        return 0


    def yahooBooleanScrap(self, query, pageNum, filename):
        # write csv header
        columns=['Source', 'Description', 'Title', 'Email', 'Url']
        try:
            self.writeCsvheader(filename, columns)
        except:
            self.error= "File path incorrect or File already exist! Please choose other name or delete orign file!"
            self.scrapFinished= True
            return 0

        url= "https://search.yahoo.com/search?q="+ query
        try:
            driver= self.headlessDriver()
            driver.get(url)
        except:
            self.scrapFinished= True
            return 0
        time.sleep(self.loginTime)
        try:
            driver.find_element_by_xpath("//button[@name='agree']").click()
            time.sleep(1)
        except:
            pass
        for i in range(pageNum):
            
            if i== 0:
                soup = BeautifulSoup(driver.page_source, 'html.parser')

                itemNodes= soup.find_all('div', attrs={'class':'dd algo algo-sr relsrch Sr'})
                try:
                    nextBtn= driver.find_element_by_xpath("//a[@class='next']")
                except:
                    nextBtn= ''
                self.yahooOnepageScrap(soup, filename, columns)
                self.progress= int(100/pageNum)
                if len(itemNodes)> 0 and nextBtn== '':
                    break
                elif itemNodes== []:
                    self.error= "There is no match or maybe you are blocked! Please try again later!\n Or You can use VPN! :)"
                    break
            else:
                try:
                    nextBtn= driver.find_element_by_xpath("//a[@class='next']")
                except:
                    nextBtn= ''
                if nextBtn== '':
                    break
                try:
                    nextBtn.click()
                except:
                    break
                time.sleep(self.timeout)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                self.yahooOnepageScrap(soup, filename, columns)
                try:
                    self.progress= int((100/pageNum)*(i+1))
                except:
                    break
        self.scrapFinished= True
        driver.close()
        return 0
    
    def bingBooleanScrap(self, query, pageNum, filename):
        # write csv header
        columns=['Source', 'Description', 'Title', 'Email', 'Url']
        try:
            self.writeCsvheader(filename, columns)
        except:
            self.error= "File path incorrect or File already exist! Please choose other name or delete orign file!"
            self.scrapFinished= True
            return 0


        url= "https://www.bing.com/search?q="+ query
        try:
            driver= self.headlessDriver()
            driver.get(url)
        except:
            self.scrapFinished= True
            return 0
        time.sleep(self.loginTime)

        try:
            driver.find_element_by_id("bnp_hfly_cta2").click()
            time.sleep(1)
        except:
            pass

        for i in range(pageNum):
            
            if i== 0:
                soup = BeautifulSoup(driver.page_source, 'html.parser')

                itemNodes= soup.find_all('li', attrs={'class':'b_algo'})
                print(itemNodes)
                pageBtns= driver.find_elements_by_xpath("//a[@class= 'b_widePag sb_bp']")
                self.bingOnepageScrap(soup, filename, columns)
                self.progress= int(100/pageNum)
                if len(itemNodes)> 0 and pageBtns== []:
                    break
                if itemNodes== []:
                    self.error= "There is no match or maybe you are blocked! Please try again later!\n Or You can use VPN! :)"
                    break
            else:
                pageBtns= driver.find_elements_by_xpath("//a[@class= 'b_widePag sb_bp']")
                if pageBtns== []:
                    break
                for nextBtn in pageBtns:
                    if nextBtn.text.strip()== str(i+1):
                        try:
                            try:
                                nextBtn.click()
                            except:
                                time.sleep(self.timeout)
                                nextBtn.click()
                            time.sleep(self.timeout)
                            soup = BeautifulSoup(driver.page_source, 'html.parser')
                            self.bingOnepageScrap(soup, filename, columns)
                            self.progress= int((100/pageNum)*(i+1))
                            break
                        except:
                            break

        self.scrapFinished= True
        driver.close()

        return 0

class GoogleMapScrap():
    def __init__(self):
        super().__init__()
        self.lock = threading.Lock()
        self.loginTime= 5
        self.timeout= 1
        self.scrapFinished= False
        self.progress= 1
        self.error= ''

    def headlessDriver(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument(f"--window-size=1920, 900")
        options.add_argument("--hide-scrollbars")
        try:
            driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
            agent = driver.execute_script("return navigator.userAgent")
            driver.close()
            options.add_argument("user-agent="+agent)
            driver= webdriver.Chrome(options= options, executable_path="chromedriver.exe")
            
            return driver
        except:
            print("You must use same chrome version with chrome driver!")
            self.lock.acquire()
            self.error= "You must use same chrome version with chrome driver!"
            self.lock.release()
            return 0
            
    def headDriver(self):
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
            self.lock.acquire()
            self.error= "You must use same chrome version with chrome driver!"
            self.lock.release()
            return 0

    def setProgress(self):
        if self.scrapFinished:
            if(self.error== ''):
                # _thread.start_new_thread( self.progressBar.setValue, (100, ) )
                # self.progressBar.setValue(100)
                
                self.desc.setText('Success!')
                self.desc.setStyleSheet('font: 20px; color: green')
                self.progressBar.setValue(self.progress)
                # threading.Timer(100.0, self.setProgress).start()
                return 0
            else:
                self.desc.setText(self.error)
                self.desc.setStyleSheet('color: red')
                # self.progressBar.setStyleSheet(COMPLETED_STYLE)
                return 0
        else:

            self.progressBar.setValue(self.progress)
            threading.Timer(2.0, self.setProgress).start()

    def startProgressDialog(self):
        self.dlg= QDialog()
        self.dlg.setStyleSheet("background-color:#303030; color:#dddddd")
        self.dlg.setWindowTitle('Scrap percent')
        self.desc= QLabel("Now inserting into file, Don't open file before finish!")
        vbox= QVBoxLayout()
        vbox.addWidget(self.desc)
        self.progressBar= QProgressBar(self.dlg)
        self.progressBar.setMaximum(101)
        vbox.addWidget(self.progressBar)
        hbox= QHBoxLayout()
        stopBtn= QPushButton('Stop')
        stopBtn.clicked.connect(self.dlgClose)
        finishBtn= QPushButton('Finish')
        finishBtn.clicked.connect(self.dlgClose)
        hbox.addWidget(stopBtn)
        hbox.addWidget(finishBtn)
        vbox.addLayout(hbox)
        self.dlg.setLayout(vbox)
        self.dlg.setWindowModality(Qt.ApplicationModal)
        self.setProgress()
        self.dlg.exec_()
        

    def dlgClose(self):
        self.dlg.close()

    def writeCsvheader(self, filename, columns):
        try:
            os.remove(filename)
        except:
            pass
        df= pd.DataFrame(columns= columns)
        # filename= str(datetime.datetime.now()).replace(':', '-')+'.csv'
        df.to_csv(filename, mode= 'x', index= False, encoding='utf-8-sig')
        # return filename

    def saveToCsv(self, filename, newPage, columns):
        df = pd.DataFrame(newPage, columns = columns)
        print("Now items writed in csv file!")
        df.to_csv(filename, mode='a', header=False, index=False, encoding='utf-8-sig')

    def start(self, url, pageNum, filename):
        
        threading.Thread(target= self.googlemapScrapCore, args = (url, pageNum, filename,)).start()

        self.startProgressDialog()

    # this part is for email search in target url
    def webEmailScrapLogin(self, url):
        emails= []
        driver= self.headlessDriver()
        urlValid= False
        if(driver== 0):
            print("Couldn't get driver, reason maybe chrome driver!")
            return 0
        try:
            driver.get(url)
            time.sleep(self.loginTime)
            urlValid= True
        except:
            driver.close()
            print("An exception occurred, maybe url is invalid or can't access!")
            return 0

        # to ge domurl
        url= url.strip()
        urltmp= url[8:]
        urltmp= urltmp.split('/')[0]
        domurl= url[:8]+ urltmp
        if(url[-1]== '/'):
            domurl= url[:-1]
        if urlValid== True:
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            newEmails= self.emailFinder(soup)
            emails.extend(newEmails)
            # urls= self.urlFinder(soup, domurl)
            urls= self.contactAbtUrlFinder(soup, domurl)
            for url1 in urls:
                # self.webEmailScrapRecursion(self.driver, url1)
                newEmails= self.webEmailScrapNavbar(driver, url1)
                emails.extend(newEmails)
            # self.emailField.append('Ended!')
            driver.close()

        return emails

    def webEmailScrapNavbar(self, driver, url):
        urlValid= False
        emails= []
        try:
            driver.get(url)
            time.sleep(self.timeout)
            urlValid= True
        except:
            driver.close()
            return emails
        if urlValid== True:
            soup= BeautifulSoup(driver.page_source, 'html.parser')
            emails= self.emailFinder(soup)
            return emails


    def emailFinder(self, soup):
        EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
        emails= []
        if soup != None:
            for re_match in re.finditer(EMAIL_REGEX, soup.text):
                email = re_match.group()
                emails.append(email)
            return emails
        else:
            return emails


    def contactAbtUrlFinder(self, soup, domurl):
        urls= []
        alinks= soup.find_all('a')
        for alink in alinks:

            try:
                alink= alink.attrs['href']
                alink= alink.strip()
            except:
                continue
            if len(alink)>0 and alink[-1]== '/':
                alink= alink[:-1]
            if len(alink)> 0:
                
                if ('http' in alink):
                    if domurl in alink:
                        if ('contact' in alink.lower()) or ('about'in alink.lower()):
                            urls.append(alink)
                elif(alink== "#"):
                    pass
                elif('http' not in alink):
                    if alink[0]== '/':
                        if ('contact' in (domurl+ alink).lower()) or ('about' in (domurl+ alink).lower() ):
                            urls.append(domurl+ alink)
                    else:
                        if ('contact' in (domurl+ '/'+ alink).lower()) or ('about' in (domurl+ '/'+ alink).lower()):
                            urls.append(domurl+'/'+ alink)
        return urls


    def googlemapOnepageScrap(self, driver, filename, columns):
        try:
            itemClicks= driver.find_elements_by_xpath("//div[@class= 'VkpGBb']")
            for itemClick in itemClicks:
                try:
                    itemClick.click()
                    time.sleep(self.timeout* 2)
                    soup= BeautifulSoup(driver.page_source, 'html.parser')
                    itemNode= soup.find('div', attrs= {'class': 'xpdopen'})
                    newPage= []
                    businessName= itemNode.find('h2').text
                    address= itemNode.find('span', attrs= {'class': 'LrzXr'}).text
                    phoneNumber= 0
                    try:
                        phoneNumber= itemNode.find('span', attrs= {'class': 'LrzXr zdqRlf kno-fv'}).text
                    except:
                        pass
                    
                    website= 0
                    try:
                        if ('http' in itemNode.find('div', attrs= {'class': 'QqG1Sd'}).find('a').attrs['href']):
                            website= itemNode.find('div', attrs= {'class': 'QqG1Sd'}).find('a').attrs['href']
                    except:
                        pass
                    email= ''
                    # emails= 0
                    # if(website!= 0):
                    #     try:
                    #         emails= self.webEmailScrapLogin(website)
                    #     except:
                    #         pass
                    # if emails!= 0:
                    #     for email1 in emails:
                    #         email+= email1+'  '

                    new = {'Business Name': businessName, 'Address': address, 'Phone Number': phoneNumber, 'Website': website, 'Email': email}
                    newPage.append(new)
                    self.saveToCsv(filename, newPage, columns)
                except:
                    continue
        except:
            pass

    def googlemapScrapCore(self, url, pageNum, filename):

        columns=['Business Name', 'Address', 'Phone Number', 'Website', 'Email']
        try:
            self.writeCsvheader(filename, columns)
        except:
            self.lock.acquire()
            self.error= "File path incorrect or File already exist! Please choose other name or delete orign file!"
            self.scrapFinished= True
            self.lock.release()
            return 0
        try:
            driver= self.headlessDriver()
            driver.get(url)
            time.sleep(self.loginTime)
        except:
            self.lock.acquire()
            self.scrapFinished= True
            self.lock.release()
            return 0
        
        try:
            driver.find_element_by_xpath("//div[@class= 'VkpGBb']").click()
            time.sleep(self.timeout)
            # driver.find_element_by_xpath("//div[@class= 'VkpGBb']").click()
        except:
            
            try:
                driver.find_element_by_xpath("//a[@class= 'axGQJc']").click()
                time.sleep(self.timeout)
                driver.find_element_by_xpath("//div[@class= 'VkpGBb']").click()
                time.sleep(self.timeout)
            except:
                try:
                    # soup = BeautifulSoup(driver.page_source, 'html.parser')
                    # print(soup.find_all('a'))
                    # driver.find_element_by_xpath("//div[@class= 'D1DGDc']/a[0]").click()
                    researchs= driver.find_elements_by_tag_name('a')
                    for research in researchs:
                        print(research.text)
                        if "web results for" in research.text:
                            print(research)
                            research.click()
                            time.sleep(self.timeout*2)
                            break
                    driver.find_element_by_xpath("//div[@class= 'VkpGBb']").click()
                    time.sleep(self.timeout)
                except:
                    self.lock.acquire()
                    self.error= "There is no match for that url or this machine is not supported for that type url.\n Else maybe You are blocked!"
                    self.scrapFinished= True
                    self.lock.release()

        for i in range(pageNum):
            
            if i== 0:
                # soup = BeautifulSoup(driver.page_source, 'html.parser')
                pageBtns= driver.find_elements_by_xpath("//span[@class='SJajHc NVbCr']/ancestor::td[position()=1]")
                self.googlemapOnepageScrap(driver, filename, columns)
                self.lock.acquire()
                self.progress= int(100/pageNum)
                self.lock.release()
                if pageBtns== []:
                    break

            else:
                pageBtns= driver.find_elements_by_xpath("//span[@class='SJajHc NVbCr']/ancestor::td[position()=1]")
                if pageBtns== []:
                    break
                for nextBtn in pageBtns:
                    if nextBtn.text.strip()== str(i+1):
                        try:
                            try:
                                nextBtn.click()
                            except:
                                time.sleep(self.timeout)
                                nextBtn.click()
                            time.sleep(self.timeout*5)
                            # soup = BeautifulSoup(driver.page_source, 'html.parser')
                            self.googlemapOnepageScrap(driver, filename, columns)
                            self.lock.acquire()
                            self.progress= int((100/pageNum)*(i+1))
                            self.lock.release()
                            break
                        except:
                            break
        self.lock.acquire()
        self.progress= 100
        self.scrapFinished= True
        self.lock.release()
        driver.close()



class YelpPageScrap():
    def __init__(self):
        super().__init__()
        self.headers= {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"
        }
        self.lock = threading.Lock()
        self.threadFlag= 0
        self.loginTime= 5
        self.timeout= 1
        self.scrapFinished= False
        self.progress= 0
        self.error= ''

    def headlessDriver(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument(f"--window-size=1920, 900")
        options.add_argument("--hide-scrollbars")
        try:
            driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
            agent = driver.execute_script("return navigator.userAgent")
            driver.close()
            options.add_argument("user-agent="+agent)
            driver= webdriver.Chrome(options= options, executable_path="chromedriver.exe")
            
            return driver
        except:
            print("You must use same chrome version with chrome driver!")
            self.lock.acquire()
            self.error= "You must use same chrome version with chrome driver!"
            self.lock.release()
            return 0
            
    def headDriver(self):
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
            self.lock.acquire()
            self.error= "You must use same chrome version with chrome driver!"
            self.lock.release()
            return 0

    def setProgress(self):
        if self.scrapFinished:
            if(self.error== ''):
                # _thread.start_new_thread( self.progressBar.setValue, (100, ) )
                # self.progressBar.setValue(100)
                
                self.desc.setText('Success!')
                self.desc.setStyleSheet('font: 20px; color: green')
                self.lock.acquire()
                self.progressBar.setValue(100)
                self.lock.release()
                return 0
            else:
                self.desc.setText(self.error)
                self.desc.setStyleSheet('color: red')
                # self.progressBar.setStyleSheet(COMPLETED_STYLE)
                return 0
        else:

            self.progressBar.setValue(self.progress)
            threading.Timer(2.0, self.setProgress).start()

    def startProgressDialog(self):
        self.dlg= QDialog()
        self.dlg.setWindowTitle('Scrap percent')
        self.dlg.setStyleSheet("background-color:#303030; color:#dddddd")
        self.desc= QLabel("Now inserting into file, Don't open file before finish!")
        vbox= QVBoxLayout()
        vbox.addWidget(self.desc)
        self.progressBar= QProgressBar(self.dlg)
        self.progressBar.setMaximum(101)
        vbox.addWidget(self.progressBar)
        hbox= QHBoxLayout()
        stopBtn= QPushButton('Stop')
        stopBtn.clicked.connect(self.dlgClose)
        finishBtn= QPushButton('Finish')
        finishBtn.clicked.connect(self.dlgClose)
        hbox.addWidget(stopBtn)
        hbox.addWidget(finishBtn)
        vbox.addLayout(hbox)
        self.dlg.setLayout(vbox)
        self.dlg.setWindowModality(Qt.ApplicationModal)
        self.setProgress()
        self.dlg.exec_()
        

    def dlgClose(self):
        self.dlg.close()

    def writeCsvheader(self, filename, columns):
        try:
            os.remove(filename)
        except:
            pass
        df= pd.DataFrame(columns= columns)
        # filename= str(datetime.datetime.now()).replace(':', '-')+'.csv'
        df.to_csv(filename, mode= 'x', index= False, encoding='utf-8-sig')
        # return filename

    def saveToCsv(self, filename, newPage, columns):
        df = pd.DataFrame(newPage, columns = columns)
        print("Now items writed in csv file!")
        df.to_csv(filename, mode='a', header=False, index=False, encoding='utf-8-sig')

    def start(self, url, pageNum, filename):
        
        threading.Thread(target= self.yelppageScrapCore, args = (url, pageNum, filename,)).start()

        self.startProgressDialog()

    # this part is for email search in target url
    def webEmailScrapLogin(self, url):
        emails= []
        driver= self.headlessDriver()
        urlValid= False
        if(driver== 0):
            print("Couldn't get driver, reason maybe chrome driver!")
            return 0
        try:
            driver.get(url)
            time.sleep(self.loginTime)
            url= driver.current_url
            urlValid= True
        except:
            driver.close()
            print("An exception occurred, maybe url is invalid or can't access!")
            return 0

        # to ge domurl
        url= url.strip()
        urltmp= url[8:]
        urltmp= urltmp.split('/')[0]
        domurl= url[:8]+ urltmp
        if(url[-1]== '/'):
            domurl= url[:-1]
        if urlValid== True:
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            newEmails= self.emailFinder(soup)
            emails.extend(newEmails)
            # urls= self.urlFinder(soup, domurl)
            urls= self.contactAbtUrlFinder(soup, domurl)
            for url1 in urls:
                # self.webEmailScrapRecursion(self.driver, url1)
                newEmails= self.webEmailScrapNavbar(driver, url1)
                emails.extend(newEmails)
            # self.emailField.append('Ended!')
            driver.close()

        return emails


    def webEmailScrapNavbar(self, driver, url):
        urlValid= False
        emails= []
        try:
            driver.get(url)
            time.sleep(self.timeout)
            urlValid= True
        except:
            driver.close()
            return emails
        if urlValid== True:
            soup= BeautifulSoup(driver.page_source, 'html.parser')
            emails= self.emailFinder(soup)
            return emails


    def emailFinder(self, soup):
        EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
        emails= []
        if soup != None:
            for re_match in re.finditer(EMAIL_REGEX, soup.text):
                email = re_match.group()
                emails.append(email)
            return emails
        else:
            return emails


    def contactAbtUrlFinder(self, soup, domurl):
        urls= []
        alinks= soup.find_all('a')
        for alink in alinks:

            try:
                alink= alink.attrs['href']
                alink= alink.strip()
            except:
                continue
            if len(alink)>0 and alink[-1]== '/':
                alink= alink[:-1]
            if len(alink)> 0:
                
                if ('http' in alink):
                    if domurl in alink:
                        if ('contact' in alink.lower()) or ('about'in alink.lower()):
                            urls.append(alink)
                elif(alink== "#"):
                    pass
                elif('http' not in alink):
                    if alink[0]== '/':
                        if ('contact' in (domurl+ alink).lower()) or ('about' in (domurl+ alink).lower() ):
                            urls.append(domurl+ alink)
                    else:
                        if ('contact' in (domurl+ '/'+ alink).lower()) or ('about' in (domurl+ '/'+ alink).lower()):
                            urls.append(domurl+'/'+ alink)
        return urls



    def yelppageOnepageScrap(self, url, filename, columns, pageNum):
    # def yelppageOnepageScrap(self, soup, filename, columns):
        domurl= "https://www.yelp.com"
        response= requests.get(url, headers= self.headers)
        soup= BeautifulSoup(response.text, 'html.parser')
        try:
            yelpDoms= soup.find_all('div', attrs= {'class': 'container__09f24__21w3G hoverable__09f24__2nTf3 margin-t3__09f24__5bM2Z margin-b3__09f24__1DQ9x padding-t3__09f24__-R_5x padding-r3__09f24__1pBFG padding-b3__09f24__1vW6j padding-l3__09f24__1yCJf border--top__09f24__1H_WE border--right__09f24__28idl border--bottom__09f24__2FjZW border--left__09f24__33iol border-color--default__09f24__R1nRO'})
            for yelpDom in yelpDoms:
                try:
                    businessName= yelpDom.find('h4').text
                    site= yelpDom.find('a').attrs['href']
                    response= requests.get(domurl+ site)
                    time.sleep(0.5)

                    soup = BeautifulSoup(response.text, 'html.parser')
                    detailNode= soup.find_all('div', attrs= {'class': 'css-0 padding-t2__373c0__11Iek padding-r2__373c0__28zpp padding-b2__373c0__34gV1 padding-l2__373c0__1Dr82 border--top__373c0__3gXLy border--right__373c0__1n3Iv border--bottom__373c0__3qNtD border--left__373c0__d1B7K border-radius--regular__373c0__3KbYS background-color--white__373c0__2uyKj'})[-1]
                    newPage= []
                    website= detailNode.find_all('p', attrs= {'class': "text__373c0__2Kxyz text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa- text-weight--semibold__373c0__2l0fe text-size--large__373c0__3t60B"})[0].text

                    address= detailNode.find_all('p', attrs= {'class': "text__373c0__2Kxyz text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa- text-weight--semibold__373c0__2l0fe text-size--large__373c0__3t60B"})[2].text.replace('Get Directions', '')
                    phoneNumber= detailNode.find_all('p', attrs= {'class': "text__373c0__2Kxyz text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa- text-weight--semibold__373c0__2l0fe text-size--large__373c0__3t60B"})[1].text
                    
                    email= ''
                    # emails= 0
                    # try:
                    #     urlForEmail= domurl+detailNode.find_all('p', attrs= {'class': "text__373c0__2Kxyz text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa- text-weight--semibold__373c0__2l0fe text-size--large__373c0__3t60B"})[0].find('a').attrs['href']
                    #     emails= self.webEmailScrapLogin(urlForEmail)
                    # except:
                    #     pass

                    # if emails!= 0:
                    #     for email1 in emails:
                    #         email+= email1+'  '

                    new = {'Business Name': businessName, 'Address': address, 'Phone Number': phoneNumber, 'Website': website, 'Email': email}
                    newPage.append(new)
                    self.lock.acquire()
                    self.saveToCsv(filename, newPage, columns)
                    self.lock.release()
                except:
                    continue
        except:
            pass
        self.lock.acquire()
        self.progress+= int(100/pageNum)
        self.threadFlag+= 1
        self.lock.release()
        

    def yelppageScrapCore(self, url, pageNum, filename):
        pageInterval= 10

        if(url[-1]== "/"):
            url= url[:-1]

        columns=['Business Name', 'Address', 'Phone Number', 'Website', 'Email']
        try:
            self.writeCsvheader(filename, columns)
        except:
            self.lock.acquire()
            self.error= "File path incorrect or File already exist! Please choose other name or delete orign file!"
            self.scrapFinished= True
            self.lock.release()
            return 0
        for i in range(pageNum):
            
            if i== 0:
                # soup = BeautifulSoup(driver.page_source, 'html.parser')
                try:
                    response= requests.get(url, headers= self.headers)
                except:
                    continue
                urls= []
                soupone = BeautifulSoup(response.text, 'html.parser')
                yelpDoms= soupone.find_all('div', attrs= {'class': 'container__09f24__21w3G hoverable__09f24__2nTf3 margin-t3__09f24__5bM2Z margin-b3__09f24__1DQ9x padding-t3__09f24__-R_5x padding-r3__09f24__1pBFG padding-b3__09f24__1vW6j padding-l3__09f24__1yCJf border--top__09f24__1H_WE border--right__09f24__28idl border--bottom__09f24__2FjZW border--left__09f24__33iol border-color--default__09f24__R1nRO'})
                if(yelpDoms== []):
                    self.lock.acquire()
                    self.error= "There is no match for that url or this machine is not supported for that type url.\n Else maybe You are blocked!"
                    self.lock.release()
                    break
                pageInterval= len(yelpDoms)
                for ii in range(pageNum):
                    if ii== 0:
                        urls.append(url)
                    else:

                        nextIndex= str(ii*pageInterval)
                        nextUrl= url+ '&start='+ nextIndex
                        urls.append(nextUrl)
                modifiedUrls= modifyUrls(urls)
                for modifiedUrl in modifiedUrls:
                    self.lock.acquire()
                    self.threadFlag= 0
                    self.lock.release()
                    for one in modifiedUrl:
                        threading.Thread(target= self.yelppageOnepageScrap, args = (one, filename, columns, pageNum,)).start()
                    while self.threadFlag!= len(modifiedUrl):
                        time.sleep(2)
                    print("now Thread one finish!")
        self.lock.acquire()
        self.progress= 100
        self.scrapFinished= True
        self.lock.release()

# class YellowPageScrap():
#     def __init__(self):
#         super().__init__()

#         self.lock = threading.Lock()
#         self.loginTime= 5
#         self.timeout= 1
#         self.scrapFinished= False
#         self.progress= 1
#         self.error= ''

#     def headlessDriver(self):
#         options = Options()
#         options.add_argument("--headless")
#         options.add_argument(f"--window-size=1920, 900")
#         options.add_argument("--hide-scrollbars")
#         try:
#             driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
#             agent = driver.execute_script("return navigator.userAgent")
#             driver.close()
#             options.add_argument("user-agent="+agent)
#             driver= webdriver.Chrome(options= options, executable_path="chromedriver.exe")
            
#             return driver
#         except:
#             print("You must use same chrome version with chrome driver!")
#             self.lock.acquire()
#             self.error= "You must use same chrome version with chrome driver!"
#             self.lock.release()
#             return 0
            
#     def headDriver(self):
#         options = Options()
#         options.headless = False
#         options.add_argument("--window-size=1920,1200")
#         try:
#             driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
#             agent = driver.execute_script("return navigator.userAgent")
#             driver.close()
#             options.add_argument("user-agent="+agent)
#             driver= webdriver.Chrome(options= options, executable_path="chromedriver.exe")
#             return driver
#         except:
#             print("You must use same chrome version with chrome driver!")
#             self.lock.acquire()
#             self.error= "You must use same chrome version with chrome driver!"
#             self.lock.release()
#             return 0

#     def setProgress(self):
#         if self.scrapFinished:
#             if(self.error== ''):
#                 # _thread.start_new_thread( self.progressBar.setValue, (100, ) )
#                 # self.progressBar.setValue(100)
                
#                 self.desc.setText('Success!')
#                 self.desc.setStyleSheet('font: 20px; color: green')
#                 self.progressBar.setValue(100)
#                 return 0
#             else:
#                 self.desc.setText(self.error)
#                 self.desc.setStyleSheet('color: red')
#                 # self.progressBar.setStyleSheet(COMPLETED_STYLE)
#                 return 0
#         else:

#             self.progressBar.setValue(self.progress)
#             threading.Timer(2.0, self.setProgress).start()

#     def startProgressDialog(self):
#         self.dlg= QDialog()
#         self.dlg.setWindowTitle('Scrap percent')
#         self.dlg.setStyleSheet("background-color:#303030; color:#dddddd")
#         self.desc= QLabel("Now inserting into file, Don't open file before finish!")
#         vbox= QVBoxLayout()
#         vbox.addWidget(self.desc)
#         self.progressBar= QProgressBar(self.dlg)
#         self.progressBar.setMaximum(101)
#         vbox.addWidget(self.progressBar)
#         hbox= QHBoxLayout()
#         stopBtn= QPushButton('Stop')
#         stopBtn.clicked.connect(self.dlgClose)
#         finishBtn= QPushButton('Finish')
#         finishBtn.clicked.connect(self.dlgClose)
#         hbox.addWidget(stopBtn)
#         hbox.addWidget(finishBtn)
#         vbox.addLayout(hbox)
#         self.dlg.setLayout(vbox)
#         self.dlg.setWindowModality(Qt.ApplicationModal)
#         self.setProgress()
#         self.dlg.exec_()
        

#     def dlgClose(self):
#         self.dlg.close()

#     def writeCsvheader(self, filename, columns):
#         try:
#             os.remove(filename)
#         except:
#             pass
#         df= pd.DataFrame(columns= columns)
#         # filename= str(datetime.datetime.now()).replace(':', '-')+'.csv'
#         df.to_csv(filename, mode= 'x', index= False, encoding='utf-8-sig')
#         # return filename

#     def saveToCsv(self, filename, newPage, columns):
#         df = pd.DataFrame(newPage, columns = columns)
#         print("Now items writed in csv file!")
#         df.to_csv(filename, mode='a', header=False, index=False, encoding='utf-8-sig')

#     def start(self, url, pageNum, filename):
        
#         threading.Thread(target= self.yellowpageScrapCore, args = (url, pageNum, filename,)).start()

#         self.startProgressDialog()

#     def yellowpageScrapCore(self, url, pageNum, filename):

#         if(url[-1]== "/"):
#             url= url[:-1]
#         columns=['Business Name', 'Address', 'Phone Number', 'Website', 'Email']
#         try:
#             self.writeCsvheader(filename, columns)
#         except:
#             self.lock.acquire()
#             self.error= "File path incorrect or File already exist! Please choose other name or delete orign file!"
#             self.scrapFinished= True
#             self.lock.release()
#             return 0
#         try:
#             driver= self.headlessDriver()
#             driver.get(url)
#         except:
#             self.lock.acquire()
#             self.scrapFinished= True
#             self.lock.release()
#             return 0
#         time.sleep(self.loginTime)

#         for i in range(pageNum):
            
#             if i== 0:
#                 # soup = BeautifulSoup(driver.page_source, 'html.parser')
#                 itemClicks= driver.find_elements_by_xpath("//div[@class='v-card']")
#                 if itemClicks== []:
#                     self.lock.acquire()
#                     self.error= "There is no match for that url or this machine is not supported for that type url.\n Else maybe You are blocked!"
#                     self.lock.release()
#                     break
                
#                 self.yellowpageOnepageScrap(driver, filename, columns)
#                 self.lock.acquire()
#                 self.progress= int(100/pageNum)
#                 self.lock.release()
#                 try:
#                     nextBtn= driver.find_element_by_xpath("//a[@class= 'next ajax-page']").text
#                 except:
#                     break

#             else:
#                 nextUrl= url+ "?page="+str(i+1)
#                 driver.get(nextUrl)
#                 time.sleep(self.timeout)
#                 self.yellowpageOnepageScrap(driver, filename, columns)
#                 self.lock.acquire()
#                 self.progress= int(100/pageNum*(i+1))
#                 self.lock.release()
#                 try:
#                     nextBtn= driver.find_element_by_xpath("//a[@class= 'next ajax-page']").text
#                 except:
#                     break
#         self.lock.acquire()
#         self.progress= 100
#         self.scrapFinished= True
#         self.lock.release()
#         driver.close()

#     def yellowpageOnepageScrap(self, driver, filename, columns):
#         domurl= "https://www.yellowpages.com"
#         try:
#             soup=BeautifulSoup(driver.page_source, 'html.parser')
#             tmpNodes= soup.find_all('a', attrs= {'class': 'business-name'})
#             itemClicks= []
#             for tmpNode in tmpNodes:
#                 try:
#                     tmp= domurl+ tmpNode.attrs['href']
#                     itemClicks.append(tmp)
#                 except:
#                     continue
#             # itemClicks= driver.find_elements_by_xpath("//div[@class='v-card']")
#             for itemClick in itemClicks:
#                 try:
#                     driver.get(itemClick)
#                     time.sleep(self.timeout)
#                     soup= BeautifulSoup(driver.page_source, 'html.parser')
#                     itemNode= soup.find('header', attrs= {'id': 'main-header'})
#                     newPage= []
#                     businessName= itemNode.find('h1').text
#                     address= itemNode.find('h2', attrs= {'class': 'address'}).text
#                     phoneNumber= 0
#                     try:
#                         phoneNumber= itemNode.find('p', attrs= {'class': 'phone'}).text
#                     except:
#                         pass
                    
#                     website= 0
#                     try:
#                         website= itemNode.find('a', attrs= {'class': 'primary-btn website-link'}).attrs['href']
#                     except:
#                         pass
#                     email= ''
#                     # emails= 0
#                     # if(website!= 0):
#                     #     try:
#                     #         emails= self.webEmailScrapLogin(website)
#                     #     except:
#                     #         pass
#                     # if emails!= 0:
#                     #     for email1 in emails:
#                     #         email+= email1+'  '

#                     new = {'Business Name': businessName, 'Address': address, 'Phone Number': phoneNumber, 'Website': website, 'Email': email}
#                     newPage.append(new)
#                     self.saveToCsv(filename, newPage, columns)
#                 except:
#                     continue
#         except:
#             pass


#     # this part is for email search in target url
#     def webEmailScrapLogin(self, url):
#         emails= []
#         driver= self.headlessDriver()
#         urlValid= False
#         if(driver== 0):
#             print("Couldn't get driver, reason maybe chrome driver!")
#             return 0
#         try:
#             driver.get(url)
#             time.sleep(self.loginTime)
#             urlValid= True
#         except:
#             driver.close()
#             print("An exception occurred, maybe url is invalid or can't access!")
#             return 0

#         # to ge domurl
#         url= url.strip()
#         urltmp= url[8:]
#         urltmp= urltmp.split('/')[0]
#         domurl= url[:8]+ urltmp
#         if(url[-1]== '/'):
#             domurl= url[:-1]
#         if urlValid== True:
#             soup = BeautifulSoup(driver.page_source, 'html.parser')
#             newEmails= self.emailFinder(soup)
#             emails.extend(newEmails)
#             # urls= self.urlFinder(soup, domurl)
#             urls= self.contactAbtUrlFinder(soup, domurl)
#             for url1 in urls:
#                 # self.webEmailScrapRecursion(self.driver, url1)
#                 newEmails= self.webEmailScrapNavbar(driver, url1)
#                 emails.extend(newEmails)
#             # self.emailField.append('Ended!')
#             driver.close()

#         return emails


#     def webEmailScrapNavbar(self, driver, url):
#         urlValid= False
#         emails= []
#         try:
#             driver.get(url)
#             time.sleep(self.timeout)
#             urlValid= True
#         except:
#             driver.close()
#             return emails
#         if urlValid== True:
#             soup= BeautifulSoup(driver.page_source, 'html.parser')
#             emails= self.emailFinder(soup)
#             return emails


#     def emailFinder(self, soup):
#         EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
#         emails= []
#         if soup != None:
#             for re_match in re.finditer(EMAIL_REGEX, soup.text):
#                 email = re_match.group()
#                 emails.append(email)
#             return emails
#         else:
#             return emails


#     def contactAbtUrlFinder(self, soup, domurl):
#         urls= []
#         alinks= soup.find_all('a')
#         for alink in alinks:

#             try:
#                 alink= alink.attrs['href']
#                 alink= alink.strip()
#             except:
#                 continue
#             if len(alink)>0 and alink[-1]== '/':
#                 alink= alink[:-1]
#             if len(alink)> 0:
                
#                 if ('http' in alink):
#                     if domurl in alink:
#                         if ('contact' in alink.lower()) or ('about'in alink.lower()):
#                             urls.append(alink)
#                 elif(alink== "#"):
#                     pass
#                 elif('http' not in alink):
#                     if alink[0]== '/':
#                         if ('contact' in (domurl+ alink).lower()) or ('about' in (domurl+ alink).lower() ):
#                             urls.append(domurl+ alink)
#                     else:
#                         if ('contact' in (domurl+ '/'+ alink).lower()) or ('about' in (domurl+ '/'+ alink).lower()):
#                             urls.append(domurl+'/'+ alink)
#         return urls
class YellowPageScrap():
    def __init__(self):
        super().__init__()
        self.lock = threading.Lock()
        self.loginTime= 5
        self.timeout= 1
        self.scrapFinished= False
        self.progress= 1
        self.error= ''

    def headlessDriver(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument(f"--window-size=1920, 900")
        options.add_argument("--hide-scrollbars")
        try:
            driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
            agent = driver.execute_script("return navigator.userAgent")
            driver.close()
            options.add_argument("user-agent="+agent)
            driver= webdriver.Chrome(options= options, executable_path="chromedriver.exe")
            
            return driver
        except:
            print("You must use same chrome version with chrome driver!")
            self.lock.acquire()
            self.error= "You must use same chrome version with chrome driver!"
            self.lock.release()
            return 0
            
    def headDriver(self):
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
            self.lock.acquire()
            self.error= "You must use same chrome version with chrome driver!"
            self.lock.release()
            return 0

    def setProgress(self):
        if self.scrapFinished:
            if(self.error== ''):
                # _thread.start_new_thread( self.progressBar.setValue, (100, ) )
                # self.progressBar.setValue(100)
                
                self.desc.setText('Success!')
                self.desc.setStyleSheet('font: 20px; color: green')
                self.progressBar.setValue(100)
                return 0
            else:
                self.desc.setText(self.error)
                self.desc.setStyleSheet('color: red')
                # self.progressBar.setStyleSheet(COMPLETED_STYLE)
                return 0
        else:

            self.progressBar.setValue(self.progress)
            threading.Timer(2.0, self.setProgress).start()

    def startProgressDialog(self):
        self.dlg= QDialog()
        self.dlg.setWindowTitle('Scrap percent')
        self.dlg.setStyleSheet("background-color:#303030; color:#dddddd")
        self.desc= QLabel("Now inserting into file, Don't open file before finish!")
        vbox= QVBoxLayout()
        vbox.addWidget(self.desc)
        self.progressBar= QProgressBar(self.dlg)
        self.progressBar.setMaximum(101)
        vbox.addWidget(self.progressBar)
        hbox= QHBoxLayout()
        stopBtn= QPushButton('Stop')
        stopBtn.clicked.connect(self.dlgClose)
        finishBtn= QPushButton('Finish')
        finishBtn.clicked.connect(self.dlgClose)
        hbox.addWidget(stopBtn)
        hbox.addWidget(finishBtn)
        vbox.addLayout(hbox)
        self.dlg.setLayout(vbox)
        self.dlg.setWindowModality(Qt.ApplicationModal)
        self.setProgress()
        self.dlg.exec_()
        

    def dlgClose(self):
        self.dlg.close()

    def writeCsvheader(self, filename, columns):
        try:
            os.remove(filename)
        except:
            pass
        df= pd.DataFrame(columns= columns)
        # filename= str(datetime.datetime.now()).replace(':', '-')+'.csv'
        df.to_csv(filename, mode= 'x', index= False, encoding='utf-8-sig')
        # return filename

    def saveToCsv(self, filename, newPage, columns):
        df = pd.DataFrame(newPage, columns = columns)
        print("Now items writed in csv file!")
        df.to_csv(filename, mode='a', header=False, index=False, encoding='utf-8-sig')

    def start(self, url, pageNum, filename):
        
        threading.Thread(target= self.yellowpageScrapCore, args = (url, pageNum, filename,)).start()

        self.startProgressDialog()

    def yellowpageScrapCore(self, url, pageNum, filename):

        if(url[-1]== "/"):
            url= url[:-1]
        columns=['Business Name', 'Address', 'Phone Number', 'Website', 'Email']
        try:
            self.writeCsvheader(filename, columns)
        except:
            self.lock.acquire()
            self.error= "File path incorrect or File already exist! Please choose other name or delete orign file!"
            self.scrapFinished= True
            self.lock.release()
            return 0

        for i in range(pageNum):
            
            if i== 0:
                # soup = BeautifulSoup(driver.page_source, 'html.parser')
                url= "https://www.yellowpages.com/los-angeles-ca/restaurants?page="+str(i+1)
                response= requests.get(url)
                time.sleep(0.5)
                soup = BeautifulSoup(response.text, 'html.parser')
                itemNodes= soup.find_all('div', attrs= {'class': 'v-card'})
                if itemNodes== []:
                    self.lock.acquire()
                    self.error= "There is no match for that url or this machine is not supported for that type url.\n Else maybe You are blocked!"
                    self.lock.release()
                    break
                
                self.yellowpageOnepageScrap(soup, filename, columns)
                self.lock.acquire()
                self.progress= int(100/pageNum)
                self.lock.release()
                ifnext= soup.find('a', attrs= {'class': 'next ajax-page'})
                if (ifnext== None):
                    break

            else:
                url= "https://www.yellowpages.com/los-angeles-ca/restaurants?page="+str(i+1)
                response= requests.get(url)
                time.sleep(0.5)
                soup = BeautifulSoup(response.text, 'html.parser')
                self.yellowpageOnepageScrap(soup, filename, columns)
                self.lock.acquire()
                self.progress= int(100/pageNum*(i+1))
                self.lock.release()
                ifnext= soup.find('a', attrs= {'class': 'next ajax-page'})
                if (ifnext== None):
                    break
        self.lock.acquire()
        self.progress= 100
        self.scrapFinished= True
        self.lock.release()

    def yellowpageOnepageScrap(self, soup, filename, columns):
        domurl= "https://www.yellowpages.com"
        try:
            itemNodes= soup.find_all('div', attrs= {'class': 'v-card'})
            if itemNodes==[]:
                return 0
            else:
                for itemNode in itemNodes:
                    newPage= []
                    businessName= itemNode.find('h2').text
                    streetAddress= ''
                    try:
                        streetAddress= itemNode.find('div', attrs= {'class': 'street-address'}).text
                    except:
                        pass
                    locality= ''
                    try:
                        locality= itemNode.find('div', attrs= {'class': 'locality'}).text
                    except:
                        pass
                    address= streetAddress+ ' '+locality
                    phobeNumber= ''
                    try:
                        phoneNumber= itemNode.find('div', attrs= {'class': 'phones phone primary'}).text
                    except:
                        pass
                    website= ''
                    try:
                        website= itemNode.find('a', attrs= {'class': 'track-visit-website'}).attrs['href']
                    except: 
                        pass
                    email= ''
                    new = {'Business Name': businessName, 'Address': address, 'Phone Number': phoneNumber, 'Website': website, 'Email': email}
                    newPage.append(new)
                    self.saveToCsv(filename, newPage, columns)
        except:
            return 0


    # this part is for email search in target url
    def webEmailScrapLogin(self, url):
        emails= []
        driver= self.headlessDriver()
        urlValid= False
        if(driver== 0):
            print("Couldn't get driver, reason maybe chrome driver!")
            return 0
        try:
            driver.get(url)
            time.sleep(self.loginTime)
            urlValid= True
        except:
            driver.close()
            print("An exception occurred, maybe url is invalid or can't access!")
            return 0

        # to ge domurl
        url= url.strip()
        urltmp= url[8:]
        urltmp= urltmp.split('/')[0]
        domurl= url[:8]+ urltmp
        if(url[-1]== '/'):
            domurl= url[:-1]
        if urlValid== True:
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            newEmails= self.emailFinder(soup)
            emails.extend(newEmails)
            # urls= self.urlFinder(soup, domurl)
            urls= self.contactAbtUrlFinder(soup, domurl)
            for url1 in urls:
                # self.webEmailScrapRecursion(self.driver, url1)
                newEmails= self.webEmailScrapNavbar(driver, url1)
                emails.extend(newEmails)
            # self.emailField.append('Ended!')
            driver.close()

        return emails


    def webEmailScrapNavbar(self, driver, url):
        urlValid= False
        emails= []
        try:
            driver.get(url)
            time.sleep(self.timeout)
            urlValid= True
        except:
            driver.close()
            return emails
        if urlValid== True:
            soup= BeautifulSoup(driver.page_source, 'html.parser')
            emails= self.emailFinder(soup)
            return emails


    def emailFinder(self, soup):
        EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
        emails= []
        if soup != None:
            for re_match in re.finditer(EMAIL_REGEX, soup.text):
                email = re_match.group()
                emails.append(email)
            return emails
        else:
            return emails


    def contactAbtUrlFinder(self, soup, domurl):
        urls= []
        alinks= soup.find_all('a')
        for alink in alinks:

            try:
                alink= alink.attrs['href']
                alink= alink.strip()
            except:
                continue
            if len(alink)>0 and alink[-1]== '/':
                alink= alink[:-1]
            if len(alink)> 0:
                
                if ('http' in alink):
                    if domurl in alink:
                        if ('contact' in alink.lower()) or ('about'in alink.lower()):
                            urls.append(alink)
                elif(alink== "#"):
                    pass
                elif('http' not in alink):
                    if alink[0]== '/':
                        if ('contact' in (domurl+ alink).lower()) or ('about' in (domurl+ alink).lower() ):
                            urls.append(domurl+ alink)
                    else:
                        if ('contact' in (domurl+ '/'+ alink).lower()) or ('about' in (domurl+ '/'+ alink).lower()):
                            urls.append(domurl+'/'+ alink)
        return urls

class LinkedinGeneralScrap():
    def __init__(self):
        super().__init__()
        self.lock = threading.Lock()
        self.loginTime= 5
        self.timeout= 1
        self.scrapFinished= False
        self.progress= 1
        self.error = ''
        self.threadFlag= 0

    def headlessDriver(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument(f"--window-size=1920, 900")
        options.add_argument("--hide-scrollbars")
        try:
            driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
            agent = driver.execute_script("return navigator.userAgent")
            driver.close()
            options.add_argument("user-agent="+agent)
            driver= webdriver.Chrome(options= options, executable_path="chromedriver.exe")
            
            return driver
        except:
            print("You must use same chrome version with chrome driver!")
            self.lock.acquire()
            self.error= "You must use same chrome version with chrome driver!"
            self.lock.release()
            return 0
            
    def headDriver(self):
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
            self.lock.acquire()
            self.error= "You must use same chrome version with chrome driver!"
            self.lock.release()
            return 0

    def setProgress(self):
        if self.scrapFinished:
            if(self.error== ''):
                # _thread.start_new_thread( self.progressBar.setValue, (100, ) )
                # self.progressBar.setValue(100)
                
                self.desc.setText('Success!')
                self.desc.setStyleSheet('font: 20px; color: green')
                # self.progressBar.setValue(100)
                return 0
            else:
                self.desc.setText(self.error)
                self.desc.setStyleSheet('color: red')
                # self.progressBar.setStyleSheet(COMPLETED_STYLE)
                return 0
        else:

            self.progressBar.setValue(self.progress)
            threading.Timer(2.0, self.setProgress).start()

    def startProgressDialog(self):
        self.dlg= QDialog()
        self.dlg.setWindowTitle('Scrap percent')
        self.dlg.setStyleSheet("background-color:#303030; color:#dddddd")
        self.desc= QLabel("Now inserting into file, Don't open file before finish!")
        vbox= QVBoxLayout()
        vbox.addWidget(self.desc)
        self.progressBar= QProgressBar(self.dlg)
        self.progressBar.setMaximum(101)
        vbox.addWidget(self.progressBar)
        hbox= QHBoxLayout()
        stopBtn= QPushButton('Stop')
        stopBtn.clicked.connect(self.dlgClose)
        finishBtn= QPushButton('Finish')
        finishBtn.clicked.connect(self.dlgClose)
        hbox.addWidget(stopBtn)
        hbox.addWidget(finishBtn)
        vbox.addLayout(hbox)
        self.dlg.setLayout(vbox)
        self.dlg.setWindowModality(Qt.ApplicationModal)
        self.setProgress()
        self.dlg.exec_()
        

    def dlgClose(self):
        self.dlg.close()

    def writeCsvheader(self, filename, columns):
        try:
            os.remove(filename)
        except:
            pass
        df= pd.DataFrame(columns= columns)
        # filename= str(datetime.datetime.now()).replace(':', '-')+'.csv'
        df.to_csv(filename, mode= 'x', index= False, encoding='utf-8-sig')
        # return filename

    def saveToCsv(self, filename, newPage, columns):
        df = pd.DataFrame(newPage, columns = columns)
        print("Now items writed in csv file!")
        df.to_csv(filename, mode='a', header=False, index=False, encoding='utf-8-sig')

    def start(self, username, password, intendedUrl, pageNum, filename):
        
        threading.Thread(target= self.linkedinGeneralScrapCore, args = (username, password, intendedUrl, pageNum, filename,)).start()

        self.startProgressDialog()

    def linkedinGeneralScrapCore(self, username, password, intendedUrl, pageNum, filename):
        

        if(intendedUrl[-1]== "/"):
            intendedUrl= intendedUrl[:-1]
        columns=['First Name', 'Last Name', 'Job Title', 'Company Name', 'Profile Url', 'Location', 'Email']
        try:
            self.writeCsvheader(filename, columns)
        except:
            self.lock.acquire()
            self.error= "File path incorrect or File already exist! Please choose other name or delete orign file!"
            self.scrapFinished= True
            self.lock.release()
            return 0
        
        urls = []
        for i in range(pageNum):
            nextintendedUrl = intendedUrl + "&page=" + str(i + 1)
            urls.append(nextintendedUrl)
        modifiedUrls = modifyUrls(urls)
        print(modifiedUrls)
        for modifiedUrl in modifiedUrls:
            self.lock.acquire()
            self.threadFlag= 0
            self.lock.release()
            for one in modifiedUrl:
                threading.Thread(target= self.linkedinGeneralOnepageScrap, args = (one, filename, columns, pageNum, username, password, )).start()
            while self.threadFlag!= len(modifiedUrl):
                time.sleep(2)
            print("now Thread one finish!")
        self.lock.acquire()
        self.scrapFinished= True
        self.lock.release()


    def linkedinGeneralOnepageScrap(self, url, filename, columns, pageNum, username, password):
        signinUrl = "https://www.linkedin.com/uas/login"
        # Login part

        try:
            driver= self.headlessDriver()
            driver.get(signinUrl)
            time.sleep(self.timeout * 2)
            username_input = driver.find_element_by_id('username')
            username_input.send_keys(username)

            password_input = driver.find_element_by_id('password')
            password_input.send_keys(password)
            password_input.submit()
            time.sleep(self.timeout)
        except:
            print('/////////////////////loginpart error')
            self.lock.acquire()
            self.progress+= int(100/pageNum)
            self.threadFlag+= 1
            self.lock.release()
            return 0
        
        
        driver.get(url)
        time.sleep(self.timeout)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        itemNodes = soup.find_all('div', attrs={'class': 'entity-result__item'})
        if itemNodes == []:
            print('///////////////////itemNodes error')
            self.lock.acquire()
            self.threadFlag+= 1
            self.lock.release()
            return 0
        nodeLinks= []
        for itemNode in itemNodes:
            nodeLink= itemNode.find('a').attrs['href']
            nodeLinks.append(nodeLink)

        for nodeLink in nodeLinks:
            newPage= []
            try:
                driver.get(nodeLink)
                time.sleep(self.timeout)
                profileUrl= nodeLink
                soup1= BeautifulSoup(driver.page_source, 'html.parser')
                name= soup1.find('li', attrs= {'class': 'inline t-24 t-black t-normal break-words'}).text.strip()
                jobtitle= soup1.find('h2', attrs= {'class': 'mt1 t-18 t-black t-normal break-words'}).text.strip()
                location= soup1.find('li', attrs= {'class': 't-16 t-black t-normal inline-block'}).text.strip()
                companyName= ''
                try:
                    companyName= soup1.find('span', attrs= {'class': 'text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view'}).text.strip()
                except:
                    pass
                firstLast= name.split(' ', 1)
                if len(firstLast)>= 2:
                    firstname= firstLast[0]
                    lastname= firstLast[1]
                else:
                    firstname= firstLast[0]
                    lastname= ''
                # emails= self.emailFinder(soup)
                email= ''
                # for email1 in emails:
                #      email+= email1+ ' '

                new = {'First Name': firstname, 'Last Name': lastname, 'Job Title': jobtitle, 'Company Name': companyName, 'Profile Url': profileUrl, 'Location': location, 'Email': email}
                newPage.append(new)
                self.lock.acquire()
                self.saveToCsv(filename, newPage, columns)
                self.lock.release()
            except:
                continue
        self.lock.acquire()
        self.progress+= int(100/pageNum)
        self.threadFlag+= 1
        self.lock.release()
        driver.close()



    def emailFinder(self, soup):
        EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
        emails= []
        if soup != None:
            for re_match in re.finditer(EMAIL_REGEX, soup.text):
                email = re_match.group()
                emails.append(email)
            return emails
        else:
            return emails


class LinkedinNavScrap():
    def __init__(self):
        super().__init__()
        self.lock = threading.Lock()
        self.loginTime= 5
        self.timeout= 1
        self.scrapFinished= False
        self.progress= 1
        self.error= ''

    def headlessDriver(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument(f"--window-size=1920, 900")
        options.add_argument("--hide-scrollbars")
        try:
            driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
            agent = driver.execute_script("return navigator.userAgent")
            driver.close()
            options.add_argument("user-agent="+agent)
            driver= webdriver.Chrome(options= options, executable_path="chromedriver.exe")
            
            return driver
        except:
            print("You must use same chrome version with chrome driver!")
            self.lock.acquire()
            self.error= "You must use same chrome version with chrome driver!"
            self.lock.release()
            return 0
            
    def headDriver(self):
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
            self.lock.acquire()
            self.error= "You must use same chrome version with chrome driver!"
            self.lock.release()
            return 0

    def setProgress(self):
        if self.scrapFinished:
            if(self.error== ''):
                # _thread.start_new_thread( self.progressBar.setValue, (100, ) )
                # self.progressBar.setValue(100)
                
                self.desc.setText('Success!')
                self.desc.setStyleSheet('font: 20px; color: green')
                self.progressBar.setValue(100)
                return 0
            else:
                self.desc.setText(self.error)
                self.desc.setStyleSheet('color: red')
                # self.progressBar.setStyleSheet(COMPLETED_STYLE)
                return 0
        else:

            self.progressBar.setValue(self.progress)
            threading.Timer(2.0, self.setProgress).start()

    def startProgressDialog(self):
        self.dlg= QDialog()
        self.dlg.setWindowTitle('Scrap percent')
        self.dlg.setStyleSheet("background-color:#303030; color:#dddddd")
        self.desc= QLabel("Now inserting into file, Don't open file before finish!")
        vbox= QVBoxLayout()
        vbox.addWidget(self.desc)
        self.progressBar= QProgressBar(self.dlg)
        self.progressBar.setMaximum(101)
        vbox.addWidget(self.progressBar)
        hbox= QHBoxLayout()
        stopBtn= QPushButton('Stop')
        stopBtn.clicked.connect(self.dlgClose)
        finishBtn= QPushButton('Finish')
        finishBtn.clicked.connect(self.dlgClose)
        hbox.addWidget(stopBtn)
        hbox.addWidget(finishBtn)
        vbox.addLayout(hbox)
        self.dlg.setLayout(vbox)
        self.dlg.setWindowModality(Qt.ApplicationModal)
        self.setProgress()
        self.dlg.exec_()
        

    def dlgClose(self):
        self.dlg.close()

    def writeCsvheader(self, filename, columns):
        try:
            os.remove(filename)
        except:
            pass
        df= pd.DataFrame(columns= columns)
        # filename= str(datetime.datetime.now()).replace(':', '-')+'.csv'
        df.to_csv(filename, mode= 'x', index= False, encoding='utf-8-sig')
        # return filename

    def saveToCsv(self, filename, newPage, columns):
        df = pd.DataFrame(newPage, columns = columns)
        print("Now items writed in csv file!")
        df.to_csv(filename, mode='a', header=False, index=False, encoding='utf-8-sig')

    def start(self, username, password, intendedUrl, pageNum, filename):
        
        threading.Thread(target= self.linkedinNavScrapCore, args = (username, password, intendedUrl, pageNum, filename,)).start()

        self.startProgressDialog()

    def linkedinNavScrapCore(self, username, password, intendedUrl, pageNum, filename):
        signinUrl= "https://www.linkedin.com/uas/login"

        if(intendedUrl[-1]== "/"):
            intendedUrl= intendedUrl[:-1]
        columns=['First Name', 'Last Name', 'Job Title', 'Company Name', 'Profile Url', 'Location', 'Email']
        try:
            self.writeCsvheader(filename, columns)
        except:
            self.lock.acquire()
            self.error= "File path incorrect or File already exist! Please choose other name or delete orign file!"
            self.scrapFinished= True
            self.lock.release()
            return 0
        try:
            driver= self.headlessDriver()
            driver.get(signinUrl)
        except:
            self.lock.acquire()
            self.error= "Couldn't access linkedin Login page!"
            self.scrapFinished= True
            self.lock.release()
            return 0
        time.sleep(self.timeout* 2)
        # Login part

        username_input = driver.find_element_by_id('username')
        username_input.send_keys(username)

        password_input = driver.find_element_by_id('password')
        password_input.send_keys(password)
        password_input.submit()
        time.sleep(self.timeout)

        for i in range(pageNum):
            
            if i== 0:
                driver.get(intendedUrl)
                time.sleep(self.loginTime)
                # scroll part
                try:
                    for i in range(8):
                        time.sleep(0.5)
                        recentList = driver.find_elements_by_xpath("//section[@class='result-lockup']")
                        if len(recentList) == 0 :
                            break
                        else :
                            driver.execute_script("arguments[0].scrollIntoView();", recentList[len(recentList) - 1 ] )
                except:
                    pass
                soup= BeautifulSoup(driver.page_source, 'html.parser')

                itemNodes= soup.find_all('section', attrs= {'class': 'result-lockup'})
                if itemNodes== []:
                    self.lock.acquire()
                    self.error= "There is no match for that url or this machine is not supported for that type intendedUrl.\n Else maybe You are blocked!"
                    self.lock.release()
                    break
                
                self.linkedinNavOnepageScrap(driver, soup, filename, columns)
                self.lock.acquire()
                self.progress= int(100/pageNum)
                self.lock.release()

            else:
                nextintendedUrl= intendedUrl+ "&page="+str(i+1)
                driver.get(nextintendedUrl)
                time.sleep(self.loginTime)
                # scroll part
                try:
                    for i in range(8):
                        time.sleep(0.5)
                        recentList = driver.find_elements_by_xpath("//section[@class='result-lockup']")
                        if len(recentList) == 0 :
                            break
                        else :
                            driver.execute_script("arguments[0].scrollIntoView();", recentList[len(recentList) - 1 ] )
                except:
                    pass
                soup= BeautifulSoup(driver.page_source, 'html.parser')

                itemNodes= soup.find_all('section', attrs= {'class': 'result-lockup'})
                if itemNodes== []:
                    break
                self.linkedinNavOnepageScrap(driver, soup, filename, columns)
                self.lock.acquire()
                self.progress= int(100/pageNum*(i+1))
                self.lock.release()
        self.lock.acquire()
        self.progress= 100
        self.scrapFinished= True
        self.lock.release()
        driver.close()

    def linkedinNavOnepageScrap(self, driver, soup, filename, columns):
        try:
            domurl= "https://www.linkedin.com"
            itemNodes= soup.find_all('section', attrs= {'class': 'result-lockup'})
            nodeLinks= []
            for itemNode in itemNodes:
                try:
                    tmp= domurl+ itemNode.find('a', attrs= {'class': 'ember-view result-lockup__icon-link'}).attrs['href']
                    nodeLink= tmp.split(',', 1)[0].replace('sales/people', 'in')
                    nodeLinks.append(nodeLink)
                except:
                    continue

            for nodeLink in nodeLinks:
                newPage= []
                try:
                    driver.get(nodeLink)
                    time.sleep(self.timeout)
                    profileUrl= driver.current_url
                    soup1= BeautifulSoup(driver.page_source, 'html.parser')
                    name= soup1.find('li', attrs= {'class': 'inline t-24 t-black t-normal break-words'}).text.strip()
                    jobtitle= soup1.find('h2', attrs= {'class': 'mt1 t-18 t-black t-normal break-words'}).text.strip()
                    location= soup1.find('li', attrs= {'class': 't-16 t-black t-normal inline-block'}).text.strip()
                    companyName= ''
                    try:
                        companyName= soup1.find('span', attrs= {'class': 'text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view'}).text.strip()
                    except:
                        pass
                    firstLast= name.split(' ', 1)
                    if len(firstLast)>= 2:
                        firstname= firstLast[0]
                        lastname= firstLast[1]
                    else:
                        firstname= firstLast[0]
                        lastname= ''
                    # emails= self.emailFinder(soup)
                    email= ''
                    # for email1 in emails:
                    #      email+= email1+ ' '

                    new = {'First Name': firstname, 'Last Name': lastname, 'Job Title': jobtitle, 'Company Name': companyName, 'Profile Url': profileUrl, 'Location': location, 'Email': email}
                    newPage.append(new)
                    self.saveToCsv(filename, newPage, columns)
                except:
                    continue
        except:
            pass



    def emailFinder(self, soup):
        EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
        emails= []
        if soup != None:
            for re_match in re.finditer(EMAIL_REGEX, soup.text):
                email = re_match.group()
                emails.append(email)
            return emails
        else:
            return emails

def showdialog(wintitle, title, desc, icon= 'warn'):
    msg = QMessageBox()
    msg.setStyleSheet("background-color:#303030; color:#dddddd")
    if icon== 'warn':
        msg.setIcon(QMessageBox.Warning)
    elif icon== 'info':
        msg.setIcon(QMessageBox.Information)
    elif icon== 'critical':
        msg.setIcon(QMessageBox.Critical)
    elif icon== 'que':
        msg.setIcon(QMessageBox.Question)
    msg.setText(title)
    msg.setInformativeText(desc)
    msg.setWindowTitle(wintitle)
    # msg.setDetailedText("The details are as follows:")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    sys.exit(msg.exec_())

def process_exists(process_name):
    try:
        if process_name in (p.name() for p in psutil.process_iter()):
            return True

    except:
        return False
        



def main():
    app = QApplication(sys.argv)
    # exeName= os.path.basename(__file__)
    exeName= "ScrapToolUI.exe"
    # if(process_exists(exeName)):
    #     showdialog("Process running", 'Already running same process', 'First close the previous exe and run again!')
    # else:
    scrap= totalpage() 
    sys.exit(app.exec_())
    # app.exec_()
   
if __name__ == '__main__':
    main()





