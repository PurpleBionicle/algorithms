from _ast import Import

import Sort.Some_bubble.Bubble
from Search_substring import KMP, BMH, direct_passage, RK
from Sort.Simple_sorts import Insertion
from Sort.Some_bubble import Bubble, Comb, Shaker


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
    if k == 1:
        i = int(input('1.Сортировка пузырьком\n'
                      '2.Сортировка перемешиванием\n'
                      '3.Сортировка расчёской\n'))
        if i==1:
            Sort.Some_bubble.Bubble.sort()
        elif i==2:
            Sort.Some_bubble.Shaker.sort()
        elif i==3:
            Sort.Some_bubble.Comb.sort()
        else:
            raise Exception

    elif k == 2:
        i = int(input('1.Сортировка вставками\n'
                      '2.Сортировка выбором\n'))
        if i==1:
            Sort.Simple_sorts.Insertion()
        elif i==2:
            pass
        else:
            raise Exception


    elif k == 3:
        i = int(input('1.Быстрая сортировка\n'
                      '2.Сортировка слиянием\n'
                      '3.Пирамидальная сортировка\n'))

    else:
        raise Exception


if __name__ == '__main__':

    print('Выберите один из вариантов:')
    i = int(input('1.Сортировка\n'
                  '2.Поиск подстроки\n'
                  ))

    if i == 1:
        k = int(input('1.Пузырьковые сортировки\n'
                      '2.Простые сортировки\n'
                      '3.Эффективные сортировки\n'))
        sort_navigate(k)
    elif i == 2:
        k = int(input('1.Прямой обход\n'
                      '2.По алгоритму Рабина-Карпа(РК)\n'
                      '3.По алгоритму Кнута-Морриса-Пратта(КМП)\n'
                      '4.По алгоритму Бойера-Мура-Хорспула(БМХ)\n'))
        substring_navigate(k)
    else:
        raise IndexError
