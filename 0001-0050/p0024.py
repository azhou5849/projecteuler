def get_nth_lexicographic(lst, n, count_from_zero = True):
    """
    Get the n-th permutation of the elements of lst, sorted by lexicographic order
    If count_from_zero is set to False, then the count starts at 1
    """
    if not count_from_zero:
        return get_nth_lexicographic(lst, n - 1)
    L = len(lst)
    factorials = [1 for _ in range(L)]
    for i in range(1,L):
        factorials[i] = i * factorials[i - 1]

    unused = sorted(lst)
    permutation = []
    while len(unused) > 0:
        chunk_size = factorials[-1]
        m = n // chunk_size
        permutation.append(unused[m])
        n = n % chunk_size
        unused.pop(m)
        factorials.pop(-1)
    return permutation

get_nth_lexicographic(list(range(10)), 1000000, count_from_zero = False)
