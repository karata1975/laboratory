# Задача 2. Сокращения
#
# В одной компании наступили «тёмные времена», и сотрудников стали сокращать. Зарплаты сотрудников хранятся в списке из
# N этих самых зарплат. Зарплаты уже уволенных сотрудников обозначаются в списке числом 0.
#
# Напишите программу, которая запрашивает у пользователя количество сотрудников и их зарплаты, затем удаляет все
# элементы списка со значением 0 и выводит в консоль, сколько сотрудников осталось, а также их зарплаты.
# Дополнительный список использовать нельзя.
#
#
# Пример:
#
# Кол-во сотрудников: 7
#
# Зарплата 1 сотрудника: 10000
#
# Зарплата 2 сотрудника: 25000
#
# Зарплата 3 сотрудника: 0
#
# Зарплата 4 сотрудника: 50000
#
# Зарплата 5 сотрудника: 60000
#
# Зарплата 6 сотрудника: 0
#
# Зарплата 7 сотрудника: 17000
#
# Осталось сотрудников: 5
#
# Зарплаты: [10000, 25000, 50000, 60000, 17000]
#
# Дополнительно: выведите на экран максимальную и минимальную зарплату оставшихся сотрудников. Для этого используйте
# функции max и min. Да, те самые, которыми нельзя называть переменные. В скобках функций просто укажите список.
#
# Пример:
#
# Максимальная зп: 60000
#
# Минимальная зп: 10000

staf_count = int(input('\nВведите кол-во сотрудников: '))
salary_list = []
count = 0

for i in range(staf_count):
    print('Зарплата', i + 1, 'сотрудника:', end=' ')
    salary = int(input())
    salary_list.append(salary)
    count += 1
    if salary == 0:
        salary_list.remove(0)
        count -= 1
print('\nОсталось сотрудников:', count)
print('Зарплаты:', salary_list)
print('Максимальная зп:', max(salary_list))
print('Минимальная зп:', min(salary_list))
