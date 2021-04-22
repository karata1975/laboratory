print('Задача 5. Текстовый редактор')


# Мы продолжаем разрабатывать новый текстовый редактор,
# и в этот раз нам поручили написать для него код,
# который считает количество любой буквы
# и любой цифры в тексте (а не только буквы Ы как раньше).
#
# Напишите функцию count_letters,
# которая принимает на вход текст и подсчитывает,
# какое в нём количество цифр K и букв N.
#
# Функция должна вывести на экран информацию
# о найденных буквах и цифрах в определенном формате.
#
# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищём? л
#
# Количество цифр 0: 2
# Количество букв л: 1

def count_letters(text):
    count_n(number_count)
    count_l(letter_count)


def count_n(number_count):
    for i in text:
        if number == i:
            number_count += 1
    print('\nКоличество цифр', number, ':', number_count)


def count_l(letter_count):
    for j in text:
        if letter == j:
            letter_count += 1
    print('Количество букв', letter, ':', letter_count)


text = input('\nВведите текст: ')
number = input('Какую цифру ищем? ')
letter = input('Какую букву ищем? ')

number_count = 0
letter_count = 0

count_letters(text)
