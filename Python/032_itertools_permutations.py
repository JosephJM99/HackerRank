'''
itertools.permutations(iterable[, r])

This tool returns successive r length permutations of elements in an iterable.

If r is not specified or is None, then f defaults to the length of the iterable, and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.
'''


from itertools import permutations


if __name__ == '__main__':
    s, k = input().split()

    results =[''.join(x) for x in list(permutations(s, int(k)))]
    results.sort()
    for x in results:
        print(x)