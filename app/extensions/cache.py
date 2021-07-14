from flask_caching import Cache


def init_app(app):
    cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache', 'CACHE_DEFAULT_TIMEOUT': 500})
    app.cache = cache

