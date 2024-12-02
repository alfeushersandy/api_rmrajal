from flask import Blueprint, request
from app.controller.user import UserController

user_bp = Blueprint('user', __name__)
controller = UserController()

# Decorator untuk membuat route case-insensitive
def lowercase_route(f):
    def wrapper(*args, **kwargs):
        # Mengubah path menjadi lowercase
        request.path = request.path.lower()
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper


@user_bp.route('/', methods=['GET'])
@lowercase_route
def index():
    return controller.index()

