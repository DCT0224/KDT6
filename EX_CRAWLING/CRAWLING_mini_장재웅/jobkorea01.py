from urllib.request import Request

from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup
import collections

if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable

try:
    search_word = quote('데이터분석가')
    url = f'https://www.jobkorea.co.kr/Search/?stext={search_word}'
    html = urlopen(url)

    soup = BeautifulSoup(html, 'html.parser')
    job_lists = soup.find_all('article', {'class':'list-item'})
    count= 0
    for job_item in job_lists:
        job_title = job_item.find('div', {'class':'list-section-corp'})
        job_title_link = job_title.find('a')['title']
        print(f'[{count:2d}] {job_title_link}', end=': ')

        job_info = job_item.find('div', {'class': 'list-section-information'})
        job_info_link = job_info.find('a').text
        job_info_str = job_info_link.replace("\n", '').strip()
        print(job_info_str, end=', ')

        job_group = job_item.find('ul', {'class': 'chip-information-group'})
        job_group_str = job_group.text.replace('\n', '').strip()
        print(job_group_str)
        count += 1


except Exception as e:
    print(e)