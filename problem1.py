Ivan1 = int(input('Рост Бори = '))
Ivan2 = int(input('Рост Димы = '))
Ivan3 = int(input('Рост Вовы = '))

max_val = 0
mid_val = 0
low_val = 0

if Ivan1 > Ivan2:
    if Ivan1 > Ivan3:
        max_val = Ivan1
        if Ivan2 > Ivan3:
            mid_val = Ivan2
            low_val = Ivan3
        else:
            mid_val = Ivan3
            low_val = Ivan2
    elif Ivan3 > Ivan2:
        max_val = Ivan3
        mid_val = Ivan1
        low_val = Ivan2
else:
    if Ivan2 > Ivan3:
        max_val = Ivan2
        if Ivan3 > Ivan1:
            mid_val = Ivan3
            low_val = Ivan1
        else:
            mid_val = Ivan3
            low_val = Ivan1
    else:
        max_val = Ivan3
        if Ivan1 > Ivan2:
            mid_val = Ivan1
            low_val = Ivan2
        else:
            mid_val = Ivan2
            low_val = Ivan1


print(max_val)
print(mid_val)
print(low_val)



