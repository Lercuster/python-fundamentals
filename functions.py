def binary_search(a: list, val):
    """Бинарный поиск, работает только
    с ОТСОРТИРОВАННЫМ!!! массивомб О(log(n))
    Возвращает индекс найденного элемента или None, если элемент не найден"""
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (high + low) // 2
        if a[mid] == val:
            return mid
        if a[mid] > val:
            high = mid - 1
        if a[mid] < val:
            low = mid + 1
    print("done")
    return None


def find_smallest(a: list):
    minn = a[0]
    index = 0
    for i in range(1, len(a)):
        if a[i] < minn:
            minn = a[i]
            index = i
    return index


def rev(b: list) -> list:
    for i in range(0, (len(a) // 2)):
        buf = b[i]
        b[i] = b[len(b) - i - 1]
        b[len(b) - i - 1] = buf
    return b


def pick_sort(a: list, reverse=False) -> list:
    """ сортировка выбором,  О(n^2)"""
    b = []
    aa = a.copy()
    for i in range(0, len(aa)):
        b.append(aa.pop(find_smallest(aa)))
    if reverse:
        return rev(b)
    return b


def quick_sort(a: list) -> list:
    """ Быстрая сортировка, через рекурсию.
    """
    a_left = []
    a_right = []
    if len(a) < 2:                      # Базовый случай
        return a
    else:                               # Рекурсивный случай
        node_index = len(a) // 2
        for i in range(len(a)):
            if i == node_index:
                continue
            if a[i] <= a[node_index]:
                a_left.append(a[i])
            else:
                a_right.append(a[i])
        return quick_sort(a_left) + [a[node_index]] + quick_sort(a_right)