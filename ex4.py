# Задание 4

# Возьмите словарь с ответами из функции get_answer
# Запишите его содержимое в формате csv в формате: "ключ"; "значение". Каждая пара ключ-значение должна располагаться на отдельной строке

import csv

answers = {'привет': 'и тебе привет!', 'как дела': 'лучше всех', 'что нового': 'Ничего особого'}

with open('answers.csv', 'w', encoding='utf-8') as f:
    fields = ['ключ', 'значение']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    list_dict = []
    for key, value in answers.items():
        new_dic = dict({'ключ': key, 'значение': value})
        list_dict.append(new_dic)
    writer.writerows(list_dict)
