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


# Часть 2
def password_validator(min_length: int = 8, min_uppercase: int = 1, min_lowercase: int = 1, min_special_chars: int = 1):
    
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(username: str, password: str, *args, **kwargs) -> Any:
            errors = []
            special_chars = "!@#$%^&*()-_=+[]{};:'\",.<>/?"
            
            if len(password) < min_length:
                errors.append(f"Пароль должен содержать минимум {min_length} символов")
            
            uppercase_count = sum(1 for char in password if char.isupper())
            if uppercase_count < min_uppercase:
                errors.append(f"Пароль должен содержать минимум {min_uppercase} заглавных букв")
            
            lowercase_count = sum(1 for char in password if char.islower())
            if lowercase_count < min_lowercase:
                errors.append(f"Пароль должен содержать минимум {min_lowercase} строчных букв")
            
            special_count = sum(1 for char in password if char in special_chars)
            if special_count < min_special_chars:
                errors.append(f"Пароль должен содержать минимум {min_special_chars} специальных символов")
            
            if errors:
                raise ValueError(" | ".join(errors))
            
            return func(username, password, *args, **kwargs)
        return wrapper
    return decorator

def username_validator(func: Callable):
  
    @wraps(func)
    def wrapper(username: str, password: str, *args, **kwargs) -> Any:
        if ' ' in username:
            raise ValueError("Введите имя пользователя без пробелов")
        return func(username, password, *args, **kwargs)
    return wrapper

@username_validator
@password_validator(min_length=10, min_uppercase=2, min_lowercase=2, min_special_chars=2)
def register_user(username: str, password: str, filename: str = "users.csv") -> None:
  
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(["Username", "Password"])
        writer.writerow([username, password])

try:
    register_user("JohnDoe", "PassWord123+!")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")
