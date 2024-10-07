# -----------------------------------------
# 데이터 타입 변환하기
# int ==> float
# float ==> int
# str ==> int
# str ==> float
# int ==> str
# float ==> str
# int ==> bool
# float ==> bool
# bool ==> int
# bool ==> float
# --------------------------------------------
# 정수 int 데이터 변환 ------------------------
num=-9

print(num, float(num))
print(num, str(num))
print(num, bool(num))

# 실수 float 데이터 변환 ------------------------
num=7.82

print(num, int(num))
print(num, str(num))
print(num, bool(num))

# 문자 str 데이터 변환 --------------------------
num='59'

print(num, int(num))
print(num, float(num))
print(num, bool(num))
print('', bool(''))
print('0', bool('0'))

print('25m', int('25m'))