from unittest import TestCase
from app.api.services import load_all_from_cache, load_from_cache, save_to_cache


def test_save_to_cache(app, data):
    save_to_cache(data)
    cached = app.cache.get(data.get('sys', {}).get('id'))
    TestCase().assertDictEqual(cached, data)


def test_load_from_cache(app, data):
    key = data.get('sys', {}).get('id')
    app.cache.set(key=key, value=data)
    loaded = load_from_cache(key)
    TestCase().assertDictEqual(data, loaded)


def test_load_all_from_cache(app, data):
    save_to_cache(data)
    loaded = load_all_from_cache(5)
    TestCase().assertDictEqual(data, loaded.get('data', [])[0])
