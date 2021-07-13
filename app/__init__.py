from flask import Flask
from .api import resources
from .extensions import configuration, cors

app_name = 'Weather Buddy API'

def create_app(**config):
    app = Flask(__name__)
    configuration.init_app(app, **config)
    resources.init_app(app)
    cors.init_app(app)

    return app