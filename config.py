import os


class Config():
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI')

class DevConfig(Config):
    DEBUG=True

class ProdConfig(Config):
    pass

config_options={
    'development':DevConfig,
    'production':ProdConfig,
}