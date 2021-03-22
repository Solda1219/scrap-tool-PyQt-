import pandas as pd
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import time
import os
from enum import Enum
import re

# social compare
COMPARE_SOCIAL_FACEBOOK = 'facebook.com'
COMPARE_SOCIAL_INSTAGRAM = 'instagram.com'
COMPARE_SOCIAL_LINKEDIN = 'linkedin.com'
COMPARE_SOCIAL_PINTEREST = 'pinterest.com'
# file names
FILE_RESULT = 'result.csv'
FILE_EMAIL = 'email.csv'
FILE_URL_WORD = 'word1_url.csv'
FILE_URL_INIT = 'init_url.csv'
FILE_SOCIAL_LINK = 'social.csv'
# carrelage
def listToString(s):
    res = "" 
    index = 0
    for ele in s:
        if index != 0:
            res += "  "
        res += ele
        index +=1
    return res

class UrlState(Enum):
    URL_TEXT = 1
    URL_NO_TEXT = 2

class GoogleURLScraper():
    def __init__(self, receive_dlg):
        self.scrap_dialog = receive_dlg
        self.init()
    def init(self):
        self.social_flag = False
        self.end_flag = False
        self.searchstop_flag = False
        self.search_string = []
        self.search_info = {'string_num':0, 'start':0}
        self.pro_num = 0
        self.beyond_time = -1
        self.start_time = 0
        self.url_state = UrlState.URL_NO_TEXT
    def getWordList(self, string):
        res = []
        if string.find(',') != -1:
            res = string.split(',')
        elif string.find('*') != -1:
            res = string.split('*')
        elif string.find('-') != -1:
            res = string.split('-')
        elif string != '':
            res.append(string)
        return res
    def set_searchdata(self, word_url, word_email, word_nation, beyond_time, url_state, social_state):
        self.init()
        self.social_flag = social_state
        res = False
        if word_url == '':
            self.scrap_dialog.setAlert('Word URL is empty')
            return res
        urls = self.getWordList(word_url)
        emails= self.getWordList(word_email)
        self.beyond_time = beyond_time
        self.url_state = url_state
        string = "*"
        for url in urls:
            string += url + '*'
            search_item = {'string':'', 'word_email':[], 'word_nation':'', 'word_url':[]}
            search_item['string'] = string
            search_item['word_url'] = urls
            search_item['word_email'] = emails
            search_item['word_nation'] = word_nation
            self.search_string.append(search_item)
        if word_nation != '':
            string = "*"
            for url in urls:
                string += url + '.' + word_nation + '*'
                search_item = {'string':'', 'word_email':[], 'word_nation':'', 'word_url':[]}
                search_item['string'] = string
                search_item['word_url'] = urls
                search_item['word_email'] = emails
                search_item['word_nation'] = word_nation
                self.search_string.append(search_item)
        return True
    def scrape_stop(self):
        self.searchstop_flag = True
        self.end_flag = True
    def scrape_start(self):
        self.searchstop_flag = False
        self.end_flag = False
        self.scrape()
    def end(self):
        self.end_flag = True
        self.scrap_dialog.resultEnd()
    def scrape(self): # thread scrap start
        # self.scrap_dialog.endExcel()
        email_columns=['url', 'email']
        social_columns = ['url', 'facebook', 'instagram', 'linkedin', 'pinterest']
        if self.search_info['start'] == 0 and self.search_info['string_num'] == 0:
            ### write csv headers
            # eamil result
            if os.path.exists(FILE_RESULT):
                os.remove(FILE_RESULT)
            df = pd.DataFrame(columns = email_columns)
            df.to_csv(FILE_RESULT, mode='x', index=False, encoding='utf-8')
            # all urls
            if os.path.exists(FILE_URL_INIT):
                os.remove(FILE_URL_INIT)
            df = pd.DataFrame()
            df.to_csv(FILE_URL_INIT, mode='x', index=False, encoding='utf-8')
            # checked url
            if os.path.exists(FILE_URL_WORD):
                os.remove(FILE_URL_WORD)
            df = pd.DataFrame()
            df.to_csv(FILE_URL_WORD, mode='x', index=False, encoding='utf-8')
            # emails of checked url
            if os.path.exists(FILE_EMAIL):
                os.remove(FILE_EMAIL)
            df = pd.DataFrame(columns = email_columns)
            df.to_csv(FILE_EMAIL, mode='x', index=False, encoding='utf-8')

            # social links
            if os.path.exists(FILE_SOCIAL_LINK):
                os.remove(FILE_SOCIAL_LINK)
            df = pd.DataFrame(columns = social_columns)
            df.to_csv(FILE_SOCIAL_LINK, mode='x', index=False, encoding='utf-8')
        # search all pages and write
        try:
            search_index = 0
            for search_item in self.search_string:
                if self.search_info['string_num'] > search_index:
                    continue
                string = search_item['string']
                word_url = search_item['word_url']
                word_email = search_item['word_email']
                word_nation = search_item['word_nation']
                
                index = 0
                for url in search(string, tld='com.pk', lang='es', start = self.search_info['start'], pause = 2.0, user_agent = 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'):
                    if self.searchstop_flag == True:
                        self.search_info['start'] = index + self.search_info['start']
                        self.search_info['string_num'] = search_index
                        self.end_flag = True
                        return
                    if self.end_flag == True:
                        self.search_info['start'] = 0
                        self.search_info['string_num'] = 0
                        print('scrap end')
                        return
                    index += 1
                    # print(url)
                    df = pd.DataFrame([url])
                    df.to_csv(FILE_URL_INIT, mode='a', header=False, index=False, encoding='utf-8')
                    item = {'url':'', 'email':''}
                    if self.isUrl(url, word_url): # check to contain search string
                        # print(url)
                        # url = self.getInitUrl(url)
                        ### save word_url
                        df = pd.DataFrame([url])
                        df.to_csv(FILE_URL_WORD, mode='a', header=False, index=False, encoding='utf-8')

                        ### save social links
                        if self.social_flag:
                            social_links = self.links(url)
                            df = pd.DataFrame([social_links])
                            df.to_csv(FILE_SOCIAL_LINK, mode='a', header=False, index=False, encoding='utf-8')

                        new = []
                        item['url'] = url
                        email = self.email(url, word_email, word_nation)
                        if email == '':
                            continue
                        
                        print(email)
                        item['email'] = email
                        new.append(item)
                        ## save datas in csv
                        df = pd.DataFrame(new, columns = email_columns)
                        df.to_csv(FILE_RESULT, mode='a', header=False, index=False, encoding='utf-8')
                self.search_info['start'] = 0
                search_index += 1
            self.search_info['string_num'] = 0
            self.end_flag = True
            self.scrap_dialog.resultEnd()
            print('end scrap')
        except:
            print("An exception occurred")
            # self.scrap_dialog.lbl_head.setStyleSheet("QLabel { color : red;}")
            # self.scrap_dialog.setAlert('No Internet')
            self.end_flag = True
            self.scrap_dialog.resultEnd(True)
            print('end scrap')
            self.search_info['string_num'] = 0
    def start_process(self): # thread progress bar run
        self.start_time = time.perf_counter()
        self.pro_num = 0
        while self.end_flag != True:
            # beyond time check
            dt = time.perf_counter() - self.start_time
            if self.beyond_time != -1 and dt > self.beyond_time:
                self.end()
            if self.pro_num >=49:
                self.pro_num = 0
            self.pro_num += 1
            if self.scrap_dialog != None:
                self.scrap_dialog.setProcess(self.pro_num * 2)
            time.sleep(1)
        if self.searchstop_flag != True:
            self.scrap_dialog.setProcess(99)
        print('end progress')
    def isUrl(self, url, word_url):
        res = False
        for item in word_url:
            if url.find(item) != -1:
                res = True
        if res == False and self.url_state == UrlState.URL_TEXT:
            res = True
        return res
    def getInitUrl(self, url):
        res = ''
        head_string = url.split('//')[0] + '//'
        url = url.replace(head_string, '')
        res = head_string + url.split('/')[0]
        return res
    def email(self, url, word_email, word_nation):
        res = ''
        list = []
        # if url.split('.')[-1] != 'com':
        #     head_string = url.split('//')[0] + '//www.'
        #     email = url.replace(head_string, '')
        #     if self.isEmail(email, word_email, word_nation):
        #         list.append(email)
        EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
        response = None
        try:
            response = requests.get(url, timeout = 2)
        except:
            print("An exception occurred")
            # self.scrap_dialog.setState('error)
        if response != None:
            soup = BeautifulSoup(response.text, 'html.parser')
            if soup != None:
                init_list = []
                for re_match in re.finditer(EMAIL_REGEX, soup.text):
                    email = re_match.group()
                    init_list.append(email)
                    if self.isEmail(email, word_email, word_nation):
                        list.append(email)
                #### save email.csv file
                if len(init_list) != 0: 
                    new = []
                    item = {'url':'', 'email':''}
                    item['url'] = url
                    item['email'] = listToString(init_list)
                    new.append(item)
                    ## save datas in csv
                    columns=['url', 'email']
                    df = pd.DataFrame(new, columns = columns)
                    df.to_csv(FILE_EMAIL, mode='a', header=False, index=False, encoding='utf-8')
        s = listToString(list)
        if s != '':
            res = s
        return res
    def isEmail(self, email, word_email, word_nation):
        res = False
        if len(word_email) == 0:
            if word_nation == '':
                res = True
            elif email.find('.'+word_nation) != -1:
                res = True
        else: 
            for email_item in word_email:
                if email_item != '':
                    if word_nation == '':
                        if email.find(email_item) != -1:
                            res = True
                    elif email.find(email_item) != -1 and email.find('.'+word_nation) != -1:
                        res = True
        return res
    def links(self, url):
        res = {'url':'', 'facebook':'', 'instagram':'', 'linkedin':'', 'pinterest':''}
        res['url'] = url
        response = None
        try:
            response = requests.get(url, timeout = 2)
        except:
            print("exception create timeout")
            # self.scrap_dialog.setState('error)
        if response != None:
            soup = BeautifulSoup(response.text, 'html.parser')
            if soup != None:
                for item in soup.find_all('a'):
                    try:
                        social_url = item.attrs['href']
                        # facebook
                        if social_url.find(COMPARE_SOCIAL_FACEBOOK) != -1:
                            res['facebook'] = social_url
                        # instagram
                        if social_url.find(COMPARE_SOCIAL_INSTAGRAM) != -1:
                            res['instagram'] = social_url
                        # linkedin
                        if social_url.find(COMPARE_SOCIAL_LINKEDIN) != -1:
                            res['linkedin'] = social_url
                        # pinterest
                        if social_url.find(COMPARE_SOCIAL_PINTEREST) != -1:
                            res['pinterest'] = social_url
                    except:
                        continue
        return res
