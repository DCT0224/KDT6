# New! 단축키 … 첫 글자를 탐색할 수 있도록 Drive 단축키가 업데이트되었습니다.
# 위에 라인 : 셀 내용을 파일로 생성/ 한번 생성후에는 마스킹

# --------------------------------------------------------------------------
# 경로 지정
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# 모듈 로딩
# --------------------------------------------------------------------------

import torch
import torch.nn as nn
import torch.nn.functional as F

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
class DynamicModel(nn.Module):

    # 모델 구조 설계 함수 즉, 생성자 메서드
    def __init__(self, in_in, in_out, out_out, h_ins=[], h_outs=[]):
        super().__init__()
        
        self.in_layer=nn.Linear(in_in, h_ins[0] if len(h_ins) else in_out )
        
        self.h_layers=nn.ModuleList()
        for idx  in range(len(h_ins)):
            self.h_layers.append( nn.Linear(h_ins[idx], h_outs[idx])  )
        
        self.out_layer=nn.Linear(h_outs[-1]  if len(h_outs) else in_out, out_out)
        
        
    # 학습 진행 콜백 메서드
    def forward(self, x): 
        # 입력층
        y=self.in_layer(x)               # y=x1w1+x2w2+x3w3+b
        y=F.leaky_relu(y)                         # 0 <= y
        #y=F.relu(self.in_layer(x) )

        # 은닉층
        for linear in self.h_layers:
            y=linear(y)
            y=F.leaky_relu(y) 
            #y=F.relu( linear(y) )
            
        # 출력층
        return self.out_layer(y)      

# 모델 호출
# MODEL_PATH='../Project/MyModels/'
# MODEL_FILE = 'loss(2.01475)_score(0.73614).pth'
MODEL_FILE = r'C:\VSCode\KDT\Torch_DL\models\weather\Reg\loss(1.52000)_score(0.88678).pth'
Weather_Model = torch.load(MODEL_FILE, weights_only=False)



# 사용자 정의 함수----------------------------------------------------------
# WEB에서 사용자에게 보여주고 입력받는 함수 ---------------------------------
# 함수명 : showHTML
# 재 료 : 사용자 입력 데이터, 판별 결과
# 결 과 : 사용자에게 보여질 HTML 코드

# def showHTML(text, msg):
#     print("Content-Type: text/html; charset=utf-8")
#     print(f"""
    
#         <!DOCTYPE html>
#         <html lang="en">
#          <head>
#           <meta charset="UTF-8">
#           <title>---여름 기온 예측---</title>
#          </head>
#          <body>
#           <form>
#             <textarea name="text" rows="10" colos="40" >{text}</textarea>
#             <p><input type="submit" value="오늘 최고기온 예측!!">{msg}</p>
#           </form>
#          </body>
#         </html>""")
    
def showHTML(text1, text2, text3, text4, msg):
    print("Content-Type: text/html; charset=utf-8")
    print(f"""
    <!DOCTYPE html>
    <html lang="ko">
     <head>
      <meta charset="UTF-8">
      <title>여름 기온 예측</title>
      <style>
        body {{
          background-color: #ffe9b0;  /* 여름 느낌의 밝은 색상 */
          color: #333;
          font-family: 'Arial', sans-serif;
          text-align: center;
          padding: 50px;
        }}
        h1 {{
          color: #ff6347;  /* 여름 과일 색상 */
        }}
        input[type="text"] {{
          width: 80%;
          font-size: 18px;
          padding: 10px;
          margin: 5px 0;
          border-radius: 5px;
          border: 1px solid #ccc;
        }}
        input[type="submit"] {{
          background-color: #ffcc00; /* 여름 느낌의 색상 */
          color: #333;
          padding: 10px 20px;
          border: none;
          border-radius: 5px;
          font-size: 20px;
          cursor: pointer;
        }}
        input[type="submit"]:hover {{
          background-color: #ffd700;
        }}
        p {{
          font-size: 18px;
        }}
      </style>
     </head>
     <body>
      <h1>여름 기온 예측</h1>
      <form>
        <input type="text" name="data1" value="{text1}" placeholder="첫 번째 데이터" />
        <input type="text" name="data2" value="{text2}" placeholder="두 번째 데이터" />
        <input type="text" name="data3" value="{text3}" placeholder="세 번째 데이터" />
        <input type="text" name="data4" value="{text4}" placeholder="네 번째 데이터" />
        <p><input type="submit" value="오늘 최고기온 예측!!">{msg}</p>
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
        print("Data received for prediction:", data)  # 디버깅용 로그
        data = data.split(',')
        
        # 데이터 형식 확인
        if len(data) != model.in_layer.in_features:
            raise ValueError(f"입력 데이터의 차원이 맞지 않습니다. 기대 차원: {model.in_layer.in_features}, 실제 차원: {len(data)}")
        
        data = list(map(float, data))
        dataTS = torch.FloatTensor(data).reshape(1, -1)

        # 검증 모드로 모델 설정
        model.eval()
        with torch.no_grad():
            # 추론/평가
            pre_val = model(dataTS)
        return f'예측된 최고 온도는 {pre_val.item():.2f}도 입니다.'
    
    except Exception as e:
        print(f"Error during prediction: {e}")  # 에러 로그 추가
        return f'오류 발생: {e}'  # 구체적인 오류 메시지 반환


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

# (3-2) Form안에 데이터 가져오기
avg_temp = form.getvalue("avg_temp", default="")
ground_temp = form.getvalue("ground_temp", default="")
min_temp = form.getvalue("min_temp", default="")
dew_temp = form.getvalue("dew_temp", default="")

# (3-3) 판별하기
msg = ""
if avg_temp != "" and ground_temp != "" and min_temp != "" and dew_temp != "":
    input_data = f"{avg_temp},{ground_temp},{min_temp},{dew_temp}"
    result = predict_model(Weather_Model, input_data)
    msg = f"{result}"

# (4) 사용자에게 WEB 화면 제공
showHTML(avg_temp, ground_temp, min_temp, dew_temp, msg)
