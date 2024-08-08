import os

basedir = os.path.abspath(os.path.dirname(__file__))


import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', '8a2b4c6d8e0f1a2b3c4d5e6f7a8b9c0d')
    CLOUDINARY_CLOUD_NAME = os.environ.get('CLOUDINARY_CLOUD_NAME', 'dmed8jwoe')
    CLOUDINARY_API_KEY = os.environ.get('CLOUDINARY_API_KEY', '949245388128451')
    CLOUDINARY_API_SECRET = os.environ.get('CLOUDINARY_API_SECRET', 'OBqbghUa2hi8kxDg6eglk2Z5fkk')
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'password')
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE', 'SSIS')

class cloudConfig:
    CLOUD_NAME = os.environ.get('CLOUD_NAME')
    API_KEY = os.environ.get('API_KEY', '949245388128451')
    API_SECRET = os.environ.get('API_SECRET', 'OBqbghUa2hi8kxDg6eglk2Z5fkk')


# from os import getenv


# SECRET_KEY = '8a2b4c6d8e0f1a2b3c4d5e6f7a8b9c0d'
# class cloudConfig:
#     CLOUD_NAME = getenv("CLOUD_NAME")
#     API_KEY = getenv("API_KEY")
#     API_SECRET = getenv("API_SECRET")
# class Config:
#     SECRET_KEY = getenv("SECRET_KEY")
#     MYSQL_HOST = getenv("MYSQL_HOST")
#     MYSQL_USER = getenv("MYSQL_USER")
#     MYSQL_PASSWORD = getenv("MYSQL_PASSWORD")
#     MYSQL_DATABASE = getenv("MYSQL_DATABASE")
    

