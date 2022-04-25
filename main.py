import General_input
import Sort
from Search_substring import KMP, BMH, direct_passage, RK
from Sort.Efficient_sorts import Heap, Merge, Quick
from Sort.Simple_sorts import Insertion, Selection
from Sort.Some_bubble import Bubble, Comb, Shaker


def print_answer(answer):
    print(f"результат={answer}")


def substring_navigate(k):
    ":param k: определяет какая функция-поиска подстроки будет вызываться"
    str, substr = '', ''
    answer = ''
    if k != 0:
        str, substr = General_input.substr()
    if k == 1:
        answer = direct_passage.substr_search(str, substr)

    elif k == 2:
        answer = RK.substr_search(str, substr)

    elif k == 3:
        answer = KMP.substr_search(str, substr)

    elif k == 4:
        answer = BMH.substr_search(str, substr)

    elif k == 0:
        pass

    else:
        raise IndexError

    print_answer(answer)


def sort_navigate(k):
    ":param k: определяет какая функция-сортировка будет вызываться"
    list = []
    answer = []
    if k != 0:
        list = General_input.sort()

    if k == 1:
        i = int(input('1.Сортировка пузырьком\n'
                      '2.Сортировка перемешиванием\n'
                      '3.Сортировка расчёской\n'))
        if i == 1:
            answer = Sort.Some_bubble.Bubble.sort(list)
        elif i == 2:
            answer = Sort.Some_bubble.Shaker.sort(list)
        elif i == 3:
            answer = Sort.Some_bubble.Comb.sort(list)
        else:
            raise Exception

    elif k == 2:
        i = int(input('1.Сортировка вставками\n'
                      '2.Сортировка выбором\n'))
        if i == 1:
            answer = Sort.Simple_sorts.Insertion.sort(list)
        elif i == 2:
            answer = Sort.Simple_sorts.Selection.sort(list)
        else:
            raise Exception

    elif k == 3:
        i = int(input('1.Быстрая сортировка\n'
                      '2.Сортировка слиянием\n'
                      '3.Пирамидальная сортировка\n'))
        if i == 1:
            answer = Sort.Efficient_sorts.Quick.sort(list)
        elif i == 2:
            answer = Sort.Efficient_sorts.Merge.sort(list)
        elif i == 3:
            answer = Sort.Efficient_sorts.Heap.sort(list)
        else:
            raise Exception

    elif k == 0:
        pass

    else:
        raise Exception

    print_answer(answer)


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
