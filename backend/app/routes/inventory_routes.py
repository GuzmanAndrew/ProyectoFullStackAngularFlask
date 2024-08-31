from flask import Blueprint, request, jsonify
from app.services.inventory_service import InventoryService

inventory_bp = Blueprint('inventory', __name__)


@inventory_bp.route('/all', methods=['GET'])
def get_inventory():
    try:
        return jsonify(InventoryService.get_all_inventory())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@inventory_bp.route('/create', methods=['POST'])
def add_inventory_item():
    try:
        data = request.get_json()
        return InventoryService.add_inventory_item(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@inventory_bp.route('/update/<item_id>', methods=['PUT'])
def update_inventory_item(item_id):
    try:
        data = request.get_json()
        return InventoryService.update_inventory_item(item_id, data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
