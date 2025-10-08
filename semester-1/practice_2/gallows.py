import random


def gallows():

    words = ['питон', 'программа', 'компьютер', 'клавиатура', 'монитор',
             'мышь', 'процессор', 'память', 'диск', 'сеть']

    word = random.choice(words)
    guessed_letters = set()
    attempts = 10

    print("Игра 'Виселица'!")
    print(f"Слово загадано. У вас {attempts} попыток.")

    while attempts > 0:
        # Показываем текущее состояние слова
        display = ''.join(
            [letter if letter in guessed_letters else '_' for letter in word])
        print(f"Слово: {display}")
        print(f"Попыток осталось: {attempts}")

        # Проверяем победу
        if all(letter in guessed_letters for letter in word):
            print(f"Поздравляем! Вы угадали слово: {word}")
            return

        # Получаем букву от игрока
        guess = input("Введите букву: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Введите одну букву!")
            continue

        if guess in guessed_letters:
            print("Вы уже вводили эту букву!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Верно! Эта буква есть в слове.")
        else:
            attempts -= 1
            print("Неверно! Этой буквы нет в слове.")

    print(f"Игра окончена! Загаданное слово: {word}")


gallows()
