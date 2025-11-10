from random import choice, uniform


def format_float_return(func):
    def wrapper():
        result = func()
        if isinstance(result, float):
            str_number = str(result)
            if len(str_number.split('.')[1]) >= 3:
                rez = round(result, 2)
                return rez
        else:
            return result
    return wrapper


# Не изменяйте код ниже: он поможет проверить работу декоратора.
# Декорируем функцию:
@format_float_return
def test_function_1():
    """Возвращает случайное число типа float в диапазоне от -10 до 10,
    например -4.3897268052813265.
    """
    return uniform(-10, 10)


# Декорируем вторую функцию:
@format_float_return
def test_function_2():
    """Возвращает случайный элемент списка sequence - число или строку."""
    sequence = [
        3.1415926535,
        'pi',
        3.14,
        'пи',
        'три целых четырнадцать сотых',
        3.14159
    ]
    # Функция choice() из модуля random возвращает
    # случайный элемент последовательности.
    return choice(sequence)


# Вызовем задекорированные функции для проверки работы декоратора:
print(test_function_1())
print(test_function_2())
