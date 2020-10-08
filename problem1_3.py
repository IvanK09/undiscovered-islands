rub = int(input('Сколько_у_тебя_рублей - '))
if rub >= 10:
    if rub <= 20:
        print(rub, 'рублей')
    else:
        b = rub % 10
        if b == 1:
            print(rub, 'рубль')
        elif (b >= 2) and (b <= 4):
            print(rub, 'рубля')
        else:
            print(rub, 'рублей')
elif rub < 0:
    print('Введи_нормальное_число_например_14')
else:
    if rub == 1:
        print(rub, 'рубль')
    elif (rub >= 2) and (rub <= 4):
        print(rub, 'рубля')
    else:
        print(rub, 'рублей')