print('Задача 5. Марсоход 2')

# К роботу Валли отправили ещё одного робота Билли.
# Это его первый поход на Марс,
# поэтому он тестируется в прямоугольном помещении размером 15 на 20 метров.
# Марсоход высаживается в центре комнаты (в точке 8, 10),
# после чего управление им передаётся оператору - пользователю вашей программы.
#
# Программа спрашивает
# в какую сторону оператор хочет направить робота:
# север (клавиша W),
# юг (клавиша S),
# запад (клавиша A)
# или восток (клавиша D).
#
# Оператор делает выбор,
# марсоход перемещается на 1 метр в эту сторону и программа сообщает новую позицию марсохода.
# Если марсоход упёрся в стену,
# то он не должен пытаться перемещаться в сторону стены, в этом случае его позиция не меняется.
#
# Пример:
#
# [Программа]: Марсоход находится на позиции 6, 19, введите команду:
# [Оператор]: A
# [Программа]: Марсоход находится на позиции 5, 19, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:

print(
    '\nВ какую сторону оператор хочет направить робота:\nсевер (клавиша W),\nюг (клавиша S),'
    '\nзапад (клавиша A)\nили восток (клавиша D)? ')
ask = 'WSAD' * 20
x = 8
y = 10

print()
for symbol in ask:
    print('[Программа]: Марсоход находится на позиции ', x, y, ' введите команду:')
    print('[Оператор]: ', end='')
    ask_up = input('')
    if ask_up == 'W' and y < 20:
        y += 1
    if ask_up == 'S' and y < 20:
        y -= 1
    if ask_up == 'A' and x < 15:
        x -= 1
    if ask_up == 'D' and x < 15:
        x += 1
