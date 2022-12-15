from flask import Flask, session, Response, make_response, request, jsonify

from .models.user import User
from .extensions import db
from .routes.auth import auth
from .routes.product import product_routes
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from .models.product import Product
from flask_login import current_user, LoginManager, login_required
from flask_cors import CORS, cross_origin
from flask.sessions import SecureCookieSessionInterface
from dotenv import load_dotenv, find_dotenv
import stripe
import os

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SESSION_COOKIE_SAMESITE'] = "None"
app.config['SESSION_COOKIE_SECURE'] = 'Secure'

app.register_blueprint(auth)
app.register_blueprint(product_routes)

db.init_app(app)

login_manager = LoginManager(app)
login_manager.init_app(app)

session_cookie = SecureCookieSessionInterface().get_signing_serializer(app)

# @app.after_request
# def cookies(response):
#     same_cookie = session_cookie.dumps(dict(session))
#     response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
#     response.set_cookie('session', value="cookie_value", domain='127.0.0.1', samesite="None", secure="Secure")
#     response.headers.add("Set-Cookie", f"session={same_cookie}; Secure; HttpOnly; SameSite=None; Path=/;")
#     return response

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class MyModelView(ModelView):
  def is_accessible(self):
    return True
    # return current_user.is_authenticated and current_user.role == "ADMIN"

class MyAdminIndexView(AdminIndexView):
  def is_accessible(self):
    return True
    # return current_user.is_authenticated and current_user.role == "ADMIN"

admin = Admin(app, index_view=MyAdminIndexView())
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Product, db.session))

load_dotenv(find_dotenv())

stripe.api_key = os.getenv('STRIPE_SECRET')

#We can check by calling this from the front end if the backend is live
@app.route('/')
def initialize():
  return '', 204

@app.route('/stripe-checkout', methods=['POST'])
def checkout():
  data = request.json
  name = data["name"]
  amount = data["amount"] * 100
  try:
    checkout_session = stripe.checkout.Session.create(
      payment_method_types=['card'],
      line_items=[
        {
          'name': name,
          'quantity': 1,
          "currency": "usd",
          "amount": amount
        },
      ],
      mode='payment',
      success_url="http://127.0.0.1:5173/",
      cancel_url="http://127.0.0.1:5173/",
    )
  except Exception as e:
      return jsonify(error=str(e)), 403

  return jsonify({"url": checkout_session["url"]})


@app.route('/authenticate', methods=['POST'])
@login_required
def authenticate():
  if(current_user.is_authenticated):
    return jsonify({
      'is_authenticated': current_user.is_authenticated,
      'role': current_user.role
    })
  return jsonify({
    'is_authenticated': current_user.is_authenticated
  })

#Creates database and initializes it with admin user.
# with app.app_context():
#   db.create_all()
#   db.session.add(User(user_name = 'admin', password = 'admin', role = 'ADMIN'))
#   db.session.commit()