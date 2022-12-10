from flask import Blueprint, request, jsonify
from ..models.user import User
from ..extensions import db
from flask_login import login_user

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def login_user():
  data = request.get_json()
  user_name = data['user_name']
  password = data['password']
  user = User.query.filter_by(user_name = user_name, password = password).first()
  login_user(user)
  return jsonify({
    'user_name': user.user_name,
    'role': user.role
  })