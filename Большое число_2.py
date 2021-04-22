print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

number_all = int(input('Сколько будет цифр: '))
max_number = 0
max_sum = 0

print()
for num in range(1, number_all + 1):
    print(num, ':', 'Введите число: ', end=' ')
    number = int(input())
    summ = 0
    current_n = number  # текущее число
    while number > 0:
        summ += number % 10
        number //= 10
    if summ > max_sum:
        max_sum = summ
        max_number = current_n
print()
print('Число:', max_number, 'имеет максимальную сумму цифр: ', max_sum)
