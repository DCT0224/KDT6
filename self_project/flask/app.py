
from flask import Flask, request, render_template, jsonify
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
import torchvision.models as models

app = Flask(__name__)

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


# 모델 로드
def load_model():
    # ResNet152 모델을 정의하고, fc 레이어를 변경
    model = models.resnet152(pretrained=False)
    model.fc = nn.Linear(2048, 29)  # 실제 클래스 수에 맞춰 조정

    # 저장된 모델 가중치 파일 로드
    model.load_state_dict(torch.load(
        r'C:\Users\KDP-14\Desktop\VSCode\KDT6\self_project\flask\model_train_wb.pth',
        map_location=device  # device로 로드
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
        # 이미지 전처리 및 모델 예측 수행
        image_tensor = preprocess_image(image)
        model = load_model()
        class_idx = predict_image(image_tensor, model)

        # 예측 결과 전달
        result = {
            'predicted_class': CLASS_NAMES[class_idx]
        }
        
        return render_template('result.html', 
                               predicted_class=result['predicted_class'] 
                               )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
