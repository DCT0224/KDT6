from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd


data=[]
for num in range(1,51):
    html = urlopen(f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={num}&sido=&gugun=&store=')
    bs = BeautifulSoup(html.read(),'html.parser')
    center_t = bs.select('td.center_t')
    for i in range(10):
        try:
            area=center_t[6*i].text
            name=center_t[6*i+1].text
            ad=center_t[6*i+3].text
            phone=center_t[6*i+5].text
            data.append([area,name,ad,phone])
        except IndexError:
            pass
print(data)

dataDF= pd.DataFrame(data,columns=['지역','매장명','주소','전화번호'])
dataDF.to_csv('hollys_branches.csv',index=False,encoding='utf-8-sig')

