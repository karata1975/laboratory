print('Задача 9. Пирамидка 2')

# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран, заполняя нечётными числами вот так:

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29


level = int(input('Введите количество уровней пирамиды: '))
number = 1

print()
for line in range(level):
    space = level - line - 1
    print('   ' * space, end='')
    for num in range(line + 1):
        print(number, end='    ')
        number += 2
    print()
