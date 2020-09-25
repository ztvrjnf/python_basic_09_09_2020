"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

import os

file_path = os.path.join(os.path.dirname(__file__), 'task1.txt')

with open(file_path, 'w', encoding='UTF-8') as file:
    while True:
        line = input('Введите текст \n')
        if not line:
            break
        file.write(f'{line}\n')