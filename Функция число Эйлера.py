print('Задача 5. Число Эйлера')

# Напишите программу, которая находит сумму  ряда с точностью до 1e-5.

# P.S: Формулу смотреть на сайте :)

# e = 1/0! + 1/1! + 1/2! + 1/3! + ...

# Пример:

# Точность: 1e-20
# Результат: 2.7182818284590455

import math

rezult = 0
precision = 1e-5
i = 0
addmember = 1

while addmember > precision:
    addmember = 1 / math.factorial(i)
    rezult += addmember
    i += 1

print('\nРезультат: ', rezult)
