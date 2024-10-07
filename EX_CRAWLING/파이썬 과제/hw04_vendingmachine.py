# -----객체 지향 프로그래밍(OPP:object-oriented programming)-----
# 우리가 살고 있는 실제 세계가 객체(object)들로 구성되어 있음.
# 객체는 속성과 동작을 가짐.
# 클래스 : 객체에 대한 설계도
# 인스턴스 : 클래스로부터 만들어지는 각각의 객체를 그 클래스의 인스턴스라고 함.
#            - 파이썬에서는 모든 것이 객체로 구성됨.
#            - 객체의 특징: 사용할 수 있는 메소드를 가지고 있음.
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def reset(self):
        self.count = 0
    def get(self):
        return self.count

a = Counter() # Counter 클래스의 객체 생성
print(a.count)
a.increment()
print("카운터 a의 값은",a.get())
print("카운터 a의 값은",a.count)

class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
class Counter:
    def __init__(self,init_value=0):
        self.count = init_value
    def increment(self):
        self.count += 1
a = Counter(100) # 카운터의 초기 값은 100
b = Counter()    # 카운터의 초기 값은 0

class Counter:
    def __init__(self,init_Value=0):
        self.count = init_Value
        self.increment()
    def increment(self):
        self.count += 1
    def show(self):
        s = "현재 설정값"
        print(s,self.count) # self.count: 인스턴스 변수
a = Counter(0)
a.show()

b = Counter(100)
b.show()

class Car:
    def __init__(self,speed,color,model):
        self.speed = speed
        self.color = color
        self.model = model
    def drive(self):
        self.speed = 60
myCar = Car(0,"blue","E-class")

print('자동차 객체를 생성하였습니다.')
print('자동차의 속도는',myCar.speed)

myCar.drive()
print('자동차의 속도는',myCar.speed)

class Student:
    def __init__(self,name=None,age=0):
        self.__name = name
        self.__age = age
    def print_info(self):
        print(f'name: {self.__name},age: {self.__age}')

obj=Student('HongGilDong',21)
obj.print_info()
# print(obj.__age)

class Student:
    def __init__(self,name=None,age=0):
        self.__name = name
        self.__age = age
    def getAge(self):
        return self.__age
    def getName(self):
        return self.__name
    def setAge(self,age):
        self.__age = age
    def setName(self,name):
        self.__name = name

obj=Student('Alice',20)
print(obj.getName())
obj.setName('Charlie')
print(obj.getName())

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def withdraw(self,amount):
        self.__balance -= amount
        print('통장에서 ',amount,'원 출금되었음.')
        return self.__balance
    def deposit(self,amount):
        self.__balance += amount
        print('통장에서 ',amount,'원 입금되었음.')
        return self.__balance
a = BankAccount()
a.deposit(100)
a.withdraw(10)