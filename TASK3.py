"""
Response verification - OpenWeather Map API (https://openweathermap.org/api)
TASK: Create a Postman collection to check various aspects of weather data. Then, write a python script that runs this
collection and analyzes the responses
"""

import requests
import json

with open('Weather_data.json', 'r') as file:
    data = json.load(file)

for item in data['item']:
    country_name = item['name']
    request_data = item['request']

    url = request_data['url']['raw']

    response = requests.get(url)

    if response.status_code == 200:
        print(f'Weather data {country_name}:')
        weather_data = response.json()
        print(json.dumps(weather_data, indent=2))
    else:
        print(f'Response for {country_name} has failed. Response code: {response.status_code}')
