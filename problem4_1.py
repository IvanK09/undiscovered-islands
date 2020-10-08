day = int(input('Введите номер дня - '))
if day <= 5:
    print('Сегодня рабочий день')
elif day > 7:
    print('Номер дня ведён не верно')
else:
    print('Сегодня выходной')