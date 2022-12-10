from flask import Flask

from .models.user import User
from .extensions import db
from .routes.register import register
from .routes.login import login

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

app.register_blueprint(register)
app.register_blueprint(login)

db.init_app(app)

#We can check by calling this from the front end if the backend is live
@app.route('/')
def initialize():
  return '', 204

#Creates database and initializes it with admin user.
with app.app_context():
  db.create_all()
  db.session.add(User(user_name = 'admin', password = 'admin', role = 'ADMIN'))
  db.session.commit()