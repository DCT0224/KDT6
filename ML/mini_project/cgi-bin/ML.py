# 위에 라인 : 셀 내용을 파일로 생성/ 한번 생성후에는 마스킹

# 모듈 로딩--------------------------------------------
import os.path     # 파일 및 폴더 관련
import cgi, cgitb  # cgi 프로그래밍 관련
import joblib      # AI 모델 관련
import sys, codecs # 인코딩 관련
from pydoc import html # html 코드 관련 : html을 객체로 처리?
import joblib
import sklearn
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import VotingClassifier, BaggingClassifier, GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import ElasticNet, Ridge, Lasso, LinearRegression, LogisticRegression
import numpy as np

# 동작관련 전역 변수----------------------------------
SCRIPT_MODE = True    # Jupyter Mode : False, WEB Mode : True
cgitb.enable()         # Web상에서 진행상태 메시지를 콘솔에서 확인할수 있도록 하는 기능


# 사용자 정의 함수-----------------------------------------------------------
# WEB에서 사용자에게 보여주고 입력받는 함수 ---------------------------------
# 함수명 : showHTML
# 재 료 : 사용자 입력 데이터, 판별 결과
# 결 과 : 사용자에게 보여질 HTML 코드
def showHTML(data, msg):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    <!DOCTYPE html>
    <html lang="en">
     <head>
      <meta charset="UTF-8">
      <title>---건강 점수 측정---</title>
     </head>
     <body>
      <form>
        <input type='text' name='q0' placeholder='주당 공부 시간' value='{data[0]}'><br/>
        <input type='text' name='q1' placeholder='출석률' value='{data[1]}'><br/>
        <input type='text' name='q2' placeholder='이전 학기 성적' value='{data[2]}'><br/>
        <input type='text' name='q3' placeholder='부모 학력' value='{data[3]}'><br/>
        <input type='text' name='q4' placeholder='사교육 여부(예=1, 아니요=0)' value='{data[4]}'><br/>
        <p><input type="submit" value="결과보기"></p>
        <p>{msg}</p>
      </form>
     </body>
    </html>""")

    
# 사용자 입력 텍스트 판별하는 함수---------------------------------------------------------------------------

# ['Study Hours per Week', 'Attendance Rate', 'Previous Grades', 'Parent Education Level',
                        #   'Participation in Extracurricular Activities']

def detectLang(data_input):
    result=""
    if data_input == [""]*5: result="입력 대기" 
    elif len(data_input) !=9: 
      
        result ="다시 입력하세요."
    
    model=joblib.load(r'C:\Users\KDP-14\Desktop\VSCode\KDT6\ML\mini_project\cgi-bin\best_model.joblib')
    scaler=joblib.load(r'C:\Users\KDP-14\Desktop\VSCode\KDT6\ML\mini_project\cgi-bin\mmScaler.joblib')

    data_input = list(map(int, data_input))
    d=data_input
    
    sample=[d]
    d=scaler.transform(sample)
    
    
    # print(dataTS, dataTS.shape)

    # test data 예측-----------------------------------------
    # 모델 로드
    # pklfile = r'C:\Users\KDP-43\Desktop\DL_project\cgi-bin\model\alive_1\model_all.pth'

    # SepsisModel = joblib.load(pklfile)

    
    result_num = model.predict(sample)
    result=['Not Passed', 'Pass']



    return result[int(result_num)]

# 기능 구현 ------------------------------------------------
# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) #웹에서만 필요 : 표준출력을 utf-8로

# # (2) 모델 로딩

# pklfile = r'C:\Users\KDP-43\Desktop\DL_project\cgi-bin\model\alive_1\model_all.pth'
    
# SepsisModel = joblib.load(pklfile)

# ## 저장경로
# SAVE_PATH= r'C:\Users\KDP-25\Desktop\test\Web\project\model\dl'

# # 저장 파일명
# SAVE_MODEL = SAVE_PATH+'\health_wbs.pth'

# if os.path.exists(SAVE_MODEL):
#    with open('../model/ml/ML_model.pikle') as f:
#         Model= torch.load(SAVE_MODEL, weights_only=False)
#    print("경로상 파일이 존재합니다.")
# else:
#    print(f'{SAVE_MODEL} 파일이 존재하지 않습니다. 다시 확인하세요.')



# (3) WEB 사용자 입력 데이터 처리
# (3-1) HTML 코드에서 사용자 입력 받는 form 태크 영역 객체 가져오기
form = cgi.FieldStorage()
# (3-2) Form안에 textarea 태크 속 데이터 가져오기
data = []
data.append(form.getvalue("q0", default="20"))
data.append(form.getvalue("q1", default="180"))
data.append(form.getvalue("q2", default="60"))
data.append(form.getvalue("q3", default="8"))
data.append(form.getvalue("q4", default="0"))
# data.append(form.getvalue("q5", default="2"))
# data.append(form.getvalue("q6", default="3"))
# data.append(form.getvalue("q7", default="3"))
# data.append(form.getvalue("q8", default="60"))
#text ="Happy New Year" # 테스트용 (쥬피터 내부)

# (3-3) 판별하기
# msg =""
# if not '' in data:
result_input = detectLang(data)
result_input = f'{result_input}'

# result_input = detectLang(data)

# data 초기화
data = [""]*9
# (4) 사용자에게 WEB 화면 제공
showHTML(data,result_input)

'''
python -m http.server --cgi 8080
'''