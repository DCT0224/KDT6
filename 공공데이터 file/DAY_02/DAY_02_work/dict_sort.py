## city data Dict 형태로 만들기
import operator


data = {'Seoul':['South Korea','Asia','9,655,000'],
        'Tokyo':['Japan','Asia','14,110,000'],
        'Beijing':['China','Asia','21,540,000'],
        'London':['United Kingdom','Europe','14,800,000'],
        'Berlin':['United Kingdom','Europe','3,426,000'],
        'Mexico City':['Mexico','America','21,200,000']}






while True:
    print('-'*50)
    print('1. 전체 데이터 출력')
    print('2. 수도 이름 오름차순 출력')
    print('3. 모든 도시의 인구수 내림차순 출력')
    print('4. 특정 도시의 정보 출력')
    print('5. 대륙별 인구수 계산 및 출력')
    print('6. 프로그램 종료')
    print('-'*50)
    select_menu=int(input('메뉴를 입력하세요.: '))
    print(select_menu)

    if select_menu == 3:
        for d in data:
             data[d][2]=int(data[d][2].replace(',',''))

        sorted_num = dict(sorted(data.items(), key= lambda x:x[1][2], reverse=True))
        

        index = 1
        for d in sorted_num:
             print(f'{index} {d} : {sorted_num[d][2]:,}')
             index += 1
             
    if select_menu == 6:
        print('프로그램을 종료합니다.')
        break

    if select_menu == 1:
        index = 1
        for d in data:
            data[d][2]=data[d][2].replace(',','')
            print(f'[{index}] {d} : {data[d]}')
            index +=1

    if select_menu == 2:
        index = 1
        sorted_center = dict(sorted(data.items(), key=operator.itemgetter(0)))
        for d in sorted_center:
            print(f'[{index}] {d} : {data[d][0]} {data[d][1]} {data[d][2]}')
            index +=1


    if select_menu == 4:
        select_city=input('출력할 도시 이름을 입력하세요: ')
        print(select_city)
        if select_city not in data.keys():
            print(f'도시이름: {select_city}은 key에 없습니다.')

        else:
            print(f'{select_city}')
            print(f'국가:{data[select_city][0]} 대륙:{data[select_city][1]} 인구수:{data[select_city][2]}')

    if select_menu == 5:
        select_con=input('대륙 이름을 입력하세요(Asia, Europe, America): ')
        print(select_con)

        sum_list=[]
        for d in data:
            if data[d][1]==select_con:
                print(f'{d} : {data[d][2]}')
                data[d][2]=int(data[d][2].replace(',',''))
                sum_list.append(data[d][2])

        print(f'{select_con} 전체 인구수: {sum(sum_list):,}')




