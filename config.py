import os

class Config:
    SECRET_KEY = 'your_super_secret_key'
    SQLALCHEMY_DATABASE_URI = (
        r"mssql+pyodbc://DynamTech:DynamTech@11.0.0.10\DYNAMTECH"
        r"/ACM?driver=SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
