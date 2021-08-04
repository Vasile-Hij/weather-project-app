#!/bin/usr/env python3
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, UserToCityMapping
from .__init__ import db
import configparser
import requests
import math

main = Blueprint('main', __name__)


def readConfig():
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    return parser


def getApiKey():
    api_key = readConfig()
    return api_key.get("openweathermap", 'api', fallback='No api key was found')


def getUnits():
    units = readConfig()
    return units.get("units", "unit", fallback='No metric unit inserted')


def getWeatherData(city):
    api_key = getApiKey()
    units = getUnits()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}"
    data = requests.get(url).json()
    return data


@main.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@main.route('/signup')
def signup():
    return render_template('signup.html')


@main.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('main.login'))

    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@main.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists!')
        return redirect(url_for('main.login'))

    new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
    try:
        db.session.add(new_user)
        db.session.commit()
    except:
        return 'Failed to add the { new_user } on database'
    return redirect(url_for('main.login'))


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@main.route('/contact')
def contact():
    return render_template('contact.html')


is_fahrenheit = False


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    cities = UserToCityMapping.query.all()
    weather_data = []
    for city in cities:
        data = getWeatherData(city.city_name)
        weather = {
                'city': city.city_name,
                'celsius': math.ceil(data['main']['temp']),
                'fahrenheit': math.ceil((int(data['main']['temp']) * 9 / 5) + 32),
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'pressure': data['main']['pressure'],
                'wind_celsius': data['wind']['speed'],
                'wind_fahrenheit': math.ceil((data['wind']['speed']) * 2.23694),
                'humidity': data['main']['humidity'],
                'country': data['sys']['country'],
        }
        weather_data.append(weather)
    return render_template('profile.html', weather_data=weather_data, username=current_user.username, is_fahrenheit=is_fahrenheit)


@main.route('/profile', methods=['POST'])
@login_required
def postCity():
    error_message = ''
    new_city = request.form.get('city')
    if not new_city.isnumeric or new_city == '':
        error_message = 'Please enter a city name as: Bucharest'
    if new_city:
        existing_city = UserToCityMapping.query.filter_by(user_id=current_user.id, city_name=new_city).first()
        if not existing_city:
            new_city_data = getWeatherData(new_city)
            if new_city_data['cod'] == 200:
                new_city_obj = UserToCityMapping(user_id=current_user.id, city_name=new_city)
                db.session.add(new_city_obj)
                db.session.commit()
            else:
                error_message = 'City does not exist in the world!'
        else:
            error_message = 'This city was checked. See below!'
    if error_message:
        flash(error_message, 'Error')
    else:
        flash('City added successfully!')
    return redirect(url_for('main.profile'))


@main.route('/profile/<city_name>')
@login_required
def deleteCity(city_name):
    city = UserToCityMapping.query.filter_by(city_name=city_name).first()
    try:
        db.session.delete(city)
        db.session.commit()
    except:
        return 'Failed to delete city. Please try again!'
    flash(f'Successfully deleted {city.city_name}', 'success')
    return redirect(url_for('main.profile'))


@main.route('/switch_units', methods=['GET'])
def switch():
    global is_fahrenheit
    is_fahrenheit = not is_fahrenheit
    return redirect(url_for('main.profile'))


@main.errorhandler(404)
def page_not_found():
    return render_template('index.html')
