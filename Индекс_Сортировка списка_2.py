def selection_sort(my_list):
    for i_mn in range(len(my_list)):
        for curr in range(i_mn, len(my_list)):
            if my_list[curr] < my_list[i_mn]:
                my_list[curr], my_list[i_mn] = my_list[i_mn], my_list[curr]


list_item = [1, 4, -3, 0, 10]
print('\nИзначальный список:', list_item)

selection_sort(list_item)

print('Отсортированный список:', list_item)
