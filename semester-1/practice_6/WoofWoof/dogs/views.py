# dogs/views.py

from django.shortcuts import render
import requests


def index(request):
    """
    Главная страница приложения dogs.py
    Позволяет вводить породы собак через запятую и
    отображает их фотографии.
    """
    images = [
    ]  # список словарей вида {'breed': порода, 'url': ссылка на фото}

    # Получаем строку пород из GET-запроса
    # например: 'african, chow, dingo'
    breeds_input = request.GET.get('breeds')

    if breeds_input:  # если пользователь ввёл что-то
        # Разбиваем строку на список пород, убираем лишние пробелы
        breeds = [b.strip() for b in breeds_input.split(',')]

        for breed in breeds:
            # Формируем URL для Dog API для каждой породы
            url = f'https://dog.ceo/api/breed/{breed}/images/random'

            # Отправляем GET-запрос
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                if data['status'] == 'success':
                    # Добавляем словарь с породой и ссылкой на фото в список images
                    images.append({'breed': breed, 'url': data['message']})
                else:
                    # Если порода не найдена, можно добавить пустую картинку или текст
                    images.append({'breed': breed, 'url': None})
            else:
                # Если сервер API недоступен
                images.append({'breed': breed, 'url': None})

    # Передаём список images в шаблон index.html
    return render(request, 'index.html', {'images': images})
