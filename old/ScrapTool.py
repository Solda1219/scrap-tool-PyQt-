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
import subprocess

# The tab part of UI
class tabdemo(QTabWidget):
    def __init__(self, parent = None):
        super(tabdemo, self).__init__(parent)
        self.dashboard = QWidget()
        self.dashboard.setStyleSheet("background-color:rgb(56, 58, 89); border-radius: 10px")
        self.webemail = QWidget()
        self.webemail.setStyleSheet("background-color:rgb(56, 58, 89); border-radius: 10px")
        self.socialmail = QWidget()
        # setStyleSheet("QLineEdit { background-color: yellow }")
        self.socialmail.setStyleSheet(" background-color:rgb(56, 58, 89); border-radius: 10px; ")
        # QLabel { color: rgb(254, 121, 190) }
        self.googlemap = QWidget()
        self.googlemap.setStyleSheet("background-color:rgb(56, 58, 89); border-radius: 10px")
        self.yellowpage = QWidget()
        self.yellowpage.setStyleSheet("background-color:rgb(56, 58, 89); border-radius: 10px")
        self.yelppage = QWidget()
        self.yelppage.setStyleSheet("background-color:rgb(56, 58, 89); border-radius: 10px")
        self.linkedinnav = QWidget()
        self.linkedinnav.setStyleSheet("background-color:rgb(56, 58, 89); border-radius: 10px")
        self.linkedingeneral= QWidget()
        self.linkedingeneral.setStyleSheet("background-color:rgb(56, 58, 89); border-radius: 10px")
      

        self.setStyleSheet('QTabBar::tab { background-color:rgb(56, 58, 89);color: rgb(254, 121, 190); border-width: 2px; border-style: solid; border-bottom: 0px; border-color: gray; border-top-left-radius: 6px; border-top-right-radius: 6px; padding: 5px;} QTabBar::tab:selected { background-color: rgb(98, 114, 164); }')
        self.addTab(self.dashboard,"Tab 1")

        self.addTab(self.webemail,"Tab 2")
        self.addTab(self.socialmail,"Tab 3")
        self.addTab(self.googlemap, "Tab 4")
        self.addTab(self.yellowpage, "Tab 5")
        self.addTab(self.yelppage, "Tab 6")
        self.addTab(self.linkedinnav, "Tab 7")
        self.addTab(self.linkedingeneral, "Tab 8")
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
        layout = QVBoxLayout()
        layout.addStretch(0)
        layout.setContentsMargins(-1, -1, -1, 0)
        title= "<strong>Power Scrap</strong>"
        text= "This is scraping tool! This provides website email scrap and social mail scrap for free.\n\
        But this also has powerful scrap tools like Yellow, Yelp page and Linkedin scrap tool.\n If you want to use this functions, just improve your membership. Thanks!"
        titleLabel= QLabel(title)
        titleLabel.setAlignment(Qt.AlignCenter)
        titleLabel.setStyleSheet('color: rgb(254, 121, 190); font-size: 40px; font-family: NSimSun;')
        label= QLabel(text)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet('color: rgb(98, 114, 164); font-size:14px')
        layout.addWidget(titleLabel)
        layout.addWidget(label)
        layout.addStretch(0)
        self.setTabText(0,"Dashboard")
        self.dashboard.setLayout(layout)
      
    def webemailUI(self):
        description = "<strong>Please enter any website's url where you want to scrap email from.</strong>\n"
        label= QLabel(self.webemail)
        label.setText(description)
        label.setStyleSheet('margin-left: 210px; margin-top: 90px; color: rgb(254, 121, 190)')
        layout= QFormLayout()
        layout.addRow(label, )

        labelForEdit= QLabel('Url')
        labelForEdit.setStyleSheet('color: rgb(254, 121, 190);')
        # labelForEdit.setStyleSheet('margin-left: 210px; margin-top: 100px')
        Edit= QLineEdit()
        Edit.setStyleSheet('background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        Edit.resize(200,10)
        layout.addRow(labelForEdit,Edit)
        startForWebEmail= QPushButton(self.webemail)
        startForWebEmail.setText('Start')
        startForWebEmail.setStyleSheet('background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:5px; padding: 3px')
        startForWebEmail.setFixedWidth(100)

        # trigger webemail scrap
        startForWebEmail.clicked.connect(partial(self.webemailScrapTrigger, Edit))

        # startForWebEmail.setStyleSheet('margin-left: 290px; margin-top: 120px')
        layout.addRow('', startForWebEmail)
        self.webemail.setLayout(layout)


        self.setTabText(1,"Website Email")

    def socialmailUI(self):
        # QLabel().setStyleSheet('color: rgb(254, 121, 190)')
        layout = QFormLayout()
        labelForKey= QLabel('Keyword/Category/Job title')
        labelForKey.setStyleSheet('margin-top: 20px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForKey) 
        EditForKey= QLineEdit()
        EditForKey.setStyleSheet('margin-bottom: 5px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        layout.addRow('', EditForKey)
        labelForLocation= QLabel('Location(Optional)')
        labelForLocation.setStyleSheet('color: rgb(254, 121, 190)')
        layout.addRow('', labelForLocation)
        EditForLocation= QLineEdit()
        EditForLocation.setStyleSheet('margin-bottom: 5px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        layout.addRow('', EditForLocation)
        labelForSelctSocial= QLabel('Select Social Network')
        labelForSelctSocial.setStyleSheet('color: rgb(254, 121, 190)')
        layout.addRow('', labelForSelctSocial)
        selectSocial= QComboBox()
        selectSocial.addItem('Instagram.com')
        selectSocial.addItem('Facebook.com')
        selectSocial.addItem('Linkedin.com')
        selectSocial.addItem('Twitter.com')
        selectSocial.setStyleSheet('margin-bottom: 5px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        layout.addRow('', selectSocial)
        labelForCountry= QLabel('Country')
        labelForCountry.setStyleSheet('color: rgb(254, 121, 190)')
        layout.addRow('', labelForCountry)
        EditForCountry= QLineEdit()
        EditForCountry.setStyleSheet('margin-bottom: 5px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        layout.addRow('', EditForCountry)
        labelForEngine= QLabel('Select search engine')
        labelForEngine.setStyleSheet('color: rgb(254, 121, 190)')
        layout.addRow('', labelForEngine )
        selectEngine= QComboBox()
        selectEngine.addItem('Google')
        selectEngine.addItem('Yahoo')
        selectEngine.addItem('Bing')
        selectEngine.setStyleSheet('margin-bottom: 5px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        layout.addRow('', selectEngine)
        labelForEmailType= QLabel('Email type for search')
        labelForEmailType.setStyleSheet('color: rgb(254, 121, 190)')
        layout.addRow('', labelForEmailType)
        selectForEmailType= QComboBox()
        selectForEmailType.addItem('@gmail.com')
        selectForEmailType.addItem('@yahoo.com')
        selectForEmailType.addItem('@outlook.com')
        selectForEmailType.addItem('@zoho.com')
        selectForEmailType.setStyleSheet('margin-bottom: 5px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        layout.addRow('', selectForEmailType)
        labelForPageNum= QLabel('Please type Page count(optional)')
        labelForPageNum.setStyleSheet('color: rgb(254, 121, 190)')
        layout.addRow('', labelForPageNum )
        EditForPageNum= QLineEdit()
        EditForPageNum.setStyleSheet('margin-bottom: 5px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        layout.addRow('', EditForPageNum)

        labelForPath= QLabel('Please choose file path to save(optional)')
        labelForPath.setStyleSheet('margin-top: 5px; margin-bottom: 5px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForPath)

        # This is save path part
        savePathForm= QFormLayout()
        # EditForFileName= QLineEdit('scrap')
        # EditForFileName.setStyleSheet('margin-bottom:5px')
        # savePathForm.addRow(QLabel('File Name'), EditForFileName)

        nowPath= os.path.dirname(os.path.abspath(__file__))
        print(nowPath)

        savePathBtn= QPushButton('Driver Location')
        savePathBtn.setStyleSheet('background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:5px; padding: 2px')
        savePath= QLineEdit()
        savePath.setText(nowPath+'/save.csv')
        savePath.setStyleSheet('margin-bottom:15px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
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
        startForSocial.setStyleSheet('background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:5px; padding: 3px')
        layout.addRow(QLabel(''), startForSocial)
        self.setTabText(2,"Socila Mail")
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
        labelForDesc.setStyleSheet('margin-top: 30px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForDesc)
        eidtForGoogleMap= QLineEdit()
        eidtForGoogleMap.setStyleSheet('margin-bottom:10px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        layout.addRow('', eidtForGoogleMap)

        labelForPageNum= QLabel('Please type Page count(optional)')
        labelForPageNum.setStyleSheet('margin-top: 10px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForPageNum )
        EditForPageNum= QLineEdit()
        EditForPageNum.setStyleSheet('margin-bottom: 10px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        layout.addRow('', EditForPageNum)

        # This is save path part
        labelForPath= QLabel('Please choose file path to save(optional)')
        labelForPath.setStyleSheet(' margin-bottom: 10px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForPath)

        
        savePathForm= QFormLayout()

        nowPath= os.path.dirname(os.path.abspath(__file__))
        print(nowPath)

        savePathBtn= QPushButton('Driver Location')
        savePathBtn.setStyleSheet('background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:5px; padding: 2px')
        savePath= QLineEdit()
        savePath.setText(nowPath+'/save.csv')
        savePath.setStyleSheet('margin-bottom:15px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        savePathBtn.clicked.connect(partial(self.filePathSelect, savePath))
        savePathForm.addRow(savePathBtn, savePath)
        
        layout.addRow('', savePathForm)
        startForGoogleMap= QPushButton(self.webemail)
        startForGoogleMap.setText('Start')
        startForGoogleMap.setFixedWidth(100)
        startForGoogleMap.setStyleSheet('background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:5px; padding: 3px')
        layout.addRow(QLabel(''), startForGoogleMap)
        self.setTabText(3,"Google Map")
        self.googlemap.setLayout(layout)

        startForGoogleMap.clicked.connect(partial(self.googlemapScrapTrigger, eidtForGoogleMap, EditForPageNum, savePath))

        

    def yellowpageUI(self):
        layout= QFormLayout()
        labelForDesc= QLabel("Please enter any yellow page's url where you want to scrap from.")
        labelForDesc.setStyleSheet('margin-top: 30px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForDesc)
        eidtForYellowPage= QLineEdit()
        eidtForYellowPage.setStyleSheet('margin-bottom:10px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        layout.addRow('', eidtForYellowPage)

        labelForPageNum= QLabel('Please type Page count(optional)')
        labelForPageNum.setStyleSheet('margin-top: 10px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForPageNum )
        EditForPageNum= QLineEdit()
        EditForPageNum.setStyleSheet('margin-bottom: 10px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        layout.addRow('', EditForPageNum)

        # This is save path part
        labelForPath= QLabel('Please choose file path to save(optional)')
        labelForPath.setStyleSheet(' margin-bottom: 10px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForPath)

        
        savePathForm= QFormLayout()

        nowPath= os.path.dirname(os.path.abspath(__file__))
        print(nowPath)

        savePathBtn= QPushButton('Driver Location')
        savePathBtn.setStyleSheet('background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:5px; padding: 2px')
        savePath= QLineEdit()
        savePath.setText(nowPath+'/save.csv')
        savePath.setStyleSheet('margin-bottom:15px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        savePathBtn.clicked.connect(partial(self.filePathSelect, savePath))
        savePathForm.addRow(savePathBtn, savePath)
        
        layout.addRow('', savePathForm)
        startForYellowPage= QPushButton(self.webemail)
        startForYellowPage.setText('Start')
        startForYellowPage.setFixedWidth(100)
        startForYellowPage.setStyleSheet('background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:5px; padding: 3px')
        layout.addRow(QLabel(''), startForYellowPage)
        self.setTabText(4,"Yellow Page")
        self.yellowpage.setLayout(layout)

        startForYellowPage.clicked.connect(partial(self.yellowpageScrapTrigger, eidtForYellowPage, EditForPageNum, savePath))


    def yelppageUI(self):
        layout= QFormLayout()
        labelForDesc= QLabel("Please enter any yelp page's url where you want to scrap from.")
        labelForDesc.setStyleSheet('margin-top: 30px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForDesc)
        eidtForYelpPage= QLineEdit()
        eidtForYelpPage.setStyleSheet('margin-bottom:10px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        layout.addRow('', eidtForYelpPage)

        labelForPageNum= QLabel('Please type Page count(optional)')
        labelForPageNum.setStyleSheet('margin-top: 10px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForPageNum )
        EditForPageNum= QLineEdit()
        EditForPageNum.setStyleSheet('margin-bottom: 10px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        layout.addRow('', EditForPageNum)

        # This is save path part
        labelForPath= QLabel('Please choose file path to save(optional)')
        labelForPath.setStyleSheet(' margin-bottom: 10px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForPath)

        
        savePathForm= QFormLayout()

        nowPath= os.path.dirname(os.path.abspath(__file__))
        print(nowPath)

        savePathBtn= QPushButton('Driver Location')
        savePathBtn.setStyleSheet('background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:5px; padding: 2px')
        savePath= QLineEdit()
        savePath.setText(nowPath+'/save.csv')
        savePath.setStyleSheet('margin-bottom:15px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        savePathBtn.clicked.connect(partial(self.filePathSelect, savePath))
        savePathForm.addRow(savePathBtn, savePath)
        
        layout.addRow('', savePathForm)
        startForYelpPage= QPushButton(self.webemail)
        startForYelpPage.setText('Start')
        startForYelpPage.setFixedWidth(100)
        startForYelpPage.setStyleSheet('background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:5px; padding: 3px')
        layout.addRow(QLabel(''), startForYelpPage)
        self.setTabText(5,"Yelp Page")
        self.yelppage.setLayout(layout)

        startForYelpPage.clicked.connect(partial(self.yelppageScrapTrigger, eidtForYelpPage, EditForPageNum, savePath))


    def linkedinnavUI(self):
        layout = QFormLayout()

        labelForUsername= QLabel('Linkedin Username')
        labelForUsername.setStyleSheet('margin-top:30px; margin-bottom: 5px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForUsername)
        username= QLineEdit()
        username.setStyleSheet(" margin-bottom: 15px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px")
        layout.addRow('', username)
        labelForPass= QLabel('Linkedin Password')
        labelForPass.setStyleSheet('margin-bottom: 5px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForPass)
        password= QLineEdit()
        password.setStyleSheet("margin-bottom: 15px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px")
        layout.addRow('', password)
        labelForIntendedUrl= QLabel('Intended Url')
        labelForIntendedUrl.setStyleSheet('margin-bottom: 5px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForIntendedUrl)
        intendedUrl= QLineEdit()
        intendedUrl.setStyleSheet("margin-bottom: 15px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px")
        layout.addRow('', intendedUrl)
        labelForPageNum= QLabel('Please type Page count(optional)')
        labelForPageNum.setStyleSheet('margin-bottom: 5px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForPageNum )
        EditForPageNum= QLineEdit()
        EditForPageNum.setStyleSheet('margin-bottom: 15px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        layout.addRow('', EditForPageNum)

        # This is save path part
        labelForPath= QLabel('Please choose file path to save(optional)')
        labelForPath.setStyleSheet(' margin-bottom: 5px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForPath)

        
        savePathForm= QFormLayout()

        nowPath= os.path.dirname(os.path.abspath(__file__))

        savePathBtn= QPushButton('Driver Location')
        savePathBtn.setStyleSheet('background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:5px; padding: 2px')

        savePath= QLineEdit()
        savePath.setText(nowPath+'/save.csv')
        savePath.setStyleSheet('margin-bottom:15px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        savePathBtn.clicked.connect(partial(self.filePathSelect, savePath))
        savePathForm.addRow(savePathBtn, savePath)
        
        layout.addRow('', savePathForm)
        

        startForLinkedinNav= QPushButton('Start')
        startForLinkedinNav.setFixedWidth(100)
        startForLinkedinNav.setStyleSheet('background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:5px; padding: 3px')
        layout.addRow(QLabel(), startForLinkedinNav)

        self.setTabText(6,"Linkedin Sales Nav")
        self.linkedinnav.setLayout(layout)
        startForLinkedinNav.clicked.connect(partial(self.linkedinNavScrapTrigger, username, password, intendedUrl, EditForPageNum, savePath))



    def linkedingeneralUI(self):
        layout = QFormLayout()

        labelForUsername= QLabel('Linkedin Username')
        labelForUsername.setStyleSheet('margin-top:30px; margin-bottom: 5px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForUsername)
        username= QLineEdit()
        username.setStyleSheet(" margin-bottom: 15px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px")
        layout.addRow('', username)
        labelForPass= QLabel('Linkedin Password')
        labelForPass.setStyleSheet('margin-bottom: 5px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForPass)
        password= QLineEdit()
        password.setStyleSheet("margin-bottom: 15px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px")
        layout.addRow('', password)
        labelForIntendedUrl= QLabel('Intended Url')
        labelForIntendedUrl.setStyleSheet('margin-bottom: 5px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForIntendedUrl)
        intendedUrl= QLineEdit()
        intendedUrl.setStyleSheet("margin-bottom: 15px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px")
        layout.addRow('', intendedUrl)
        labelForPageNum= QLabel('Please type Page count(optional)')
        labelForPageNum.setStyleSheet('margin-bottom: 5px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForPageNum )
        EditForPageNum= QLineEdit()
        EditForPageNum.setStyleSheet('margin-bottom: 15px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        layout.addRow('', EditForPageNum)

        # This is save path part
        labelForPath= QLabel('Please choose file path to save(optional)')
        labelForPath.setStyleSheet(' margin-bottom: 5px; color: rgb(254, 121, 190)')
        layout.addRow('', labelForPath)

        
        savePathForm= QFormLayout()

        nowPath= os.path.dirname(os.path.abspath(__file__))

        savePathBtn= QPushButton('Driver Location')
        savePathBtn.setStyleSheet('background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:5px; padding: 2px')

        savePath= QLineEdit()
        savePath.setText(nowPath+'/save.csv')
        savePath.setStyleSheet('margin-bottom:15px; background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:10px')
        savePathBtn.clicked.connect(partial(self.filePathSelect, savePath))
        savePathForm.addRow(savePathBtn, savePath)
        
        layout.addRow('', savePathForm)
        

        startForLinkedGeneral= QPushButton('Start')
        startForLinkedGeneral.setFixedWidth(100)
        startForLinkedGeneral.setStyleSheet('background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:5px; padding: 3px')
        layout.addRow(QLabel(), startForLinkedGeneral)

        self.setTabText(7,"Linkedin General")
        self.linkedingeneral.setLayout(layout)
        startForLinkedGeneral.clicked.connect(partial(self.linkedinGeneralScrapTrigger, username, password, intendedUrl, EditForPageNum, savePath))


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
        self.setStyleSheet('background-color: silver')
        self.userEmail= ''
        self.loginStatus= False
        splitter1 = QSplitter()
        splitter1.setOrientation(Qt.Vertical)
        header= QFrame(splitter1)
        header.setFixedHeight(70)
        header.setFrameShape(QFrame.StyledPanel)
        layoutForHead= QHBoxLayout(self)
        btnSuper= QPushButton('Super member!')
        btnSuper.setStyleSheet('background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:5px; padding: 5px')
        layoutForHead.addWidget(btnSuper)
        self.btnLogin= QPushButton('Login')
        self.btnLogin.setStyleSheet('background-color: rgb(98, 114, 164); color: rgb(254, 121, 190); border: 2px solid gray; border-radius:5px; padding: 5px')
        if self.loginStatus== True:
            self.btnLogin.setText('Logout')
        self.btnLogin.clicked.connect(self.loginUI)
        layoutForHead.addWidget(self.btnLogin)
        header.setLayout(layoutForHead)

        body = QFrame(splitter1)
        body.setFrameShape(QFrame.StyledPanel)
        layoutForBody= QHBoxLayout(self)
        self.tab= tabdemo()

        self.setdisableAllTab(False)


        layoutForBody.addWidget(self.tab)
        body.setLayout(layoutForBody)
        hbox= QHBoxLayout(self)
        hbox.addWidget(splitter1)
        self.setFixedWidth(800)
        self.setMinimumSize(800, 650)
        # self.setFixedHeight(550)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    
        if reply == QMessageBox.Yes:
            # when cloe, will be loged out
            if(self.userEmail!= ''):
                self.logout()
            event.accept()
            print('Window closed')
        else:
            event.ignore()

    def setdisableAllTab(self, status):
        for i in range(7):
            self.tab.setTabEnabled(i+1, status)

    def setLoginTab(self, status):
        for i in range(2):
            self.tab.setTabEnabled(i+1, status)

    def setSuperTab(self, status):
        for i in range(5):
            self.tab.setTabEnabled(i+3, status)

    def loginUI(self):
        if self.btnLogin.text()== 'Login':
            self.loginDg = QDialog()
            # self.loginDg.setMinimumSize(300, 200)
            # self.loginDg.resize(300, 200)
            layout= QFormLayout()
            email= QLineEdit()
            layout.addRow(QLabel('Email'), email)
            password= QLineEdit()
            layout.addRow(QLabel('Password'), password)
            btnLogin= QPushButton("Login")
            btnLogin.clicked.connect(partial(self.login, email, password))
            # btnLogin.setStyleSheet('margin-bottom: 5px')
            layout.addRow(QLabel(), btnLogin)
            btnRegister= QPushButton('Register')

            # this is register part
            # btnRegister.clicked.connect(self.registerUI)
            labelForRegister= QLabel("Didn't you register?")


            # labelForRegister.setStyleSheet('margin-top: 10px')
            # btnRegister.setStyleSheet('margin-top: 10px')
            layout.addRow(labelForRegister, btnRegister)
            self.loginDg.setLayout(layout)
            self.loginDg.setWindowTitle("Login")
            self.loginDg.setWindowModality(Qt.ApplicationModal)

            self.loginDg.exec_()
        elif self.btnLogin.text()== 'Logout':
            self.logout()

    def login(self, email, password):
        loginUrl= 'http://127.0.0.1:8000/login'
        if(email.text()== '' or password.text()== ''):
            self.showdialog('Validation', 'Validation Error', 'You must fill out all fields!')
        else:
            PARAMS= {
                'email': email.text(),
                'password': password.text()
                }
            print(PARAMS)
            try:
                r= requests.get(url= loginUrl, params= PARAMS)
                print(r)
                user= r.json()
                if(user['email']):
                    self.userEmail= user['email']
                    print(self.userEmail)
                    self.setLoginTab(True)
                    self.loginStatus= True
                    self.btnLogin.setText('Logout')
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

    def showLoginSuccessdialog(self):
        msg = QMessageBox()
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
        logoutUrl= 'http://127.0.0.1:8000/logout'
        r= requests.get(url= logoutUrl, params= {'email': self.userEmail})
        if(r.text== "logout success"):
            self.setdisableAllTab(False)
            self.showdialog('Success', 'Logout Success', 'Successfully loged out!', 'info')
            self.loginStatus= False
            self.btnLogin.setText('Login')
        else:
            self.showdialog('Error', 'Something went wrong from server!', 'critical')

        
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
        self.dlg= QDialog()
        self.dlg.setWindowTitle('Scrap percent')
        self.desc= QLabel("Now inserting into file, Don't open file before finish!")
        vbox= QVBoxLayout()
        vbox.addWidget(self.desc)
        self.progressBar= QProgressBar(self.dlg)
        self.progressBar.setMaximum(100)
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

        query= f"""{EditForKey}+"{selectForEmailType}"+AND+"{EditForCountry}"+AND+"{EditForLocation}"+site:{selectSocial} """
        

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
        self.desc= QLabel("Now inserting into file, Don't open file before finish!")
        vbox= QVBoxLayout()
        vbox.addWidget(self.desc)
        self.progressBar= QProgressBar(self.dlg)
        self.progressBar.setMaximum(100)
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
            driver.find_element_by_xpath("//a[@class= 'axGQJc']").click()
            time.sleep(self.timeout)
            try:
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
        self.desc= QLabel("Now inserting into file, Don't open file before finish!")
        vbox= QVBoxLayout()
        vbox.addWidget(self.desc)
        self.progressBar= QProgressBar(self.dlg)
        self.progressBar.setMaximum(100)
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



    def yelppageOnepageScrap(self, soup, filename, columns):
        domurl= "https://www.yelp.com"
        try:
            yelpDoms= soup.find_all('div', attrs= {'class': 'container__09f24__21w3G hoverable__09f24__2nTf3 margin-t3__09f24__5bM2Z margin-b3__09f24__1DQ9x padding-t3__09f24__-R_5x padding-r3__09f24__1pBFG padding-b3__09f24__1vW6j padding-l3__09f24__1yCJf border--top__09f24__1H_WE border--right__09f24__28idl border--bottom__09f24__2FjZW border--left__09f24__33iol border-color--default__09f24__R1nRO'})
            for yelpDom in yelpDoms:
                try:
                    businessName= yelpDom.find('h4').text
                    site= yelpDom.find('a').attrs['href']
                    driver= self.headlessDriver()
                    driver.get(domurl+ site)
                    time.sleep(self.loginTime)

                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    driver.close()
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
                    self.saveToCsv(filename, newPage, columns)
                except:
                    continue
        except:
            pass

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
                    response= requests.get(url)
                except:
                    continue
                soup = BeautifulSoup(response.text, 'html.parser')
                yelpDoms= soup.find_all('div', attrs= {'class': 'container__09f24__21w3G hoverable__09f24__2nTf3 margin-t3__09f24__5bM2Z margin-b3__09f24__1DQ9x padding-t3__09f24__-R_5x padding-r3__09f24__1pBFG padding-b3__09f24__1vW6j padding-l3__09f24__1yCJf border--top__09f24__1H_WE border--right__09f24__28idl border--bottom__09f24__2FjZW border--left__09f24__33iol border-color--default__09f24__R1nRO'})
                if(yelpDoms== []):
                    self.lock.acquire()
                    self.error= "There is no match for that url or this machine is not supported for that type url.\n Else maybe You are blocked!"
                    self.lock.release()
                    break
                pageInterval= len(yelpDoms)
                self.yelppageOnepageScrap(soup, filename, columns)
                self.lock.acquire()
                self.progress= int(100/pageNum)
                self.lock.release()

            else:
                nextIndex= str(i*pageInterval)
                nextUrl= url+ '&start='+ nextIndex
                try:
                    response= requests.get(nextUrl)
                except:
                    continue
                soup = BeautifulSoup(response.text, 'html.parser')
                self.yelppageOnepageScrap(soup, filename, columns)
                self.lock.acquire()
                self.progress= int((100/pageNum)*(i+1))
                self.lock.release()

        self.lock.acquire()
        self.progress= 100
        self.scrapFinished= True
        self.lock.release()
        driver.close()

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
        self.desc= QLabel("Now inserting into file, Don't open file before finish!")
        vbox= QVBoxLayout()
        vbox.addWidget(self.desc)
        self.progressBar= QProgressBar(self.dlg)
        self.progressBar.setMaximum(100)
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
        try:
            driver= self.headlessDriver()
            driver.get(url)
        except:
            self.lock.acquire()
            self.scrapFinished= True
            self.lock.release()
            return 0
        time.sleep(self.loginTime)

        for i in range(pageNum):
            
            if i== 0:
                # soup = BeautifulSoup(driver.page_source, 'html.parser')
                itemClicks= driver.find_elements_by_xpath("//div[@class='v-card']")
                if itemClicks== []:
                    self.lock.acquire()
                    self.error= "There is no match for that url or this machine is not supported for that type url.\n Else maybe You are blocked!"
                    self.lock.release()
                    break
                
                self.yellowpageOnepageScrap(driver, filename, columns)
                self.lock.acquire()
                self.progress= int(100/pageNum)
                self.lock.release()
                try:
                    nextBtn= driver.find_element_by_xpath("//a[@class= 'next ajax-page']").text
                except:
                    break

            else:
                nextUrl= url+ "?page="+str(i+1)
                driver.get(nextUrl)
                time.sleep(self.timeout)
                self.yellowpageOnepageScrap(driver, filename, columns)
                self.lock.acquire()
                self.progress= int(100/pageNum*(i+1))
                self.lock.release()
                try:
                    nextBtn= driver.find_element_by_xpath("//a[@class= 'next ajax-page']").text
                except:
                    break
        self.lock.acquire()
        self.progress= 100
        self.scrapFinished= True
        self.lock.release()
        driver.close()

    def yellowpageOnepageScrap(self, driver, filename, columns):
        domurl= "https://www.yellowpages.com"
        try:
            soup=BeautifulSoup(driver.page_source, 'html.parser')
            tmpNodes= soup.find_all('a', attrs= {'class': 'business-name'})
            itemClicks= []
            for tmpNode in tmpNodes:
                try:
                    tmp= domurl+ tmpNode.attrs['href']
                    itemClicks.append(tmp)
                except:
                    continue
            # itemClicks= driver.find_elements_by_xpath("//div[@class='v-card']")
            for itemClick in itemClicks:
                try:
                    driver.get(itemClick)
                    time.sleep(self.timeout)
                    soup= BeautifulSoup(driver.page_source, 'html.parser')
                    itemNode= soup.find('header', attrs= {'id': 'main-header'})
                    newPage= []
                    businessName= itemNode.find('h1').text
                    address= itemNode.find('h2', attrs= {'class': 'address'}).text
                    phoneNumber= 0
                    try:
                        phoneNumber= itemNode.find('p', attrs= {'class': 'phone'}).text
                    except:
                        pass
                    
                    website= 0
                    try:
                        website= itemNode.find('a', attrs= {'class': 'primary-btn website-link'}).attrs['href']
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
        self.desc= QLabel("Now inserting into file, Don't open file before finish!")
        vbox= QVBoxLayout()
        vbox.addWidget(self.desc)
        self.progressBar= QProgressBar(self.dlg)
        self.progressBar.setMaximum(100)
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
                time.sleep(self.timeout)
                soup= BeautifulSoup(driver.page_source, 'html.parser')

                itemNodes= soup.find_all('div', attrs= {'class': 'entity-result__item'})
                if itemNodes== []:
                    self.lock.acquire()
                    self.error= "There is no match for that url or this machine is not supported for that type intendedUrl.\n Else maybe You are blocked!"
                    self.lock.release()
                    break
                
                self.linkedinGeneralOnepageScrap(driver, soup, filename, columns)
                self.lock.acquire()
                self.progress= int(100/pageNum)
                self.lock.release()

            else:
                nextintendedUrl= intendedUrl+ "&page="+str(i+1)
                driver.get(nextintendedUrl)
                time.sleep(self.timeout)
                soup= BeautifulSoup(driver.page_source, 'html.parser')

                itemNodes= soup.find_all('div', attrs= {'class': 'entity-result__item'})
                if itemNodes== []:
                    break
                self.linkedinGeneralOnepageScrap(driver, soup, filename, columns)
                self.lock.acquire()
                self.progress= int(100/pageNum*(i+1))
                self.lock.release()
        self.lock.acquire()
        self.progress= 100
        self.scrapFinished= True
        self.lock.release()
        driver.close()

    def linkedinGeneralOnepageScrap(self, driver, soup, filename, columns):
        try:
            itemNodes= soup.find_all('div', attrs= {'class': 'entity-result__item'})
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
                    emails= self.emailFinder(soup)
                    email= ''
                    for email1 in emails:
                         email+= email1+ ' '

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
        self.desc= QLabel("Now inserting into file, Don't open file before finish!")
        vbox= QVBoxLayout()
        vbox.addWidget(self.desc)
        self.progressBar= QProgressBar(self.dlg)
        self.progressBar.setMaximum(100)
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
                    emails= self.emailFinder(soup)
                    email= ''
                    for email1 in emails:
                         email+= email1+ ' '

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

# this is part to know if exe already running
# def showdialog( wintitle, title, desc, icon= 'warn'):
#     msg = QMessageBox()
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
#     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#     # msg.buttonClicked.connect(self.emailDlgClose)
#     msg.exec_()

# def process_exists(process_name):
#     call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
#     # use buildin check_output right away
#     output = subprocess.check_output(call).decode()
#     # check in last line for process name
#     last_line = output.strip().split('\r\n')[-1]
#     # because Fail message could be translated
#     return last_line.lower().startswith(process_name.lower())


def main():
    app = QApplication(sys.argv)
    # if process_exists("ScrapTool.exe"):
    #     showdialog('Error', 'Another ScrapTool is already running!', 'Please close the first exe and try agiain!')
    # else:
    ww= totalpage()
    # ww.show()
    sys.exit(app.exec_())
   
if __name__ == '__main__':
    main()





