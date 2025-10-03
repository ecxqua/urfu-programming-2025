def print_pack_report(count_of_cakes):
    """
    Фасовка пирожных в коробку в зависмости от их количества
    """
    if count_of_cakes % 5 == 0 and count_of_cakes % 3 == 0:
        print(f"{count_of_cakes} - расфасуем по 3 или по 5")
    elif count_of_cakes % 5 == 0 and count_of_cakes % 3 != 0:
        print(f"{count_of_cakes} - расфасуем по 5")
    elif count_of_cakes % 3 == 0 and count_of_cakes % 5 != 0:
        print(f"{count_of_cakes} - расфасуем по 3")
    else:
        print(f"{count_of_cakes}  - не заказываем!")

print_pack_report(5)

