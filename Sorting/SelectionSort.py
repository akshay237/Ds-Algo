arr = [45, 23, 5, 35, 2, 9, 3]
n = len(arr)


# Array sorted in ascending order
def sortInAscending(arr, n):
    for i in range(n):
        min_idx = i
        # find the index of minimum value in each iteration
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # Swap the minimum value with the first value in each iteration
        # If in the current position we have the right element than we won't swap
        if min_idx != i:
            temp = arr[i]
            arr[i] = arr[min_idx]
            arr[min_idx] = temp


# Array sorted in descending order
def sortInDescending(arr, n):
    for i in range(n):
        max_idx = i
        # find the index of max value in each iteration
        for j in range(i+1, n):
            if arr[max_idx] < arr[j]:
                max_idx = j
        # Swap the max value with the first value in each iteration
        # If in that position only we have the right element than we won't swap
        if max_idx != i:
            temp = arr[i]
            arr[i] = arr[max_idx]
            arr[max_idx] = temp


# Print the array elements
def printArray():
    for i in arr:
        print(i, end=" ")


print("Array sorted in ascending order is: ")
sortInAscending(arr, n)
printArray()
print("\nArray sorted in Descending order is: ")
sortInDescending(arr, n)
printArray()