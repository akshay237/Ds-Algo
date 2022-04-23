def rearrange(arr, n):
# code here
    i = 0
    j = n - 1
    while i < j:
        while (i < n) and (arr[i] > 0):
            i += 1
        while (j >= 0) and(arr[j] < 0):
            j -= 1
        if i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        if i == j:
            i += 1

    if i == 0 or i == n:
        return 0

    k = 1
    while (k < n-1) and (i < n):
        temp = arr[k]
        arr[k] = arr[i]
        arr[i] = temp
        i = i + 1
        k = k + 2

    return arr


arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
n = len(arr)
array = rearrange(arr, n)
print(array)