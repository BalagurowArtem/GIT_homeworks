from homework_2 import get_weather, format_weather_message, notify_weather

def main() -> None:
    city = input ('Введите город')
    weather_dict = get_weather(city = city)
    message = format_weather_message(weather_dict)
    print(message)
    input('Нажмите Enter для уведомления')
    notify_weather(message)

main()