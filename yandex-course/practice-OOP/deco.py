"""В строке, переданной под ключом name, каждый символ, кроме первого и последнего, должен быть заменён на звёздочки *. Первый и последний символы должны остаться, как были; общее количество символов должно совпадать с исходным.
В строке, переданной под ключом password, каждый символ должен быть заменён на звёздочку *. Количество звёздочек должно соответствовать количеству символов в исходном пароле.
Пример:

# Исходная функция возвращает такой словарь:
{
    'name': 'Vasya',
    'password': '123456'
}

# Задекорированная функция должна вернуть такой словарь:
{
    'name': 'V***a',
    'password': '******'
} """

# Напишите декоратор obfuscator


def obfuscator(func):
    def wrapper():
        rez = func()
        for key, value in rez.items():
            if key == 'name':
                middle = len(value)-2
                rez[key] = value[0] + middle*'*' + value[-1]
            else:
                rez[key] = len(value) * '*'
        return rez
    return wrapper


@obfuscator
def get_credentials():
    return {
        'name': 'StasBasov',
        'password': 'iamthebest'
    }


print(get_credentials())
