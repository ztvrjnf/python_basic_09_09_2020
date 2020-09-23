"""
Необходимо создать (не программно) текстовый файл, где каждая строка
описывает учебный предмет и наличие лекционных, практических и лабораторных
занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь, содержащий
название предмета и общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр)

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

subj = {}
with open('task6.txt', 'r', encoding="utf-8") as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        print(subject)
        subj[subject] = 0
        try:
            subj[subject] += int(lecture)
        except ValueError:
            _ = 1
        try:
            subj[subject] += int(lab)
        except ValueError:
            _ = 1
        try:
            subj[subject] += int(practice)
        except ValueError:
            _ = 1
    print(f'Общее количество часов по предметам - \n {subj}')
