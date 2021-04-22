a = int(input('Введите перовое число: '))
c = input('Введите действие: ')
b = int(input('Введите второе число: '))

for i in c:
    if i == '+':
        print('\nОтвет = ', a + b)
    elif i == '-':
        print('\nОтвет = ', a - b)
    elif i == '*':
        print('\nОтвет = ', a * b)
    else:
        print('\nОтвет = ', a / b)
