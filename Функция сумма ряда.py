print('Задача 9. Сумма ряда')


# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)

# e = 1 - x ** 2 / 2! + x ** 4 / 4! - x ** 6 / 6! + ...


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709

def sum_of_series(precision, x):
    previous = i = 0
    current = fn = xn = 1
    while abs(current - previous) > precision:
        previous = current
        xn *= x * x
        i += 1
        fn *= 2 * i * (2 * i - 1)
        current += (-1 if i % 2 else 1) * xn / fn
    return current


precision = float(input('\nВведите точность: '))
x = float(input('\nВведите x: '))

print('Сумма ряда: ', sum_of_series(precision, x))
