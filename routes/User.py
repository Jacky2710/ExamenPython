from flask import Blueprint, request, jsonify
from controllers.userController import users, crear, login

user_bp = Blueprint('users', __name__)

@user_bp.route('/users', methods=['GET'])
def index():
    return users()

@user_bp.route('/users/create', methods=['POST'])
def create():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    return crear(name, email, password)

@user_bp.route('/users/login', methods=['POST'])
def login_route():
    data = request.get_json()
    return login(data['email'], data['password'])
