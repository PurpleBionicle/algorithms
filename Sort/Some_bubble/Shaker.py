import General_input
def sort():
    n,a = General_input.sort()
    left = 0
    right = n-1
    while left<right:
        for i in range(right , left, -1):
            # обратный проход
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]

        left+=1
            # прямой проход
        for i in range(left,right):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        right-=1

    print(f'Результат:{a}')
