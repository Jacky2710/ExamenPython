from flask import Blueprint, request, jsonify
from controllers.userController import users, crear, login

user_bp=Blueprint('users', __name__)

@user_bp.route('/', methods=['GET'])
def index():
    user = users()
    return jsonify(user)

@user_bp.route('/crear', methods=['POST'])
def create():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    new= crear(name, email, password)
    return jsonify(new)





@user_bp.route('/login', methods=['POST'])
def login():
    data=request.get_json()
    return login(data['email'], data['password'])