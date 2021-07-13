import requests
from app.utils import get_api_url


def get_weather_by_city_service(city_name: str) -> dict:
    API_URL = get_api_url(param=city_name)
    data = requests.get(API_URL).json()
    return data


def save_to_cache(data: dict) -> None:
    pass


def load_from_cache(max_number) -> list:
    return []
