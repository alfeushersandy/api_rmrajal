from flask import request, jsonify
from app.model.user import UserModel
from app.utils.convert import convert_pass

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
            return jsonify({f'error': str(e)}), 500
        
    def get_user_by_username(self, username):
        try:
            user = self.model.get_user(username)
            return user
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        
    def verify_password(self, password, username):
       user = self.get_user_by_username(username)
       if user:
            decrypted_password = convert_pass(user['vc_password'], "D")
            return decrypted_password == password
       return False
    
    def login(self):
        try:
            # Ambil data dari request
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')

            # Validasi login
            if not username or not password:
                return jsonify({'message': 'Username and password are required'}), 400

            user = self.get_user_by_username(username)
            if user and self.verify_password(password, username):
                return jsonify({
                    'message': 'Login successfully',
                    'user': {
                        'username': user['vc_username']
                    }
                }), 200
            else:
                return jsonify({'message': 'Invalid username or password'}), 401
        except Exception as e:
            return jsonify({'error': str(e)}), 500
