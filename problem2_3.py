cents = int(input('Сколько_у_тебя_копейек - '))
if cents >= 10:
    if cents <= 20:
        print(cents, 'копеек')
    else:
        b = cents % 10
        if b == 1:
            print(cents, 'копйка')
        elif (b >= 2) and (b <= 4):
            print(cents, 'копеек')
        else:
            print(cents, 'копеек')
elif cents < 0:
    print('Введи_нормальное_число_например_14')
else:
    if cents == 1:
        print(cents, 'копейка')
    elif (cents >= 2) and (cents <= 4):
        print(cents, 'копеек')
    else:
        print(cents, 'копеек')