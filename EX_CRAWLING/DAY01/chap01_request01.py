from urllib.request import urlopen
from bs4 import BeautifulSoup

melon_url = 'https://www.melon.com/chart/index.htm'
html = urlopen(melon_url)

soup = BeautifulSoup(html.read(), 'html.parser')
print(soup)
# HTTPError: HTTP Error 406: Not Acceptable => 사람이 아닌 로봇으로 인식해서 크롤링을 막음.