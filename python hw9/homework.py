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
