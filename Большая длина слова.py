print('Задача 7. Великий и могучий')

# Паоло изучает русский язык: занимается по учебникам, читает книги, слушает музыку.
# Особенно Паоло понравилась книга “Преступление и наказание”.
# И ему стало интересно,
# какое можно найти самое длинное слово в этой книге, чтобы потом сравнить его с аналогом на своём языке.
#
# Напишите программу,
# которая получает на вход текст и находит длину самого длинного слова в нём.
# Слова в тексте разделяются одним пробелом.
#
# Пример:
# Введите текст: Меня зовут Петр
# Длина самого длинного слова: 5

print('Введите текст: ', end='')
text = input()
symbol = 0
word_max = 0

for i in text:
    if i != ' ':
        symbol += 1
    else:
        symbol = 0
    if symbol > word_max:
        word_max = symbol
print('\nДлина самого длинного слова: ', word_max)
