def substr_search(str, substr):
    """
    Метод основан на словаре смещений - насколько можно двигаться ,исходя
    из конца проверяемой подстроки
    :param  строки и подстрока
    :return: индекс 1 элемента подстроки
    """

    substr_set = set()
    substr_shift = {}  # словарь
    len_of_sub = len(substr)

    """ Создание словаря смещений"""
    for i in range(len_of_sub - 2, -1, -1):
        if substr[i] not in substr_set:
            substr_shift[substr[i]] = len_of_sub - i - 1
            substr_set.add(substr[i])

    if substr[-1] not in substr_set:
        substr_shift[substr[-1]] = len_of_sub

    substr_shift['*'] = len_of_sub

    """Поиск построки"""

    if len_of_sub <= len(str):
        i = len_of_sub - 1

        while i < len(str):
            k = 0
            j = 0
            flag_of_find = False
            for j in range(len_of_sub - 1, -1, -1):
                if str[i - k] != substr[j]:
                    if j == len_of_sub - 1:  # если последний знак подстроки
                        off = substr_shift[str[i]] if substr_shift.get(str[i], False) \
                            else substr_shift['*']
                    else:
                        off = substr_shift[substr[j]]
                    i += off
                    flag_of_find = True
                    break

                k += 1

            if not flag_of_find:
                return i - k + 1
        return -1

    return -1
