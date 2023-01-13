from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import User
import requests
from .data import *


views = Blueprint('views', __name__)

api_key = '57fc3439dc46a8578604c33691f100e3'
months = {
    '1': 'Jan', '2': 'Feb', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'Aug', '9': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
}
def convertTimeToDate(time):
    month = months[str(int(time[6:7]))]
    day = time[7:9]
    date = month + day
    return date

@views.route('/')
@login_required
def home():
    return render_template('index.html', user=current_user)

@views.route('/forecast/<location>', methods=['GET', 'POST'])
@login_required
def forecast(location):
    if location == 'local':
        forecast = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={current_user.lat}&lon={current_user.long}&appid={api_key}').json()
        return render_template('local_weather.html', user=current_user, forecast=forecast, round=round, convertTimeToDate=convertTimeToDate)
    else: 
        return render_template('weather.html', location=location, user=current_user, locationConverter=locationConverter)
# ADD GEOAPIFY API