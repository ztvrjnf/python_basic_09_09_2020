"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

my_file = open('task2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('task2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('task2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    word_count = content[i]
    word_count = word_count.split()
    print(f'Количество слов в {i + 1} строке {len(word_count)}')
my_file = open('task2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()
