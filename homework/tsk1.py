"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""


from sys import argv


def money(time, salary, bonus):
    return time * salary + bonus


_, time, salary, bonus, = argv

try:
    print(money(float(time), float(salary), float(bonus)))
except ValueError as e:
    print("data entry error")
