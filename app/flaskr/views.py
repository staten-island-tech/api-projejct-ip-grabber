from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import User
import requests
from .data import *

views = Blueprint('views', __name__)

api_key = '57fc3439dc46a8578604c33691f100e3'

@views.route('/')
@login_required
def home():
    return render_template('index.html', user=current_user)

# @views.route('/forecast/<location>', methods=['GET', 'POST'])
# @login_required
# def forecast(location):
#     if location == 'local':
#         forecast = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={current_user.lat}&lon={current_user.long}&appid={api_key}').json()
#         print(forecast)
#         return render_template('local_weather.html', user=current_user, forecast=forecast)
#     else: 
#         return render_template('weather.html', location=location, user=current_user, locationConverter=locationConverter)

@views.route('/forecast/<location>', methods=['GET', 'POST'])
@login_required
def forecast(location):
    if request.method == 'POST':
        city_code = request.form.get('search')
        state_code = 'TX'
        country_code = 'US'
        locationConverter = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_code},{state_code},{country_code}&limit=5&appid={api_key}').json()
        print(locationConverter, city_code)
        for x in locationConverter['main']:
            lat = x['lat']
            lon = x['lon']
        print(lat, lon)
        currentWeather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}').json()
        print(currentWeather)
        for x in currentWeather:
            temp = x['temp']
        print(temp)
        return render_template('weather.html', user=current_user, forecast=forecast, locationConverter=locationConverter, currentWeather=currentWeather)
    else: 
        return render_template('weather.html', location=location, user=current_user)

# ADD GEOAPIFY API