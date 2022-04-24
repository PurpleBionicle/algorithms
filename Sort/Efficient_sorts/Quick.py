def sort(list):
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
