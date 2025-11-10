people = ['Антон', 'Соня', 'Коля', 'Женя', 'Тоня', 'Стёпа']


def say_to_all(sequence):
    for item in sequence:
        if item[0].lower() == 'с':
            (lambda item: print(f'Здравствуй, {item}!'))(item)
        else:
            (lambda item: print(f'Привет, {item}!'))(item)


say_to_all(people)
