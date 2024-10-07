# --------------------------------------
# 객체비교연산자
# - 힙에 저장된 데이터가 동일 인스턴스인지
#   비교
# - 연산자 :  is, is not
# - 결과: True, False
# -------------------------------------- 
no1=71
no2=71

print(f'{no1} is {no2} : {no1 is no2}') 

no2=72
print(f'{no1} is {no2} : {no1 is no2}') 

no2=71.0
print(f'{no1} is {no2} : {no1 is no2}') 
print(f'{no1} == {no2} : {no1 == no2}') 