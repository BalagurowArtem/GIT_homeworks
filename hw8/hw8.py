from dataclasses import dataclass, field  
from typing import List, Dict, Any, Optional, Set
import json
from random import choice

@dataclass
class City:
    name: str
    population: int
    subject: str
    district: str
    latitude: float
    longitude: float
    is_used: bool = False

class JsonFile:
    def __init__(self, filename: str):
        self.filename = filename
        
    def read_data(self)-> List[Dict[str, Any]]:
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)
        
    def write_data(self, data: List[Dict[str, Any]]):

        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

class CitiesSerializer:
    def __init__(self, city_data: List[Dict[str, Any]]):
    
        self.cities: List[City] = []
        self._serialize_cities(city_data)

    def _serialize_cities(self, city_data: List[Dict[str, Any]]):

        for city in city_data:
           
            self.cities.append(
                City(
                    name=city['name'],

                    population=city['population'],

                    subject=city['subject'],

                    district=city['district'],

                    latitude=float(city['coords']['lat']),

                    longitude=float(city['coords']['lon']),

                    
                )
            )
    
    def get_all_cities(self) -> List[City]:
        return self.cities
    
class CityGame:
    def __init__(self, cities_serializer: CitiesSerializer):
        self.cities = cities_serializer.get_all_cities()
        self.cities_set: Set[str] = {city.name for city in self.cities}
        self.used_cities: Set[str] = set()
        self.computer_city: str = ''
        self.bad_letters: Set[str] = self.calculate_bad_letters()

    def calculate_bad_letters(self) -> Set[str]:
        all_letters = {city.name[-1].lower() for city in self.cities}
        first_letters = {city.name[0].lower() for city in self.cities}
        return all_letters - first_letters
    
    def start_game(self) -> str:
        self.computer_city = choice(list(self.cities_set))

        self.cities_set.remove(self.computer_city)

        self.used_cities.add(self.computer_city)

        return self.computer_city
    
    def human_turn(self, city: str) -> bool:
        if city not in self.cities_set:
            return False
    
        if self.computer_city and city[0].lower() != self.computer_city[-1].lower():
            return False
    
        self.cities_set.remove(city)
        self.used_cities.add(city)
        return True
    
    def  computer_turn(self, human_city: str) -> Optional[str]:
        last_letter = human_city[-1].lower()

        for city in self.cities_set:
            if city[0].lower() == last_letter and city[-1] .lower() not in self.bad_letters:

                self.computer_city = city
                self.cities_set.remove(city)
                self.used_cities.add(city)
                return city
        return None
    
class GameManager:
    def __init__(self, json_file: JsonFile, cities_serializer: CitiesSerializer, city_game: CityGame):

        self.json_file = json_file

        self.cities_serializer = cities_serializer
        self.city_game = city_game

    def __call__(self):
        self.run_game()

    def run_game(self):
       print('Начнем игру в "Города"!')

       print(f'Компьютер загадал город: {self.city_game.start_game()}')

       while True:
            human_city = input('Введите город: ')
            if not self.city_game.human_turn(human_city):
                print('Неверный город. Попробуйте снова в следующий раз.')
                break

            computer_city = self.city_game.computer_turn(human_city)
            if not computer_city:
                print("Вы победили машину. Захват человечества откладывается. Поздравляю!")
                break

            print(f'Компьютер загадал город: {computer_city}')

