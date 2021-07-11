from flask import Flask

app_name = 'Weather Buddy API'

def create_app():
    app = Flask(__name__)

    # TODO: Load app settings
    # TODO: Set api endpoints
    @app.get('/')
    def index():
        return app_name

    # TODO: Apply CORS

    return app