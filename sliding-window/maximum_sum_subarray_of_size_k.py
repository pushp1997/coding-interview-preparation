"""
Maximum Sum Subarray of Size K (easy)

Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Leetcode: https://leetcode.com/problems/maximum-subarray/ [53]
* The leetcode problem is much advanced as it involves a window of flexible size
"""
from typing import List


# My 1st approach, O(n)
def max_sub_array_of_size_k(k: int, nums: List[int]) -> int:
    max_sum: int = 0
    cur_sum: int = 0
    i: int = 0
    for j in range(len(nums)):
        # Until the desired size of the window has been reached increase the window size and the element to the max
        if j - i < k:
            cur_sum += nums[j]
            max_sum = cur_sum
            continue

        cur_sum -= nums[i]
        cur_sum += nums[j]

        max_sum = max(max_sum, cur_sum)
        i += 1

    return max_sum
