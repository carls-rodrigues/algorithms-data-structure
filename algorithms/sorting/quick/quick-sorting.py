import math
array = [70, 93, 66, 9, 48, 77, 55, 56, 74, 56,
         31, 84, 84, 17, 22, 16, 69, 45, 90, 96,
         56, 50, 40, 19, 35, 11, 73, 73, 89, 16,
         63, 59, 9, 29, 67, 56, 6, 21, 11, 79,
         76, 42, 62, 60, 59, 84, 76, 27, 29, 65
         ]


def quick(array, left, right):
    index = None

    if len(array) > 1:
        index = partition(array, left, right)

        if left < index - 1:
            quick(array, left, index - 1)
        if index < right:
            quick(array, index, right)

    return array


def partition(array, left, right):
    pivot = array[math.floor((right + left) / 2)]
    i = left
    j = right

    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1

        if i <= j:
            swap(array, i, j)
            i += 1
            j -= 1

    return i


def swap(array, index1, index2):
    tmp = array[index1]
    array[index1] = array[index2]
    array[index2] = tmp


print(quick(array, 0, len(array) - 1))
