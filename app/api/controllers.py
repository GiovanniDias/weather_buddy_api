from flask import json, make_response, Response, jsonify
from werkzeug.exceptions import InternalServerError
from app.utils import get_status_code
from ..api.services import get_weather_by_city_service, load_from_cache, save_to_cache

class WeatherController:
    def get_weather_by_city(city_name: str) -> Response:
        try:
            data = get_weather_by_city_service(city_name)
            status_code = get_status_code(data)
            response = make_response(jsonify(data), status_code)
            
            if status_code == 200:
                save_to_cache(data)
            
            response.headers['Content-Type'] = 'application/json'
            return response

        except InternalServerError as e:
            print(e)

    def get_weather_list(args: dict) -> Response:
        max_number = args.get('max_number')
        if max_number is None:
            max_number = 5

        try:
            status_code = 200
            data = load_from_cache(max_number)
            response = make_response(jsonify(data), status_code)
            response.headers['Content-Type'] = 'application/json'    
            return response
        
        except InternalServerError as e:
            print(e)
