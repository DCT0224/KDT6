class VendingMachine:
    def __init__(self, input_dict):
        '''
        생성자
        :param input_dict: 초기 자판기 재료량(dict 형태)
        '''
        
        self.input_money = 0
        self.inventory = input_dict


    def report(self):
        print('-' * 80)
        print(f"재료 현황: coffee: {self.inventory['coffee']} cream: {self.inventory['cream']} sugar: {self.inventory['sugar']} water: {self.inventory['water']} cup: {self.inventory['cup']} change: {self.inventory['change']}")
        print('-' * 80)

    def turn_off_machine(self):
        print('-' * 50)
        print('커피 자판기 동작을 종료합니다.')
        print('-' * 50)

    def run(self):
        '''
        커피 자판기 동작 및 메뉴 호출 함수
        '''
        # 기능 구현 및 다른 메소드 호출
        self.input_money = int(input('동전을 투입하세요: '))
        menu = '''
[menu]
1. 블랙 커피
2. 프림 커피
3. 설탕 프림 커피
4. 재료 현황
5. 종료
'''
        if self.input_money < 300:
            print(f'투입된 돈 ({self.input_money})이 300원보다 작습니다.')
            print(f'{self.input_money}원을 반환합니다.')
            self.turn_off_machine()
            
        else:
            while True:
                print('-' * 50)
                print(f'커피 자판기 (잔액:{self.input_money}원)')
                print('-' * 50)            
                print(menu)
                menu_choice = int(input('메뉴를 선택하세요: '))
                if menu_choice == 5:
                    print(f'종료를 선택했습니다. {self.input_money}원이 반환됩니다.')
                    self.turn_off_machine()
                    break

                elif menu_choice == 4:
                    self.report()

                elif menu_choice == 1:
                    if (self.inventory['coffee'] >= 30) and (self.inventory['water'] >= 100) and (self.inventory['cup'] >= 1):
                        self.inventory['coffee'] -= 30
                        self.inventory['water'] -= 100
                        self.inventory['cup'] -= 1
                        self.inventory['change'] += 300
                        self.input_money -= 300
                        print(f'블랙 커피를 선택하셨습니다. 잔액 {self.input_money}')
                        self.report()

                    else: 
                        print('재료가 부족합니다.')
                        self.report()
                        print(f'{self.input_money}원을 반환합니다.')
                        self.turn_off_machine()
                        break

                elif menu_choice == 2:
                    if (self.inventory['coffee'] >= 15) and (self.inventory['cream'] >= 15) and (self.inventory['water'] >= 100) and (self.inventory['cup'] >= 1):
                        self.inventory['coffee'] -= 15
                        self.inventory['cream'] -= 15
                        self.inventory['water'] -= 100
                        self.inventory['cup'] -= 1
                        self.inventory['change'] += 300
                        self.input_money -= 300
                        print(f'프림 커피를 선택하셨습니다. 잔액 {self.input_money}')
                        self.report()
                        
                    else: 
                        print('재료가 부족합니다.')
                        self.report()
                        print(f'{self.input_money}원을 반환합니다.')
                        self.turn_off_machine()
                        break
                
                elif menu_choice == 3:
                    if (self.inventory['coffee'] >= 10) and (self.inventory['cream'] >= 10) and (self.inventory['sugar'] >= 10) and (self.inventory['water'] >= 100) and (self.inventory['cup'] >= 1):
                        self.inventory['coffee'] -= 10
                        self.inventory['cream'] -= 10
                        self.inventory['sugar'] -= 10
                        self.inventory['water'] -= 100
                        self.inventory['cup'] -= 1
                        self.inventory['change'] += 300
                        self.input_money -= 300
                        print(f'설탕 프림 커피를 선택하셨습니다. 잔액 {self.input_money}')
                        self.report()

                    else: 
                        print('재료가 부족합니다.')
                        self.report()
                        print(f'{self.input_money}원을 반환합니다.')
                        self.turn_off_machine()
                        break

                else:
                    print('잘못 선택하셨습니다. 다시 입력해주세요')

                if self.input_money < 300:
                    print(f'잔액이 ({self.input_money})이 300원보다 작습니다.')
                    print(f'{self.input_money}원을 반환합니다.')
                    self.turn_off_machine()
                    break

            
            


# VendingMachine 객체 생성
inventory_dict = {
    'coffee': 100,
    'cream': 100,
    'sugar': 100, 
    'water': 500,
    'cup': 5,
    'change': 0
}
coffee_machine = VendingMachine(inventory_dict)
coffee_machine.run()    # VendingMachine 동작 메소드

    