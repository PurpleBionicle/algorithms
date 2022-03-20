from search_substring import KMP, BMH

if __name__ == '__main__':

    print('Выберите один из вариантов:')
    i = int(input('1.Сортировка\n'
                  '2.Поиск подстроки\n'
                  ))

    if i == 1:
        pass
    elif i == 2:
        k = int(input('1.Поиск подстроки по алгоритму КМП\n'
                      '2.По алгоритму БМХ\n'))
        if k == 1:
            KMP.str_search()

        elif k == 2:
            BMH.str_search()

        else:
            raise IndexError

    else:
        raise IndexError
