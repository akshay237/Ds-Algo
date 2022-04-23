def binarySearch(arr, l, r, key):
    if r >= l:
        # find the middle position
        # if we use mid = (l+r)//2 than our code is not correct it won't work for large input
        mid = l + (r - l) // 2
        # if middle index value matches the key
        if arr[mid] == key:
            return mid
        # if the middle element less than the key value
        # for itertative approach change the value of l and r depending on the key.
        elif arr[mid] > key:
            return binarySearch(arr, l, mid - 1, key)
        # if the middle value is greater than the key value
        else:
            return binarySearch(arr, mid + 1, r, key)
    # if key is not matched with any value of array
    else:
        return -1


arr = [2, 3, 5, 9, 23, 35, 45]
n = len(arr)
key = int(input("Enter the value you want to search: \n"))
index = binarySearch(arr,0, n - 1, key)
if index == -1:
    print("The key you want to search is not present in the sorted array.")
else:
    print("The key is present at index", index + 1)