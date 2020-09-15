"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
"""


def num_div(user_a, user_b):
    return user_a / user_b


'''
while True:
    user_input = input('Введите натуральное число\n')
    if user_input.isdigit():
        user_input = int(user_input)
        break
    print('Ошибка ввода')

'''

while True:
    try:
        user_a = float(input("Укажите первое число: "))
    except ValueError:
        print('Ошибка ввода')
        continue
    try:
        user_b = float(input("Укажите второе число: "))
    except ValueError:
        print('Ошибка ввода')
        continue
    try:
        print(num_div(user_a, user_b))
    except ZeroDivisionError:
        print('На ноль делить нельзя, попробуй еще раз')
        continue
    break
