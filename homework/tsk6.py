"""
Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем
регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""

user_str = input()


def int_func(capital):
    return capital.capitalize()


i = 0
output = ''
mapping = user_str.split()
while i != len(mapping):
    mopp = mapping[i]
    mopp = str(mopp)
    output = output + (int_func(mopp)) + ' '
    i += 1
print(output)
