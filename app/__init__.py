from flask import Flask
from .api import resources
from .extensions import configuration, cors, cache


def create_app(*argv, **kwargs):
    app = Flask(__name__)
    configuration.init_app(app, **kwargs)
    cache.init_app(app)
    resources.init_app(app)
    cors.init_app(app)

    return app
