import os
import requests
import json

from flask import Flask, render_template
from dotenv import dotenv_values

env_values = dotenv_values('.env')
#API_KEY = env_values['API_KEY']

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = 'I am the one who knocks'

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

    # @app.route('/')
    # def home():
    #     # Need to get user location and input that as latitude and longitude 

    #     # return f"Current Temp is {round(data['main']['temp'] - 273)}°C
    #     return render_template('index.html')

    # return app

    # New Content!

    # flask --app flaskr --debug run

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app