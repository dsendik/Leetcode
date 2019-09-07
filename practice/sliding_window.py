"""
This function finds the largest sum of k numbers in a list of numbers.
This is done using the sliding window technique, where each window is made up
of k elements in the list. For each iteration, the window slides one place.
"""

def maxSlidingWindow(nums, k):
    n = len(nums)

    # When the list is too small and when the list and target are same length.
    if n < k or k < 2:
        return "invalid input"
    if n == k:
        return nums[::]

    current_max = -1
    current_max_win = []
    window = sum([nums[i] for i in range(0, k)])

    for i in range(0, n - k):
        window = window - nums[i] + nums[i + k]  # this is the slide
        current_win = nums[(i + 1):(i + 1) + k]

        if window > current_max:
            current_max = window
            current_max_win = current_win
        current_max = max(window, current_max)

    return current_max_win


# test cases
# print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 6, 7])
print(maxSlidingWindow([-5, -2, -1, -8, -10], 3) == [-5, -2, -1])
print(maxSlidingWindow([1, 3, -1, -3, 5, 1, 1, 1], 2) == [5, 1])
print(maxSlidingWindow([1, 3, -1, -3, 5, 1, 1, 1], 0) == "invalid input")
print(maxSlidingWindow([], 2) == "invalid input")
print(maxSlidingWindow([], 0) == "invalid input")
print(maxSlidingWindow([10, 10, 10, 10], 2) == [10, 10])
print(maxSlidingWindow([2, 2], 3) == "invalid input")
print(maxSlidingWindow([1, 2, 3, 4, 1], 1) == "invalid input")
print(maxSlidingWindow([1, 2, 3, 4, 1], 5) == [1, 2, 3, 4, 1])
