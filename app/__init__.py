from flask import Flask
from .api import resources
from .extensions import configuration, cors, cache

app_name = 'Weather Buddy API'

def create_app(**config):
    app = Flask(__name__)
    configuration.init_app(app, **config)
    cache.init_app(app)
    resources.init_app(app)
    cors.init_app(app)

    return app