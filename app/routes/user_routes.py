from flask import Blueprint
from app.controller.user import UserController

user_bp = Blueprint('user', __name__)
controller = UserController()

user_bp.route('/', methods=['GET'])(controller.index)

