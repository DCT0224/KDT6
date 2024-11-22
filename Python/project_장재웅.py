
# hemocytometer 계산


def cnt_result(a,b):
    result = a/b*2*(10**4)
    return result
# a = total count cell 수
# b = 칸수, 한칸단 cell 수로 평균을 내기 위함
# Trypan blue 10µl+ Cell sus 10µl : 1대1 비율이기 때문에 2
# 10⁴ : 한 칸의 부피 V = 10⁴ml 이므로 1ml이 되도록 곱해준다.
# 1mm * 1mm * 0.1mm = 0.1mm³=10⁻⁴ml
# 1ml = 1cm³=10³mm³

def n_chg(num):
    num=str(num)
    return f'{num[0]}.{num[1]}*(10^{len(num)-1})'
# 깔끔한 유효숫자 표현방식


while True:
    square_nums=input("square 수 입력 : ")
    if square_nums.isdecimal(): # 입력된 값이 숫자인지 확인
        square_nums=int(square_nums)
        if square_nums > 9:
            print("1 ~ 9사이 숫자만 입력하세요.") # hemocytometer를 나눴을때 Square 9개가 나옴.
            continue
        else:
            break 
    else:
        print("숫자를 입력하세요.") 
        continue


isOK=False # while 반복문 멈추기 위해
total=0 # cell_n의 총합을 구하기 위해
while True:
    
    if isOK:
        break
    cell_n=input("*****각 square의 cell count 값 입력***** \n주의) Square의 개수와 입력값이 같아야 합니다.\n(예.squre 수 4개 : 80,100,90,120) : ").split(",") # 사각형 속 데이터 입력받기
    
    if len(cell_n) == square_nums: # 입력 값의 수와 사각형의 개수가 같으면
        for num in cell_n:
            if num.isdecimal(): # 입력된 값이 숫자인지 확인
                if 50<=int(num)<=150: # 미생물 counting 유효 범위 50~150
                    total=total+int(num)
                    isOK=True
                else:
                    print("각 Square당 count 유효 범위는 50~150입니다.\n 보다 정확한 값을 위해 희석배수를 올리세요.")
                    total=0
                    isOK=False
                    break # for 문 끝내는 break
            else:
                print("숫자만 입력하세요.")
                total=0
                isOK=False
                break
    else:
        print("올바른 개수의 값을 입력하세요.") # 다르면 계속 물어라
        continue
            


if square_nums == 1:
    n1=int(cnt_result(total,square_nums))
    print(f'\n(1µl당 들어있는 cell number : {n_chg(n1)} cells/ml)')
elif square_nums == 2: 
    n2=int(cnt_result(total,square_nums))
    print(f'\n(1µl당 들어있는 cell number : {n_chg(n2)} cells/ml)')
elif square_nums == 3: 
    n3=int(cnt_result(total,square_nums))
    print(f'\n(1µl당 들어있는 cell number : {n_chg(n3)} cells/ml)')
elif square_nums == 4: 
    n4=int(cnt_result(total,square_nums))
    print(f'\n(1µl당 들어있는 cell number : {n_chg(n4)} cells/ml)')
elif square_nums == 5: 
    n5=int(cnt_result(total,square_nums))
    print(f'\n(1µl당 들어있는 cell number : {n_chg(n5)} cells/ml)')
elif square_nums == 6: 
    n6=int(cnt_result(total,square_nums))
    print(f'\n(1µl당 들어있는 cell number : {n_chg(n6)} cells/ml)')
elif square_nums == 7: 
    n7=int(cnt_result(total,square_nums))
    print(f'\n(1µl당 들어있는 cell number : {n_chg(n7)} cells/ml)')
elif square_nums == 8: 
    n8=int(cnt_result(total,square_nums))
    print(f'\n(1µl당 들어있는 cell number : {n_chg(n8)} cells/ml)')
else:
    n9=int(cnt_result(total,square_nums))
    print(f'\n(1µl당 들어있는 cell number : {n_chg(n9)} cells/ml)')





