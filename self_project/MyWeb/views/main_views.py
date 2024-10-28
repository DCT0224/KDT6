from flask import Blueprint, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename

# Blueprint 설정
bp = Blueprint('main', __name__, url_prefix='/')

# 허용할 파일 확장자
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': '파일이 없습니다'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': '선택된 파일이 없습니다'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        
        # 여기에 이미지 분류 모델을 호출하는 코드를 추가하세요
        # 예: result = your_model.predict(file)
        
        # 임시 응답 (실제 모델 결과로 교체 필요)
        result = {
            'class': '예측된 클래스',
            'confidence': 0.95
        }
        
        return jsonify({
            'success': True,
            'filename': filename,
            'prediction': result
        })
    
    return jsonify({'error': '허용되지 않는 파일 형식입니다'}), 400