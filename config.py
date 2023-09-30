import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'f1850606e92a702c9306cd08ff3283f33cb5c09351600c06717a7500a63b41e7'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'postgresql://postgres:postgres@localhost/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'c200b45e2c936aa9ecdd714f104a5baa4e11bbd1da75294ec808bb6ead352aa5'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True
print("Config imported")  # Add this line

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
config_name = os.environ.get('FLASK_ENV', 'development')

config = config_by_name[config_name]


