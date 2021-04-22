lower = int(input('Введите первое число: '))
upper = int(input('Введите второе число: '))
count = 0

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
