from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
soup = BeautifulSoup(html.read(),'html.parser')


# soup.find('ul',{'id':'seven-day-forecast-list'})
# ul_link=soup.find('ul',{'id':'seven-day-forecast-list'})
# print(len(ul_link)) # => 9개 나오는 구간

# 찾아서 들어감
# li_link=ul_link.find('li')
# div_link=li_link.find('div')
# p_link = div_link.find_all('p')
# #----------------------------------
# print(p_link[0].string) # Overnight
# print(p_link[1].find('img')['title'])
# print(p_link[2].string) # 온도
# print(p_link[3].string)

# for ul in ul_link:
#     li_link=ul_link.find_all('li')
#     div_link=li_link.find('div')
#     p_link = div_link.find_all('p')
#     print(p_link[0].string) # Overnight
#     print(p_link[1])
#     print(p_link[2].string) # 온도
#     print(p_link[3].string)

def main():
    page=urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
    html = BeautifulSoup(page.read(),'html.parser')

    print('National Weather Service Scraping')
    print('-'*80)

    parse_use_find(html)
    parse_use_select(html)

def parse_use_find(html):
    '''
    find() 함수를 사용하여 html 내용을 크롤링
    '''
    print('[find 함수 사용]')
    forecast_items = html.find_all('div',{'class':'tombstone-container'})
    print('총 tomstone-container 검색 개수 : ', len(forecast_items))
    
    try:
        for day in forecast_items:
            period= day.find('p',{'class':'period-name'}).text
            img_desc = day.find('img')['title'] # img의 'title' 속성값 가져오기
            short_desc = day.find('p',{'class':'short-desc'}).text

            low_temp = day.find('p',class_='temp')
            if low_temp is not None:
                temp = low_temp.text
            else:
                temp = ""

            print('-'*80)
            print('[Period]: {0}'.format(period))
            print('[short_desc]: {0}'.format(short_desc))
            print('[Temperatur]: {0}'.format(temp))
            print('[Image desc]: {0}'.format(img_desc))
    except:
        print('예외가 발생했습니다.')

def parse_use_select(html):
    '''
    find() 함수를 사용하여 html 내용을 크롤링
    '''
    print('[select 함수 사용]')
    forecast_items = html.select('div.tombstone-container')
    print('총 tomstone-container 검색 개수 : ', len(forecast_items))

    try:
         for day in forecast_items:
            period= day.select_one('p.period-name').text
            img_desc = day.select_one('img')['title'] # img의 'title' 속성값 가져오기
            short_desc = day.select_one('p.short-desc').text

            low_temp = day.select_one('p.temp')
            if low_temp is not None:
                temp = low_temp.text
            else:
                temp = ""

            print('-'*80)
            print('[Period]: {0}'.format(period))
            print('[short_desc]: {0}'.format(short_desc))
            print('[Temperatur]: {0}'.format(temp))
            print('[Image desc]: {0}'.format(img_desc))
    except:
        print('예외가 발생했습니다.')

main()

# 고민해보기!!!
# page=urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
# html = BeautifulSoup(page.read(),'html.parser')
# forecast_items = html.select('div.tombstone-container')
# data=forecast_items[0]
# data1=data.select_one('img')['title']
# print(data1)
# data=forecast_items.select_one('p.period-name')
# print(data)
# try:
#     for day in forecast_items:
#             period= day.find('p',{'class':'period-name'}).text
#             img_desc = day.find('img')['title'] # img의 'title' 속성값 가져오기
#             short_desc = day.find('p',{'class':'short-desc'}).text

#             low_temp = day.find('p',class_='temp')
#             if low_temp is not None:
#                 temp = low_temp.text
#             else:
#                 temp = ""

#             print('-'*80)
#             print('[Period]: {0}'.format(period))
#             print('[short_desc]: {0}'.format(short_desc))
#             print('[Temperatur]: {0}'.format(temp))
#             print('[Image desc]: {0}'.format(img_desc))
# except:
#         print('예외가 발생했습니다.')

# print(forecast_items)