'''
Created on 02/05/2018

@author: ernesto
'''
#!/bin/python3

import sys


def merge(a, i, j, k, l, t):
    it = 0
    ric = 0
    fic = 0
    th = k - i
    io = i
    print("th {}".format(th))
    while i <= j and k <= l:
        if a[i] <= a[k]:
            print("it {} de i {} es {}".format(it, i, a[i]))
            if it >= th:
                print("fic")
                fic += 1
            t[it] = a[i]
            i += 1
        else:
            print("it {} de k {} es {}".format(it, k, a[k]))
            if it < th:
                print("ric")
                ric += 1
            t[it] = a[k]
            k += 1
        it += 1
    while i <= j:
        print("it a {} de i {} es {}".format(it, i, a[i]))
        t[it] = a[i]
        if it >= th:
            print("fic a")
            fic += 1
        i += 1
        it += 1
    while k <= l:
        t[it] = a[k]
        if it < th:
            ric += 1
        k += 1
        it += 1
    a[io:l + 1] = t[:it]
    return ric, fic

        
def merge_sort(a, i, j, t):
    ric = 0
    fic = 0
    if j > i:
        m = i + ((j - i) >> 1)
        ric1, fic1 = merge_sort(a, i, m, t)
        ric2, fic2 = merge_sort(a, min(m + 1, j), j, t)
        ric3, fic3 = merge(a, i, m, min(m + 1, j), j, t)
        print("i {} j {} ric1 {} fic1 {} ric2 {} fic2 {} ric3 {} fic3 {}".format(i, j, ric1, fic1, ric2, fic2, ric3, fic3))
        ric = ric1 + ric2 + ric3
        fic = fic1 + fic2 + fic3
    return ric, fic


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

