from flask_caching import Cache


def init_app(app):
    Cache(app, config={'CACHE_TYPE': 'SimpleCache'})
