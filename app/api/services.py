import requests
from datetime import datetime
from flask import current_app
from app.utils import get_api_url


def get_weather_by_city_service(city_name: str) -> dict:
    API_URL = get_api_url(param=city_name)
    data = requests.get(
        url=API_URL,
        headers={
            'Content-Type': 'application/json',
        }
    ).json()
    return data


def save_to_cache(data: dict, timeout: int = 300) -> None:
    key = data.get('sys', {}).get('id')
    data['fetched_at'] = datetime.now()
    current_app.cache.set(key=key, value=data, timeout=timeout)


def load_from_cache(key: str) -> list:
    return current_app.cache.get(key=key)
    

def load_all_from_cache(max_number) -> list:
    field = 'fetched_at'
    cache = current_app.cache
    
    keys = list(filter(
        lambda item: isinstance(cache.get(item), dict),
        cache.cache._cache
    ))
    cached_items = [cache.get(key) for key in keys if key is not None]

    data = {"data": sorted(cached_items, key=lambda x: x[field], reverse=True)[:max_number]}
        
    return data