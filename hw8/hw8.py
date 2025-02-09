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