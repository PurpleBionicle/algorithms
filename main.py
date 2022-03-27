from search_substring import KMP, BMH, direct_passage, RK
from sort import Bubble , Shaker


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
    if k <= 4:
        if k <= 2:
            if k == 1:
                Bubble.sort()
            else:
                Shaker.sort()
        else:
            if k == 3:
                pass  # 3
            else:
                pass  # 4
    elif k <= 8:
        if k <= 6:
            if k == 5:
                pass
            else:
                pass  # 6
        else:
            if k == 7:
                pass
            else:
                pass  # 8
    else:
        raise Exception


if __name__ == '__main__':

    print('Выберите один из вариантов:')
    i = int(input('1.Сортировка\n'
                  '2.Поиск подстроки\n'
                  ))

    if i == 1:
        k = int(input('1.Сортировка пузырьком\n'
                      '2.Сортировка перемешиванием\n'
                      '3.Сортировка расчёской\n'
                      '4.Сортировка вставками\n'
                      '5.Сортировка выбором\n'
                      '6.Быстрая сортировка\n'
                      '7.Сортировка слиянием\n'
                      '8.Пирамидальная сортировка\n'))
        sort_navigate(k)
    elif i == 2:
        k = int(input('1.Прямой обход\n'
                      '2.По алгоритму Рабина-Карпа(РК)\n'
                      '3.По алгоритму Кнута-Морриса-Пратта(КМП)\n'
                      '4.По алгоритму Бойера-Мура-Хорспула(БМХ)\n'))
        substring_navigate(k)
    else:
        raise IndexError
