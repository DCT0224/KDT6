import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests


chrome_driver_path = "path_to_chromedriver"  
service = Service(chrome_driver_path)

url = 'https://comic.naver.com/webtoon/list?titleId=670143'
# 웹 드라이버 실행
driver = webdriver.Chrome()

driver.get(url)
time.sleep(1)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

# name =soup.find('div', class_='css-12etink ee4wkaf15').find('img').get('alt')
# blank=soup.find('div', class_='tag_wrap tag_detail').text
# common=soup.find('p', class_='css-1ndhscg ee4wkaf25').text
# category = soup.find('div', class_='tag_wrap tag_detail')
# category2=str(category).split('"')[3]

# print(name)
# print(blank)
# print(common)
# print(category2)