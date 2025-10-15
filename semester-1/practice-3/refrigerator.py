import datetime
from decimal import Decimal


def add(items: dict[str, list[dict]], title: str, amount: Decimal, expiration_date=None):
    """
    Добавляет новую партию товара в складскую систему.

    Args:
        items (dict): Словарь с товарами и их партиями
        title (str): Название товара
        amount (Decimal): Количество товара в партии
        expiration_date (str, optional): Дата окончания срока годности в формате 'ГГГГ-ММ-ДД'
    """
    # Если указана дата окончания срока годности, преобразуем строку в объект date
    if expiration_date is not None:
        expiration_date = datetime.datetime.strptime(
            expiration_date, r'%Y-%m-%d').date()
    items[title] = items.get(title, []) + [{
        'amount': amount,
        'expiration_date': expiration_date
    }]


def add_by_note(items, note):
    """
    Добавляет товар в систему на основе текстовой записи.

    Форматы записи:
    - "Название товара количество" (без даты)
    - "Название товара количество ГГГГ-ММ-ДД" (с датой)

    Args:
        items (dict): Словарь с товарами и их партиями
        note (str): Текстовая запись с информацией о товаре
    """
    # Разбиваем запись на части по пробелам
    parts = note.split()

    # Проверяем, содержит ли последняя часть дату (формат с дефисами)
    if '-' in parts[-1]:
        expiration_date = parts[-1]
        amount = Decimal(parts[-2])
        title = ' '.join(parts[:-2])
    else:
        expiration_date = None
        amount = Decimal(parts[-1])
        title = ' '.join(parts[:-1])

    add(items, title, amount, expiration_date)


def find(items, needle):
    """
    Находит товары, в названии которых содержится искомая строка (без учета регистра).

    Args:
        items (dict): Словарь с товарами и их партиями
        needle (str): Строка для поиска в названиях товаров

    Returns:
        list: Список названий товаров, содержащих искомую строку
    """
    search_term = needle.lower()

    # Ищем все товары, в названии которых содержится искомая строка
    return [key for key in items.keys() if search_term in key.lower()]


def amount(items, needle):
    """
    Вычисляет общее количество товара по поисковому запросу.

    Args:
        items (dict): Словарь с товарами и их партиями
        needle (str): Строка для поиска в названиях товаров

    Returns:
        Decimal: Суммарное количество найденного товара во всех партиях
    """

    matching_keys = find(items, needle)
    total = Decimal(0)

    # Проходим по всем товарам в системе
    for product_title, batches in items.items():
        if product_title in matching_keys:
            for batch in batches:
                total += batch['amount']

    return total


goods = {
    'Пельмени Универсальные': [
        # Первая партия пельменей
        {'amount': Decimal(
            '0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
        # Вторая партия пельменей
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
    ],
    'Вода': [
        # Партия воды (без срока годности)
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}
