# ------------------------------------------------------------------
# Flask Framework에서 WebServer 구동 파일
# - 파일명 : app.py
# ------------------------------------------------------------------
# 모듈 로딩 --------------------------------------------------------
from flask import Flask, render_template

# 사용자 정의함수 ----------------------------------------------------
def create_app():

    # 전역변수 ----------------------------------------------------------
    # Flask Web Server 인스턴스 생성
    APP = Flask(__name__)

    # 라우팅 기능 함수 --------------------------------------------------
    # @Flask Web Server 인스턴스 생성.route('URL')
    # http://127.0.0.1:5000/
    @APP.route('/')
    def index():
        # return '''<body style='background-color:skyblue;'>
        #             <h1>HELLO</h1>
        #             </body>'''
        return render_template('index.html')
    # http://127.0.0.1:5000/info
    # http://127.0.0.1:5000/info/
    @APP.route('/info')
    @APP.route('/info/')
    def info():
        return '''<body style='background-color:yellow; text-align:center'>
                    <h1>INFORMATION</h1>
                    </body>'''

    # http://127.0.0.1:5000/info/문자열변수
    @APP.route('/info/<name>')
    def printInfo(name):
    #     return f'''
    #              <body style='background-color:pink; text-align:center'>
    #             <h1>{name}'s INFORMATION</h1>
    #             HELLO~
    #             </body>
    # '''
        return render_template('info.html',name=name)

    # http://127.0.0.1:5000/info/정수
    @APP.route('/info/<int:age>')
    def checkAge(age):
        return f'''
                <body style='background-color:pink; text-align:center'>
                나이 : {age}
                </body>
    '''

    # http://127.0.0.1:5000/go
    @APP.route('/go')
    def goHome():
        return APP.redirect('/info')

    return APP

# 조건부 실행 -------------------------------------------------------
if __name__ == '__main__':
    # Flask Web Server 구동
    app=create_app()
    app.run()

'''/ <-- 루트 root : SW의 시작 폴더, Linux/Mac 저장소 시작점'''