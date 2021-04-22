# Задача 2. Цифры больше пяти

# Пользователь вводит последовательность из N чисел. Напишите программу,
# которая подсчитывает общее количество цифр больше пяти во всей последовательности.

number_all = int(input('Сколько будет цифр: '))
numiral = int(input('Введите контрольное число: '))
n_cout = 0

while numiral < 0 or numiral > 9:
    numiral = int(input('Неправильный ввод, введите числа в последовательности от 0 до 9: '))

for num in range(1, number_all + 1):
    print(num, ': Введите число: ', end='')
    number = int(input())
    while number > numiral:
        if number % 10 > numiral:
            n_cout += 1
        number //= 10
print('Общее количество цифр больше', numiral, '=', n_cout)
