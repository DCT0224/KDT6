from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import requests
html=requests.get('https://finance.naver.com/sise/sise_market_sum.naver')
soup=BeautifulSoup(html.text,'html.parser')
temp = soup.select('a.tltle')
company_name = []
company_url = []
for i in range(10):
    company_name.append(temp[i].text)
    company_url.append(temp[i]['href'])


# 직접 들어가는 해당 주소 만들기
base = 'https://finance.naver.com'
com_url = base + company_url[0]
print(com_url)
html=requests.get(com_url)
soup=BeautifulSoup(html.text,'html.parser')

# # 종목이름
# print(soup.find('h2').text)
# # 종목코드
# print(soup.find('span',{'class':'code'}).text)
blind_link = soup.find('dl',{'class':'blind'})
dd_link = blind_link.find_all('dd')
# 종목명
print(dd_link[1].text[4:])
# 종목코드
print(dd_link[2].text[5:11])
# 현재가
now=dd_link[3].text.split()
print(now[1])
# 전일가
print(dd_link[4].text[4:])
# 시가
print(dd_link[5].text[3:])
# 고가
print(dd_link[6].text[3:])
# 저가
print(dd_link[8].text[3:])

while True:
    print('-'*30)
    print('[네이버 코스피 상위 10대 기업 목록]')
    print('-'*30)
    for i in range(10):
        print(f'[{i+1}] {company_name[i]}')
    num = int(input('주가를 검색할 기업의 번호를 입력하세요(-1:종료):'))

    if num == -1:
        print('프로그램 종료')
        break

    print(base + company_url[num])
    base = 'https://finance.naver.com'
    com_url = base + company_url[num-1]
    html=requests.get(com_url)
    soup=BeautifulSoup(html.text,'html.parser')
    blind_link = soup.find('dl',{'class':'blind'})
    dd_link = blind_link.find_all('dd')

    print(f'종목명 : {dd_link[1].text[4:]}')
    print(f'종목코드 : {dd_link[2].text[5:11]}')
    print(f'현재가 : {now[1]}')
    print(f'전일가 : {dd_link[4].text[4:]}')
    print(f'시가 : {dd_link[5].text[3:]}')
    print(f'고가 : {dd_link[6].text[3:]}')
    print(f'저가 : {dd_link[8].text[3:]}')


    
        


