from flask import Blueprint, request, jsonify
from app.services.inventory_service import InventoryService

inventory_bp = Blueprint('inventory', __name__)


@inventory_bp.route('/', methods=['GET'])
def get_inventory():
    return jsonify(InventoryService.get_all_inventory())


@inventory_bp.route('/', methods=['POST'])
def add_inventory_item():
    data = request.get_json()
    return InventoryService.add_inventory_item(data)


@inventory_bp.route('/<item_id>', methods=['PUT'])
def update_inventory_item(item_id):
    data = request.get_json()
    return InventoryService.update_inventory_item(item_id, data)
