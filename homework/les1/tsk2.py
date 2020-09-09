"""Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк."""

sec_int = int(input("Enter amount of seconds\n"))

min_int = sec_int // 60
hour_int = min_int // 60
sec_int = sec_int % 60
min_int = min_int % 60
print(hour_int, ':', min_int, ':', sec_int)

