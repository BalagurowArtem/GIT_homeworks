from dataclasses import dataclass
from typing import List, Dict, Iterator, Optional, Any


@dataclass
class City:
    name: str
    lat: float
    lon: float
    district: str
    population: int
    subject: str


class CitiesIterator:
    
    required_fields = {'name', 'district', 'population', 'subject', 'coords'}
    coords_fields = {'lat', 'lon'}

    def __init__(self, cities: List[Dict[str, Any]]) -> None:
        self.cities_raw = cities
        self.population_filter: Optional[int] = None
        self.sort_key: Optional[str] = None
        self.sort_reverse: bool = False
        self.cities: List[City] = []
        self.index: int = 0
        
        self.prepare_cities()

    def validate_city_dict(self, city_dict: Dict[str, Any]) -> None:
        missing = self.required_fields - city_dict.keys()
        if missing:
            raise KeyError(f"Нет обязательных полей: {missing} в {city_dict.get('name', '')}")

        coords = city_dict.get("coords")
        if not isinstance(coords, dict):
            raise ValueError(f"Поле 'coords' должно быть словарём в  {city_dict.get('name', '')}")

        missing_coords = self.coords_fields - coords.keys()
        if missing_coords:
            raise KeyError(f"Нет координат {missing_coords} в {city_dict.get('name', '')}")

    def dict_to_city(self, city_dict: Dict[str, Any]) -> City:
        self.validate_city_dict(city_dict)
        
        try:
            lat = float(city_dict["coords"]["lat"])
            lon = float(city_dict["coords"]["lon"])
            population = int(city_dict["population"])
        except (ValueError, TypeError) as e:
            raise ValueError(f"Некорректный формат данных в {city_dict.get('name', '')}") from e

        return City(
            name=city_dict["name"],
            lat=lat,
            lon=lon,
            district=city_dict["district"],
            population=population,
            subject=city_dict["subject"]
        )

    def prepare_cities(self) -> None:
        self.cities = []
        
        for city_dict in self.cities_raw:
            try:
                city = self.dict_to_city(city_dict)
                if self.population_filter is None or city.population >= self.population_filter:
                    self.cities.append(city)
            except (KeyError, ValueError) as e:
                print(f"Возникла ошибка при обработке {city_dict.get('name', 'unknown')}: {e}")
                continue
        
        if self.sort_key:
        
            if self.cities and not hasattr(self.cities[0], self.sort_key):
                raise AttributeError(f"Не получается сортировать по полю '{self.sort_key}' (такого поля нет в City)")
            
            self.cities.sort(
                key=lambda city: getattr(city, self.sort_key),
                reverse=self.sort_reverse
            )
        
        self.index = 0

    def set_population_filter(self, min_population: Optional[int]) -> None:
        if min_population is not None and min_population < 0:
            raise ValueError("Минимальное население не может быть отрицательным")
            
        self.population_filter = min_population
        self.prepare_cities()

    def sort_by(self, parameter: str, reverse: bool = False) -> None:
        self.sort_key = parameter
        self.sort_reverse = reverse
        self.prepare_cities()

    def __iter__(self) -> Iterator[City]:
        self.index = 0
        return self

    def __next__(self) -> City:
        if self.index >= len(self.cities):
            raise StopIteration()
        
        city = self.cities[self.index]
        self.index += 1
        return city


def test_cities_iterator():
    cities_data = [
        {
            "coords": {"lat": "52.65", "lon": "90.08333"},
            "district": "Сибирский",
            "name": "Абаза",
            "population": 14816,
            "subject": "Хакасия"
        },
        {
            "coords": {"lat": "55.75583", "lon": "37.61778"},
            "district": "Центральный",
            "name": "Москва",
            "population": 12655050,
            "subject": "Москва"
        },
        {
            "coords": {"lat": "53.68333", "lon": "53.65"},
            "district": "Приволжский",
            "name": "Абдулино",
            "population": 17274,
            "subject": "Оренбургская область"
        },  
    ]
    
    iterator = CitiesIterator(cities_data)
    
    print("Сортировка по возрастанию населения")
    iterator.set_population_filter(15000)
    for city in iterator:
        print(f"{city.name} ({city.population} чел.)")
    
    print("Сортировка по убывания населения")
    iterator.sort_by("population", reverse=True)
    for city in iterator:
        print(f"{city.name} ({city.population} чел.)")

    print(" Сортировка по названию")
    iterator.sort_by("name")
    for city in iterator:
        print(f"{city.name} ({city.population} чел.)")
    

if __name__ == "__main__":
    test_cities_iterator()