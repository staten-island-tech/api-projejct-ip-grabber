import requests, json

api_key = '57fc3439dc46a8578604c33691f100e3'

currentWeather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat=30.34&lon=100.99&appid={api_key}').json()
print(currentWeather)