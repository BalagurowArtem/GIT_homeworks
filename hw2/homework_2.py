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

def get_weather(city:str = CITY, api_key: str = API_KEY, units: str = UNITS, language: str = LANGUAGE) -> dict:

    """
    Keyword Arguments:
    city -- (default: {CITY})
    api_kei --  (default: {API_KEY})
    units --  (default: {UNITS})
    language -- (default: {LANGUAGE})

    """

    url: str = rf'https://api.openweathermap.org/data/2.5/weather?q=Чита&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru'
    response = requests.get(url)
    return response.json()

def format_weather_message(weather_dict: dict) -> str:

   
    temp = weather_dict["main"]["temp"]

    feels_like = weather_dict["main"]["feels_like"]

    description = weather_dict["weather"][0]["description"]

    return (f'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}')

