from repeated_dna_sequences import find_repeated_sequences


def test_find_repeated_sequences():
    inputs_string = [
        "ACGT",
        "AGACCTAGAC",
        "AAAAACCCCCAAAAACCCCCC",
        "GGGGGGGGGGGGGGGGGGGGGGGGG",
        "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT",
        "TTTTTGGGTTTTCCA",
        "AAAAAACCCCCCCAAAAAAAACCCCCCCTG",
        "ATATATATATATATAT",
    ]
    inputs_k = [3, 3, 8, 12, 10, 14, 10, 6]

    ans = [
        set(),
        {"GAC", "AGA"},
        {"AAACCCCC", "AAAAACCC", "AAAACCCC"},
        {"GGGGGGGGGGGG"},
        {
            "CCCCTTTTTT",
            "TTTTTCCCCC",
            "TTTTCCCCCC",
            "TTCCCCCCCT",
            "CCCCCCTTTT",
            "CCCCCCCTTT",
            "CCCCCTTTTT",
            "TTTCCCCCCC",
            "TCCCCCCCTT",
        },
        set(),
        {"AAAACCCCCC", "AAAAACCCCC", "AAACCCCCCC", "AAAAAACCCC"},
        {"ATATAT", "TATATA"},
    ]

    for i in range(len(inputs_k)):
        assert find_repeated_sequences(inputs_string[i], inputs_k[i]) == ans[i]
