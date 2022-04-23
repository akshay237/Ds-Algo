array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
array1 = [2, 1, 1, 3, 5]
array2 = [2, 3, 4]
map = dict()


def firstRecurringElement(arr):
    for i in arr:
        if i in map:
            map[i] += 1
            return i
            break
        map[i] = 1
    return -1


element = firstRecurringElement(array1)
print(element)


