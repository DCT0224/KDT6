# -----------------------------------------------------------------------
# 클래스(Class)
# - 객체지향언어(OOP)에서 데이터를 정의하는 자료형
# - 데이터를 정의할 수 있는 데이터가 가진 속성과 기능을 명시
# - 구성요소 : 속성/attribute/field + 기능/method
# -----------------------------------------------------------------------
# 클래스 정의 : 햄버거를 나타내는 클래스
# 클래스 이름 : 버거
# 클래스 속성 : 번, 패티, 야채, 치즈
# 클래스 기능 : 햄버거 설명 기능
# -----------------------------------------------------------------------

class Bugger:

    # 힙 영역에 객체 생성 시 속성값 저장 기능
    def __init__(self,bread,patty,veg,kind):
        self.bread=bread
        self.patty=patty
        self.veg=veg
        self.kind=kind

    # 기능 즉 메서드
    def printInfo(self):
        print(f'brand : {self.kind}')
        print(f'빵 종류 : {self.bread}')
        print(f'패티 종류 : {self.patty}')
        print(f'야채 종류 : {self.veg}')

    # 속성을 변경하거나 읽어오는 메서드 => getter/setter 메서드
    def get_bread(self):
        return self.bread
        # 직접 접근

    def set_bread(self,bread):
        self.bread=bread
        # 간접 접근

        
## 객체 생성 -------------------------------------------------------------
## 불고기 버거 객체 생성
bugger1=Bugger('브리오슈','불고기','양상추,양파,토마토','롯데리아')

## 치즈 버거 객체 생성
bugger2=Bugger('참깨곡물빵','쇠고기패티','치즈,양상추,양파,토마토','맥도날드')

## 버거 정보 확인
bugger1.printInfo()

# 속성 읽은 방법 : (1) 직접 접근 읽기 , (2) 간접 접근 읽기 - getter 메서드 사용
print(bugger1.bread, bugger1.get_bread())

# 속성 변경 방법 : (1) 직접 접근 읽기 , (2) 간접 접근 읽기 - setter 메서드 사용
bugger1.bread='들깨방'
bugger1.set_bread('올리브빵')


bugger2.printInfo()

# 버거 인스턴스 속성 변경
bugger1.patty='치킨'
bugger1.printInfo()