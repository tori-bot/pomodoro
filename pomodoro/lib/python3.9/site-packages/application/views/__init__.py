from .api1 import api1
from flask import Flask


def init_views(app:Flask):
    app.register_blueprint(api1)