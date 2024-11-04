import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models.payment import Base  # SQLAlchemy Base import


db_url = 'sqlite:///../parkingdb.db'
# Docker Compose에서 정의된 환경 변수로 MariaDB 연결 설정
# DATABASE_URL = "mysql+pymysql://wpuser:abc123!!@mariadb:3306/wordpress

# 컨테이너 deployment 할 때
# import logging
# import sqlalchemy
# from sqlalchemy.orm import sessionmaker
# import sys
# import os
#
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from models.parking import Base  # Base는 SQLAlchemy에서 테이블 정의를 위한 베이스 클래스입니다.
#
# # 환경 변수 설정 (secret.yaml에 맞춰 설정)
# DB_USER = os.getenv('MYSQL_USER')
# DB_PASSWORD = os.getenv('MYSQL_PASSWORD')
# DB_HOST = os.getenv('MYSQL_HOST')
# DB_NAME = os.getenv('MYSQL_DATABASE')
# DB_PORT = os.getenv('MYSQL_PORT')
#
# logging.info(f"DB_USER: {DB_USER}, DB_PASSWORD: {DB_PASSWORD}, DB_HOST: {DB_HOST}, DB_NAME: {DB_NAME}, DB_PORT: {DB_PORT}")
#
# db_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = sqlalchemy.create_engine(db_url, echo=True)
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False, bind=engine)

def create_tables():
    Base.metadata.create_all(engine)

def get_db():
    with SessionLocal() as db:
        yield db