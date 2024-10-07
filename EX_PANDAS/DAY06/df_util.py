# ---------------------------------------------------------------------
# Series/DataFrame에서 사용되는 사용자 정의 함수들
# ---------------------------------------------------------------------
# 함수기능 : DataFrame의 기본정보와 속성 확인 기능
# 함수이름 : checkDataFrame
# 매개변수 : DataFrame 인스턴스, DataFrame 인스턴스 이름
# 리턴값/반환값 : 없음
# ---------------------------------------------------------------------
def chechDatatFrame(object,name):
    print(f'\n[{name}]')
    object.info()
    print(f'[Index]   : {object.index}')
    print(f'[Columns] : {object.columns}')
    print(f'[Ndim]    : {object.ndim}')