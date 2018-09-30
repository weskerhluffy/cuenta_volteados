'''
Created on 02/05/2018

@author: ernesto
'''
#!/bin/python3

# XXX: https://www.hackerrank.com/challenges/ctci-merge-sort/problem

import sys
from array import array

def merge(a,i1,j1,i2,j2,t):
    ic=0
    k=i1
    i=i1
    while k<=j2:
        if i2>j2 or (i1<=j1 and a[i1]<=a[i2]):
            t[k]=a[i1]
            i1+=1
        else:
            if k<i2:
                ic+=j1-i1+1
            t[k]=a[i2]
            i2+=1
        k+=1
#    a[i:j2+1]=t[i:j2+1]
    for k in range(i,j2+1):
        a[k]=t[k]
    return ic
        
def merge_sort(a,i,j,t):
    ic=0
    if j>i:
        m=i+((j-i)>>1)
        icl=merge_sort(a,i,m,t)
        icr=merge_sort(a,min(m+1,j),j,t)
        ics=merge(a,i,m,min(m+1,j),j,t)
        ic=icl+icr+ics
    return ic

def countInversions(arr,sz,tmp):
    # Complete this function
#    print(arr)
    r=merge_sort(arr,0,sz-1,tmp)
#    assert arr==sorted(arr),"got {} expe {}".format(arr,sorted(arr))
    return r

if __name__ == "__main__":
    t = int(input().strip())
    arr=array('I', [0]*(int(1E5)))
    tmp=array('I', [0]*(int(1E5)))
    for a0 in range(t):
        n = int(input().strip())
#        arr = list(map(int, input().strip().split(' ')))
        for i,c in enumerate(input().strip().split(" ")):
            arr[i]=int(c)
        result = countInversions(arr,n,tmp)
        print(result)

