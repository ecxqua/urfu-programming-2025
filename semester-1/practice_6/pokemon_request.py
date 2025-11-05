import requests
import json

# Задание 1
params = {'limit': 20}
response = requests.get('https://pokeapi.co/api/v2/pokemon', params=params)

# Преобразуем JSON-ответ в словарь Python
data = response.json()

for pokemon in data['results']:
    # Каждый элемент содержит имя и ссылку (url), но выводим только имя
    print(pokemon['name'])


# Задание 2
pokemonchick = input('Введите имя покемона: ').lower()

url = f'https://pokeapi.co/api/v2/pokemon/{pokemonchick}'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Печатаем весь ответ красиво отформатированным JSON-ом
    print(json.dumps(data, indent=4, ensure_ascii=False))  # красиво форматирует
else:
    print("Ошибка: покемон не найден или сервер недоступен.")


# Задание 3
pokemonchick = input('Введите имя покемона: ').lower()

url = f'https://pokeapi.co/api/v2/pokemon/{pokemonchick}'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    name = data['name']
    height = data['height']
    weight = data['weight']

    # Типы и способности возвращаются списками словарей, достаем имена
    types = [t['type']['name'] for t in data['types']]
    abilities = [a['ability']['name'] for a in data['abilities']]

    # Вывод информации в понятном формате
    print(f"Имя: {name}")
    print(f"Типы: {', '.join(types)}")
    print(f"Способности: {', '.join(abilities)}")
    print(f"Рост: {height}")
    print(f"Вес: {weight}")

else:
    print("Ошибка: покемон не найден или сервер недоступен.")
