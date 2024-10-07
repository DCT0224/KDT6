import pandas as pd
from tabulate import tabulate

# dust.xlsx 불러오기
dust = pd.read_excel('dust.xlsx')

print(dust.head())
print(tabulate(dust.head(),headers='keys',tablefmt='pretty'))

print(dust.info())

dust.rename(columns={'날짜':'date','아황산가스':'so2',
                     '일산화탄소':'co','오존':'o3',
                     '이산화질소':'no2'},inplace=True)

print(tabulate(dust.head(),headers='keys',tablefmt='psql'))

dust['date'] = dust['date'].str[:10]
print(tabulate(dust.head(),headers='keys',tablefmt='psql'))

dust['date'] = pd.to_datetime(dust['date'])
print(dust.dtypes)

dust['year']=dust['date'].dt.year
dust['month']=dust['date'].dt.month
dust['day']=dust['date'].dt.day
print(dust.columns)

dust = dust[['date','year','month','day','so2','co','o3','no2','PM10','PM2.5']]
print(dust.columns)

print('결측치 개수 확인하기')
print(dust.isna().sum())

print('결측치를 포함한 데이터 출력')
print(dust[dust.isna().any(axis=1)])

# 결측치 채우기
# 결측치가 나타나기 이전 값으로 결측치를 채움(method=‘ffill’)
print(pd.__version__)
print('결측치 채우기')
dust.ffill(inplace=True)
print(dust.isnull().sum())

# 이전 결측치의 index를 다시 출력해서 확인
print(dust.iloc[132:134])


##-----------------------------------------------------------------------
# 날씨 데이터 엑셀 파일 읽기
weather = pd.read_excel('weather.xlsx')
print(tabulate(weather.head(),headers='keys',tablefmt='psql'))

# 날씨 데이터 기본 정보 출력
print(weather.info())

# 불필요한 컬럼(‘지점’, ‘지점명’) 삭제 및 컬럼 이름을 영문으로 변경
weather.drop(['지점','지점명'],axis=1,inplace=True)

weather.columns = ['date','temp','wind','rain','humidity']
print(tabulate(weather.head(),headers='keys',tablefmt='pretty'))

# weather[‘date’] 컬럼에서 시간 정보 삭제 후 데이터 타입 확인
# 기존: 년도-월-일 시간-> 변경: 년도-월-일
weather['date'] = pd.to_datetime(weather['date'].dt.date)
print(weather.info())
print(weather.head())

# 날씨 데이터 결측치 개수 확인하기
print('날씨 데이터 결측치 개수 확인하기')
print(weather.isna().sum())

print('날씨 데이터에서 결측치를 포함하는 행 출력')
print(weather[weather.isna().any(axis=1)])

# 날씨 데이터 결측치 채우기
# 결측치가 나타나기 이전 값으로 채움
weather.ffill(inplace=True)
print(weather.isna().sum())

# 이전 결측치의 index의 값 비교
print(weather.iloc[[369,565,742]])

# 강수량 측정
# 기상청에서는 0.1 단위로 강수량을 측정:	강수량이 0.1 이하면 0으로 표시함
# 강수량([‘rain’]	컬럼)에서 0인 데이터를 0.01로 변경	후 빈도수 출력

print('강수량이 0인 항목을 0.01로 변경')
weather['rain'] = weather['rain'].replace(0,0.01)
print(weather['rain'].value_counts())

# 두 데이터를 병합하기 위해 필요 없는 행을 삭제
# 미세먼지 데이터와 날씨 데이터의 (행,열 )의 크기 확인
print('dust','weather의 크기 확인')
print('dust.shape',dust.shape)
print('weather.shape',weather.shape)

print(dust.iloc[740:])

print((weather.iloc[740:]))

dust.drop(index=743,inplace=True)
print(dust.shape)

# 두 데이터프레임을 병합해서 새로운 데이터프레임 생성
# 두 데이터프레임에서 ['date']컬럼을 기준으로 병합

print('dust, weather 데이터 프레임 merge')

merged_df = pd.merge(dust,weather,on='date')
print(merged_df.head())

# 모든 요소별 상관관계 확인
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

print(merged_df.corr())

# 미세먼지(PM10)를 기준으로 상관관계 분석
# PM10	데이터와 상관관계를 내림차순 정렬
print('미세먼지(PM10)과 상관관계 분석')
corr = merged_df.corr()
print(corr['PM10'].sort_values(ascending=False)) # 내림차순 정렬

import matplotlib.pyplot as plt

merged_df.hist(column=['so2',	'co',	'o3',	'no2','PM10','PM2.5',	'temp',	'wind',	'rain',	'humidity'],
               bins=50,figsize=(20,15))
plt.show()

import seaborn as sns
import koreanize_matplotlib
plt.figure(figsize=(15,10))
daygraph=sns.barplot(x='day',y='PM10',data=merged_df)
plt.title('날짜별 PM10 농도')
plt.show()

plt.figure(figsize=(15,10))
sns.heatmap(data=corr,annot=True,fmt='.2f',cmap='hot')
plt.show()

plt.figure(figsize=(15,10))
x = merged_df['PM10']
y = merged_df['PM2.5']

plt.plot(x,y,marker = 'o',linestyle='none',color='red',alpha=0.5)
plt.title('PM10 vs. PM2.5')
plt.xlabel('PM10')
plt.ylabel('PM2.5')
plt.show()