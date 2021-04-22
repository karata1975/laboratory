number = int(input('Введите число: '))

print()
for row in range(number + 1):
    for col in range(number + 1):
        if row == row + col:
            print(row, end='\t')
        elif col == col + row:
            print(col, end='\t')
        elif row <= -col + number:
            print(row + col, end='\t')
    print()
