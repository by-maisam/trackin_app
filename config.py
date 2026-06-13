import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'trackin-dev-secret-key-change-in-production')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///trackin.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False