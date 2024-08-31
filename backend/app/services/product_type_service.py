from app.models.product_type import ProductType
from app.utils.db import db


class ProductTypeService:

    @staticmethod
    def get_all_product_types():
        product_types = ProductType.query.all()
        return [ProductTypeService.to_dict(pt) for pt in product_types]

    @staticmethod
    def create_product_type(data):
        new_product_type = ProductType(
            nombre_producto=data['nombre_producto'],
            codigo_unico=data.get('codigo_unico')
        )
        db.session.add(new_product_type)
        db.session.commit()
        return ProductTypeService.to_dict(new_product_type)

    @staticmethod
    def to_dict(product_type):
        return {
            "id_producto": product_type.id_producto,
            "nombre_producto": product_type.nombre_producto,
            "codigo_unico": product_type.numero_serie
        }
