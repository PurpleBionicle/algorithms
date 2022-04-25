def sort(list):
    """
    сортировка пузырьком
    :param list: исходный массив
    :return: отсортированный массив
    """
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j + 1] < list[j]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list
