import os
from urllib.parse import quote_plus


class Config:

    # Flask security key
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")

    # Azure Blob Storage settings
    STORAGE_ACCOUNT = os.environ.get("BLOB_ACCOUNT", "cmsstorage")
    STORAGE_CONTAINER = os.environ.get("BLOB_CONTAINER", "images")
    STORAGE_KEY = os.environ.get("BLOB_STORAGE_KEY")

    # Azure SQL database settings
    DB_SERVER = os.environ.get("SQL_SERVER")
    DB_NAME = os.environ.get("SQL_DATABASE")
    DB_USERNAME = os.environ.get("SQL_USER_NAME")
    DB_PASSWORD = os.environ.get("SQL_PASSWORD")

    # Encode password safely for connection string
    ENCODED_PASSWORD = quote_plus(DB_PASSWORD) if DB_PASSWORD else ""

    # SQLAlchemy connection string
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{DB_USERNAME}:{ENCODED_PASSWORD}@{DB_SERVER}:1433/"
        f"{DB_NAME}"
        "?driver=ODBC+Driver+18+for+SQL+Server"
        "&Encrypt=yes"
        "&TrustServerCertificate=no"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Microsoft authentication settings
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    AUTHORITY = "https://login.microsoftonline.com/common"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]

    # Session storage type
    SESSION_TYPE = "filesystem"