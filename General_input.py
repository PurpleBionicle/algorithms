def sort():
    n = int(input('Введите длину массива:'))
    a = []
    for i in range(n):
        a.append(int(input(('Введите элемент:'))))
    return n, a


def substr():
    str = input('Введите строку:')
    substr = input('Введите подстроку:')
    return str, substr
