import os


class Config():
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI')
    SECRET_KEY=os.environ.get('SECRET_KEY')

class DevConfig(Config):
    DEBUG=True

class ProdConfig(Config):
    pass

config_options={
    'development':DevConfig,
    'production':ProdConfig,
}