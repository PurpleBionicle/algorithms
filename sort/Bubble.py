import general_input
def sort():
    n,a= general_input.sort()

    for i in range(n - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]

    print(f'Результат:{a}')
