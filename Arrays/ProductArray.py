def productExceptSelf(nums, n):
    # code here
    total = 1
    prod = list()
    for i in nums:
        total = total * i
    print(total)

    # for i in range(n):
    #     prod[i]= total/nums[i]
    j = 0
    while j < n -1:
        prod.append(total//nums[j])
        j += 1
    return prod


arr = [10, 3, 5, 6, 2]
n = len(arr)
new_array = productExceptSelf(arr, n)
print(new_array)