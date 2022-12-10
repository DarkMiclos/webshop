from ..extensions import db

class Product(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String)
  price = db.Column(db.Integer)
  description = db.Column(db.String)