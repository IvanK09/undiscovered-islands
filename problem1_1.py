print('Тест на знание даты начала Великой Отечественной Войны.')

def read_input_data():
    print('Введите следующие данные для задачи:')
    month = input('Впишите Месяц - ')
    day = input('Впишите День - ')
    year = input('Впишите Год - ')
    return month, year, day


month, year, day = read_input_data()

if year == '1941':
    if day == '22':
        if month == 'июнь':
            print('Вы прошли тест')
else:
    print('при данных параметрах month =', month, 'day = ',day, ' year =', year,'задачу решить нельзя')
    exit(1)





