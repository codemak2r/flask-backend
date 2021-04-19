from flask import Flask 
from common.config import Config
import logging
import logging.config

def create_app(filename):
    app = Flask(__name__)
    app.config.update(Config.load(filename))
    logging.config.dictConfig(Config.load("logger"))

    return app
