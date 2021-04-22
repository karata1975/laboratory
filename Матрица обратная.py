size = int(input('Введите размер матрицы: '))

for row in range(size):
    for col in range(size):
        if col == -row + size - 1:
            print(1, end='\t')
        elif row < -col + size:
            print(0, end='\t')
        else:
            print(2, end='\t')
    print()
