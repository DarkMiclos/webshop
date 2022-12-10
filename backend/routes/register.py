from flask import Blueprint, request
from ..models.user import User
from ..extensions import db

register = Blueprint('register', __name__)

@register.route('/register', methods=['POST'])
def register_user():
  data = request.get_json()
  user_name = data['user_name']
  password = data['password']
  user = User(user_name = user_name, password = password, role = "USER")
  db.session.add(user)
  db.session.commit()
  return data