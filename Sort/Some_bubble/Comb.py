def sort(list):
    POOLING_FACTOR = 1.247

    step = int((len(list) - 1) / POOLING_FACTOR)

    while step >= 1:
        for i in range(len(list) - step):
            if list[i] > list[i + step]:
                list[i], list[i + step] = list[i + step], list[i]
        step = int(step / POOLING_FACTOR)

    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]

    return list
