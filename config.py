class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin023:0000@localhost/pomo'


class DevConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin023:0000@localhost/pomo'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin023:0000@localhost/pomo'


config_options={
    'development':DevConfig,
    'production':ProdConfig,
}