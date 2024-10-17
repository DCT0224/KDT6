import os
import cgi
import cgitb
import torch
import sys
import torch.nn as nn
import codecs
import numpy as np
os.environ['KMP_DUPLICATE_LIB_OK']='True'

# CGI 스크립트에서 발생하는 오류를 디버깅하기 위해 활성화
SCRIPT_MODE = True    # Jupyter Mode : False, WEB Mode : True
cgitb.enable()        # Web상에서 진행상태 메시지를 콘솔에서 확인할 수 있도록 하는 기능

# 체포 확률 예측 모델 정의
class Burmodel(nn.Module):
    def __init__(self):
        super().__init__()
        self.in_layer = nn.Linear(12, 1000)
        self.bn1 = nn.BatchNorm1d(num_features=1000)

        # 은닉층들
        self.hd_layer1 = nn.Linear(1000, 2000)
        self.bn2 = nn.BatchNorm1d(num_features=2000)

        self.hd_layer2 = nn.Linear(2000, 2500)
        self.bn3 = nn.BatchNorm1d(num_features=2500)

        self.hd_layer3 = nn.Linear(2500, 2000)
        self.bn4 = nn.BatchNorm1d(num_features=2000)

        self.hd_layer4 = nn.Linear(2000, 1500)
        self.bn5 = nn.BatchNorm1d(num_features=1500)

        self.hd_layer5 = nn.Linear(1500, 1000)
        self.bn6 = nn.BatchNorm1d(num_features=1000)

        self.hd_layer6 = nn.Linear(1000, 800)
        self.bn7 = nn.BatchNorm1d(num_features=800)

        self.hd_layer7 = nn.Linear(800, 500)
        self.bn8 = nn.BatchNorm1d(num_features=500)

        self.hd_layer8 = nn.Linear(500, 300)
        self.bn9 = nn.BatchNorm1d(num_features=300)

        self.hd_layer9 = nn.Linear(300, 100)
        self.bn10 = nn.BatchNorm1d(num_features=100)

        # 출력층
        self.out_layer = nn.Linear(100, 1)

        self.leaky_relu = nn.LeakyReLU(negative_slope=0.01)

    def forward(self, input_data):
        # 입력층
        y = self.leaky_relu(self.in_layer(input_data))
        y = self.bn1(y)

        # 은닉층
        y = self.leaky_relu(self.hd_layer1(y))
        y = self.bn2(y)

        y = self.leaky_relu(self.hd_layer2(y))
        y = self.bn3(y)

        y = self.leaky_relu(self.hd_layer3(y))
        y = self.bn4(y)

        y = self.leaky_relu(self.hd_layer4(y))
        y = self.bn5(y)

        y = self.leaky_relu(self.hd_layer5(y))
        y = self.bn6(y)

        y = self.leaky_relu(self.hd_layer6(y))
        y = self.bn7(y)

        y = self.leaky_relu(self.hd_layer7(y))
        y = self.bn8(y)

        y = self.leaky_relu(self.hd_layer8(y))
        y = self.bn9(y)

        y = self.leaky_relu(self.hd_layer9(y))
        y = self.bn10(y)

        # 출력층
        return torch.sigmoid(self.out_layer(y))


# 체포 확률을 예측하는 함수
def predict_arrest_probability(model, input_data):
    with torch.no_grad():
        input_tensor = torch.FloatTensor([input_data])
        prediction = model(input_tensor)
    return prediction.item()


# 모델 로드 함수
def load_model(model_path):
    model = Burmodel() 
    model.load_state_dict(torch.load(model_path, weights_only=True))
    model.eval()
    return model


