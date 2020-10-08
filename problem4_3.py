crow = int(input('Сколько_ты_видешь_варон = '))
if crow >= 10:
    if crow <= 20:
        print(crow, 'Ворон')
    else:
        b = crow % 10
        if b == 1:
            print(crow, 'Ворона')
        elif (b >= 2) and (b <= 4):
            print(crow, 'Ворон')
        else:
            print(crow, 'Ворон')
            if crow == 0:
                print('Ворон')
elif crow < 0:
    print('Введи_нормальное_число_например_14')
else:
    if crow == 1:
        print(crow, 'Ворона')
    elif (crow >= 2) and (crow <= 4):
        print(crow, 'Ворон')
    else:
        print(crow, 'Ворон')