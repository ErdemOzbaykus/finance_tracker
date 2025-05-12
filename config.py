import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'gizli-anahtar')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///../finance.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '../uploads'))
