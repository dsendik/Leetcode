def maxSubArray(nums):
    n = len(nums)
    count = 0
    if n < 1:
        return 0

    current = nums[0]
    final_max = nums[0]
    for i in range(1, n):
        current = max(current + nums[i], nums[i])
        final_max = max(final_max, current)
        count += 1

    return final_max


print(maxSubArray([5, 3, 1]) == 9)
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
print(maxSubArray([]) == 0)
