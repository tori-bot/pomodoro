from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from  flask import Flask


db = SQLAlchemy()
migrate = Migrate(db=db)


def init_sqlalchemy(app:Flask):
    db.init_app(app)
    migrate.init_app(app)
