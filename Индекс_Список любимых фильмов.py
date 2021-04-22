films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']


def filmSearch(a):
    def low(e):
        return e.lower()

    films_2 = list(map(low, a))
    fav = []
    n = input('Количество фильмов: ')
    if not str(n).isdecimal():
        fav = 'Не введено количество фильмов'
        return fav
    else:
        n = int(n)
    for i in range(n):
        f = input('Название фильма: ').lower()
        if f in films_2:
            fav.append(f)
        else:
            fav = 'Такого фильма нет!'
            break
    return fav


print('Список любимых фильмов:', filmSearch(films))
