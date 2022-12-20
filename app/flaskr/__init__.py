import os
import requests
import json

from flask import Flask, render_template, request, redirect
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

    user_location = {}

    @app.route('/set_location', methods=['POST', 'GET'])
    def set_location():
        if request.method == 'POST':
            raw_data = request.data.decode('utf-8')
            data = json.loads(raw_data)
            # print(f'Lat: {data.lat}, Long: {data.long}')
            return 'hi'
        else:
            return redirect('/')

    @app.route('/')
    def home():
        # Need to get user location and input that as latitude and longitude 

        # return f"Current Temp is {round(data['main']['temp'] - 273)}°C
        return render_template('index.html')

    return app