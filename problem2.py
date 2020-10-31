n = str(input("Введите число в двоичной системе - "))
is_binary = True#Изначально
for a in n:#Цикл
    if a.isdigit():#True если (а) полностью число если да то True если нет то False
        if a in ["1", "0"]:#True если в нём число 1 или 0 если да то True если нет то False
            continue
        else:
            is_binary = False
            break
    else:
        is_binary = False
        break
if is_binary:#True
    print('Я потратил на это 4 часа и это работает')
else:#False
    print('Пожалуйста введите число в ДВОИЧНОЙ СИСТЕМЕ')


