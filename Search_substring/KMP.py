def find_pi(substr):
    pi = [0] * len(substr)
    j = 0
    i = 1

    while i < len(substr):
        if substr[i] != substr[j]:
            if j == 0:
                pi[i] = 0
                i += 1
            else:
                j = pi[j - 1]
        else:
            pi[i] = j + 1
            i += 1
            j += 1
    return pi


def substr_search(str, substr):
    # Кнута-Морриса-Пратта
    pi = find_pi(substr)

    i, j = 0, 0
    while i < len(str):
        if str[i] == substr[j]:
            i += 1
            j += 1
            if j == len(substr):
                return i - len(substr)
        else:
            if j > 0:
                j = pi[j - 1]
            else:
                i += 1
                if i == len(str):
                    return -1
