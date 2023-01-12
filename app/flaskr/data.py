# import requests, json

# api_key = '57fc3439dc46a8578604c33691f100e3'

# city_name = 'Tampa'
# state_code = 'FL'
# country_code = 'US'
# locationConverter = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit=5&appid={api_key}').json()

# for x in locationConverter:
#     lat = x['lat']
#     lon = x['lon']

# currentWeather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}').json()
# print(currentWeather)

# forecast = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}').json()