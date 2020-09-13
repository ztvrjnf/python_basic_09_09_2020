"""
Реализовать структуру данных «Товары». Она должна представлять собой
список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В
кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
"""

product_template = {
    'Name': 'Введите название',
    'Price': 'Введите стоимость',
    'Quantity': 'Введите количество товара',
    'Type': 'Введите еденицы измерения количества товара'
}

while True:
    product_count = input('Введите количество товаров\n')
    if product_count.isdigit():
        product_count = int(product_count)
        break
    print('Ошибка ввода')

i = 0
product_list = []
while i != product_count:
    user_input = {}
    for key, ask in product_template.items():
        user_input[key] = input(ask+'\n')
    product_list.append((i + 1, user_input))
    i += 1

print(product_list)
"Не разобрался с аналитикой товаров"
