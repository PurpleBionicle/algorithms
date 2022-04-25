def sort(list):
    """
    Метод кучи основан на двоичном дерево и извлечение оттуда элементом
    с последующей перестройкой дерева
    :param list: исходный массив
    :return: отсортированный массив
    """

    build_max_heap(list)
    for i in range(len(list) - 1, 0, -1):
        list[0], list[i] = list[i], list[0]
        max_heapify(list, index=0, size=i)

    return list


def parent(i):
    """
    :param list: индекс
    :return: индекс родителя
    """
    return (i - 1) // 2


def left(i):
    """
    :param list: индекс
    :return: индекс левого ребенка
    """
    return 2 * i + 1


def right(i):
    """
    :param list: индекс
    :return: индекс правого ребенка
    """
    return 2 * i + 2


# строит кучу
def build_max_heap(alist):
    """
    Построение дерева
    """
    length = len(alist)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(alist, index=start, size=length)
        start = start - 1


def max_heapify(alist, index, size):
    """
    Нахождение максимального элемента кучи
    """
    l = left(index)
    r = right(index)
    if (l < size and alist[l] > alist[index]):
        largest = l
    else:
        largest = index
    if (r < size and alist[r] > alist[largest]):
        largest = r
    if (largest != index):
        alist[largest], alist[index] = alist[index], alist[largest]
        max_heapify(alist, largest, size)
