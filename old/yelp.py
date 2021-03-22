import requests
import time
from bs4 import BeautifulSoup
url= "https://www.yelp.com/biz/dumpling-kitchen-san-francisco?osq=Food+Delivery"
response= requests.get(url)
time.sleep(0.5)
soup = BeautifulSoup(response.text, 'html.parser')
detailNode= soup.find_all('div', attrs= {'class': 'css-0 padding-t2__373c0__11Iek padding-r2__373c0__28zpp padding-b2__373c0__34gV1 padding-l2__373c0__1Dr82 border--top__373c0__3gXLy border--right__373c0__1n3Iv border--bottom__373c0__3qNtD border--left__373c0__d1B7K border-radius--regular__373c0__3KbYS background-color--white__373c0__2uyKj'})[-1]
# print(detailNode)
website= detailNode.find_all('p', attrs= {'class': "text__373c0__2Kxyz text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa- text-weight--semibold__373c0__2l0fe text-size--large__373c0__3t60B"})[0].text
print(website)
address= detailNode.find_all('p', attrs= {'class': "text__373c0__2Kxyz text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa- text-weight--semibold__373c0__2l0fe text-size--large__373c0__3t60B"})[2].text.replace('Get Directions', '')
phoneNumber= detailNode.find_all('p', attrs= {'class': "text__373c0__2Kxyz text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa- text-weight--semibold__373c0__2l0fe text-size--large__373c0__3t60B"})[1].text
print(address)
print(phoneNumber)