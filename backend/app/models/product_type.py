from app.utils.db import db


class ProductType(db.Model):
    __tablename__ = 'productos'

    id_producto = db.Column(db.Integer, primary_key=True)
    nombre_producto = db.Column(db.String(100), nullable=False)
    codigo_unico = db.Column(db.String(100), nullable=False)
