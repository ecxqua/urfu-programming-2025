scores = list(map(int, input('Введите баллы участников через пробел: ').split()))
student_score = int(input("Введите свой балл: "))

def check_winners(scores, student_score):
    """
    Попадает ли Стас в тройку лидеров по баллам
    """
    scores.append(student_score)
    scores.sort(reverse='True')

    if student_score in scores[:3]:
        print("Вы в тройке победителей! ")
    else:
        print('Вы не попали в тройку победителей. ')

check_winners(scores, student_score)




