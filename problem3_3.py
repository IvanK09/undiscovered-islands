years = int(input('Сколько_тебе_Лет_Или_Годов - '))
if years >= 10:
    if years <= 20:
        print(years, 'Лет')
    else:
        b = years % 10
        if b == 1:
            print(years, 'Год')
        elif (b >= 2) and (b <= 4):
            print(years, 'Года')
        else:
            print(years, 'Лет')
            if years == 0:
                print('Годов')
elif years < 0:
    print('Введи_нормальное_число_например_14')
else:
    if years == 1:
        print(years, 'Год')
    elif (years >= 2) and (years <= 4):
        print(years, 'Года')
    else:
        print(years, 'Лет')
