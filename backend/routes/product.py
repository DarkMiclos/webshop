from flask import Blueprint, request, jsonify
from ..models.product import Product
from ..extensions import db

product_routes = Blueprint('product_routes', __name__)

@product_routes.route('/create_product', methods=['POST'])
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
def update_product():
  data = request.get_json()
  name = data['name']
  price = data['price']
  description = data['description']
  get_product = Product.query.filter_by(name = name).first()
  get_product.price = price
  get_product.description = description
  db.session.commit()
  return '', 200

@product_routes.route('/delete_product', methods=['POST'])
def delete_product():
  data = request.get_json()
  name = data['name']
  Product.query.filter_by(name = name).delete()
  db.session.commit()
  return '', 200

@product_routes.route('/get_products', methods=['GET'])
def get_products():
  products = Product.query.all()
  return jsonify(products=[i.serialize for i in products])