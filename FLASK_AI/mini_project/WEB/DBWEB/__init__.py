
# 모듈 로딩 --------------------------------------------------------
from flask import Flask

# DB관련 설정
import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DB = SQLAlchemy() # 실제 DB 생성하는 애
MIGRATE = Migrate() # DB 컨트롤 하는 애



# -----------------------------------------------------------------
# Application 생성 함수
# - 함수명 : create_app <== 이름 변경 불가!!
# 사용자 정의함수 ----------------------------------------------------
def create_app():
    # Flask Web Server 인스턴스 생성
    APP = Flask(__name__)

    # DB 관련 초기화 설정
    APP.config.from_object(config)

    # DB 초기화 및 연동
    DB.init_app(APP) # 이 데이터 베이스랑 APP이랑
    MIGRATE.init_app(APP,DB) # 실제 DB랑 APP이랑 초기화 시켜서 연결해달라 ----> 여기까지가 기본 설정.

    # DB 클래스 정의 모듈 로딩
    from .models import models
    #    .폴더명

    
    # URL 처리 모듈 등록
    from .views import main_view
    APP.register_blueprint(main_view.mainBP)

    return APP

# # 조건부 실행 -------------------------------------------------------
# if __name__ == '__main__':
#     # Flask Web Server 구동
#     app=create_app()
#     app.run()

'''/ <-- 루트 root : SW의 시작 폴더, Linux/Mac 저장소 시작점'''