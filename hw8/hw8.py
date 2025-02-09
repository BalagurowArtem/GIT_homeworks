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

