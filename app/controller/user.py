from flask import request, jsonify
from app.model.user import UserModel

class UserController:
    def __init__(self):
        self.model = UserModel()

    def index(self):
        try: 
            user = self.model.get_all_user()
            return jsonify({
                    'data': [
                                {
                                    'id' : row.vc_id,
                                } for row in user 
                        ]
                    }
                ), 200
        except Exception as e:
            return jsonify(f'error: {e}'), 500