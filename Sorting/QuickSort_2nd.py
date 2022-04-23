def quickSort(arr, low, high):
    if low < high:
            pi = partition(arr, low, high)
            print(pi)
            quickSort(arr, low, pi - 1)
            quickSort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    left = low
    right = high - 1
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if right < left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[left], arr[high] = arr[high], arr[left]
    return left


def printArray():
    for i in arr:
        print(i, end=" ")


arr = [45, 23, 5, 35, 2, 9, 3]
n = len(arr)
print("Sorted Array is: ")
quickSort(arr, 0, n - 1)
printArray()