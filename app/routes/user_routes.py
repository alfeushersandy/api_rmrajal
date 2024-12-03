from flask import Blueprint, request
from app.controller.user import UserController

user_bp = Blueprint('user', __name__)
controller = UserController()


@user_bp.route('/', methods=['GET'])
def index():
    return controller.index()

@user_bp.route('/login', methods=['POST'])
def login():
    return controller.login()


