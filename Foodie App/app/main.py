from flask import Flask
from app.restaurant import restaurant_bp
from app.dish import dish_bp
from app.admin import admin_bp
from app.user import user_bp
from app.order import order_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(restaurant_bp)
    app.register_blueprint(dish_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(order_bp)

    return app