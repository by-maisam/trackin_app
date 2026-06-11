import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'trackin-dev-secret-key-change-in-production')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 
        'postgresql://postgres:password@localhost:5432/postgres'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False