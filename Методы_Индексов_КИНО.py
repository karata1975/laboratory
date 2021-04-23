# Задача 3. Кино
#
# Мы поддерживаем свой киносайт и хотим сделать так, чтобы пользователи после регистрации могли создать
# собственный рейтинг фильмов из тех, которые есть на сайте. Вот сам список фильмов (конечно же, можете брать свои):
#
#
# films = [
#
#     'Крепкий орешек', 'Назад в будущее', 'Таксист',
#
#     'Леон', 'Богемская рапсодия', 'Город грехов',
#
#     'Мементо', 'Отступники', 'Деревня',
#
#     'Проклятый остров', 'Начало', 'Матрица'
#
# ]
#
#
# Напишите программу, которая позволяет добавлять в свой рейтинг фильмы, удалять их оттуда,
# а также вставлять на нужное пользователю место. Обеспечьте контроль ввода и сделайте так,
# чтобы в список нельзя было добавить один и тот же фильм несколько раз.
#
#
# Пример:
#
# Ваш текущий топ фильмов: []
#
# Название фильма: Леон
#
# Команды: добавить, вставить, удалить
#
# Введите команду: добавить
#
#
# Ваш текущий топ фильмов: [‘Леон’]
#
# Название фильма: Леон
#
# Команды: добавить, вставить, удалить
#
# Введите команду: добавить
#
# Этот фильм уже есть в вашем списке.
#
#
# Ваш текущий топ фильмов: [‘Леон’]
#
# Название фильма: Матрица
#
# Команды: добавить, вставить, удалить
#
# Введите команду: добавить
#
#
# Ваш текущий топ фильмов: [‘Леон’, ‘Матрица’]
#
# Название фильма: Леон
#
# Команды: добавить, вставить, удалить
#
# Введите команду: удалить
#
#
# Ваш текущий топ фильмов: [‘Матрица’]
#
# Название фильма: …..


def menu(film, film_list):
    for i_film in film_list:
        if i_film == film:
            return True
    return False


films = [

    'Крепкий орешек', 'Назад в будущее', 'Таксист',

    'Леон', 'Богемская рапсодия', 'Город грехов',

    'Мементо', 'Отступники', 'Деревня',

    'Проклятый остров', 'Начало', 'Матрица'

]

top_films = []

while True:
    print('Ваш текущий топ фильмов:', top_films)
    new_film = input('Название фильма: ')
    if menu(new_film, films):
        print('Команды: добавить, вставить, удалить')
        command = input('Введите команду: ')
        if command == 'добавить':
            top_films.append(new_film)
        if command == 'удалить':
            if menu(new_film, top_films):
                top_films.remove(new_film)
            else:
                print('Такого фильма нет!')
        if command == 'вставить':
            index = int(input('На какое место? '))
            top_films.insert(index - 1, new_film)
    else:
        print('Такого фильма нет на сайте!')
