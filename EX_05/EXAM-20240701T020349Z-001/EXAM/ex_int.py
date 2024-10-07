# --------------------------------------
# 정수 데이터 살펴보기
# - 타입 : class 'int'
# - 표현 : 10진수, 8진수, 2진수 16진수
# --------------------------------------
# 정수의 데이터 타입 학인
print( type(-4), type(0), type(7) )

number= 17

# 정수의 표현/표기법
# [1] 10진수 => 2진수 내장함수 bin(정수)
print(f'{number}의 2진수 : {bin(number)} {type(bin(number))}')

# [2] 10진수 => 8진수 내장함수 oct(정수)
print(f'{number}의 8진수 : {oct(number)} {type(oct(number))}')

# [3] 10진수 => 16진수 내장함수 hex(정수)
print(f'{number}의 16진수 : {hex(number)} {type(hex(number))}')

# ----------------------------------------------------
# 산술연산자 : 덧셈, 뺄셈, 곱셈, 나눗셈, 몫, 나머지, 제곱
# ----------------------------------------------------
no1=19
no2=5

print(f'덧셈    {no1}+{no2}  = {no1+no2}')
print(f'뺄셈    {no1}-{no2}  = {no1-no2}')
print(f'곱셈    {no1}*{no2}  = {no1*no2}')
print(f'나눗셈  {no1}/{no2}  = {no1/no2}')
print(f'몫      {no1}//{no2} = {no1//no2}')
print(f'나머지  {no1}%{no2}  = {no1%no2}')
print(f'제곱    {no1}**{no2} = {no1**no2}')
