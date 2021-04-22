height = float(input('Рост пациента: '))
ves = float(input('Введите вес пациента: '))

index = round(ves / height ** 2, 2)

if index < 18.5:
    print('\nНе добор массы тела.')
elif index < 25:
    print('\nМасса тела в норме.')
elif index < 30:
    print('\nИдёт избыток массы тела.')
else:
    print('\nУ вас ожирение.')
