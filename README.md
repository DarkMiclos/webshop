# webshop
* To run the program create a python virtual environment: 
```
cd backend
python -m venv env
```

* Run the virtual environment

* Have nodejs and python installed.

* Run this in the virtual environment:
```
pip install flask, flask_sqlalchemy, flask_login, flask_admin, flask_cors, python_dotenv, stripe
```

* On the first run create the tables like this in app.py:
```
with app.app_context():
  db.create_all()
  db.session.add(User(user_name = 'admin', password = 'admin', role = 'ADMIN'))
  db.session.commit()
```

Create a .env file in the backend directory and write your stripe secret key into it:
```
STRIPE_SECRET=value
```

* Run the backend server with:
```
flask run
```

* On the frontend install the npm packages:
```
npm i
```

* Run the frontend server:
```
npm run dev
```

* Now both the backend and frontend should be running, access the frontend on: 127.0.0.1:5173/
