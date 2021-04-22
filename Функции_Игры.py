print('Задача 9. Недоделка')


# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
#
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
#
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
#
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
#
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
#
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
#
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.


def rock_paper_scissors():
    player = int(input('\nВведите соответствующее число: 1-камень, 2-ножницы, 3-бумага: \n'))
    if player == 1 or player == 2 or player == 3:
        comp(player, comp)
    else:
        print('Ошибка ввода!')


def comp(player, comp):
    comp = random.randint(1, 3)
    if player == 1 and comp == 1:
        print('Ничья!')
    elif player == 1 and comp == 2:
        print('Игрок победил!')
    elif player == 1 and comp == 3:
        print('Игрок проиграл!')
    if player == 2 and comp == 1:
        print('Игрок проиграл!')
    elif player == 2 and comp == 2:
        print('Ничья!')
    elif player == 2 and comp == 3:
        print('Игрок победил!')
    if player == 3 and comp == 1:
        print('Игрок победил!')
    elif player == 3 and comp == 2:
        print('Игрок проиграл!')
    elif player == 3 and comp == 3:
        print('Ничья!')


def guess_the_number(player, comp):
    player = int(input('Введите любое число от 1 до 3: '))
    comp = random.randint(1, 3)
    if player == comp:
        print('Игрок выйграл!')
    else:
        print('Игрок проиграл!')


def mainMenu(ask_menu):
    print('\nВыберите игру: ')
    print('1 - Камень, ножницы, бумага')
    print('2 - Угадай число\n', end='')
    ask_menu = int(input())
    if ask_menu == 1:
        rock_paper_scissors()
    elif ask_menu == 2:
        guess_the_number(player, comp)
    else:
        print('Ошибка ввода!')
        mainMenu(ask_menu)


import random

ask_menu = 0
player = 0

mainMenu(ask_menu)

while True:
    ask = input('\nВы хотите сыграть ещё: да\нет: ')
    if ask == 'да':
        mainMenu(ask_menu)
    else:
        break
print('\nКонец игры!')
