for row in range(20 + 1):
    for coin in range(30 + 1):
        if row == 0:
            print('-', end='')
        elif coin == 0:
            print('|', end='')
        elif coin == 30:
            print('|', end='')
        else:
            print(' ', end='')
    print()
