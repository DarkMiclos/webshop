from flask import Flask

from .models.user import User
from .extensions import db
from .routes.auth import auth
from .routes.product import product_routes
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from .models.product import Product
from flask_login import current_user, LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

app.register_blueprint(auth)
app.register_blueprint(product_routes)

db.init_app(app)

login_manager = LoginManager(app)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class MyModelView(ModelView):
  def is_accessible(self):
    return current_user.is_authenticated and current_user.role == "ADMIN"

class MyAdminIndexView(AdminIndexView):
  def is_accessible(self):
    return current_user.is_authenticated and current_user.role == "ADMIN"

admin = Admin(app, index_view=MyAdminIndexView())
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Product, db.session))

#We can check by calling this from the front end if the backend is live
@app.route('/')
def initialize():
  return '', 204

#Creates database and initializes it with admin user.
# with app.app_context():
#   db.create_all()
#   db.session.add(User(user_name = 'admin', password = 'admin', role = 'ADMIN'))
#   db.session.commit()