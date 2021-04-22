print('Задача 10. Яма ')

# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
#
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345


number = int(input('Введите число: '))

print()
for line in range(number):
    for left in range(number, number - line - 1, -1):
        print(left, end='')
    point = 2 * (number - line - 1)
    print('.' * point, end='')
    for right in range(number - line, number + 1):
        print(right, end='')
    print()
