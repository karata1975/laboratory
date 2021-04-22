list_1 = [1, 2, 3, 4, 5]
print('\nИзначальный список:', list_1)

step = 1

while step <= 1:
    sdvig = list_1[-step:] + list_1[:-step]
    print('Сдвинутый список:', sdvig)
    step += 1
