import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'MYSQL_DATABASE_URI', 'mysql+pymysql://admin:Andrewseigokan9*@inventario-instance.chq24qc2yds6.us-east-1.rds.amazonaws.com:3306/inventario_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://ramirezandrew172:6puGhj5eE3CAgc5s@inventario-clu.zhdb5.mongodb.net/inventario_db?retryWrites=true&w=majority&appName=inventario-clu')
