import os


class Config():
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:okunzo254@localhost/pomodoro'
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLACHEMY_TRACK_MODIFICATIONS=False

class DevConfig(Config):
    DEBUG=True

class ProdConfig(Config):
    pass

config_options={
    'development':DevConfig,
    'production':ProdConfig,
}