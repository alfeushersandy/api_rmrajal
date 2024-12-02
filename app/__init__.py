import os 
from flask import Flask 
from app.config.database import Database
from app.routes.user_routes import user_bp


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # konfigurasi database 
    db = Database()

    # inisiasi user
    app.register_blueprint(user_bp, url_prefix='/user')

    return app