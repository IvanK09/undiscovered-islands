print('Тест_на_знание_даты_основания Санкт-Петербурга')

def read_input_data():
    print('Введите следующие данные для задачи:')
    month = input('Впишите Месяц - ')
    day = input('Впишите День - ')
    year = input('Впишите Год - ')
    return month, year, day


month, year, day = read_input_data()

if year == '1703':
    if day == '27':
        if month == 'май':
            print('Вы прошли тест')
else:
    print('при данных параметрах month =', month, 'day = ',day, ' year =', year,'задачу решить нельзя')
    exit(1)

