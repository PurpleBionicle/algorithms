
def str_search():
    global j
    str = input('Введите строку:')
    substr = input('Введите подстроку:')

    substr_set = set()
    substr_shift = {}  # словарь
    len_of_sub = len(substr)

    """ Создание словаря смещений"""
    for i in range(len_of_sub - 2, -1, -1):
        if i not in substr_set:
            substr_set.add(substr[i])
            substr_shift[substr[i]] = len_of_sub - i - 1

    if substr[-1] not in substr_set:
        substr_shift[substr[-1]] = len_of_sub

    substr_shift['*'] = len_of_sub

    """Поиск построки"""
    i=len_of_sub
    while i <len(str):
        k=0
        for j in range(len_of_sub-1,-1,-1):
            if str[i-k] != substr[j]:
                if j==len_of_sub-1: # если последний знак подстроки
                    off= substr_shift[str[i]] if substr_shift.get(str[i],False) \
                        else substr_shift['*']
                else:
                    off= substr_shift[substr[j]]
                i+=off
                break

            k+=1

        if j==0:
            print(f'Найдена подстрока с индексом {i-k+1}')
            break

