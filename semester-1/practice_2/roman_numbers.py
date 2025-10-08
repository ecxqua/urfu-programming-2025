def to_roman(number):
    """Конвертер арабского числа в римское

    Args:
        number (int): число, которое нужно преобразовать в римское

    Returns:
        int: преобразованное римское число
    """
    if not 0 < number < 4000:
        print("Число должно быть в диапазоне от 1 до 3999")

    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    roman_numeral = ''
    i = 0
    while number > 0:
        # Сравнение и вычитание
        for _ in range(number // val[i]):
            roman_numeral += syb[i]
            number -= val[i]
        i += 1  # Переход к следующему значению
    return roman_numeral


print(to_roman(1949))  # MCMXLIX
print(to_roman(2023))  # MMXXIII
print(to_roman(3999))  # MMMCMXCIX
print(to_roman(0))


def from_roman(roman):
    """Конвертер из римского числа в арабское

    Args:
        roman (int): римское число

    Returns:
        int: арабское число
    """
    if not roman:
        print("Римское число не может быть пустым")

    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    # Алгоритм преобразования
    arabic_number = 0
    i = 0
    while i < len(roman):
        # Проходим по всем паттернам в порядке списка
        found = False
        for j in range(len(syb)):
            pattern = syb[j]

            # Проверяем, начинается ли строка с текущего паттерна
            if roman.startswith(pattern, i):
                arabic_number += val[j]
                i += len(pattern)
                found = True
                break

        if not found:
            print(f"Некорректная римская цифра: {roman}")

    return arabic_number


print(from_roman("MCMXLIX"))   # 1949
print(from_roman("MMXXIII"))   # 2023
print(from_roman("MMMCMXCIX"))  # 3999
print(from_roman("IV"))        # 4
print(from_roman("IX"))        # 9
