"""
Реализовать функцию, принимающую несколько параметров, описывающих
данные пользователя: имя, фамилия, год рождения, город проживания, email,
телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def profile_template(template: tuple):
    def profiler(items):
        profile = {}
        for name, item in zip(template, items):
            profile[name] = item
        return profile
    return profiler


profile_template_1 = profile_template(('Name', 'Surname', 'Birth_year', 'City', 'Email', 'Phone'))
user_input = input().split()
output = profile_template_1(user_input)
print(output)

