import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

f = open('gender.csv',encoding='euc_kr')
data = csv.reader(f)
city_list = ['대구광역시','대구광역시 중구','대구광역시 동구','대구광역시 서구','대구광역시 남구',
             '대구광역시 북구','대구광역시 수성구','대구광역시 달서구','대구광역시 달성군','대구광역시 군위군']




def draw_pie_chart(city,mix_value):
    plt.pie(mix_value,labels=['남자','여자'],autopct='%.1f%%',startangle=90)
    plt.title(city)
    plt.show()


male_list = []
female_list = []
for city in city_list:
    for row in data:
        if city in row[0]:
            for i in range(105,106):
                male_list.append(int(row[i].replace(',','')))
                female_list.append(int(row[i+103].replace(',','')))
            break

for i in range(len(city_list)):
    print(f'{city_list[i]} : (남:{male_list[i]} 여:{female_list[i]})')

label=['남자','여자']

# plt.figure(figsize={20,40})
for i in range(len(city_list)):
    plt.subplot(5,2,i+1)
    plt.pie([male_list[i],female_list[i]],labels=label,autopct='%.1f%%',startangle=90)
    plt.title(city_list[i])

plt.suptitle(f'대구광역시 구별 남녀 인구 비율')

plt.show()






