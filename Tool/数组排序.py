my_list = [
    [1, 3], [2, 4], [1, 2], [5, 7], [3, 2], [9, 1]
]


import functools


def cmp(a, b):
    if a[0] < b[0]:
        return -1
    elif a[0] > b[0]:
        return 1
    elif a[1] > b[1]:
        return -1
    else:
        return 1


my_list.sort(key=functools.cmp_to_key(cmp))
print(my_list)



