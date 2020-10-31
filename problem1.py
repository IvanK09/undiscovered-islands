s = input('Введите число в двоичной системе - ')
cou = 0
for i in str(s):
    if i == "1":
        cou = cou + 1
count = 0
for i in str(s):
    if i == "0":
        count = count + 1
print('Нулей -',count)
print('Едениц -',cou)
