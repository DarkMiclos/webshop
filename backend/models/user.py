from ..extensions import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key = True)
  user_name = db.Column(db.String)
  password = db.Column(db.String)
  role = db.Column(db.String)