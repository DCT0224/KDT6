# ------------------------------------------------------------------
# Flask Framework에서 WebServer 구동 파일
# - 파일명 : app.py
# ------------------------------------------------------------------
# 모듈 로딩 --------------------------------------------------------
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # 설정 추가
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 최대 16MB 파일
    app.config['UPLOAD_FOLDER'] = 'static/uploads'
    
    # Blueprint 등록
    from . import main_views
    app.register_blueprint(main_views.bp)
    
    return app