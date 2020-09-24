from problem_helper import read_float_param


print('Задача номер 6')
piece_count = read_float_param('Количество Штук - ')
price_per_piece = read_float_param('Стоймасть_одной_штуки - ')
spend_per_piece = read_float_param('Одна_Штука_Расход - ')
Profit = (price_per_piece - spend_per_piece) * piece_count
print('Прибыль = ', Profit)
