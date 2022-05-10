from flask_apscheduler import APScheduler
from flask_apscheduler.scheduler import BackgroundScheduler
from flask import Flask

scheduler = APScheduler(scheduler=BackgroundScheduler(timezone="Asia/Shanghai"))


def init_apscheduler(app:Flask):
    scheduler.init_app(app)
    scheduler.start()


