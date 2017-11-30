# Задание 3 

# 1) Скачайте файл по ссылке
# 2) Прочитайте его и подсчитайте количество слов в тексте

# Вариант 1
with open('referat.txt', 'r', encoding='utf-8') as ref: 
    content = ref.read()
    print(len(content))

# Вариант 2
with open('referat.txt', 'r', encoding='utf-8') as ref_2:
    content_count_list = []
    for ref_2_line in ref_2:
        ref_2_line = len(str(ref_2_line))
        content_count_list.append(ref_2_line)
    print(sum(content_count_list))
