"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий
набор натуральных чисел. У пользователя необходимо запрашивать новый
элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
значениями, то новый элемент с тем же значением должен разместиться после них.
"""

my_list = [23, 7, 5, 5, 3, 3, 2]

while True:
    user_input = input('Введите натуральное число\n')
    if user_input.isdigit():
        user_input = int(user_input)
        break
    print('Ошибка ввода')
i = 0
unchanged_list = len(my_list)
while i != len(my_list):
    if user_input > my_list[i]:
        my_list.insert(i, user_input)
        break
    i += 1
    if i < len(my_list):
        continue
    else:
        my_list.append(user_input)
        break

print(my_list)
