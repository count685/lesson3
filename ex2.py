# Задание 2

# 1) Напечатайте в консоль даты: вчера, сегодня, месяц назад
# 2) Превратите строку "01/01/17 12:10:03.234567" в объект datetime

import datetime

today = datetime.datetime.now()
print(today.strftime('%d.%m.%Y'))

yesterday = today - datetime.timedelta(days = 1)
print(yesterday.strftime('%d.%m.%Y'))

month_ago = today - datetime.timedelta(days = 31)
print(month_ago.strftime('%d.%m.%Y'))

date_test_convert = "01/01/17 12:10:03.234567"
date_dt = datetime.datetime.strptime(date_test_convert, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)