import os 
from flask import Flask, request
from app.config.database import Database
from app.routes.user_routes import user_bp
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    # CORS(app)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # konfigurasi database 
    db = Database()

    # inisiasi user
    app.register_blueprint(user_bp, url_prefix='/user')

    @app.before_request
    def lowercase_path():
        request.path = request.path.lower()



    return app