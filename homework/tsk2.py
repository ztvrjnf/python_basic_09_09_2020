"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

user_input = input("введите строку\n")
user_list = list(user_input)
i = 0
while i != len(user_list):
    a = user_list[i]
    b = user_list[i+1]
    user_list[i] = b
    user_list[i+1] = a
    i += 2
    if len(user_list) - i < 2:
        break
print(user_list)
