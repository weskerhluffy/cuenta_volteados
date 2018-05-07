'''
Created on 02/05/2018

@author: ernesto
'''
#!/bin/python3

import sys


def merge(a, i, j, k, l):
    it = 0
    io = i
    while i <= j and k <= l:
        if a[i] <= a[k]:
            t[it] = a[i]
            i += 1
        else:
            t[it] = a[k]
            k += 1
        it += 1
    while i <= j:
        t[it] = a[i]
        i += 1
        it += 1
    while k <= l:
        t[it] = a[k]
        k += 1
        it += 1
    a[io:l + 1] = t[:it]

        
def merge_sort(a, i, j, t):
    if j > i:
        m = i + ((j - i) >> 1)
        merge_sort(a, i, m, t)
        merge_sort(a, min(m + 1, j), j, t)
        merge(a, i, m, min(m + 1, j), j, t)


def countInversions(arr):
    # Complete this function
    print("arr {}".format(arr))
    merge_sort(arr, 0, len(arr) - 1, [0] * len(arr))
    assert arr == sorted(arr)


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = countInversions(arr)
        print(result)

