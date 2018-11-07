import os
basedir = os.path.abspath(os.path.dirname(__file__))

#PostGreSQL
POSTGRES = {
    'user': 'AnhNTV20',
    'pw': 'password',
    'db': 'SeeBook',
    'host': 'localhost',
    'port': '5432',
}
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'AnhNTV20'
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 5
    UPLOAD_FOLDER = '/home/anhntv20/Desktop/AnhNTV20/App/static'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    LANGUAGES = ['en', 'es']
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')