from flask import Flask 
from utils.config import Config

def create_app(env):
    app = Flask(__name__)
    app.config.update(Config.load(env))

    return app
