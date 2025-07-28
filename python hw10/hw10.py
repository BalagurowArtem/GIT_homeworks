import csv
from typing import Callable, Any, Optional
from functools import wraps

# Часть 1

def password_checker(func: Callable):
   
    @wraps(func)
    def wrapper(password: str):
       
        if len(password) < 8:
            return "В пароле должно быть минимум 8 символов"
        
        if not any(char.isdigit() for char in password):
            return "В пароле должна быть минимум одна цифра"
        
        if not any(char.isupper() for char in password):
            return "В пароле должна быть минимум одна заглавная буква"
        
        if not any(char.islower() for char in password):
            return "В пароле должна быть минимум одна строчная буква"
        
        special_chars = "!@#$%^&*()-_=+[]{};:'\",.<>/?"
        if not any(char in special_chars for char in password):
            return "В пароле должна быть минимум один специальный символ"
        
        return func(password)
    
    return wrapper
