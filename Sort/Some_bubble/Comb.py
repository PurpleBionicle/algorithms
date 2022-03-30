import General_input


def sort():
    n, a = General_input.sort()

    POOLING_FACTOR = 1.247

    step = int((len(a) - 1) / POOLING_FACTOR)

    while step >= 1:
        for i in range(len(a) - step):
            if a[i] > a[i + step]:
                a[i], a[i + step] = a[i + step], a[i]
        step = int(step / POOLING_FACTOR)

    for i in range(n - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]

    print(f'Результат:{a}')
