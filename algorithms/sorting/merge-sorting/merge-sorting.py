import math
array = [70, 93, 66, 9, 48, 77, 55, 56, 74, 56,
         31, 84, 84, 17, 22, 16, 69, 45, 90, 96,
         56, 50, 40, 19, 35, 11, 73, 73, 89, 16,
         63, 59, 9, 29, 67, 56, 6, 21, 11, 79,
         76, 42, 62, 60, 59, 84, 76, 27, 29, 65
         ]


def mergeSortRec(array):

    length = len(array)
    if length == 1:
        return array

    mid = math.floor(length / 2)

    left = array[:mid]
    right = array[mid: length]

    return merge(mergeSortRec(left), mergeSortRec(right))


def merge(left, right):
    result = list()
    il = 0
    ir = 0

    while il < len(left) and ir < len(right):
        if(left[il] < right[ir]):
            result.append(left[il])
            il += 1
        else:
            result.append(right[ir])
            ir += 1

    while il < len(left):
        result.append(left[il])
        il += 1

    while ir < len(right):
        result.append(right[ir])
        ir += 1

    return result


print(mergeSortRec(array))
