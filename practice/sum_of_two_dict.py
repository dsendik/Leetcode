def twoSum(nums, target):
    keys = range(len(nums))
    mynums = {}
    indices1 = -1
    indices2 = -1
    list = []

    for i in keys:
        mynums[i] = nums[i]
        list.append(i)
    # print(mynums)
    for i in mynums:
        if (target - i) in nums:
            # print("found")
            indices1 = mynums.get(target - i)
            indices2 = mynums.get(i)
    return [indices1, indices2]


# test cases
# print((twoSum([2,7,11,15], 9) == [0,1]))
# print((twoSum([2,7,11,15], 13) == [0, 2]))
# print((twoSum([], 9) == [-1,-1]))
# print((twoSum([2,7,11,15], 9) == [0,1]))
# print((twoSum([2,7,11,15], 8) == [-1,-1]))
# print((twoSum([3, 3], 6) == [0, 1]))
print((twoSum([1, 2, 5, 1], 2) == [0, 3]))
