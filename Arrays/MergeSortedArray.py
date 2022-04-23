import array

# def mergeSorted(list1, list2):
#     if len(list1) == 0 | len(list2) == 0:
#         return "Please provide valid list"
#
#     myList = list()
#     for i in range(len(list1)):
#         myList.append(list1[i-1])
#
#     for j in range(len(list2)):
#         myList.append(list2[j-1])
#
#     myList.sort()
#     return myList
#
#
# list1 = [0, 3, 4, 31]
# list2 = [4, 6, 30]
# myList = mergeSorted(list1, list2)
# print(myList)
def morgeSortedArrays(arr1, arr2):
    length1 = len(arr1)
    length2 = len(arr2)
    # print(length1)
    # print(length2)
    if length1 == 0:
        return arr2
    if length2 == 0:
        return arr1
    myList = array.array('i', [])
    i = 0
    j = 0
    while (i < length1) & (j < length2):
        if arr1[i] <= arr2[j]:
            myList.append(arr1[i])
            i = i + 1
            # print(myList)
            # print("i :", i)
            # print(length1)
        else:
            myList.append(arr2[j])
            j = j + 1
            # print(myList)
            # print("j :", j)
            # print(length2)
    if i < length1:
        for x in range(i, length1):
            myList.append(arr1[x])
    if j < length2:
        for x in range(j, length2):
            myList.append(arr2[x])
    return myList


arr1 = array.array('i', [0, 3, 4, 31])
arr2 = array.array('i', [4, 6, 30])
arr = morgeSortedArrays(arr1, arr2)
print(arr)