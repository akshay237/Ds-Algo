arr = [45, 23, 5, 35, 2, 9, 3]
n = len(arr)


def BubbleSort(arr, n):
    for i in range(n):
        swap = False
        # check the adjacent element by inner for loop
        for j in range(0, n - i - 1):
            # For descending order reverse the compare statement
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swap = True
                # we can use one line also for swap i.e arr[j], arr[j+1] = arr[j+1], arr[j]
        # We have used the swap variable because if array is already in sorted order than we can come out of loop
        if not swap:
            break


def printArray():
    for i in arr:
        print(i, end=" ")


print("Bubble Sort of the given array is: ")
BubbleSort(arr, n)
printArray()