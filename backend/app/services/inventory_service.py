from app.models.inventory_item import InventoryItem
from app.utils.db import mongo
from bson import ObjectId


class InventoryService:

    @staticmethod
    def get_all_inventory():
        items = mongo.db.inventario.find()
        return [InventoryService.to_dict(item) for item in items]

    @staticmethod
    def add_inventory_item(data):
        item = InventoryItem.from_dict(data)
        result = mongo.db.inventario.insert_one(item.to_dict())
        return InventoryService.to_dict(mongo.db.inventario.find_one({"_id": result.inserted_id}))

    @staticmethod
    def update_inventory_item(item_id, data):
        status = data.get('status')
        if status is not None:
            mongo.db.inventario.update_one(
                {'_id': ObjectId(item_id)},
                {'$set': {'status': status}}
            )
        return InventoryService.to_dict(mongo.db.inventario.find_one({'_id': ObjectId(item_id)}))

    @staticmethod
    def to_dict(item):
        item['_id'] = str(item['_id'])
        return item
