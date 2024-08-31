from bson import ObjectId


class InventoryItem:
    def __init__(self, usuario, nombre_producto, numero_serie, fecha_entrega, status):
        self.usuario = usuario
        self.nombre_producto = nombre_producto
        self.numero_serie = numero_serie
        self.fecha_entrega = fecha_entrega
        self.status = status

    def to_dict(self):
        return {
            "usuario": self.usuario,
            "nombre_producto": self.nombre_producto,
            "numero_serie": self.numero_serie,
            "fecha_entrega": self.fecha_entrega,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return InventoryItem(
            usuario=data.get('usuario'),
            nombre_producto=data.get('nombre_producto'),
            numero_serie=data.get('numero_serie'),
            fecha_entrega=data.get('fecha_entrega'),
            status=data.get('status')
        )
