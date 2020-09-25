"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import os
import random

file_path = os.path.join(os.path.dirname(__file__), 'task5.txt')

to_file_numbers = [random.randint(1, 100) for _ in range(random.randint(10, 200))]


def sum_all():
    try:
        with open('task5.txt', 'w+') as file_obj:
            numbers = ' '.join(map(str, to_file_numbers))
            file_obj.writelines(numbers)
            my_numb = numbers.split()
            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка ввода данных')


sum_all()
