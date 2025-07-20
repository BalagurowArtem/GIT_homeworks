from typing import Dict, List, Any, Union, Optional, Set
from pprint import pprint
from marvel import full_dict

# 2
user = input("ID фильмов (через пробел): ")
elements: List[Optional[int]] = []
for element in user.split():
    try:
        elements.append(int(element))
    except ValueError:
        elements.append(None)
print("Итоговый список:")
pprint(elements)

# 3
filtered = {k: i for k, i in full_dict.items() if k in elements}
pprint(filtered)

# 4
directors = {i['director'] for i in full_dict.values() if i['director'] != 'TBA' and i['director'] != 'Нет данных'}
print("Уникальные режиссеры:", directors)

# 6
films_ch = {k: i for k, i in full_dict.items() if i['title'] and i['title'].startswith('Ч')}
pprint(films_ch)

# 7
