# ---------------------------------------
# 산술 연산자 
# 종류 : +   -  *   /  //  %  **
# ---------------------------------------
print( "10 + 3 =", 10+3)
print( "10 - 3 =", 10-3)
print( "10 * 3 =", 10*3)
print( "10 / 3 =", 10/3)

print( "10 // 3 =", 10//3)
print( "10 %  3 =", 10%3)
print( "10 ** 3 =", 10**3)


# --------------------------------------
# 입력 받은 숫자 4칙연산 계산 결과 출력
# input()
# --------------------------------------
num1=input("숫자 1 : ")
num2=input("숫자 2 : ")

# 키보드로 입력된 문자 str을 정수 int로 변환
# 함수 : int()
print( num1, type(num1) )
num1=int(num1)
print( num1, type(num1) )
num2=int(num2)

print( num1, "+", num2, "=", num1+num2)
print( num1, "-", num2, "=", num1-num2)
print( num1, "*", num2, "=", num1*num2)
print( num1, "/", num2, "=", num1/num2)
print( num1, "//", num2, "=", num1//num2)
print( num1, "%", num2, "=", num1%num2)
