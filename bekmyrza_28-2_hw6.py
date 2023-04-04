# #ДЗУрок6 Дэдлайн 26.03.2023 23 59
# ДЗ*:
# 1. Написать функцию bubble_sort или selection_sort,
# принимающую в качестве входящего параметра не отсортированный список.
# 2. Алгоритм функции должен сортировать список методом пузырьковой сортировки или методом сортировки выбором.
# 3. Функция в итоге должна возвращать отсортированный список.
# Применить 1 раз данную функцию
# 4. Написать функцию binary_search,
# принимающую в качестве входящего параметра элемент для поиска и список в котором необходимо искать.
# 5. Алгоритм должен искать с помощью двоичного поиска,
# изображенного на блок-схеме презентации.
# 6. Функция в итоге должна распечатать результат.
# Применить 1 раз эту функцию

import random
from random import randint, choice
from buble_function import bubble_sort
from selection_function import selection


unsort_list = []
while len(unsort_list) != 10:
    item = random.randint(1, 300)

    unsort_list.append(item)

# print(unsort_list)


selection(unsort_list)



sort_finish = 0
while sort_finish == 0:
    bubble_sort(unsort_list, 0, 0)
    print(unsort_list)
    # selection(unsort_list)
    if unsort_list == sorted(unsort_list):
        sort_finish = 1

# selection(unsort_list)

print('finally', unsort_list)


