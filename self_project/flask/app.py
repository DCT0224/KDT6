from flask import Flask, request, render_template, jsonify
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
import torchvision.models as models
import pymysql
from datetime import datetime, timedelta

app = Flask(__name__)

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# MySQL 데이터베이스 설정
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'refrigerator'
}

# 모델 로드
def load_model():
    model = models.resnet152(pretrained=False)
    model.fc = nn.Linear(2048, 29)
    model.load_state_dict(torch.load(
        r'C:\Users\KDP-14\Desktop\VSCode\LocalData\self_project\models\model_train_wb.pth',
        map_location=device
    ))
    model.eval()
    return model

# 이미지 전처리 함수
def preprocess_image(image):
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    image_tensor = preprocess(image).unsqueeze(0).to(device)
    return image_tensor

# 예측 함수
def predict_image(image_tensor, model):
    with torch.no_grad():
        output = model(image_tensor)
        probabilities = torch.softmax(output, dim=1)[0]
        class_idx = probabilities.argmax().item()
        return class_idx

# 한글 클래스 이름
CLASS_NAMES = [
    "사과", "바나나", "비트", "피망", "양배추", "당근", "콜리플라워", "고추", 
    "오이", "가지", "마늘", "생강", "포도", "키위", "레몬", "상추", "망고", 
    "양파", "오렌지", "배", "완두콩", "파인애플", "석류", "감자", "무", 
    "시금치", "고구마", "토마토", "수박"
]

# 데이터베이스에 예측 결과 저장
# 데이터베이스에서 소비 기한 가져오기 및 저장
def save_to_database(item_name):
    try:
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        # 소비 기한 가져오기
        query_get_period = "SELECT `소비기한 (일수)` FROM 과채류_정보_데이터셋 WHERE 식품 = %s"
        cursor.execute(query_get_period, (item_name,))
        result = cursor.fetchone()

        if result:
            # 소비 기한을 사용해 권장 소비 날짜 계산
            consumption_days = int(result[0])  # 소비 기한(일수)
            recommended_date = datetime.now() + timedelta(days=consumption_days)

            # 저장 방식은 기본값으로 설정
            storage_method = "냉장 보관"

            # 새 데이터를 삽입
            query_insert = """
            INSERT INTO fruit_data (item_name, storage_method, consumption_period, recommended_consumption_date)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query_insert, (item_name, storage_method, consumption_days, recommended_date))
            connection.commit()
        else:
            print(f"'{item_name}'에 대한 소비 기한 데이터를 찾을 수 없습니다.")

    except Exception as e:
        print("DB 저장 오류:", e)
    finally:
        connection.close()



# 메인 업로드 페이지
@app.route('/')
def upload_page():
    return render_template('ref.html')

# 이미지 예측 라우트
@app.route('/ref/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': '이미지 파일이 없습니다.'}), 400

    file = request.files['file']
    image = Image.open(file).convert('RGB')

    try:
        # 이미지 전처리 및 예측
        image_tensor = preprocess_image(image)
        model = load_model()
        class_idx = predict_image(image_tensor, model)
        predicted_class = CLASS_NAMES[class_idx]

        # 추천 보관법 조회
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        # 추천 보관법 가져오기
        query_storage_tip = "SELECT `추천 보관법 (상세)` FROM 과채류_정보_데이터셋 WHERE 식품 = %s"
        cursor.execute(query_storage_tip, (predicted_class,))
        storage_tip = cursor.fetchone()
        storage_tip = storage_tip[0] if storage_tip else "추천 보관법 정보가 없습니다."

        # fruit_data 테이블에서 데이터 가져오기
        query_fruit_data = "SELECT item_name, storage_method, recommended_consumption_date FROM fruit_data"
        cursor.execute(query_fruit_data)
        fridge_data = cursor.fetchall()

        # 데이터베이스 연결 종료
        connection.close()

        # 예측 결과를 데이터베이스에 저장
        save_to_database(predicted_class)

        # 결과 HTML 페이지 렌더링
        return render_template(
            'result.html',
            predicted_class=predicted_class,
            storage_tip=storage_tip,
            fridge_data=fridge_data  # 냉장고 데이터 전달
        )

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)