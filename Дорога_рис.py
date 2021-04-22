for row in range(20 + 1):
    for col in range(50 + 1):
        if row == 10:
            print('-', end='')
        elif col == row + 30:
            print('\\', end='')
        elif col == -row + 20:
            print('/', end='')
        elif col == 25:
            print('|', end='')
        else:
            print(' ', end='')
    print()
