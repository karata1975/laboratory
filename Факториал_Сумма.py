print('Задача 6. Сумма факториалов')

# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N!


N = int(input('Введите число: '))
N1 = 1
count_N1 = 0

for i in range(2, N + 1):
    N1 *= i
    for j in range(N1):
        count_N1 += 1
print('Сумма факториалов равна ', count_N1)

# N1 - факториал.
# i - переменная цикла.
# j - переменная цикла.
