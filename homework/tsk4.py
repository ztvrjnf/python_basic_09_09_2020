"""
Программа принимает действительное положительное число x и целое
отрицательное число y. Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y). При решении
задания необходимо обойтись без встроенной функции возведения числа в степень
"""


def my_func(x, y):
    return x ** y


def my_func_2(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    else:
        return 1 / res



while True:
    try:
        user_1 = float(input("Укажите первое число: "))
        if user_1 < 0:
            print('Попробуй ввести положительное число')
            continue
    except ValueError:
        print('Ошибка ввода')
        continue
    try:
        user_2 = int(input("Укажите второе число: "))
        if user_2 > 0:
            print('Попробуй ввести отрицательное число')
            continue
    except ValueError:
        print('Ошибка ввода')
        continue
    print(my_func(user_1, user_2))
    print(my_func_2(user_1, user_2))
    break
