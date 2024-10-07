'''
- Jobkorea에서 데이터 크롤링 해오기 (iframe이라서 BS로 크롤링 불가능)

<데이터사이언티스트& 데이터엔지니어& 머신러닝엔지니어> 
(검색어 포함)빅데이터, 인공지능, 데이터, 개발자
- get_keyword => 취업공고에 올라온 keyword
- get_school => 취업공고에 올라온 학력
- 
'''
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.jobkorea.co.kr/recruit/joblist?menucode=duty')

driver.switch_to.frame('devHHReqLyAreaFrame')
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
print(soup)
# results = soup.find_all('tr',{'class':'devloopArea'})
# print(results)

