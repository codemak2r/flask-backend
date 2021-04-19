from flask import Flask 
import pymysql
pymysql.install_as_MySQLdb()
from common.config import Config
import logging
import logging.config
from common.core import JSONEncoder
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
from app.models.user import *
from app.models.permission import *

def create_app(filename):
    app = Flask(__name__)
    app.config.update(Config.load(filename))
    db.init_app(app)
    migrate.init_app(app,db)
    logging.config.dictConfig(Config.load("logger"))
    from app.api.v1.test import api_v1
    app.register_blueprint(api_v1)
    app.json_encoder = JSONEncoder
    
    return app
