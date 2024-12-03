import os 
from flask import Flask, request, jsonify
from app.config.database import Database
from app.routes.user_routes import user_bp
from flask_cors import CORS
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)

    CORS(app)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    # Konfigurasi JWT
    app.config['JWT_SECRET_KEY'] = '6a5cdea88eb45d863620bfa73b6ef87039cc2fe845085a7a20cf6a5dcf0e11785711fee83927eae023ec37e4b0d41b471397c6b1b5138a2ece65e27d78f866d6'  # Ganti dengan kunci rahasia yang kuat
    jwt = JWTManager(app)

    @jwt.unauthorized_loader
    def unauthorized_response(callback):
        return jsonify({
            'msg': 'Authorization header is missing or invalid. Please provide a valid token.'
        }), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({
            'msg': 'Invalid token. Please log in again.'
        }), 401

    @jwt.expired_token_loader
    def expired_token_callback(error):
        return jsonify({
            'msg': 'Token has expired. Please log in again.'
        }), 401


    # konfigurasi database 
    db = Database()

    # inisiasi user
    app.register_blueprint(user_bp, url_prefix='/user')

    @app.before_request
    def lowercase_path():
        request.path = request.path.lower()



    return app