from random import choices
from random import shuffle

def password_generator():
    """
    Генерация пароля в зависимости от выбранных параметров с выбором в терминале

    Returns:
        string: Пароль
    """
    # Параметры для генерациия пароля
    low_reg = int(input('Наличие нижнего регистра 1 - да, 0 - нет '))
    high_reg = int(input('Наличие верхнего регистра 1 - да, 0 - нет '))
    spec_symb = int(input('Наличие спецсимволов регистра 1 - да, 0 - нет '))
    numbers = int(input('Наличие цифр регистра 1 - да, 0 - нет '))
    len_pass = int(input('Длина пароля '))

    # Списки символов для генерации пароля
    chars_symb = '!@#$%^&*'
    chars_int = '0123456789'
    chars_abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Основные переменные
    count_of_flags = low_reg + high_reg + spec_symb + numbers
    count_of_symbols = len_pass // count_of_flags
    extra_count = len_pass % count_of_flags

    password = []

    # Проверка выбранных парметров, генерация пароля
    if low_reg == 1:
        password+=choices(chars_abc.lower(), k=count_of_symbols)
    if high_reg == 1:
        password += choices(chars_abc, k=count_of_symbols)
    if spec_symb == 1:
        password += choices(chars_symb, k=count_of_symbols+extra_count)
    if numbers == 1:
        password += choices(chars_int, k=count_of_symbols)

    shuffle(password)
    print(''.join(password))

password_generator()