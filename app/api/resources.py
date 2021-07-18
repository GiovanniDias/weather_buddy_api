from flask import Response, request
from .controllers import WeatherController as controller


def init_app(app):
    @app.route('/')
    def index():
        return app.config.APP_NAME

    @app.get('/weather/<city_name>')
    @app.cache.cached()
    def get_weather_by_city(city_name: str) -> Response:
        return controller.get_weather_by_city(city_name)

    @app.route('/weather', methods=['GET'])
    def get_weather_cached_list() -> Response:
        return controller.get_weather_list(args=request.args)
        