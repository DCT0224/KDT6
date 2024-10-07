import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 1. 대구 기온 데이터에서 시작 연도, 마지막 연도를 입력하고 특정 월의 최고 기온 및 최저 기온의 평균값을 구하고 그래프로 표현  
# * daegu-utf8.csv	또는	daegu-utf8-df.csv 파일 이용  
# * 데이터 구조 
# ['날짜', '지점', '평균기온', '최저기온', '최고기온’] 
# [0]        [1]      [2]        [3]         [4] 
# * 화면에서 측정할 달을 입력 받아서 진행   
# * 해당 기간 동안 최고기온 평균값 및 최저기온 평균값 계산 - 
#       최고기온 및 최저기온 데이터를 이용하여 입력된 달의 각각 평균값을 구함 - 
#       문자열 형태의 ‘날짜’ 열의 데이터는 datetime 으로 변경함:  
# * 하나의 그래프 안에 2개의 꺾은선 그래프로 결과를 출력 - 
#       마이너스 기호 출력 깨짐 방지 - - 
#       입력된 월을 이용하여 그래프의 타이틀 내용 변경 
#       최고 온도는 빨간색, 최저 온도는 파란색으로 표시하고 각각 마커 및 legend를 표시

tem_df=pd.read_csv('daegu-utf8-df.csv')
# print(tem_df.shape) => (42180, 5)

start_year=int(1980)
end_year=int(2010)

# 문자열 형태의 ‘날짜’ 열의 데이터는 datetime 으로 변경
tem_df['날짜']	=	pd.to_datetime(tem_df['날짜'],	format='%Y-%m-%d')
print(tem_df['날짜'].dtype)


# 입력받은 값 사이 해당 년도의 데이터 뽑아내기
year_df=tem_df[(tem_df['날짜'].dt.year > start_year) & (tem_df['날짜'].dt.year > end_year)]

def main():
    tem_df=pd.read_csv('daegu-utf8-df.csv')
    start_year=int(input('시작 연도를 입력하세요: '))
    end_year=int(input('마지막 연도를 입력하세요: '))
    search_month=int(input('기온 변화를 측정할 달을 입력하세요: '))

    # 문자열 형태의 ‘날짜’ 열의 데이터는 datetime 으로 변경
    tem_df['날짜']	=	pd.to_datetime(tem_df['날짜'],	format='%Y-%m-%d')
    
    # 시작 연도와 마지막 연도를 입력 받아 해당 년도 데이터 추출
    year_df=tem_df[(tem_df['날짜'].dt.year >= start_year) & (tem_df['날짜'].dt.year <= end_year)]
    month_df=year_df[tem_df['날짜'].dt.month == search_month]

    range_year=end_year-start_year+1
    year_list=list(range(start_year,end_year+1))
    print(year_list)

    decade_high_temp_list	=	[]
    decade_low_temp_list	=	[]

    for i in range(range_year):
        # if month_df['날짜'].dt.year == start_year + i:
        target_month_df=month_df[month_df['날짜'].dt.year == (start_year + i)]
        decade_low_temp_list.append(round(target_month_df['최저기온'].mean(),1))
        decade_high_temp_list.append(round(target_month_df['최고기온'].mean(),1))
    
    print(f'{start_year} 년부터 {end_year} 년까지 {search_month} 월의 기온 변화')
    print(f'{search_month}월 최저기온 평균:')
    print(decade_low_temp_list)
    print(f'{search_month}월 최고기온 평균:')
    print(decade_high_temp_list)

    plt.plot(year_list,decade_high_temp_list,color='r',marker='s',	markersize=6,label='최고기온')
    plt.plot(year_list,decade_low_temp_list,color='b',marker='s',	markersize=6,label='최저기온')
    plt.legend()
    plt.title(f'{start_year}년부터 {end_year}년까지 {search_month}월의 기온 변화')
    plt.xticks(year_list)
    plt.rcParams['axes.unicode_minus']	=	False	
    plt.show()

main()
    