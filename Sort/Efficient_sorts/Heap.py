import General_input

def parent(i):
    return (i - 1) // 2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def sort():
    n, alist = General_input.sort()
    build_max_heap(alist)
    for i in range(len(alist) - 1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        max_heapify(alist, index=0, size=i)


    print(f'Результат:{alist}')


# строит кучу
def build_max_heap(alist):
    length = len(alist)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(alist, index=start, size=length)
        start = start - 1

# поднимает больший вверх и после вызывает себя
def max_heapify(alist,index ,size):
    l=left(index)
    r=right(index)
    largest = index
    if r<size and alist[r]>alist[index]:
        largest = r
    if l < size and alist[l] > alist[index]:
        largest = l

    if index!=largest:
        alist[largest] , alist[index] = alist[index] , alist[largest]
        max_heapify(alist,largest,size)
