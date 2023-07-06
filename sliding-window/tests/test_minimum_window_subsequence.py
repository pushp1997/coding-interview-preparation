from minimum_window_subsequence import min_window


def test_min_window():
    str1 = [
        "abcdebdde",
        "fgrqsqsnodwmxzkzxwqegkndaa",
        "qwewerrty",
        "aaabbcbq",
        "zxcvnhss",
        "alpha",
        "beta",
        "asd",
        "abcd",
    ]
    str2 = ["bde", "kzed", "werty", "abc", "css", "la", "ab", "as", "pp"]

    ans = ["bcde", "kzxwqegknd", "werrty", "abbc", "cvnhss", "lpha", "", "as", ""]

    for i in range(len(str1)):
        assert min_window(str1[i], str2[i]) == ans[i]
