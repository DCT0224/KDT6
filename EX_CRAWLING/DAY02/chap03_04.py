# from urllib.parse import urlparse
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

# urlString1 = 'https://shopping.naver.com/home/p/index.naver'

# url = urlparse(urlString1)
# print(url.scheme)
# print(url.netloc)
# print(url.path)

query='ChatGPT'
url	=	f'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={query}'
#response	=	requests.get(url)
#soup	=	BeautifulSoup(response.text,	'html.parser')
html	=	urlopen(url)
soup	=	BeautifulSoup(html.read(),	'html.parser')
blog_results	=	soup.select('a.title_link')
print('검색 결과수:	',	len(blog_results)) 
for	blog_title	in	blog_results:
    title	=	blog_title.text
    link	=	blog_title['href']
    print(f'{title},	[{link}]')

#########################################################################################33
html = urlopen(url)
soup = BeautifulSoup(html,'html.parser')
blog_results = soup.select('a.title_link') # 검색 블로그의 타이틀
print('검색 결과수: ',len(blog_results))
search_count = len(blog_results)
desc_results = soup.select('a.dsc_link') # 검색된 블로그의 간단한 설명

for i in range(search_count):
    title = blog_results[i].text
    link = blog_results[i]['href']
    print(f'{title},[{link}]')
    print(desc_results[i].text)
    print('-'*80)