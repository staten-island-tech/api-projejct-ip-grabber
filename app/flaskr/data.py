import requests, json

api_key = '57fc3439dc46a8578604c33691f100e3'

currentWeather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat=30.34&lon=100.99&appid={api_key}').json()
print(currentWeather)

forecast = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&appid={api_key}').json()
print(forecast)

locationCovert = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={api_key}').json()
print(locationCovert)