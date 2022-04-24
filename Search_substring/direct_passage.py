def substr_search(str, substr):
    # Прямой проход
    j, index = 0, 0
    for i in range(len(str)):
        if str[i] == substr[j]:
            j += 1
        else:
            j = 0
        if j == len(substr):
            return i - j + 1
            break

    if j != len(substr):
        return -1
