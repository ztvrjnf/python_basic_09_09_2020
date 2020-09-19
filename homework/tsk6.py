"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
"""

from itertools import count, cycle

for el in count(int(input('Введите стартовое число '))):
    print(el)
    if el > 45:
        break

cycle_count = 0
my_list = [True, False, 97585, None]
for el in cycle(my_list):
    print(el)
    if cycle_count > 20:
        break
    cycle_count += 1
