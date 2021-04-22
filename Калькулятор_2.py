x = '+'
C = 0

while x == '+' or x == '-' or x == '*' or x == '/':
    x = input('\nВыберите операцию: ')
    A = int(input('Введите первое число: '))
    B = int(input('Введите второе число: '))
    print()
    if x == '+':
        C = A + B
        print(A, '+', B, '=', C)
    elif x == '-':
        C = A - B
        print(A, '-', B, '=', C)
    elif x == '*':
        C = A * B
        print(A, '*', B, '=', C)
    elif x == '/':
        C = A / B
        print(A, '/', B, '=', C)
else:
    print('Ошибка: такой операции не существует. Попробуйте ещё раз.')
