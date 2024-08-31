from app.utils.db import mongo


class InventoryItem:
    def __init__(self, id_producto, cantidad, estado):
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.estado = estado

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "cantidad": self.cantidad,
            "estado": self.estado
        }

    @staticmethod
    def from_dict(data):
        return InventoryItem(
            id_producto=data.get('id_producto'),
            cantidad=data.get('cantidad'),
            estado=data.get('estado')
        )
