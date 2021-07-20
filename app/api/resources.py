from flask import Response, request
from .controllers import WeatherController as controller


def init_app(app):
    @app.get('/')
    def index():
        return app.config.APP_NAME

    @app.get('/weather/<city_name>')
    @app.cache.cached()
    def get_weather_by_city(city_name: str) -> Response:
        return controller.get_weather_by_city(city_name)

    @app.get('/weather')
    def get_weather_list() -> Response:
        return controller.get_weather_list(args=request.args)
        