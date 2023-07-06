from maximum_sum_subarray_of_size_k import max_sub_array_of_size_k


def test_max_sub_array_of_size_k():
    nums = [[2, 1, 5, 1, 3, 2], [2, 3, 4, 1, 5]]
    k = [3, 2]
    ans = [9, 7]
    for i in range(len(nums)):
        assert max_sub_array_of_size_k(k[i], nums[i]) == ans[i]
