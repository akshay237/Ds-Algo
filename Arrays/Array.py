import array

arr = array.array('i' , [1, 2, 3, 4, 5, 6])

# Append element to array
arr.append(9)  # O(1) - No Traversal
# for i in range(len(arr)):
#     print(arr[i])

# Remove element from last
arr.pop()  # O(1) - No Traversal
# for i in range(len(arr)):
#     print(arr[i])


# Insert at any index
arr.insert(2, 10)  # O(n) we have to shift the elements so have to traverse whole array
for i in range(len(arr)):
    print(arr[i])


# Reverse the array
arr.reverse()   # O(n) We have to reverse the content so have to traverse through whole array
for i in range(len(arr)):
    print(arr[i])