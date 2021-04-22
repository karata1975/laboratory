def reverse_float(num):
    parts = str(num).split('.')
    reversed_parts = [''.join(reversed(part)) for part in parts]

    return float('.'.join(reversed_parts))


number1 = reverse_float(input('Введите первое число: '))
number2 = reverse_float(input('Введите второе число: '))

print('Первое число наоборот:', number1)
print('Второе число наоборот:', number2)
print('Сумма:', number1 + number2)

# ______________________________________________________

# def reverse_float(num):
# parts = str(num).split('.')
# reversed_parts = [''.join(reversed(part)) for part in parts]

# return float( '.'.join(reversed_parts) )

# a = reverse_float(input('a'))
# b = reverse_float(input('b'))

# print('rvs a', a)
# print('rvs b', b)
# print('total', a + b)
