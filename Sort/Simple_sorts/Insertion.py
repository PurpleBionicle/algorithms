import General_input

def sort():
    n, a = General_input.sort()

    for i in range(1, n):
        current_value = a[i]
        j = i
        while j > 0 and a[j - 1] > current_value:
            a[j] = a[j - 1]
            j -= 1
        a[j] = current_value
    print(f'Результат:{a}')
