"""
Find Maximum in Sliding Window

Leetcode: https://leetcode.com/problems/sliding-window-maximum/

Statement:
Given an integer array and a window of size w, find the current maximum value in the window as it slides through the entire array.

Note: If the window size is greater than the array size, we consider the entire array as a single window.

Example:
Window size = 3
Array: -4 2 -5 3 6
Output: 2 3 6
"""

"""
# My 1st approach and naive approach O(len(nums) - window_size * window_size) or O((n-k)*k)
def find_max_sliding_window(nums, window_size):
    window_start, res_arr = 0, []
    for window_end in range(len(nums)):
        if window_end - window_start == window_size - 1:
            res_arr.append(max(nums[window_start : window_end + 1]))
            window_start += 1
    return res_arr
"""

# Ideal solution using deque O(n)

# Importing doubly ended queue
from collections import deque


def find_max_sliding_window(nums, window_size):
    res_arr = []
    # If no elements in nums return empty array
    if not nums:
        return res_arr

    # windows size is greater than length of nums then window size = len(nums)
    if window_size > len(nums):
        window_size = len(nums)

    deq = deque()

    # Insertion for the 1st window
    for i in range(window_size):
        while deq and nums[deq[-1]] <= nums[i]:
            deq.pop()
        deq.append(i)

    res_arr.append(nums[deq[0]])

    # Insertion for the consequent windows
    for i in range(window_size, len(nums)):
        while deq and nums[deq[-1]] <= nums[i]:
            deq.pop()

        # Remove first index from the window deque if
        # it doesn't fall in the current window anymore
        if deq and deq[0] <= (i - window_size):
            deq.popleft()

        # Add current element at the back of the queue
        deq.append(i)
        res_arr.append(nums[deq[0]])

    return res_arr
