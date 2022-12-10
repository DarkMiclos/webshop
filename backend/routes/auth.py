from flask import Blueprint, request, jsonify
from ..models.user import User
from ..extensions import db
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  user_name = data['user_name']
  password = data['password']
  user = User.query.filter_by(user_name = user_name, password = password).first()
  if not user and not check_password_hash(user.password, password):
    return "Invalid credentials."
  login_user(user)
  return jsonify({
    'user_name': user.user_name,
    'role': user.role
  })

@auth.route('/register', methods=['POST'])
def register():
  data = request.get_json()
  user_name = data['user_name']
  password = data['password']
  user = User(user_name = user_name, password = generate_password_hash(password, method='sha256'), role = "USER")
  db.session.add(user)
  db.session.commit()
  return '', 201

@auth.route('/logout', methods=['POST'])
def logout():
  logout_user()
  return "Successfuly logged out."