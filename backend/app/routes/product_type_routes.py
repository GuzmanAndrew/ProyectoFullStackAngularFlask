from flask import Blueprint, request, jsonify
from app.services.product_type_service import ProductTypeService

product_type_bp = Blueprint('product', __name__)


@product_type_bp.route('/all', methods=['GET'])
def get_product_types():
    try:
        return jsonify(ProductTypeService.get_all_product_types())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@product_type_bp.route('/create', methods=['POST'])
def create_product_type():
    try:
        data = request.get_json()
        return ProductTypeService.create_product_type(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
