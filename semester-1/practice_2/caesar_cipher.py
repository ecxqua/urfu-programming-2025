def caesar_cipher(text, shift):
    """
    Шифрование текста методом Цезаря

    Args:
        text(string): Текст, который нужно зашифровать
        shift(int): Шаг, с которым будет осуществлен сдвиг символа
    Returns:
        string: Текст в зашифрованном виде
    """
    
    alphabet_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 
                'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    
    alphabet_eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
                    'w', 'x', 'y', 'z']
    
    result = []
    for symb in text.lower(): # Определение языка текста
        if symb in alphabet_ru:
            flag = 0
            break
        if symb in alphabet_eng:
            flag = 1
            break

    if flag == 0: # Шифрование слова в зависимости от языка
        for char in text.lower():
            if char in alphabet_ru:
                index = (alphabet_ru.index(char) + shift) % len(alphabet_ru)
                result.append(alphabet_ru[index])
            else:
                result.append(char)
    else:
        for char in text.lower():
            if char in alphabet_eng:
                index = (alphabet_eng.index(char) + shift) % len(alphabet_eng)
                result.append(alphabet_eng[index])
            else:
                result.append(char)
    return ''.join(result)

print(caesar_cipher('скибиди', 1))
print(caesar_cipher('skibidi', 1))