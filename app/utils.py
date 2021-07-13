from flask import current_app

def get_api_url(param: str) -> str:
    base_url = current_app.config.EXTERNAL_API_URL
    api_key = current_app.config.API_KEY
    API_URL = f"{base_url}?q={param}&appid={api_key}"
    return API_URL

def get_status_code(data: dict) -> int:
    return data.get('cod')