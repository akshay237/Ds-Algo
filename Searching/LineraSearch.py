def search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


arr = [45, 23, 5, 35, 2, 9, 3]
key = int(input("Enter the key you want to search:\n"))
index = search(arr, key)
if index == -1:
    print("The Key you want to search is not present in the array.")
else:
    print("The searched key is present at index ", index + 1)
