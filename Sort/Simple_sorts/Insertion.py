def sort(list):
    """
    При сортировке вставками массив постепенно перебирается слева направо.
     При этом каждый последующий элемент размещается так, чтобы он оказался
     между ближайшими элементами с минимальным и максимальным значением.
    :param list: исходный массив
    :return: отсортированный массив
    """

    for i in range(1, len(list)):
        current_value = list[i]
        j = i
        while j > 0 and list[j - 1] > current_value:
            list[j] = list[j - 1]
            j -= 1
        list[j] = current_value
    return list
