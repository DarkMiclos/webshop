from ..extensions import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  user_name = db.Column(db.String)
  password = db.Column(db.String)
  role = db.Column(db.String)