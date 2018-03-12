def selection_sort(a_list):
    len_list = len(a_list)
    for index in range(len_list - 1):
        curr_min = a_list[index]
        curr_min_index = index
        for i in range(index + 1, len_list):
            if a_list[i] < curr_min:
                curr_min = a_list[i]
                curr_min_index = i
        a_list[index], a_list[curr_min_index] = curr_min, a_list[index]

    return a_list