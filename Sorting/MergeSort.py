def mergeSort(arr):
    if len(arr) > 1:
        m = len(arr)//2
        left = arr[:m]
        right = arr[m:]
        # Divide the array into two sorted half.
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        n1 = len(left)
        n2 = len(right)
        # Merge the two sorted arrays
        while (i < n1) and (j < n2):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        # Case when in left array elements left.
        while i < n1:
            arr[k] = left[i]
            i += 1
            k += 1
        # Case when in right array elements left.
        while j < n2:
            arr[k] = right[j]
            j += 1
            k += 1


def printArray():
    for i in arr:
        print(i, end=" ")


arr = [45, 23, 5, 35, 2, 9, 3]
n = len(arr)
print("Sorted Array is: ")
mergeSort(arr)
printArray()

