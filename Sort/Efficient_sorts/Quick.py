def sort(list):
    """
    Метод основан на двоичном дерево
    :param list: исходный массив
    :return: отсортированный массив
    """
    items_lower = []
    items_greater = []

    if len(list) <= 1:
        return list
    root = list.pop()

    for item in list:
        if item >= root:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return sort(items_lower) + [root] + sort(items_greater)
