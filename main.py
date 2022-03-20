from search_substring import KMP, BMH, direct_passage ,RK

def substring_navigate(k):
    if k == 1:
        direct_passage.substr_search()

    elif k == 2:
        RK.substr_search()

    elif k == 3:
        KMP.substr_search()

    elif k == 4:
        BMH.substr_search()

    else:
        raise IndexError

def sort_navigate(k):
    pass

if __name__ == '__main__':

    print('Выберите один из вариантов:')
    i = int(input('1.Сортировка\n'
                  '2.Поиск подстроки\n'
                  ))

    if i == 1:
        k = int(input('1.\n'
                      '2.\n'
                      '3.\n'
                      '4.\n'))
        sort_navigate(k)
    elif i == 2:
        k = int(input('1.Прямой обход\n'
                      '2.По алгоритму Рабина-Карпа(РК)\n'
                      '3.По алгоритму Кнута-Морриса-Пратта(КМП)\n'
                      '4.По алгоритму Бойера-Мура-Хорспула(БМХ)\n'))
        substring_navigate(k)
    else:
        raise IndexError
