weight, box_count, new_box = 0, [int(input('Введите вес контейнера: '))
                                 for _ in range(int(input('Кол-во контейнеров: ')))], \
                             int(input('Введите вес нового контейнера: '))

while weight < len(box_count) and box_count[weight] >= new_box:
    weight += 1
print('\nНомер, куда встанет новый контейнер:', weight + 1)
