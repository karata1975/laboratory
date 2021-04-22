s = input('Введите слово: ')
print('Кол-во уникальных букв:', len([i for i in set(s) if s.count(i) == 1]))
