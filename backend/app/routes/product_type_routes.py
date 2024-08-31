from flask import Blueprint, request, jsonify
from app.services.product_type_service import ProductTypeService

product_type_bp = Blueprint('product_type', __name__)


@product_type_bp.route('/', methods=['GET'])
def get_product_types():
    return jsonify(ProductTypeService.get_all_product_types())


@product_type_bp.route('/', methods=['POST'])
def create_product_type():
    data = request.get_json()
    return ProductTypeService.create_product_type(data)
