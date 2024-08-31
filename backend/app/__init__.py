from flask import Flask
from flask_cors import CORS
from app.utils.db import init_db, init_mongo
from app.routes.product_type_routes import product_type_bp
from app.routes.inventory_routes import inventory_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    CORS(app)

    init_db(app)
    init_mongo(app)

    app.register_blueprint(product_type_bp, url_prefix='/api/product-types')
    app.register_blueprint(inventory_bp, url_prefix='/api/inventory')

    @app.after_request
    def add_security_headers(response):
        response.headers[
            'Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'"
        return response

    return app
