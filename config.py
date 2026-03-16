import os
from urllib.parse import quote_plus

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Blob Storage
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT')
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER')
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')

    # SQL Server
    SQL_SERVER = os.environ.get('SQL_SERVER')
    SQL_DATABASE = os.environ.get('SQL_DATABASE')
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD')

    encoded_password = quote_plus(SQL_PASSWORD)

    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER_NAME}:{encoded_password}@{SQL_SERVER}:1433/"
        f"{SQL_DATABASE}"
        "?driver=ODBC+Driver+18+for+SQL+Server"
        "&Encrypt=yes"
        "&TrustServerCertificate=no"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    AUTHORITY = "https://login.microsoftonline.com/common"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"