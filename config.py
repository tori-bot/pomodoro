import os
class Config:
   SQLALCHEMY_DATABASE_URI=os.environ.get ( 'DATABASE_URI')
   SECRET_KEY = os.environ.get('SECRET_KEY')
    

class DevConfig(Config):
    
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin023:0000@localhost/pomo'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin023:0000@localhost/pomo'


config_options={
    'development':DevConfig,
    'production':ProdConfig,
}