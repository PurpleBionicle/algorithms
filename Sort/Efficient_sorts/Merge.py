def merge(list1, list2):
    i, j = 0, 0
    merge_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merge_list.append(list1[i])
            i += 1
        else:
            merge_list.append(list2[j])
            j += 1

    # остатки докидываем
    while i < len(list1):
        merge_list.append(list1[i])
        i += 1
    while j < len(list2):
        merge_list.append(list2[j])
        j += 1

    return merge_list


def sort(list):
    if len(list) < 2:
        return list

    middle = int(len(list) / 2)
    left = sort(list[:middle])
    right = sort(list[middle:])

    return merge(left, right)
