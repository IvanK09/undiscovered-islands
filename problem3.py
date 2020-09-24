from problem_helper import read_int_param


def speed_calculation(distance, time_x, time_y, speed_delta_yx):
    speed_x = (distance - time_y * speed_delta_yx) / (time_x + time_y)
    speed_y = speed_x + speed_delta_yx
    return speed_x, speed_y


def read_input_data():
    print('Введите следующие данные для задачи:')
    distance = read_int_param("общее расстояние (км) S = ")
    time_x = read_int_param('время первой части пути (ч) x = ')
    time_y = read_int_param('время второй части пути (ч) y = ')
    speed_delta_yx = read_int_param('разницу скоростей (км/ч)  z = ')
    return distance, time_x, time_y, speed_delta_yx


S, x, y, z = read_input_data()

max_time = max(x, y)

if (max_time * z) >= S:
    print('при данных параметрах S=', S, ' x=', x, ' y=', y, ' z=', z, 'задачу решить нельзя')
    exit(1)


vx, vy = speed_calculation(S, x, y, z)

if vx < vy:
    print('машина ехала на', '%.1f' % vx, ',км быстрее чем в первый раз')
elif vx > vy:
    print('машина ехала на', '%.1f' % vy, ',км быстрее чем в первый раз')
