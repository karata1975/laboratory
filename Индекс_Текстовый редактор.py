# Задача 1. Текстовый редактор: возвращение

# Мы продолжаем участвовать в разработке нового текстового редактора и делать жизнь обычных пользователей чуть лучше.
# В этот раз у нас стоит задача сделать фишку с поиском и заменой символов в выделенной строчке. Например,
# человек что-то перечислял в тексте, но ошибся и вместо точек с запятой использовал двоеточия. Лингвисты негодуют.

# Пользователь вводит строку S. Напишите программу, которая заменяет в строке все двоеточия (:) на точки с запятой (;).
# Также подсчитайте количество замен и выведите ответ на экран (и новую строку тоже). Для решения используйте список.

# Пример:

# Введите строку: гвозди:шурупы:гайки

# Исправленная строка: гвозди;шурупы;гайки

# Кол-во замен: 2


text = input('Введите строку: ')
count = 0

word_list = text.split(':')
new_word_list = ';'.join(word_list)
print('Исправленная строка:', new_word_list)

for sym in new_word_list:
    if sym == ';':
        count += 1
print('Кол-во замен:', count)

