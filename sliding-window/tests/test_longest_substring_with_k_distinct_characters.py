from longest_substring_with_k_distinct_characters import longest_substring_with_k_distinct


def test_longest_substring_with_k_distinct():
    k_list = [2, 1, 3]
    string_list = ["araaci", "araaci", "cbbebi"]
    ans_list = [4, 2, 5]

    for i in range(len(k_list)):
        assert longest_substring_with_k_distinct(k_list[i], string_list[i]) == ans_list[i]
