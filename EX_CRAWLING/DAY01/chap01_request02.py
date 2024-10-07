from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup

melon_url = 'https://www.melon.com/chart/index.htm'
urlrequest = Request(melon_url,headers={'User-Agent': 'Mozilla/5.0'})

html = urlopen(urlrequest)
soup = BeautifulSoup(html.read().decode('utf-8'), 'html.parser')
print(soup)
# HTTPError: HTTP Error 406: Not Acceptable => 사람이 아닌 로봇으로 인식해서 크롤링을 막음.