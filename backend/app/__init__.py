from flask import Flask
from app.utils.db import init_db, init_mongo
from app.routes.product_type_routes import product_type_bp
from app.routes.inventory_routes import inventory_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    init_db(app)
    init_mongo(app)

    app.register_blueprint(product_type_bp, url_prefix='/api/product-types')
    app.register_blueprint(inventory_bp, url_prefix='/api/inventory')

    return app
