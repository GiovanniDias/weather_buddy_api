from flask import Flask
from dynaconf import FlaskDynaconf

app_name = 'Weather Buddy API'

def create_app(**config):
    app = Flask(__name__)

    FlaskDynaconf(app, **config)
    
    # TODO: Set api endpoints
    @app.get('/')
    def index():
        return app_name

    # TODO: Apply CORS

    return app