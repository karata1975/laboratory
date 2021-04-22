print('Задача 1. Конвертация')

# При покупках за рубежом
# с помощью карты банки делают конвертацию через промежуточную валюту.

# Например,
# если купить что-то в евро,
# то сначала эта сумма конвертируется в доллары, а уже потом - в рубли.
#
# Напишите программу,
# которая получает на вход стоимость покупки в евро,
# затем выводит ответ в рублях.
#
# Мы живём в альтернативной реальности,
# где 1 евро = 1.25 доллара, а 1 доллар = 60.87 рублей.

shopping = float(input('Стоимость покупки в евро: '))
evro = 1.25
dollar = 60.87

konvert_dollar = round(shopping * evro, 2)
konvert_evro = round(konvert_dollar * dollar, 2)

print('\nСтоимость покупки в рублях равна', konvert_evro)
