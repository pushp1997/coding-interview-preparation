from smallest_subarray_with_given_sum import smallest_subarray_with_given_sum


def test_smallest_subarray_with_given_sum():
    s_list = [7, 7, 8]
    arr_list = [[2, 1, 5, 2, 3, 2], [2, 1, 5, 2, 8], [3, 4, 1, 1, 6]]
    ans_list = [2, 1, 3]

    for i in range(len(arr_list)):
        assert smallest_subarray_with_given_sum(s_list[i], arr_list[i]) == ans_list[i]
