import os
import requests
import json

from flask import Flask, render_template
from dotenv import dotenv_values

# New imports
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


env_values = dotenv_values('.env')
#API_KEY = env_values['API_KEY']

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def get_user_location(ip_address):
        print(ip_address)
        response = requests.get(f"http://ip-api.com/json/{ip_address}")        
        print(response.text)

    # flask --app flaskr --debug run

    # New code

    db = SQLAlchemy(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.confic['SECRET_KEY'] = 'test'
    db.init_app(app)

    class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(20), nullable=False)
        password = db.Column(db.String(80), nullable=False)

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/register')
    def register():
        return render_template('register.html')

    return app