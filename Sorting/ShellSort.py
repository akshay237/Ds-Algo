def shellSort(arr):
    # find out the gap
    gap = len(arr) // 2
    while gap > 0:
        i = 0
        j = gap
        # Start from the first element and compare it with the gap element if gap element is small than swap it traverse the whole list.
        while j < len(arr):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            # increment the counter by 1 to check all the element of list
            i += 1
            j += 1
            k = i
            # check from right to left whether the swapped elements are in right order or not.
            while k - gap > -1:
                if arr[k-gap] > arr[k]:
                    arr[k-gap], arr[k] = arr[k], arr[k-gap]
                k -= 1
        # decrement the gap
        gap = gap // 2


def printArray():
    for i in arr:
        print(i, end=" ")


arr = [45, 23, 5, 35, 2, 9, 3]
print("Sorted Array is: ")
shellSort(arr)
printArray()