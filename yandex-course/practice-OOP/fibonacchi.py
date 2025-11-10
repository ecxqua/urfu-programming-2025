def fibonacci(n):
    """Генератор чисел Фибоначчи до n-го элемента."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


sequence = fibonacci(10)
for number in sequence:
    print(number)

# def fibonacci(n):
#     # Допишите функцию.
#     first = 0
#     second = 1
#     new = 0
#     yield first
#     yield second
#     for i in range(n-2):
#         new = first + second
#         yield new
#         first = second
#         second = new
# sequence = fibonacci(10)
# for number in sequence:
#     print(number)
"""При вызове функции fibonacci с аргументом 10 получен генератор, 
который генерирует слудющую последовательность чисел:
0 1 1 2 3 5 8 13
Ожидаемая последовательность чисел:
0 1 1 2 3 5 8 13 21 34"""
