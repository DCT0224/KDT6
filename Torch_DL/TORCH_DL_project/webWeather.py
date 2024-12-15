# 위에 라인 : 셀 내용을 파일로 생성/ 한번 생성후에는 마스킹

# --------------------------------------------------------------------------
# 경로 지정
# --------------------------------------------------------------------------
import sys
sys.path.append(r'C:\Users\KDP-50\OneDrive\바탕 화면\Python06\MyClass')

# --------------------------------------------------------------------------
# 모듈 로딩
# --------------------------------------------------------------------------

from DL_Modules import *
from DL_func import *
from DL_Reg_Class import *
from ML_preprocessing import *

import os.path                          # 파일 및 폴더 관련
import cgi, cgitb                       # cgi 프로그래밍 관련
import joblib                           # AI 모델 관련
import sys, codecs                      # 인코딩 관련
from pydoc import html                  # html 코드 관련 : html을 객체로 처리?

# 동작관련 전역 변수----------------------------------
SCRIPT_MODE = True                      # Jupyter Mode : False, WEB Mode : True
cgitb.enable()                          # Web상에서 진행상태 메시지를 콘솔에서 확인할수 있도록 하는 기능

# 저장 경로
# SAVE_PATH='../Project/MyModels/'

# 모델 호출
# MODEL_PATH='../Project/MyModels/'
# MODEL_FILE = 'loss(2.01475)_score(0.73614).pth'
MODEL_FILE = r'C:\Users\KDP-50\OneDrive\바탕 화면\Python06\08.Deeping_Learning(Torch)\Project\cgi-bin\loss(2.01475)_score(0.73614).pth'
Weather_Model = torch.load(MODEL_FILE, weights_only=False)

# 사용자 정의 함수----------------------------------------------------------
# WEB에서 사용자에게 보여주고 입력받는 함수 ---------------------------------
# 함수명 : showHTML
# 재 료 : 사용자 입력 데이터, 판별 결과
# 결 과 : 사용자에게 보여질 HTML 코드

def showHTML(text, msg):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    
        <!DOCTYPE html>
        <html lang="en">
         <head>
          <meta charset="UTF-8">
          <title>---내일 기온 예측---</title>
         </head>
         <body bgcolor="antiquewhite">
          <form>
            <textarea name="text" rows="10" colos="40" >{text}</textarea>
            <p><input type="submit" value="내일 평균기온 예측!!">{msg}</p>
          </form>
         </body>
        </html>""")

# ---------------------------------------------------------------------
# 함수 이름 : predice_model()
# 함수 역할 : 모델 예측 함수
# 매개 변수 : model, data
# ---------------------------------------------------------------------

# def predict_model(model, data):
#     data = [data.split(',')]
#     dataTS = torch.FloatTensor(data).reshape(1,-1)

#     # 검증 모드로 모델 설정
#     model.eval()
#     with torch.no_grad():

#         # 추론/평가
#         pre_val=model(dataTS)
#     # return pre_val
#     print(f"{msg}")

def predict_model(model, data):
    try:
        print("Data received for prediction:", data) # 디버깅용 로그
        data = data.split(',')
        data = map(float, data)
        dataTS = torch.FloatTensor(list(data)).reshape(1,-1)

        # 검증 모드로 모델 설정
        model.eval()
        with torch.no_grad():

            # 추론/평가
            pre_val = model(dataTS)
        return f'예측된 온도는 {pre_val.item():.2f}도 입니다.'
    
    except Exception as e:
        print(f"Error during prediction: {e}") # 에러 로그 추가
        return '오류 발생!!'

# --------------------------------------------------------------------------
# 기능 구현 
# --------------------------------------------------------------------------
# (1) WEB 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach()) # 웹에서만 필요 : 표준출력을 utf-8로

# (2) 모델 로딩
if SCRIPT_MODE:
    pthfile = os.path.dirname(__file__)+ MODEL_FILE # 웹상에서는 절대경로만
else:
    pthfile = MODEL_FILE
    
# langModel = joblib.load(pthfile)

# (3) WEB 사용자 입력 데이터 처리
# (3-1) HTML 코드에서 사용자 입력 받는 form 태그 영역 객체 가져오기
form = cgi.FieldStorage()

# (3-2) Form안에 textarea 태그 속 데이터 가져오기
text = form.getvalue("text", default="")

# (3-3) 판별하기
msg = ""
if text != "":
    result = predict_model(Weather_Model, text)
    msg = f"{result}"

# (4) 사용자에게 WEB 화면 제공
showHTML(text, msg)