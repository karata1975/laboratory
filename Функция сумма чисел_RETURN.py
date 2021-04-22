def summa_N(N):
    count = 0
    for i in range(1, N + 1):
        count += i
    return count


N = int(input('Введите число: '))

total_N = summa_N(N)
total_N2 = summa_N(total_N)

print('\nСумма от 1 до', N, '=', total_N)
print('Сумма от 1 до', total_N, '=', total_N2)
