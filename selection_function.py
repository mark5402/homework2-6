
def selection(unsort_list):
    # min = 1


    print(f'unsi: {unsort_list}')
    min = unsort_list[0]
    print('min', min)
    max = 0
    print('max', max)
    i = 0
    for i in range(len(unsort_list)):
        print(f'unsi 1: {unsort_list}')
        print(i)
        # print(f'i: {i}')
        # for j in range(len(unsort_list)):
        #     print(f'unsort_list[i] {unsort_list[i]}')
        #     print(f'unsort_list[j] {unsort_list[j]}')
        #     if unsort_list[j] < unsort_list[i]:
        #         print(f'j: {j}')
        #         print(f'unsj: {unsort_list}')
        #         print(f'unsort_list[i] {unsort_list[i]}')
        #         min = unsort_list[j]
        #         print(f'min: {min}')
        #         print(f'unsj: {unsort_list}')
        #         unsort_list[i] = min
        #     print(f'uns3: {unsort_list}')
        #     print(f'min: {min}')
        #     print(f'uns3: {unsort_list}')
        # for j in range(len(unsort_list)):
        #     if unsort_list[j] > min:
        #
        if unsort_list[i] < unsort_list[0]:
            max = unsort_list[0]
            unsort_list[0] = unsort_list[i]
            unsort_list[i] = max
            print('uns list i 2: ', unsort_list[i])
            print('uns list 0: ', unsort_list[0])
            print('min', min)
            print('max', max)
            print('uns list: ', unsort_list)
    i += 1
    return unsort_list, min, max
