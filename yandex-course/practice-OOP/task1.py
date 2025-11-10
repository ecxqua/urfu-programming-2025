# Импортируйте необходимые модули.
from datetime import datetime
# Укажите два параметра функции:


def validate_record(person, date):
    # Напишите код, верните булево значение.
    try:
        datetime.strptime(date, '%d.%m.%Y')
        return True
    except ValueError:
        print(f'Некорректный формат даты в записи: {person}, {date}')
        return False


# Укажите параметры функции:
def process_people(data):
    # Объявите счётчики.
    good_count = 0
    bad_count = 0
    info = {}
    # в каждой паре значений из списка data
    # проверьте корректность формата даты рождения
    # и в зависимости от результата проверки увеличьте один из счётчиков.
    for person, date in data:
        if validate_record(person, date):
            good_count += 1
        else:
            bad_count += 1
    info['good'] = good_count
    info['bad'] = bad_count

    return info


data = [
    ('Иван Иванов', '10.01.2004'),
    ('Пётр Петров', '15.03.1956'),
    ('Зинаида Зеленая', '6 февраля 1997'),
    ('Елена Ленина', 'Второе мая тысяча девятьсот восемьдесят пятого'),
    ('Кирилл Кириллов', '26/11/2003')
]
statistics = process_people(data)
# Выведите на экран информацию о корректных и некорректных записях
# в таком формате:
# Корректных записей: <число>
# Некорректных записей: <число>
print(f"Корректных записей: {statistics['good']}")
print(f"Некорректных записей: {statistics['bad']}")
