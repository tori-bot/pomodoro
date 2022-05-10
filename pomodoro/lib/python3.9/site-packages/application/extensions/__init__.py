from .init_cli import init_cli
from .init_sqlalchemy import init_sqlalchemy,db,migrate
from .init_dotenv import init_dotenv
from .init_apscheduler import init_apscheduler
from flask import Flask



def init_extensions(app:Flask):
    init_cli(app)
    init_sqlalchemy(app)
    init_dotenv()
    init_apscheduler(app)