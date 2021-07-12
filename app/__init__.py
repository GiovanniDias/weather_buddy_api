from flask import Flask, make_response, Response, jsonify, request
from flask_cors import CORS
from dynaconf import FlaskDynaconf
from werkzeug.exceptions import InternalServerError

app_name = 'Weather Buddy API'

def create_app(**config):
    app = Flask(__name__)

    FlaskDynaconf(app, **config)
    
    # TODO: Set api endpoints
    @app.get('/')
    def index():
        return app_name

    @app.route('/weather', methods=['GET'])
    def get_weather_cached_list():
        args = request.args
        max_number = args.get('max_number')
        if max_number is None:
            max_number = 5

        # TODO: get data from cache
        # data = rerieve_cached_data()
        data = []

        try:
            if data:
                status_code = 200
                result = jsonify(data)
                response = make_response(result, status_code)
            else:
                status_code = 404
                response = Response(status=status_code)
                response.headers['Content-Type'] = 'application/json'    
        
        except InternalServerError:
            status_code = 500
            response = Response(status=status_code)
            response.headers['Content-Type'] = 'application/json'
        
        finally:
            return response

    @app.route('/weather/<city_name>', methods=['GET'])
    def get_weather_by_city(city_name):
        
        # TODO: get weather data of city_name
        # api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
        data = {}

        try:
            if data:
                status_code = 200
                result = jsonify(data)
                response = make_response(result, status_code)
            else:
                status_code = 404
                response = Response(status=status_code)
                response.headers['Content-Type'] = 'application/json'
        
        except InternalServerError:
            status_code = 500
            response = Response(status=status_code)
            response.headers['Content-Type'] = 'application/json'
        
        finally:
            return response

    CORS(app)


    return app