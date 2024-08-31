import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'MYSQL_DATABASE_URI', 'mysql+pymysql://root:Andrewseigokan9*@localhost/inventario_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/inventario_db')
