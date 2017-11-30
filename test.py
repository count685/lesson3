import csv

answers = {'привет': 'и тебе привет!', 'как дела': 'лучше всех', 'что нового': 'Ничего особого'}

list_dict = []
for key, value in answers.items():
    new_dic = dict({'ключ': key, 'значение': value})
    list_dict.append(new_dic)
print(list_dict)


with open('answers1.csv', 'w', encoding='utf-8') as f:
    fields = ['ключ', 'значение']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for k in list_dict:
        writer.writerows(k)      # не могу понять почему вылетает ошибка....
