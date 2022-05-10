from flask import Flask
from application.config import ROOT,config
from application.extensions import init_extensions
from application.views import init_views


def create_app(e="dev"):
    app = Flask(ROOT.__str__())

    # config
    app.config.from_object(config.get(e))

    #extensions
    init_extensions(app)

    #views
    init_views(app)

    return app