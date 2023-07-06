from minimum_window_substring import min_window


def test_min_window():
    s = ["PATTERN", "LIFE", "ABRACADABRA", "STRIKER", "DFFDFDFVD"]
    t = ["TN", "I", "ABC", "RK", "VDD"]
    for i in range(len(s)):
        assert min_window(s[i], t[i]) == None
