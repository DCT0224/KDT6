import csv

f = open('subwayfee.csv',encoding='utf-8-sig')
data=csv.reader(f)
header = next(data)
max_rate = 0

for row in data:
    for i in range(4,8):
        row[i] = int(row[i])
    if row[6] != 0:

        rate = (row[6]*100)/(row[4]+row[6])
        if rate > max_rate:
            max_rate = rate
            print(row,round(rate,2),'%')

f.close()