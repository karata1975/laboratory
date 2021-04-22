number = int(input('Введите число: '))

for i in range(0, number + 1):
    for j in range(0, number + 1):
        print(i + j, end='\t')
    print()
