"""
Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func(first, second, third):
    compare = first
    if compare > second:
        compare = second
    if compare > third:
        compare = third
    max_sum = first + second + third - compare
    return max_sum


while True:
    try:
        user_1 = float(input("Укажите первое число: "))
    except ValueError:
        print('Ошибка ввода')
        continue
    try:
        user_2 = float(input("Укажите второе число: "))
    except ValueError:
        print('Ошибка ввода')
        continue
    try:
        user_3 = float(input("Укажите третье число: "))
    except ValueError:
        print('Ошибка ввода')
        continue
    print(my_func(user_1, user_2, user_3))
    break
