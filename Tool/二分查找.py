def bisect(array, number):
    low = 0
    high = len(array) - 1
    mid = (low + high) // 2

    if number > array[high]:
        return high + 1

    while low < mid:
        if array[mid] is number:
            return mid
        elif number < array[mid]:
            high = mid
        elif number > array[mid]:
            low = mid
        mid = (low + high) // 2
    return mid


my_list = [1, 2, 5, 7, 12, 34, 45, 56, 79]
print(bisect(my_list, 80))