# 사용자에게 보여줄 HTML 코드 생성 함수
def showHTML(data, msg):
    print("Content-Type: text/html; charset=utf-8")
    print()
    print(f"""
    <!DOCTYPE html>
    <html lang="ko">
     <head>
      <meta charset="UTF-8">
      <title>체포 확률 예측</title>
     </head>
     <body>
      <h1>체포 확률 예측</h1>
      <form method="POST">
        <label for="Domestic">가정 내 사건 (0 또는 1):</label>
        <input type="text" id="Domestic" name="Domestic" value="{data.get('Domestic', '')}"><br>
        
        <label for="Description_ATTEMPT FORCIBLE ENTRY">강제 침입 시도 (0 또는 1):</label>
        <input type="text" id="Description_ATTEMPT FORCIBLE ENTRY" name="Description_ATTEMPT FORCIBLE ENTRY" value="{data.get('Description_ATTEMPT FORCIBLE ENTRY', '')}"><br>
        
        <label for="Description_FORCIBLE ENTRY">강제 침입 성공 (0 또는 1):</label>
        <input type="text" id="Description_FORCIBLE ENTRY" name="Description_FORCIBLE ENTRY" value="{data.get('Description_FORCIBLE ENTRY', '')}"><br>
        
        <label for="Description_HOME INVASION">주거 침입 (0 또는 1):</label>
        <input type="text" id="Description_HOME INVASION" name="Description_HOME INVASION" value="{data.get('Description_HOME INVASION', '')}"><br>
        
        <label for="Description_UNLAWFUL ENTRY">일반 건물 침입 (0 또는 1):</label>
        <input type="text" id="Description_UNLAWFUL ENTRY" name="Description_UNLAWFUL ENTRY" value="{data.get('Description_UNLAWFUL ENTRY', '')}"><br>
        
        <label for="Location Description_HOUSE">사건 발생 장소 집(0 또는 1):</label>
        <input type="text" id="Location Description_HOUSE" name="Location Description_HOUSE" value="{data.get('Location Description_HOUSE', '')}"><br>
        
        <label for="Location Description_PARKINGZONE"> 사건 발생 장소 주차장(0 또는 1):</label>
        <input type="text" id="Location Description_PARKINGZONE" name="Location Description_PARKINGZONE" value="{data.get('Location Description_PARKINGZONE', '')}"><br>
        
        <label for="Location Description_SCHOOL"> 사건 발생 장소 학교(0 또는 1):</label>
        <input type="text" id="Location Description_SCHOOL" name="Location Description_SCHOOL" value="{data.get('Location Description_SCHOOL', '')}"><br>

        <label for="Location Description_STORE"> 사건 발생 장소 가게 또는 상점(0 또는 1):</label>
        <input type="text" id="Location Description_STORE" name="Location Description_STORE" value="{data.get('Location Description_STORE', '')}"><br>
        
        <label for="Location Description_STREET">사건 발생 장소 거리(0 또는 1):</label>
        <input type="text" id="Location Description_STREET" name="Location Description_STREET" value="{data.get('Location Description_STREET', '')}"><br>
        
        <label for="District">사건 발생 장소 경찰 구역 :</label>
        <input type="text" id="District" name="District" value="{data.get('District', '')}"><br>
        
        <label for="Community Area">사건 발생 장소 사회 구역:</label>
        <input type="text" id="Community Area" name="Community Area" value="{data.get('Community Area', '')}"><br><br>

        <input type="submit" value="체포 확률 예측">
      </form>

      <!-- 결과 메시지가 있을 때만 출력 -->
       {"<p>결과: " + msg + "</p>" if msg else ""}

     </body>
    </html>""")

# 모델 경로 설정
MODEL_PATH = r'C:\Users\hoon\Desktop\KDT 6\project\DL\model_burg_train_wbs.pth'

if os.path.exists(MODEL_PATH):
    model = load_model(MODEL_PATH)
else:
    print(f"모델 파일을 찾을 수 없습니다: {MODEL_PATH}")

# 웹 인코딩 설정
if SCRIPT_MODE:
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())  # 웹에서만 필요 : 표준출력을 utf-8로

# 사용자 입력 데이터 처리
form = cgi.FieldStorage()

# 입력된 값들 가져오기
data = {field: form.getvalue(field, "") for field in [
    "Domestic", "Description_ATTEMPT FORCIBLE ENTRY", "Description_FORCIBLE ENTRY", "Description_HOME INVASION", 
    "Description_UNLAWFUL ENTRY", "Location Description_HOUSE", "Location Description_PARKINGZONE", 
    "Location Description_SCHOOL", "Location Description_STORE", "Location Description_STREET", 
    "District", "Community Area"
]}

# 모든 입력 값이 제출되었는지 확인하고, 숫자형으로 변환
try:
    input_data = [float(data[field]) for field in data]  # 12개 입력값 모두 확인
    if len(input_data) != 12:
        raise ValueError("입력값이 부족합니다. 12개의 입력값이 필요합니다.")
except ValueError as e:
    showHTML(data, f"잘못된 입력: {e}")
    sys.exit(1)

# 모델 예측 수행
prediction = predict_arrest_probability(model, input_data)
probability_percent = round(prediction * 100, 2)

# 결과 표시
showHTML(data, f"예측된 체포 확률: {probability_percent}%")