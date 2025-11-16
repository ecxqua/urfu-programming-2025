import requests


url = 'https://wttr.in'  # не изменяйте значение URL

weather_parameters = {
    '1': '',
    'T': '',
    'M': '',
    'lang': 'ru'
    # добавьте параметр запроса `T`, чтобы вернулся чёрно-белый текст
}

# передайте параметры в http-запрос
response = requests.get(url, params=weather_parameters)

print(response.text)
