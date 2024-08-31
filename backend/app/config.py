import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'MYSQL_DATABASE_URI', 'mysql+pymysql://admin:Andrewseigokan9*@product-db.c9kkkoim4kom.us-east-1.rds.amazonaws.com:3306/inventario_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://ramirezandrew172:G3FWuPqdVfnTVX43@inventario-clu.jnk1e.mongodb.net/inventario_db?retryWrites=true&w=majority&appName=inventario-clu')
