import pandas as pd
file='hollys_branches.csv'
dataDF=pd.read_csv(file)

# dataDF의 인덱스 바꿔주기
dataDF = dataDF.set_axis(range(1,len(dataDF)+1)).copy()

local = input('지역을 입력하세요: ')
mask=[]
for i in range(1,len(dataDF.index)+1):
    key = local in dataDF.loc[i,'지역']
    mask.append(key)

select_df = dataDF[mask].reset_index(drop='index')
select_df.index = select_df.index + 1
select_df = select_df.drop(columns='지역')
print(select_df)