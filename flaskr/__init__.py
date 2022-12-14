import os
import requests

from flask import Flask
from dotenv import dotenv_values

env_values = dotenv_values('.env')
API_KEY = env_values['API_KEY']

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

    # a simple page that says hello
    @app.route('/')
    def current_temp():
        # Need to get user location and input that as latitude and longitude
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat=30&lon=30&appid={API_KEY}')
        data = response.json()
        print(data)

        return f"Current Temp is {round(data['main']['temp'] - 273)}°C"

    return app