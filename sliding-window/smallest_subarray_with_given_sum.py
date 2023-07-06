"""
Smallest Subarray with a given sum (easy)

Leetcode: https://leetcode.com/problems/minimum-size-subarray-sum/ [209]

Statement:
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray
whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

Example 1:
Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

Example 2:
Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
"""

# My 1st approach O(len(arr) + len(arr)) or O(n)
from typing import List


def smallest_subarray_with_given_sum(s: int, arr: List[int]):
    smallest_subarray_size = len(arr) + 1

    # If no elements in arr return 0
    if not arr:
        return 0

    i, j, cur_sum = 0, 0, 0
    while j < len(arr):
        cur_sum += arr[j]

        if cur_sum >= s:
            while i <= j:
                if cur_sum < s:
                    break

                smallest_subarray_size = min(smallest_subarray_size, j - i + 1)
                cur_sum -= arr[i]
                i += 1

        j += 1

    return smallest_subarray_size if smallest_subarray_size <= len(arr) else 0


# Driver code
def main():
    s_list = [7, 7, 8]
    arr_list = [[2, 1, 5, 2, 3, 2], [2, 1, 5, 2, 8], [3, 4, 1, 1, 6]]

    for i in range(len(arr_list)):
        print(
            f"Smallest subarray length: {smallest_subarray_with_given_sum(s_list[i], arr_list[i])}"
        )


if __name__ == "__main__":
    main()
