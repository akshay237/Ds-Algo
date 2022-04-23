def quickSort(arr, low, high):
    if low < high:
            pi = partition(arr, low, high)
            quickSort(arr, low, pi - 1)
            quickSort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    # loop through the array
    for j in range(low, high):
        # we are incrementing i when current element is less than pivot, if current is greater than pivot we swap the i index value with next small
        # value index so we get the right position of the pivot.
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # We find the pivot position so swap the high with i + 1 index becz till i index array have smaller element.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def printArray():
    for i in arr:
        print(i, end=" ")


arr = [45, 23, 5, 35, 2, 9, 3]
n = len(arr)
print("Sorted Array is: ")
quickSort(arr, 0, n - 1)
printArray()