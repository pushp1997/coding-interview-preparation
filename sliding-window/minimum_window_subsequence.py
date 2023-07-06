"""
Minimum Window Subsequence

Leetcode: https://leetcode.com/problems/minimum-window-subsequence/ [727]

Statement:
Given strings str1 and str2, find the minimum (contiguous) substring sub_str of str1, such that every character of str2
appears in sub_str in the same order as it is present in str2.

If there is no window in str1 that covers all characters in str2, return an empty string.

If there are multiple minimum-length windows, return the one with the leftmost starting index.

Examples:

str1: "abcdebdde"
str2: "bdf"
Output: ""

str1: "abcdebdde"
str2: "bde"
Output: "bcde"
"""

"""
# My 1st approach takes 10sec for 5 test cases. Timed out on leetcode
def min_window(str1, str2):
    # If the str2 exists in str1 directly OR leaf node condition
    if len(str1) == len(str2):
        if str1 == str2:
            return str1
        else:
            return ""

    smallest = ""
    possible_small_left = min_window(str1[0: len(str1)-1], str2)
    possible_small_right = min_window(str1[1: len(str1)], str2)
    if possible_small_left:
        smallest = possible_small_left
    if possible_small_right:
        if len(possible_small_right) < len(smallest):
            smallest = possible_small_right

    if not smallest:
        l1, r2 = -1, 0
        for r1 in range(len(str1)):
            if str1[r1] == str2[r2]:
                if l1 == -1:
                    l1 = r1
                r2 += 1

            if r2 == len(str2):
                if l1 != -1: 
                    smallest = str1[l1:r1+1]
                break

    return smallest
"""

# The above approach can further be optimised by using memoization, as every possible substring


# Ideal O(n) approach two way travelling sliding window
def min_window(str1, str2):
    # Storing the length of both strings
    size_str1, size_str2 = len(str1), len(str2)
    # Initially, min length of the subsequence is infinity and min subsequnce is empty string
    length = float("inf")
    min_subsequence = ""
    # Both the pointers initially points to the 1st char of both strings
    p1, p2 = 0, 0

    # Check for every charaacter of str1
    while p1 < size_str1:
        # If the characters in both strings match
        if str1[p1] == str2[p2]:
            # increment p2 to next position
            p2 += 1
            # If all the chars from str2 have been matched
            if p2 == size_str2:
                # put an end pointer of the window at one pos next to p1
                # and start pointer of the window to p1
                start, end = p1, p1 + 1

                # Since p2 = length of str2 lets make it point to the last char
                p2 -= 1

                # Now start making window backwards to find smallest subsequence
                while p2 > -1:
                    if str1[start] == str2[p2]:
                        p2 -= 1
                    start -= 1
                # We have a small subsequence lets check if its smallest
                if end - start < length:
                    length = end - start
                    min_subsequence = str1[start + 1 : end]

                # Found a subsequence now lets look for more subsequences
                # by resetting p2 and p1 will start after the found subsequence
                p2 = 0
                p1 = start + 2

        # p1 increments no matter it matches with p1 or not
        p1 += 1

    return min_subsequence


# The above approach takes 1sec for same 5 test cases.
