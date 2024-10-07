
def draw_matrix():
    
    # 메트리스 만들기
    while True:
        n=int(input('홀수차	배열의	크기를	입력하세요:'))
        if n%2==0:
            print('짝수를 입력하였습니다.	다시 입력하세요.')

        else:
            print(f'Magic Square ({n}X{n})')
            break
    rows= n
    cols = n
    matrix = [ [0 for col in range(cols)] for row in range(rows)]
    x=0
    y=n//2
    num = 1
    matrix[x][y] = num


    for i in range(n*n-1):
        num+=1
        x-=1
        y+=1
        # x와 y의 값이 범위 내의 값인지 먼저 체크
        if x<0 and y ==n:
            x+=2
            y-=1
            if matrix[x][y]==0:
                matrix[x][y]=num
            else:
                x+=1
                matrix[x][y]=num
                if x<0:
                    x=n-1
                    matrix[x][y]=num
                    continue
                if y ==n:
                    y=0
                    matrix[x][y]=num
                    continue

        elif x<0: 
            x=n-1
            if matrix[x][y]==0:
                matrix[x][y]=num
            else:
                x+=1
                matrix[x][y]=num
                if x<0:
                    x=n-1
                    matrix[x][y]=num
                    continue
                if y ==n:
                    y=0
                    matrix[x][y]=num
                    continue
        elif y == n: 
            y=0
            if matrix[x][y]==0:
                matrix[x][y]=num
            else:
                x+=1
                matrix[x][y]=num
                if x<0:
                    x=n-1
                    matrix[x][y]=num
                    continue
                if y ==n:
                    y=0
                    matrix[x][y]=num
                    continue

        else:
            if matrix[x][y]==0:
                matrix[x][y]=num
            else:
                x+=2
                y-=1
                matrix[x][y]=num
                if x<0:
                    x=n-1
                    matrix[x][y]=num
                    continue
                if y ==n:
                    y=0
                    matrix[x][y]=num
                    continue

    for i in range(n):
        print(*matrix[i])

draw_matrix()