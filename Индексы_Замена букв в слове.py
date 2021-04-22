word = input('Введите слово: ')
replace_num = int(input('Номер символа для замены: '))
replace_sum = input('Чем заменяем: ')

sum_list = []

for sym in word:
    sum_list.append(sym)

sum_list[replace_num - 1] = replace_sum

for i in sum_list:
    print(i, end='')
