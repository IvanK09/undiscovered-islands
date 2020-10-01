# посмотреть что такое область видимости
def conditional_func(condition, func_true, func_false, val):
    condition_result = condition(val)
    if condition_result:
        return func_true(val)
    else:
        return func_false(val)


x = float(input('X = '))


result = conditional_func(lambda var: (var >= 2), lambda var: var, lambda var: (var ** 2 - 3), x)
print(result)

result = conditional_func(lambda var: (var < -1), lambda var: var ** 3 + 5, lambda var: (2 - var), x)
print(result)

result = conditional_func(lambda var: (var > 5), lambda var: var ** 2 + 1, lambda var: (3 - var), x)
print(result)

if x >= 2:
    print(x)
else:
    print(x ** 2 - 3)

if x < -1:
    print(x ** 3 + 5)
else:
    print(2 - x)

if x > 5:
    print(x ** 2 + 1)
else:
    print(3 - x)
