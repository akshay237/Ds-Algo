arr = [6, 4, 3, 2, 1]

# Brute Force Approach
# def findPairSum(array, sum):
#     for i in range(len(array)): # O(n)
#         j = i + 1
#         for j in range(len(array)): # o(n)
#             if array[i] + array[j] == sum:
#                 return True
#     return False


def findPairSum(array, sum):
    mySet = set()
    for i in range(len(array)):  # O(n)
        if arr[i] in mySet:
            return True
        mySet.add(sum - arr[i])  
    return False


value = findPairSum(arr, 9)
print(value)