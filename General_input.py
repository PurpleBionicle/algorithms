def sort():
    "Функция запрашивает у пользователя исходный массив"
    n = int(input('Введите длину массива:'))
    a = []
    for i in range(n):
        a.append(int(input(('Введите элемент:'))))
    return a


def substr():
    "Функция запрашивает у пользователя строку и подстрооку"
    str = input('Введите строку:')
    substr = input('Введите подстроку:')
    return str, substr
