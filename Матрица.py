size = int(input('Введите размер матрицы: '))

for row in range(size):
    for col in range(size):
        if row < col:
            print(0, end='\t')
        elif row > col:
            print(2, end='\t')
        else:
            print(1, end='\t')
    print()
