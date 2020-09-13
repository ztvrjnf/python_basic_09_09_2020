"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
времени года относится месяц (зима, весна, лето, осень). Напишите решения через
list и через dict.
"""

my_dict = {0: 'Зима', 1: 'Весна', 2: 'Лето', 3: 'Осень', 4: 'Зима'}
while True:
    month = input('Введите месяц\n')
    if month.isdigit():
        month = int(month)
        if month <= 12:
            break
        print('месяцев всего 12, попробуй еще раз')
        continue
    print('Ошибка ввода')
month = month // 3
print(my_dict.get(month))


my_list = ["Зима", "Весна", "Лето", "Осень", "Зима"]
while True:
    month = input('Введите месяц\n')
    if month.isdigit():
        month = int(month)
        if month <= 12:
            break
        print('месяцев всего 12, попробуй еще раз')
        continue
    print('Ошибка ввода')

month = month // 3
print(my_list[month])