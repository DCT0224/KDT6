from urllib.request import Request

from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup
import collections

if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable

try:
    search_word = quote('데이터분석가')
    url = f'https://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword={search_word}'

    urlrequest = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(urlrequest)

    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('div', {'class':'content'})
    items = content.find_all('div', {'class':'item_recruit'})
    for item in items:
        item_string = item.text.replace('\n', '').strip()
        print(item_string)
except Exception as e:
    print(e)
