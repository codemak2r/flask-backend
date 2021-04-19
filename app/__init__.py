from flask import Flask 
from common.config import Config
import logging
import logging.config

def create_app(filename):
    app = Flask(__name__)
    app.config.update(Config.load(filename))
    logging.config.dictConfig(Config.load("logger"))
    from app.api.v1.test import api_v1
    app.register_blueprint(api_v1)
    return app
