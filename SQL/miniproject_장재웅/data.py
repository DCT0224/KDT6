import pymysql
import pandas as pd
import pymysql.cursors
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
# -----------------------------------------------------------------------
conn = pymysql.connect(host='172.20.131.64',user='jaewoong',
                       password='1234',db='minipj',charset='utf8')
cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute('select * from gdp')
rows = cur.fetchall()

gdp_df = pd.DataFrame(rows)
print(gdp_df)

print()
cur.close()
conn.close()
# -----------------------------------------------------------------------
conn = pymysql.connect(host='172.20.131.64',user='jaewoong',
                       password='1234',db='minipj',charset='utf8')
cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute('select * from consumer')
rows = cur.fetchall()

con_df = pd.DataFrame(rows)
print(con_df)

print()
cur.close()
conn.close()
# -----------------------------------------------------------------------
conn = pymysql.connect(host='172.20.131.64',user='jaewoong',
                       password='1234',db='minipj',charset='utf8')
cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute('select * from juga_index')
rows = cur.fetchall()

Ko_df = pd.DataFrame(rows)
print(Ko_df)

print()
cur.close()
conn.close()
# -----------------------------------------------------------------------
conn = pymysql.connect(host='172.20.131.64',user='jaewoong',
                       password='1234',db='minipj',charset='utf8')
cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute('select * from rate')
rows = cur.fetchall()

rate_df = pd.DataFrame(rows)
print(rate_df)

print()
cur.close()
conn.close()
# -----------------------------------------------------------------------
# year를 각 데이터 프레임의 인덱스로 설정
Ko_df.set_index('year',inplace=True)
print(Ko_df)
con_df.set_index('year',inplace=True)
print(con_df)
gdp_df.set_index('year',inplace=True)
print(gdp_df)
rate_df.set_index('year',inplace=True)
print(rate_df)
# -----------------------------------------------------------------------

# 소비자 물가 상승률과 실질 GDP성장률 데이터 합치기
risegrow_df=pd.concat([con_df['rise'],gdp_df['economic growth rate']],axis=1)
print(risegrow_df)
year=risegrow_df.index.to_list()
y_data=risegrow_df[['rise','economic growth rate']]
plt.title('소비자 물가 상승률과 실질 GDP 성장률')
plt.plot(year,y_data)
plt.legend(('consumer rise','economic growth rate'))
plt.xlabel('year',fontsize=15)
plt.ylabel('increase',fontsize=15)
plt.show()

# 소비자 물가 상승률과 명목 GDP 합치기
risegrow_df=pd.concat([con_df['rise'],gdp_df['gross domestic product']],axis=1)
print(risegrow_df)
year=risegrow_df.index.to_list()
y_data=risegrow_df[['rise','gross domestic product']]
plt.title('소비자 물가 상승률과 실질 GDP 성장률')
plt.plot(year,y_data)
plt.legend(('consumer rise','gross domestic product'))
plt.xlabel('year',fontsize=15)
plt.ylabel('increase',fontsize=15)
plt.show()


# # 소비자 물가지수 상승률과 코스피, 코스닥 데이터 테이블 합치기
riseKO_df=pd.concat([con_df['rise'],Ko_df[['KOSPI','KOSDAQ']]],axis=1)
print(riseKO_df)
year=riseKO_df.index.to_list()
con_rise=riseKO_df['rise'].to_list()
KOSPI=riseKO_df['KOSPI'].to_list()
KOSDAQ=riseKO_df['KOSDAQ'].to_list()

print(KOSDAQ)

colors=sns.color_palette('magma')
colors2=sns.color_palette('viridis')
# 서브플롯 생성 (1행 2열)
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(16,8))

ax1.bar(year,KOSPI,color=colors)
ax1_twin=ax1.twinx()
ax1_twin.plot(year,con_rise,color='k',linestyle='--',marker='o')
plt.title('소비자 물가지수 상승률에 따른 KOSPI 변화')
ax1.tick_params(axis='x',rotation=45)

ax2.bar(year,KOSDAQ,color=colors2)
ax2_twin=ax2.twinx()
ax2.set_title('소비자 물가지수 상승률에 따른 KOSDAQ변화')
ax2.tick_params(axis='x',rotation=45)
ax2_twin.plot(year,con_rise,color='k',linestyle='--',marker='o')
plt.tight_layout
plt.show()

# 금리 변동과 코스피, 코스닥 데이터 테이블 합치기
rateKO_df=pd.concat([rate_df['base rate'],Ko_df[['KOSPI','KOSDAQ']]],axis=1)
print(rateKO_df)
year=rateKO_df.index.to_list()
rate=rateKO_df['base rate'].to_list()
KOSPI=rateKO_df['KOSPI'].to_list()
KOSDAQ=rateKO_df['KOSDAQ'].to_list()

colors=sns.color_palette('magma')
colors2=sns.color_palette('viridis')
# 서브플롯 생성 (1행 2열)
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(16,8))

ax1.bar(year,KOSPI,color=colors)
ax1_twin=ax1.twinx()
ax1_twin.plot(year,rate,color='r',linestyle='--',marker='o')
plt.title('금리 변동에 따른 KOSPI 변화')
ax1.tick_params(axis='x',rotation=45)

ax2.bar(year,KOSDAQ,color=colors2)
ax2_twin=ax2.twinx()
ax2.set_title('금리 변동에 따른 KOSDAQ 변화')
ax2.tick_params(axis='x',rotation=45)
ax2_twin.plot(year,rate,color='r',linestyle='--',marker='o')
plt.tight_layout
plt.show()