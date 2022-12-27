"""
Repeated DNA Sequences

Leetcode: https://leetcode.com/problems/repeated-dna-sequences/ [187]

Statement:
Given a string s that represents a DNA sequence, and a number k, return all the contiguous sequences (substrings) of length k that occur more than once in the string. The order of the returned subsequences does not matter. If no repeated subsequence is found, the function should return an empty set.

The DNA sequence is composed of a series of nucleotides abbreviated as A, C, G, and T. For example, ACGAATTCCG is a DNA sequence. When studying DNA, it is useful to identify repeated sequences in it.

Example 1:
Input: s = "CCATATGTATGGATAT", k = 4
Output: "ATAT"

Example 2:

Input: s = "AAAACCCCTAAAACCCC", k = 8
Output: ["AAAACCCC"]
"""

# My 1st approach, it works in O(n) time complexity but space complexity is O(k*n) since every possible substrings will be hashed
def find_repeated_sequences(s, k):
    seen_sequences = dict()
    res_set = set()
    start = 0
    for end in range(k-1, len(s)):
        if s[start:end+1] in seen_sequences:
            res_set.add(s[start:end+1])
        seen_sequences[s[start:end+1]] = 1
        start += 1
    return res_set

# instead we will use rolling hash technique to decrease space used.
def find_repeated_sequences(s, k):
    window_size = k
    if len(s) <= window_size:
        return set()
    base = 4
    hi_place_value = pow(base, window_size)
    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    numbers = []
    for i in range(len(s)):
        numbers.append(mapping.get(s[i]))
    hashing = 0
    substring_hashes, output = set(), set()
    for start in range(len(s) - window_size + 1):
        if start != 0:
            hashing = hashing * base - \
                numbers[start - 1] * hi_place_value + \
                numbers[start + window_size - 1]
        else:
            for end in range(window_size):
                hashing = hashing * base + numbers[end]
        if hashing in substring_hashes:
            output.add(s[start:start + window_size])
        substring_hashes.add(hashing)
    return output


# Driver Code
def main():
    inputs_string = ["ACGT", "AGACCTAGAC", "AAAAACCCCCAAAAACCCCCC", "GGGGGGGGGGGGGGGGGGGGGGGGG",
                     "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT", "TTTTTGGGTTTTCCA",
                     "AAAAAACCCCCCCAAAAAAAACCCCCCCTG", "ATATATATATATATAT"]
    inputs_k = [3, 3, 8, 12, 10, 14, 10, 6]

    for i in range(len(inputs_k)):
        print(i+1, ".\tInput Sequence: \'", inputs_string[i], "\'", sep="")
        print("\tk: ", inputs_k[i], sep="")
        print("\tRepeated Subsequence: ",
              find_repeated_sequences(inputs_string[i], inputs_k[i]))
        print("-"*100)


if __name__ == '__main__':
    main()
