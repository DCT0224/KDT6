import csv

f = open('subwayfee.csv',encoding='utf-8-sig')
data=csv.reader(f)
header = next(data)
max_rate = 0
rate = 0

for row in data:
    for i in range(4,8):
        row[i] = int(row[i])
    rate = row[4] / row[6] # 유임 승차인원 / 무임 승차인원
    if rate > max_rate:
        max_rate = rate
print(max_rate)
f.close()

### 분모(무임 승차인원)가 0인 값이 존재해서 Zerodivision Error 발생!!!!!!!