from flask import Flask, request, Blueprint
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _1
from logging.handlers import RotatingFileHandler
from elasticsearch import Elasticsearch
import os

app = Flask(__name__, template_folder='view/templates')
mail = Mail(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
babel = Babel(app)
app.config.from_object(Config)
# bp = Blueprint('errors', __name__)

#User's followers table
followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
login.login_message = _1('You need to login to access this page.')
es = Elasticsearch('http://localhost:9200')
app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) if app.config['ELASTICSEARCH_URL'] else None
if not app.debug:
    # ...

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

from App.controllers import *
from App.view import *
from App.models import *

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])