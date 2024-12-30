# weather


"""
    {"coord":{"lon":113.55,"lat":52.0333},"weather":[{"id":800,"main":"Clear","description":"ясно","icon":"01n"}],"base":"stations","main":{"temp":-18.06,"feels_like":-23.49,"temp_min":-18.06,"temp_max":-18.06,"pressure":1028,"humidity":55,"sea_level":1028,"grnd_level":919},"visibility":10000,"wind":{"speed":2,"deg":280},"clouds":{"all":6},"dt":1734252715,"sys":{"type":1,"id":8890,"country":"RU","sunrise":1734222470,"sunset":1734250452},"timezone":32400,"id":2025339,"name":"Чита","cod":200}
"""

import requests
from plyer import notification


CITY = "Чита"
API_KEY = "23496c2a58b99648af590ee8a29c5348"
UNITS = "metric"
LANGUAGE = "ru"

# url = rf'https://api.openweathermap.org/data/2.5/weather?q=Чита&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru'
