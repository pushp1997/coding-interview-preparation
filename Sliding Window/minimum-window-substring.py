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
    target_window_length = 0
    # Creating window target
    for char in t:
        if char in target_map:
            target_map[char] += 1
        else:
            target_window_length += 1
            target_map[char] = 1
    
    left, min_left = 0, 0
    right, min_right = 0, 0
    cur_window_length, min_window_length = 0, string_length+1
    window_map = {}
    while right < string_length:
        if s[right]in window_map:
            window_map[s[right]] += 1
        else:
            window_map[s[right]] = 1
        
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

        right += 1

    return s[min_left: min_right+1]

# Same solution but diff way of writing by educative
def min_window(s, t):
    # Empty string scenario
    if t == "":
        return ""
    # Creating the two hash maps
    r_count = {}
    window = {}

    # Populating r_count hash map
    for c in t:
        r_count[c] = 1 + r_count.get(c, 0)

    # Setting up the conditional variables
    current, required = 0, len(r_count)
    # Setting up a variable containing the result's starting and ending point
    # with default values and a length variable
    res, res_len = [-1, -1], float("infinity")
    # Setting up the sliding window pointers
    left = 0
    for right in range(len(s)):
        c = s[right]
        window[c] = 1 + window.get(c, 0)  # Populating the window hash map

        # Updating the current variable
        if c in r_count and window[c] == r_count[c]:
            current += 1

        while current == required:  # Adjusting the sliding window
            # update our result
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = (right - left + 1)
            # pop from the left of our window
            window[s[left]] -= 1
            if s[left] in r_count and window[s[left]] < r_count[s[left]]:
                current -= 1  # if the popped character was among the required characters and removing it has reduced its frequency below its frequency in t, decrement current
            left += 1
    left, right = res
    return s[left:right+1] if res_len != float("infinity") else ""

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
