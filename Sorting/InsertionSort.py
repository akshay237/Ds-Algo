arr = [45, 23, 5, 35, 2, 9, 3]
n = len(arr)

def insertionSort(arr, n):
    for i in range(1, n):
        key = arr[i]
        # check the current element with the predecessor and if it's small check with it's predecessor and make space for element to insert. 
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def printArray():
    for i in arr:
        print(i, end=" ")


print("Insertion sort is: ")
insertionSort(arr, n)
printArray()