from flask import Blueprint, request, jsonify, session, make_response
from ..models.user import User
from ..extensions import db
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
  print(request.json)
  data = request.json
  user_name = data['username']
  password = data['password']
  user = User.query.filter_by(user_name = user_name, password = password).first()
  if not user and not check_password_hash(user.password, password):
    return "Invalid credentials."
  login_user(user)
  # token = jwt.encode({'username': user.user_name, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, "mysecret", algorithm="HS256")
  # response = make_response()
  # response.set_cookie('jwt', token, samesite="Strict", expires=datetime.datetime.utcnow() + datetime.timedelta(days=7), httponly=True, path='/', domain="127.0.0.1")
  print(current_user)
  return jsonify({
    'username': current_user.user_name,
    'is_authenticated': current_user.is_authenticated,
    'role': current_user.role
  })

@auth.route('/register', methods=['POST'])
def register():
  data = request.json
  user_name = data['username']
  password = data['password']
  user = User(user_name = user_name, password = generate_password_hash(password, method='sha256'), role = "USER")
  db.session.add(user)
  db.session.commit()
  return '', 201

@auth.route('/logout', methods=['POST'])
def logout():
  logout_user()
  return jsonify({
    'is_authenticated': current_user.is_authenticated
  })