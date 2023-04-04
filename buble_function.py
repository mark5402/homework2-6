# def bubble_sort(unsort_list, ch_item_ex, ch_item_n):
def bubble_sort(unsort_list, ch_item_ex, ch_item_n):
    for i in range(len(unsort_list)):
        # print('ij')
        if i != 9:
            # print('i---', i )
            if unsort_list[i] > unsort_list[i+1]:
                # print(unsort_list[i+1])
                ch_item_ex = unsort_list[i + 1]
                unsort_list.remove(unsort_list[i+1])
                ch_item_n = unsort_list[i]
                unsort_list.remove(unsort_list[i])
                unsort_list.insert(i, ch_item_ex)
                unsort_list.insert(i+1, ch_item_n)
                # print('5', unsort_list)


    return unsort_list, ch_item_ex, ch_item_n
