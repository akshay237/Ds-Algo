# Heapify process will reshape the tree we are creating a max heap here.
def heapify(arr, n, i):
    largest = i         # starting node
    l = 2 * i + 1       # left child
    r = 2 * i + 2       # right child

    # Check whether the left child id greater than root if true largest will be l
    if l < n and arr[largest] < arr[l]:
        largest = l

    # Check whether the right child is greater than largest than largest will be r
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # if largest is not same than swap root with largest
        # heapify the root node too
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Create a max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    """ 
        Once max heap is created extract element one by one here we take the largest element and will put in the end and again we will heapify the
        un sorted array so we have the max value in the first so in 2nd iteration we can take it and put in 2nd last position and so on.
    """
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # Swap them
        # heapify the unsorted array
        heapify(arr, i, 0)


def printAraay():
    for i in arr:
        print(i, end=" ")


arr1 = [12, 11, 13, 5, 6, 7]
arr = [45, 23, 5, 35, 2, 9, 3]
print("Sorted Array is:")
heapSort(arr)
printAraay()