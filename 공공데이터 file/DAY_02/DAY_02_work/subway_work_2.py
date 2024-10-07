
import	csv
import	matplotlib.pyplot as plt
import pandas as pd
import	platform
import	koreanize_matplotlib

max_station = ''
max_total = -1

file_name='subwaytime.csv'
dataDF=pd.read_csv(file_name)
dataDF.drop([0],axis=0,inplace=True)

## 필요한 데이터 추출해서 데이터 프레임 만들기
hacha_data = dataDF.loc[:, ['호선명','Unnamed: 11','Unnamed: 13']]

## set index로 호선명 인덱스로 정하기
hacha_data = hacha_data.set_index('호선명')
hacha_data = hacha_data.rename(columns={'Unnamed: 11':'07:00~07:59하차','Unnamed: 13':'08:00~08:59하차'})
print(hacha_data)
hacha_data.astype(int,'07:00~07:59하차')
hacha_data.astype(int,'08:00~08:59하차')
print(hacha_data['07:00~07:59하차'].dtype())
# sum_data = hacha_data['07:00~07:59하차'] + hacha_data['08:00~08:59하차']
# print(sum_data)

# one_data = hacha_data
# print(one_data)