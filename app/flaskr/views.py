from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import User

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template('index.html', user=current_user, firstName=User.firstName)

@views.route('/forecast/<location>')
@login_required
def forecast(location):
    return render_template('weather.html', location=location, user=current_user)
