"""
Longest Substring with K Distinct Characters (medium)

Leetcode: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/ [premium]

Statement:
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""


# My 1st approach O(len(arr) + len(arr)) or O(n)
def longest_substring_with_k_distinct(k: int, string: str):
    longest_substring_len = 0

    # If empty string then return 0
    if not string:
        return longest_substring_len

    i, j, cur_len = 0, 0, 0
    cur_chars = {}

    while j < len(string):
        if string[j] not in cur_chars:
            cur_len += 1
            cur_chars[string[j]] = 0

        cur_chars[string[j]] += 1

        if cur_len <= k:
            longest_substring_len = max(longest_substring_len, j - i + 1)

        while cur_len > k:
            cur_chars[string[i]] -= 1
            if cur_chars[string[i]] == 0:
                cur_len -= 1
                del cur_chars[string[i]]
            i += 1

        j += 1

    return longest_substring_len
