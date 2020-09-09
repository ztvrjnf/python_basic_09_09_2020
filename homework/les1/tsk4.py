"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
 Для решения используйте цикл while и арифметические операции.
"""

num_int = int((input("Enter your number\n")))
highest_int = 1
while num_int:
    tmp = num_int % 10
    if tmp > highest_int:
        highest_int = tmp
    num_int //= 10
print(highest_int)