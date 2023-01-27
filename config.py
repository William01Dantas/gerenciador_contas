USERNAME = 'root'
PASSWORD = ''
SERVER = 'localhost'
DB = 'account_management'

SQLALCHEMY_DATABASE_URI = f'mtsql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'chave_secreta1'
