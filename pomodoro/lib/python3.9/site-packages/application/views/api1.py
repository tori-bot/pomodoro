from flask import Blueprint


api1 = Blueprint("api1",__name__)


@api1.get("/")
def hello():
    return "hello world"