"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

num_int = (input("Enter your number\n"))
num_int2 = num_int + num_int
num_int3 = num_int2 + num_int
int(num_int)
int(num_int2)
int(num_int3)
sum_int = int(num_int3) + int(num_int2) + int(num_int)
print(sum_int)