import general_input


def sort():
    n, a = general_input.sort()

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j + 1] < a[j]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(f'Результат:{a}')
