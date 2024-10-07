
### 클래스 만들어보기 연습


class wp:
    def __init__(self,sol,arow,gun):
        self.sol=sol
        self.arow=arow
        self.gun=gun

    def printinfo(self):
        print(f'{self.sol}')
        print(f'{self.arow}')
        print(f'{self.gun}')

    def get_sol(self):
        return self.gun
    
    def set_sol(self,sol):
        self.sol=sol

