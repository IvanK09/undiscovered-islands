def get_horoscope(h_name, h_surname, h_favorite_animal, h_zodiac_sign):
    return 'Индивидуальный гороскоп для пользователя ' + h_name + h_surname \
            + ' Кем вы были в прошлой жизни: ' + h_favorite_animal \
            + 'Ваш знак зодиака - ' + h_zodiac_sign + ' Поэтому вы - тонко чувствующая натура'


print('Задача номер 7')
name = input('Name - ')
surname = input('Surname - ')
favorite_animle = input('Favorite_animle - ')
zodiac_sign = input('Zodiac sign - ')
horoscope = get_horoscope(name, surname, favorite_animle, zodiac_sign)
print(horoscope)
