"""
Minimum Window Substring

Leetcode: https://leetcode.com/problems/minimum-window-substring/ [76]
"""

# My 1st approach, O(s+t)
def min_window(s, t):
    target_length = len(t)
    string_length = len(s)

    # If target string is empty
    if t == "":
        return ""

    # If target substring is longer than the string
    if target_length > string_length:
        return ""

    # When target substring is shorter than the string
    target_map = {}
    # Creating window target
    for char in t:
        target_map[char] = target_map.get(char, 0) + 1
    
    left, min_left = 0, 0
    right, min_right = 0, 0
    cur_window_length, target_window_length = 0, len(target_map)
    min_window_length = string_length+1
    window_map = {}
    for right in range(string_length):
        if s[right]in window_map:
            window_map[s[right]] = window_map.get(s[right], 0) + 1
        
        if s[right] in target_map and target_map[s[right]] == window_map[s[right]]:
            cur_window_length += 1

        if target_window_length == cur_window_length:
            while target_window_length == cur_window_length:
                if s[left] in target_map and window_map[s[left]] == target_map[s[left]]:
                    cur_window_length -= 1
                window_map[s[left]] -= 1
                left += 1

            if min_window_length > right - left + 2:
                min_window_length = right - left + 2
                min_left, min_right = left - 1, right

    return s[min_left: min_right+1]

# Driver Code
def main():
    s = ["PATTERN", "LIFE", "ABRACADABRA", "STRIKER", "DFFDFDFVD"]
    t = ["TN", "I", "ABC", "RK", "VDD"]
    for i in range(len(s)):
        print(i + 1, ".\ts: ", s[i], "\n\tt: ", t[i], "\n\tThe minimum substring containing ", \
            t[i], " is: ", min_window(s[i], t[i]), sep="")
        print("-" * 98)


if __name__ == '__main__':
    main()
