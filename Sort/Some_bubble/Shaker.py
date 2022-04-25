def sort(list):
    """
    сортировка пузырьком , но в обе стороны
    :param list: исходный массив
    :return: отсортированный массив
    """
    left = 0
    right = len(list) - 1
    while left < right:
        for i in range(right, left, -1):
            # обратный проход
            if list[i] < list[i - 1]:
                list[i], list[i - 1] = list[i - 1], list[i]

        left += 1
        # прямой проход
        for i in range(left, right):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
        right -= 1

    return list
