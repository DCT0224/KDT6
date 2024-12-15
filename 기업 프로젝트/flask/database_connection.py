import mysql.connector

def get_database_connection():
    return mysql.connector.connect(
        host="localhost",       # 예: "localhost" 또는 DBeaver에 설정된 호스트 주소
        user="root",   # DBeaver에서 사용하는 사용자 이름
        password="1234",  # 사용자 비밀번호
        database="기업_프로젝트"  # 데이터베이스 이름
    )