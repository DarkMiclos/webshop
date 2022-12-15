from flask import Blueprint, request, jsonify
from ..models.product import Product
from ..extensions import db
from flask_login import login_required

product_routes = Blueprint('product_routes', __name__)

@product_routes.route('/create_product', methods=['POST'])
@login_required
def create_product():
  data = request.get_json()
  name = data['name']
  price = data['price']
  description = data['description']
  created_product = Product(name = name, price = price, description = description)
  db.session.add(created_product)
  db.session.commit()
  return '', 201

@product_routes.route('/update_product', methods=['POST'])
@login_required
def update_product():
  data = request.get_json()
  id = data['id']
  name = data['name']
  price = data['price']
  description = data['description']
  get_product = Product.query.filter_by(id = id).first()
  get_product.name = name
  get_product.price = price
  get_product.description = description
  db.session.commit()
  return '', 200

@product_routes.route('/delete_product', methods=['POST'])
@login_required
def delete_product():
  data = request.get_json()
  id = data['id']
  Product.query.filter_by(id = id).delete()
  db.session.commit()
  return '', 200

@product_routes.route('/get_products', methods=['GET'])
def get_products():
  products = Product.query.all()
  return jsonify(products=[i.serialize for i in products])