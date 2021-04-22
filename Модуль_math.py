import math

number = float(input('Введите вещественное число: '))

print('\nокругляет вниз: ', math.floor(number))
print('округляет вверх: ', math.ceil(number))
print('берет модуль числа: ', abs(number))
print('извлекает квадратный корень: ', math.sqrt(number))
print('возводит экспоненту в степень, равную числу: ', math.exp(number))
print('считает натуральный логарифм числа: ', math.log(number))
print('считает логарифм числа по основанию 2: ', math.log(number, 2))
print('считает логарифм числа по основанию 10: ', math.log(number, 10))
print('считает синус: ', math.sin(number / 57.2958))
print('косинус числа: ', math.cos(number / 57.2958))
print('посчитать факториал числа: ', math.factorial(int(number)))
