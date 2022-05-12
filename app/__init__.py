from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


db=SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()

def create_app(config_name):

    app=Flask(__name__)

    # Creating the apponfigurations

    app.config.from_object(config_options[config_name])

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    

    
    db.init_app(app)

    return app
