# Problem return true if the arrays contains a common element else return false if it does not.
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [6, 7, 8, 9]
# This return False

# arr1 = [1, 2, 3, 4, 8]
# arr2 = [6, 7, 8, 9]
# This return true

arr1 = [1, 2, 3, 4, 8]
arr2 = [5, 6, 7, 9]


def findelement(array1, array2):
    num = {}
    for i in range(len(array1)):  # O(n)
        num[array1[i]] = True
    for i in range(len(array2)):   # O(n)
        if num.get(array2[i]):
            return True
        else:
            num[array2[i]] = True
    return False


value = findelement(arr1, arr2)
print(value)