'''
* 모든 커피의 가격은 300원.
* 충분한 돈을 입력하지 않거나, 자판기 내부의 물품(커피,프림,설탕,물,종이컵)이
  부족한 경우 재료가 부족하다는 메시지 출력 후 종료.
* 커피를 제공하면 재료현황 업데이트.
* 종료 선택하면 남은 돈을 반환.

- 커피 머신의 각 기능들을 함수로 구현하기.
1. 초기 자판기 재료 현황
2. 메뉴 출력 및 선택 기능 (종료를 선택할 때까지 반복)
3. 커피 제공 기능
4. 재료 현황 업데이트 기능
5. 재료 현황 출력 기능
6. 물품 현황 체크 기능
'''
class VendingMachine:
    def __init__(self,input_dict):
        '''
        생성자
        :param input_dict: 초기 자판기 재료량(dict 형태)
        '''
        self.input_money = 0
        self.inventory = input_dict
    
    def check(self):
        print('-' * 50)
        print(f"재료 현황: coffee: {self.inventory['coffee']} cream: {self.inventory['cream']} sugar: {self.inventory['sugar']} water: {self.inventory['water']} cup: {self.inventory['cup']} change: {self.inventory['change']}")
        print('-' * 50)
    
    def select_menu(self):
        self.menu =  '''
        [menu]
        1. 블랙 커피
        2. 프림 커피
        3. 설탕 프림 커피
        4. 재료 현황
        5. 종료
        '''
        print('-' * 50)
        print(f'커피 자판기 (잔액:{self.input_money}원)')
        print('-' * 50)            
        print(self.menu)

    def run(self):
        '''
        커피 자판기 동작 및 메뉴 호출 함수
        '''
        
        self.input_money = int(input('동전을 투입하세요: '))

        if self.input_money < 300: # 투입된 돈이 300원보다 작다.
            print(f'투입된 돈 ({self.input_money})이 300원보다 작습니다.')
            print(f'{self.input_money}원을 반환합니다.')
            print('-' * 50)
            print('커피 자판기 동작을 종료합니다.')
            print('-' * 50)
        else: # 돈은 충분한 경우
            while True:

                
                self.select_menu()
                menu = int(input('메뉴를 선택하세요: '))
                if menu == 1: ## 블랙 커피
                    if (self.inventory['coffee'] >= 30) and (self.inventory['water'] >= 100) and (self.inventory['cup'] >= 1):
                        self.inventory['coffee'] -= 30
                        self.inventory['water'] -= 100
                        self.inventory['cup'] -= 1
                        self.inventory['change'] += 300
                        self.input_money -= 300
                        print(f'블랙 커피를 선택하셨습니다. 잔액 {self.input_money}')
                        self.check()
                    else:
                        print('재료가 부족합니다.')
                        self.check()
                        print(f'{self.input_money}원을 반환합니다.')
                        print('-' * 50)
                        print('커피 자판기 동작을 종료합니다.')
                        print('-' * 50)
                        break
                elif menu == 2: ## 프림 커피
                    if (self.inventory['coffee'] >= 15) and (self.inventory['water'] >= 100) and (self.inventory['cup'] >= 1):
                        self.inventory['coffee'] -= 15
                        self.inventory['cream'] -= 15
                        self.inventory['water'] -= 100
                        self.inventory['cup'] -= 1
                        self.inventory['change'] += 300
                        self.input_money -= 300
                        print(f'프림 커피를 선택하셨습니다. 잔액 {self.input_money}')
                        self.check()
                    else:
                        print('재료가 부족합니다.')
                        self.check()
                        print(f'{self.input_money}원을 반환합니다.')
                        print('-' * 50)
                        print('커피 자판기 동작을 종료합니다.')
                        print('-' * 50)
                        break
                elif menu == 3: ## 크림 커피
                    if (self.inventory['coffee'] >= 15) and (self.inventory['water'] >= 100) and (self.inventory['cup'] >= 1):
                        self.inventory['coffee'] -= 15
                        self.inventory['cream'] -= 15
                        self.inventory['water'] -= 100
                        self.inventory['cup'] -= 1
                        self.inventory['change'] += 300
                        self.input_money -= 300
                        print(f'크림 커피를 선택하셨습니다. 잔액 {self.input_money}')
                        self.check()
                    else:
                        print('재료가 부족합니다.')
                        self.check()
                        print(f'{self.input_money}원을 반환합니다.')
                        print('-' * 50)
                        print('커피 자판기 동작을 종료합니다.')
                        print('-' * 50)
                        break
                elif menu == 4: ## 재료 체크
                    self.check()
                elif menu == 5:
                    print(f'종료를 선택했습니다. {self.input_money}원이 반환됩니다.')
                    print('-' * 50)
                    print('커피 자판기 동작을 종료합니다.')
                    print('-' * 50)
                    break
                if self.input_money < 300:
                    print(f'투입된 돈 ({self.input_money})이 300원보다 작습니다.')
                    print(f'{self.input_money}원을 반환합니다.')
                    print('-' * 50)
                    print('커피 자판기 동작을 종료합니다.')
                    print('-' * 50)
                    break

                    







# VendingMachine 객체 생성
inventory_dict = {'coffee': 100,'cream':100,'sugar':100,
                  'water':500,'cup':5,'change':0}
coffee_machine = VendingMachine(inventory_dict)
coffee_machine.run() # VendingMachine 동작 메소드
