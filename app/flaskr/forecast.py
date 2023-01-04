import requests, json

api_key = '57fc3439dc46a8578604c33691f100e3'

data = requests.get('https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=44.34&lon=10.99&appid={api_key}').json()
print(data)