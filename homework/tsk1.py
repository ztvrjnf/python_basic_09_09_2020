"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
    user_s = float(input("Укажите первое число: "))
    user_b = float(input("Укажите второе число: "))
"""


def num_div(user_a, user_b):
    return user_a / user_b


while True:
    user_input = input("Input two numbers separated by space")
    user_input = user_input.split()
    numbers = []
    for n in user_input:
        try:
            numbers.append(int(n))
        except ValueError:
            continue
    user_a, user_b = int(numbers[0]), int(numbers[1])
    break

print(num_div(user_a, user_b))

