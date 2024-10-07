import csv

f = open('daegu.csv','r',encoding='utf-8')
#         얘 절대 경로 써야됨.
data=csv.reader(f,delimiter=',')
count=0
for row in data:
    if count > 5 :
        break
    else:
        print(row)
    count +=1

f.close()

# ['\ufeff날짜', '지점', '평균기온(℃)', '최저기온(℃)', '최고기온(℃)']
# ['\t1907-01-31', '143', '', '-7', '0.8']
# ['\t1907-02-01', '143', '', '', '']
# ['\t1907-02-02', '143', '', '', '']
# ['\t1907-02-03', '143', '', '', '']
# ['\t1907-02-04', '143', '', '', '']
