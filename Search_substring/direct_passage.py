import General_input
def substr_search():
    # Прямой проход
    str, substr = General_input.substr()
    j, index = 0, 0
    for i in range(len(str)):
        if str[i] == substr[j]:
            j += 1
        else:
            j = 0
        if j == len(substr):
            print(f'Подстрока найдена по индексу:{i-j}')
            break

    if j!= len(substr):
        print('Подстрока не найдена')