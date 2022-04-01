import General_input


def sort():
    n, a = General_input.sort()

    for i in range(n - 1):
        minimum = min(a[i:])

        buf, a[i] = a[i], minimum

        for k in range(i + 1, n):
            if minimum == a[k]:
                a[k] = buf
                break

    print(f'Результат:{a}')
