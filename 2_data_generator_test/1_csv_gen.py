import csv
import random

with open("data__2-39204-c5bd63.csv", 'r+', encoding='cp1251') as d:
    with open('x.txt', 'w') as f:
        d_csv = csv.DictReader(d)
        no_dubles = set()
        fio = set()
        town = set()
        # разбираем элементы в множество по полям
        for row in d_csv:
            fio.add(row['ФИО'].strip())
            town.add(row['Город'].strip())

        # преобразуем списки в листы, чтобы можно было их рандомить
        _fio = list(fio)
        _town = list(town)

        # генерируем дурацкую последовательность из задачи
        first_if = 2 * '\t' + '+' + 2 * '\t' + '+' + 2 * '\t' + '+'
        second_if = 2 * '\t' + '-' + 2 * '\t' + '-' + 2 * '\t' + '-'
        third_if = 2 * '\t' + '+' + 2 * '\t' + '-' + 2 * '\t' + '+'
        fourth_if = 2 * '\t' + '-' + 2 * '\t' + '+' + 2 * '\t' + '-'
        co = 0

        fox = [third_if, fourth_if, second_if, first_if]
        while len(no_dubles) < 100:  # нам нужна сотня уникальных элементов в множестве

            # это мы получаем строку, которую будем генерить
            for_write = str(random.choice(_fio) + "   " + random.choice(_town) + " " + random.choice(fox) + '\n')
            co += 1
            no_dubles.add(for_write)

        # пишем в файл, прости господи
        _nodubles = list(no_dubles)
        for row in _nodubles:
            f.writelines(row)
        print(_nodubles, co)

# так мы можем получить максимум 60 генераций.
# Если сделать fox = set, то получим все 100, однако придётся вводить ещё один счётчик
#         a = len(_fio)
#         b = len(_town)
#         while co < 100:
#             print(co)
#
#             if co%4 == 0:
#                 fox = first_if
#             elif co%4 == 1:
#                 fox = second_if
#             elif co%4 == 2:
#                 fox = third_if
#             else:
#                 fox = fourth_if
#             for_write = str(_fio.pop() + "   " + _town.pop() + " " + fox)
#             co += 1
#             no_dubles.add(for_write)
#             if co%b == 0:
#                 _town = town.copy()
#             if co%a == 0:
#                 _fio = fio.copy()
#
#             print(no_dubles, len(no_dubles))
