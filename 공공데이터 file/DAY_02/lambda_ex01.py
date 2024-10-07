### lambda 함수: 다양한 정렬 기준을 설정
students = [('Alice',3.9,20160303),
            ('Bob',3.0,20160302),
            ('Charlie',4.3,20160301)]
print('-'*60)
print('sorted key 입력 없음')
print(sorted(students))
print('-'*60)
# 학번(studends[2])을 기준으로 오름차순 정렬
sorted_students1 = sorted(students,key = lambda s:s[2])
print(sorted_students1)
print('-'*60)

# 학점(students[1])을 기준으로 내림 차순 정렬
sorted_students2 = sorted(students,key=lambda s : s[1],reverse=True)
print(sorted_students2)