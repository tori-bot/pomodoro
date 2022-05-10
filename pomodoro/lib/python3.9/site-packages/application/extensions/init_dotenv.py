from dotenv import load_dotenv
from flask import Flask
from application.config import DOTENV


def init_dotenv():
    if DOTENV.exists():
        load_dotenv(DOTENV)
    else:
        print(f"{DOTENV} not found !")
        print(f"starting create {DOTENV}...")
        with open(DOTENV,"w")as f:
            f.write("")