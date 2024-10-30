import os

# 데이터베이스 설정
DATABASE_CONFIG = {
    'HOST': os.getenv('DB_HOST', 'localhost'),
    'PORT': os.getenv('DB_PORT', '3306'),
    'USER': os.getenv('DB_USER', 'myuser'),
    'PASSWORD': os.getenv('DB_PASSWORD', 'mypassword'),
    'NAME': os.getenv('DB_NAME', 'mydatabase'),
}