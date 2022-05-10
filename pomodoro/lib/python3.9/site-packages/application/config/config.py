from pathlib import Path


__all__ = ["ROOT","config","DOTENV"]


ROOT = Path(__file__).parent.parent.parent
DB_PATH = ROOT.joinpath("application.db")
DOTENV = ROOT.joinpath(".env")


class Base:
    DEBUG = True
    SORT_JSON_KEYS = False
    JSON_AS_ASCII = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Dev(Base):
    pass


class Pro(Base):
    DEBUG = False


config = {
    "dev":Dev,
    "pro":Pro
}