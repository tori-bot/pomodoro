import click
from flask import Flask
import argparse
import os


def args():
    p = argparse.ArgumentParser()
    p.add_argument("--port",type=int,default=5000,help="port of server",required=False)
    return p.parse_args()


@click.command("start")
def run():
    os.system(f"waitress-serve --port=5000 application:create_app")


def init_cli(app:Flask):
    app.cli.add_command(run)